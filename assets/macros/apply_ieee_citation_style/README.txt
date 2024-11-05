README
======

This small Python script is useful to automatically abbreviate journal and
conference names in BibTeX files, following IEEE style rules
(see http://www.ieee.org/documents/ieeecitationref.pdf).

Credits go to Michael Shell for producing IEEEfull.bib and IEEEabr.bib containing
all IEEE journal full and abbreviated names.
The script also contains some additional logic to fix conference names and to
fix common annoyances in .bib files (like the use of double curly brackets around
paper titles).

Francesco Montorsi - 30 dec 2012



HOW TO RUN (Windows):
=====================

1) install Python (http://python.org/), version 3.0.0 or higher
2) open a command prompt and type:

     > cd folder_containing_apply_ieee_citation_style_script
     
     > apply_ieee_citation_style.py   example.bib
     
   Then look at the differences between "example.bib" (which won't be touched)
   and the "example.tmp.bib" file created by the script. Nice, isn't it? :)
   
   You can also use batch_apply_ieeestyle_and_winmerge.py to automate the process
   of calling the script file on each .bib of a certain folder.
   batch_apply_ieeestyle_and_winmerge is handy because it can also launch
   a diffing tool to check if the script did a good job.

   
HOW TO RUN (Linux):
===================

1) open a console and type:
     $  python --version
   and check that python is >= 3.0.0; otherwise install the updated python.
   
2) type:

     $ cd folder_containing_apply_ieee_citation_style_script
     
     $ apply_ieee_citation_style.py   example.bib

   Then look at the differences between "example.bib" (which won't be touched)
   and the "example.tmp.bib" file created by the script. Nice, isn't it? :)
   
   You can also use batch_apply_ieeestyle_and_winmerge.py to automate the process
   of calling the script file on each .bib of a certain folder.
   batch_apply_ieeestyle_and_winmerge is handy because it can also launch
   a diffing tool to check if the script did a good job.
   
