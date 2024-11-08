---
layout: single
permalink: /scripts/
title:  "My Scripts & Macros"
toc: true
date:   2024-11-05
author_profile: true
---

Nowadays, all operating systems and many programs allow at least a basic type of scripting; so, scripts are useful and ready-made scripts are even more ;-)

## Bash

As any Linux user knowns, the shell is always the most used program. And the [BASH](https://www.tldp.org/LDP/abs/html/ "Click to go at the famous Advanced Bash Scripting Guide") shell is one of the most customizable program: the `.bashrc` script is executed each time a new BASH session begins.

1.  **[.bashrc](/assets/macros/bashrc)**: the Ubuntu default .bashrc plus some _aliases_ for my most used commands for **directory navigation**, **source code grepping**, etc
    
## Python

1.  **[process\_skype\_db.py](/assets/macros/process_skype_db.py)**: processes one or more Skype main.db files merging chat messages, removing duplicates, filtering based on the chat partecipants, splitting chat sessions under reasonable criteria (!); finally formats the result in a nice readable HTML page!
    
2.  **[ebook\_manager.py](/assets/macros/ebook_manager.zip)**: keeps track of your PDF library and generates a list of the files it contains, synchronize two or more ebook "repositories", validates the book filenames and more!
    
3.  **[apply\_ieee\_citation\_style.py](/assets/macros/apply_ieee_citation_style.zip)**: performs automated substitutions in the given BibTex file to comply with IEEE Citation Style guide
    

## Inkscape

1.  **[frm\_eqtexsvg.py](/assets/macros/frm_eqtexsvg.zip)**: a simple modification of [Julien Vitard's extension "Latex formula"](https://www.julienvitard.eu/en/eqtexsvg_en.html) for [Inkscape](https://inkscape.org/). This mod adds a "formula display size factor" which can be used to ensure that, regardless of the size of the paper selected for the open document in Inkscape, the Latex formulas will always be rendered with the same font/symbol size.
    

## Cadsoft EAGLE

1.  **[lbr-merge.zip](/assets/macros/lbr-merge.zip)**: this ZIP contains the lbr-contents-dump.ulp script which allows dumping all the contents of a library as SCR files and the lbr-merge.ulp script which allows to merge two libraries into one (I use these script to keep in sync different versions of the same library).
    

## My Microsoft VisualC++© macros

1.  **[ReIndentAll](/assets/macros/reindentall.dsm.txt)**: applies the `Edit->Advanced->Tabify` + `Edit->Advanced->Format` on all open docs starting from line 24; close all windows using Window->Close All then open using SHIFT key all the files you want. Then, run this macro.
    
2.  **[RemoveEmptyLines](/assets/macros/removeemptylines.dsm.txt)**: Removes all the empty lines from the selected portion of the document.
    
3.  **[MakeCodeNicer](/assets/macros/reformatcode.dsm.txt)**: Reformats the source code to look nicer, the way I like it.
    
4.  **[RemoveTrailingSpaces](/assets/macros/removetrailingspaces.dsm.txt)**: Removes the trailing spaces from the selected lines.
    
5.  **[RemoveCInlinedComments](/assets/macros/removecinlinedcomments.dsm.txt)**: Removes the C comments replacing them with C++ comments
    
6.  **[MakeUnicodeCompatible](/assets/macros/makeunicodecompatible.dsm.txt)**: Smartly adds the wxT() macro around all literals to make them Unicode compatibles.
    

## My Microsoft Word© macros

1.  **[DeleteHyperlinks](/assets/macros/deletehyp.txt)**: Removes all the hyperlinks from the selected portion of document.
    
2.  **[DeleteEmptyLines](/assets/macros/deleteemptylines.txt)**: Just does what the name says :)