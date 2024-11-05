#!/usr/bin/python
#
# apply_ieee_citation_style.py 
#    An utility script to automatically substitute full journal names with abbreviated
#    journal names. Actually this is a more generic utility which may perform automated
#    multiple text substitutions loading the mapping from external files.
#
# Author: Francesco Montorsi (c) 2012
# Creation date: 25/12/2012
#

import os
import re
import sys
import argparse


# constants
# ---------

full_len_fname = "IEEEfull.bib"      # by Michael Shell
abbr_len_fname = "IEEEabrv.bib"      # by Michael Shell

# my additional files:
abbr_generic_fname = "IEEEabrv_generic.bib"
regex_substitutions_fname = "IEEEregex.bib"


# utility functions
# -----------------

def load_names_from_IEEEbib(fname):

    # constants
    
    prefix = "@STRING{"
    divider = " = \""
    closer = "\""
    ret = dict()

    # run a super-simple BibTeX parser for @STRING{} placeholders
    
    with open(fname) as f:
        #if not any(re.search(pat, line) for line in f):
        #    return # pattern does not occur in file so we are done.
        content = f.readlines()
        for line in content:
            if line.startswith(prefix):
                #print(line)
                try:
                    line_parsed = line[len(prefix):]
                    eqsignidx = line_parsed.index(divider)   # raises a ValueError if not found
                except ValueError as e:
                    print("Error while parsing:\n  %s\n" % line_parsed)
                    return None
                    
                #key = line_parsed[:eqsignidx].strip()
                key = line_parsed[:eqsignidx].lstrip()             # do not strip spaces on the right
                if key[-1] == "\"":
                    key = key[:-1]
                line_parsed = line_parsed[eqsignidx+len(divider):]
                
                try:
                    closeridx = line_parsed.index(closer)    # raises a ValueError if not found
                    #name = line_parsed[:closeridx].strip()
                    name = line_parsed[:closeridx].lstrip()            # do not strip spaces on the right
                except ValueError as e:
                    print("Error while parsing:\n  %s\n" % line_parsed)
                    return None
                
                # simple fix for {IEEE} occurrence
                name = name.replace("{IEEE}", "IEEE")
                name = name.replace("{IEEE/TMS}", "IEEE/TMS")
                name = name.replace("{IEEE/ASME}", "IEEE/ASME")
                name = name.replace("{IEEE/ACM}", "IEEE/ACM")
                name = name.replace("{IEEE/OSA}", "IEEE/OSA")

                #print("key: %s" % key)
                #print("content: %s" % name)
                
                # eventually strip leading/closing quotes
                key = key.strip("\"'")
                name = name.strip("\"'")
                
                #print(key, name)
                ret[key] = name
                
    print("  ...found %d STRING placeholders" % len(ret))
    return ret

    
def file_replace(fname, dict_first, dict_second, dict_regex, write_out):

    # constants
    
    journal_prefix = "journal"
    conference_prefix = "booktitle"
    
    # run a super-simple BibTeX parser for journal placeholders

    sorted_keys_first = sorted(dict_first.keys())
    sorted_keys_second = sorted(dict_second.keys())
      # IMPORTANT: if we don't sort, then running this script many times with the same input
      #            may lead to different results because Python does not grant any explicit order
      #            of the keys of the dictionary!
      
    substituted_first = []
    substituted_second = []
    substituted_regex = []
    max_len = 73
    
    count = 0
    with open(fname,"r",encoding="utf8") as f:
        root_ext = os.path.splitext(fname)
        out_fname = root_ext[0] + ".tmp" + root_ext[1]
        out = open(out_fname, "w", encoding="utf8")
        for line in f:
        
            bibtex_keyword = line.strip().split("=")
            #print("bibtex_keyword: ",bibtex_keyword)
            
            # first of all, do simple string substitutions ONLY on
            # selected BibTeX entries:
            if bibtex_keyword[0].strip().lower() == journal_prefix.lower() or \
               bibtex_keyword[0].strip().lower() == conference_prefix.lower():
            
                #print("|" + line + "|")
                fix_applied = False
                
                if line.endswith("},\n"): # or line.endswith("}, \n"):
                    line = line[:-3] + " },\n"
                    #print("fixed as %s" % line)
                    fix_applied = True
                        # small trick to force IEEEabrv_generic to match also words at the end of the key
            
                # do substitutions with the first mapping dictionary
                for s_to_search in sorted_keys_first:
                    s_after = dict_first[s_to_search]
                    new_line = line.replace(s_to_search,s_after)
                    if new_line != line:
                        substituted_first.append(s_to_search)
                        line = new_line
                        
                # do substitutions with the second mapping dictionary
                for s_to_search in sorted_keys_second:
                    s_after = dict_second[s_to_search]
                    new_line = line.replace(s_to_search,s_after)
                    if new_line != line:
                        substituted_second.append(s_to_search)
                        line = new_line
                
                if fix_applied and line.endswith(" },\n"):
                    line = line[:-4] + "},\n"
                
            # then, on every line of the BibTeX file, apply regex substitutions:
            for regex_to_search in dict_regex.keys():
                s_after = dict_regex[regex_to_search]
                regex_result = regex_to_search.subn(s_after, line)
                #print("substituted")
                #print(regex_result)
                if regex_result[1] > 0 and line != regex_result[0]:
                    # NOTE: often regex_result[1] > 0 but the line has not really been changed, so that
                    #       the second check is important!
                    
                    substituted_regex.append(regex_to_search)
                    line = regex_result[0]
                        
            # NOTE: running two passes of substitutions is not the same
            #       thing as merging the two dictionaries together, which would
            #       be easily done as 
            #            dict_first.update(dict_second)
                    
            out.write(line)
            
            
        out.close()
        f.close()
        
        count = len(substituted_first) + len(substituted_second) + len(substituted_regex)
        print("  ...perfomed %s substitutions in the original file:" % count)
        for s_to_search in substituted_first:
            str = "    %s => %s" % (s_to_search, dict_first[s_to_search])
            if len(str) > max_len:
                str = str[:max_len] + "[...]"
            print(str)
        for s_to_search in substituted_second:
            str = "    %s => %s" % (s_to_search, dict_second[s_to_search])
            if len(str) > max_len:
                str = str[:max_len] + "[...]"
            print(str)
        # for s_to_search in substituted_regex:
            # str = "    %s => %s" % (s_to_search, dict_regex[s_to_search])
            # if len(str) > max_len:
                # str = str[:max_len] + "[...]"
            # print(str)
        
        
        
        if count == 0:
            print("  ...no changes done; output won't be saved.")
            os.remove(out_fname)
        else:
            if write_out:
                print("  ...saving processed text in the original file '%s'." % fname)
                os.remove(fname)
                os.rename(out_fname, fname)
            else:
                print("  ...saving processed text in '%s'" % out_fname)
        
    return count

