README
======

This is a simple modification of Julien Vitard's extension "Latex formula"
(http://www.julienvitard.eu/en/eqtexsvg_en.html) for Inkscape (http://inkscape.org/).

This mod adds a "formula display size factor" which can be used to ensure that,
regardless of the size of the paper selected for the open document in Inkscape,
the Latex formulas will always be rendered with the same font/symbol size.

The problem with the original extension "Latex formula" consists in the fact
that formulas are rendered with a size which is a function of the size of the 
paper selected for the open document in Inkscape, which may lead to formulas
with different size when the paper size is changed and new formulas are added.

How to use:

1) install pstoedit (http://www.pstoedit.net/pstoedit)
2) add pstoedit to the PATH environment variable
3) copy the *inx and *py files to "C:\Program Files (x86)\Inkscape\share\extensions" (or equivalent)
4) start Inkscape and click Extensions -> Latex formula modded by frm
5) choose for some value of the "formula display size factor" and stick with it for
   all formulas you enter in that document.
