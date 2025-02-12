#!/usr/bin/env python
# -*- coding: cp1252 -*-
"""
frm_eqtexsvg.py
functions for converting LaTeX equation string into SVG path
This extension need, to work properly:
    - a TeX/LaTeX distribution (MiKTeX ...)
    - pstoedit software: <http://www.pstoedit.net/pstoedit>

Copyright (C) 2006 Julien Vitard <julienvitard@gmail.com>

2010-04-04: Added support for custom packages
            Christoph Schmidt-Hieber <christsc@gmx.de>
            
2012-10-03: Added support for "formula display size factor"
            Francesco Montorsi <francesco.montorsi@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA

"""

import inkex, os, tempfile, sys, xml.dom.minidom

def parse_pkgs(pkgstring):
    pkglist = pkgstring.replace(" ","").split(",")
    header = ""
    for pkg in pkglist:
        header += "\\usepackage{%s}\n" % pkg

    return header
    
def parse_size(sizestr):
    return [float(sizestr), float(sizestr)]

def create_equation_tex(filename, equation, add_header=""):
    tex = open(filename, 'w')
    tex.write("""%% processed with frm_eqtexsvg.py
\\documentclass{article}
\\usepackage{amsmath}
\\usepackage{amssymb}
\\usepackage{amsfonts}
""")
    tex.write(add_header)
    tex.write("""\\thispagestyle{empty}
\\begin{document}
""")
    tex.write(equation)
    tex.write("\n\\end{document}\n")
    tex.close()

def svg_open(self,filename,doc_sizeW,doc_sizeH):
    #doc_width = inkex.unittouu(self.document.getroot().get('width'))
    #doc_height = inkex.unittouu(self.document.getroot().get('height'))
    #doc_sizeH = min(doc_width,doc_height)
    #doc_sizeW = max(doc_width,doc_height)
    

    def clone_and_rewrite(self, node_in):
        in_tag = node_in.tag.rsplit('}',1)[-1]
        if in_tag != 'svg':
            node_out = inkex.etree.Element(inkex.addNS(in_tag,'svg'))
            for name in node_in.attrib:
                node_out.set(name, node_in.attrib[name])
        else:
            node_out = inkex.etree.Element(inkex.addNS('g','svg'))
        for c in node_in.iterchildren():
            c_tag = c.tag.rsplit('}',1)[-1]
            if c_tag in ('g', 'path', 'polyline', 'polygon'):
                child = clone_and_rewrite(self, c)
                if c_tag == 'g':
                    child.set('transform','matrix('+str(doc_sizeH/700.)+',0,0,'+str(-doc_sizeH/700.)+','+str(-doc_sizeH*0.25)+','+str(doc_sizeW*0.75)+')')
                node_out.append(child)

        return node_out

    doc = inkex.etree.parse(filename)
    svg = doc.getroot()
    group = clone_and_rewrite(self, svg)
    self.current_layer.append(group)

class FRM_EQTEXSVG(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option("-f", "--formule",
                        action="store", type="string",
                        dest="formula", default="",
                        help="LaTeX formula")
        self.OptionParser.add_option("-p", "--packages",
                        action="store", type="string",
                        dest="packages", default="",
                        help="Additional packages")
        self.OptionParser.add_option("-z", "--size",
                        action="store", type="string",
                        dest="size", default="",
                        help="Formula size")                       
                        
                        
    def effect(self):

        base_dir = tempfile.mkdtemp("", "inkscape-");
        latex_file = os.path.join(base_dir, "eq.tex")
        aux_file = os.path.join(base_dir, "eq.aux")
        log_file = os.path.join(base_dir, "eq.log")
        ps_file = os.path.join(base_dir, "eq.ps")
        dvi_file = os.path.join(base_dir, "eq.dvi")
        svg_file = os.path.join(base_dir, "eq.svg")
        out_file = os.path.join(base_dir, "eq.out")
        err_file = os.path.join(base_dir, "eq.err")

        def clean():
            os.remove(latex_file)
            os.remove(aux_file)
            os.remove(log_file)
            os.remove(ps_file)
            os.remove(dvi_file)
            os.remove(svg_file)
            os.remove(out_file)
            if os.path.exists(err_file):
                os.remove(err_file)
            os.rmdir(base_dir)

        add_header = parse_pkgs(self.options.packages)
        create_equation_tex(latex_file, self.options.formula, add_header)
        os.system('latex "-output-directory=%s" -halt-on-error "%s" > "%s"' \
                  % (base_dir, latex_file, out_file))
        try:
            os.stat(dvi_file)
        except OSError:
            print >>sys.stderr, "invalid LaTeX input:"
            print >>sys.stderr, self.options.formula
            print >>sys.stderr, "temporary files were left in:", base_dir
            sys.exit(1)

        os.system('dvips -q -f -E -D 600 -y 5000 -o "%s" "%s"' % (ps_file, dvi_file))
        # cd to base_dir is necessary, because pstoedit writes
        # temporary files to cwd and needs write permissions
        separator = ';'
        if os.name == 'nt':
            separator = '&&'
        os.system('cd "%s" %s pstoedit -f plot-svg -dt -ssp "%s" "%s" > "%s" 2> "%s"' \
                  % (base_dir, separator, ps_file, svg_file, out_file, err_file))

        # forward errors to stderr but skip pstoedit header
        if os.path.exists(err_file):
            #sys.stderr.write('pstoedit produced output on stderr:\n')
            err_stream = open(err_file, 'r')
            for line in err_stream:
                if not line.startswith('pstoedit: version') and not line.startswith('running-win command line'):
                    # FM-fix: ignore the single-line 'running-win command line' etc etc
                    sys.stderr.write(line + '\n')
            err_stream.close()
 
        sz = parse_size(self.options.size)
        svg_open(self, svg_file, sz[0], sz[1])

        clean()

if __name__ == '__main__':
    e = FRM_EQTEXSVG()
    e.affect()


# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 encoding=utf-8 textwidth=99