def do_apply(file_to_be_styled, IEEEbib_path, write_out):
            

    # try to open the given file to check if we can proceed
    print("Testing access to '%s'..." % file_to_be_styled)
    try:
        with open(file_to_be_styled) as f: pass
    except IOError as e:
        print("Cannot open %s!" % file_to_be_styled)
        exit(1)
        
    print("  ...it can be accessed!")
    
    
    if IEEEbib_path[-1] != os.sep:
        IEEEbib_path = IEEEbib_path + os.sep

        
    # load abbreviations & full-length names
    print("Now processing '{0}' to load full-length journal names.".format(full_len_fname))
    full_len_dict = load_names_from_IEEEbib(IEEEbib_path + full_len_fname)
    if full_len_dict == None:
        print("...aborting")
        return
    
    print("Now processing '{0}' to load abbreviated length journal names.".format(abbr_len_fname))
    abbr_len_dict = load_names_from_IEEEbib(IEEEbib_path + abbr_len_fname)
    if abbr_len_dict == None:
        print("...aborting")
        return
        
    # now build the direct mapping  full len name <-> abbreviated name
    mapping = dict()
    for key in full_len_dict.keys():
        if key in abbr_len_dict:
            mapping[full_len_dict[key]] = abbr_len_dict[key]
    print("Mapping full len names <-> abbr names has %d entries" % len(mapping))
    #print(mapping)


    # load directly mapped strings to substitute
    print("Now processing '{0}' to load direct-mapping substitutions.".format(abbr_generic_fname))
    abbr_generic_dict = load_names_from_IEEEbib(IEEEbib_path + abbr_generic_fname)
    if abbr_generic_dict == None:
        print("...aborting")
        return    
    #print(abbr_generic_dict)
    print("Map of additional substitutions has %d entries" % len(mapping))

    # merge two dicts
    #mapping.update(abbr_generic_dict)

    # load regex strings to substitute
    print("Now processing '{0}' to load direct-mapping substitutions.".format(regex_substitutions_fname))
    regex_dict = load_names_from_IEEEbib(IEEEbib_path + regex_substitutions_fname)
    if regex_dict == None:
        print("...aborting")
        return
        
    regex_dict_ok = {}
    for key in regex_dict.keys():
        is_valid_regex = False
        
        try:
            regex = re.compile(key, re.IGNORECASE)
            is_valid_regex = True
            #print("%s is a regex!" % s_to_search)
        except:
            print("%s is NOT a valid regex!" % key)
            pass      # do nothing
            
        regex_dict_ok[regex] = regex_dict[key]
          # save the compiled regex
    print("Map of regex substitutions has %d entries" % len(regex_dict_ok))


    # now replace the occurrences of full-length names with 
    print("Now replacing all full len occurrences with abbr names in the input file...")
    return file_replace(file_to_be_styled, mapping, abbr_generic_dict, regex_dict_ok, write_out)




if __name__ == "__main__":

    # check arguments
    # ---------------

    if sys.version_info[0]<3:
        print("Sorry, Python >= 3.0.0 is required for this script to run.")
        exit(1)

    desc = """Replaces in the 'file_name' all occurrences of full-length IEEE journal names with abbreviated ones.
    Note that full-length journal names are loaded from '%s', abbreviated ones from '%s'.
    Conference names and journal names will also be abbreviated using standard IEEE abbreviations contained in '%s'.
    Finally, each regular expression in '%s' will be tested against each line of 'file_name'.
    """  % (full_len_fname,abbr_len_fname,abbr_generic_fname,regex_substitutions_fname)

    epi = "\nCopyright (c) 2012 by Francesco Montorsi (http://frm.users.sourceforge.net/)"

    parser = argparse.ArgumentParser(description=desc,epilog=epi)
    parser.add_argument('file_name', help='The file to be processed')
    parser.add_argument('-w', action='store_true', default=False, 
                        help='Write processed text in the original file (by default output is stored in a temporary file)')

    my_location = os.path.abspath(os.path.dirname(sys.argv[0]))
    args = parser.parse_args()
    #print(args)

    file_to_be_styled = args.file_name
    write_out = args.w


    # main
    # ----

    do_apply(file_to_be_styled, my_location  + os.sep + "style", write_out)

    
# else: we are called from another Python script!

