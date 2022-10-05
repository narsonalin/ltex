#!/usr/bin/env python
# coding: utf-8

import os, sys

def man():
    print ("Usage: ltex.py <option> file")
    print ("option is either")
    print ("\t -m: if need to compile with the minted package")
    print ("\t -p: for only pdf creation")
    print ("\t -b: compiles with the bibliography")
    print ("\t -r: compiles with the references to figures, tables, etc...")
    print ("\t -c: doesn't open the pdf afterward")
    print ("\t -g: compiles with the glossary ")
    print ("\t -i: compiles with the index ")
    print ("\t --help: display man")
    print ("default is pdf")

n = len(sys.argv)
do_something = True
if n < 1:
    man()

else:
    try:
        if sys.argv[1] == '--help':
            man()
            do_something = False
        elif sys.argv[1][0] == '-':
            options = sys.argv[1]
            if sys.argv[2][-3:] == 'tex':
                file = sys.argv[2][:-4]
            elif sys.argv[2][-1] == '.':
                file = sys.argv[2][:-1]
            else:
                file = sys.argv[2]
        else:
            options = ''
            if sys.argv[1][-3:] == 'tex':
                file = sys.argv[1][:-4]
            elif sys.argv[1][-1] == '.':
                file = sys.argv[1][:-1]
            else:
                file = sys.argv[1]

        if do_something:
            flag = ""
            if "m" in options:
                flag += "-shell-escape "
            if "p" in options:
                flag += "--enable-write18 "

            os.system("pdflatex " + flag + file + ".tex")

            if "g" in options:
                os.system("makeglossaries " + file)
                if len(options) == 2:
                    os.system("pdflatex " + flag + file + ".tex")
            if "r" in options:
                os.system("pdflatex " + flag + file + ".tex")
            if "i" in options:
                os.system("makeindex " + file + ".tex")
                os.system("pdflatex " + flag + file + ".tex")
            if "b" in options:
                os.system("bibtex " + file)
                os.system("pdflatex " + flag + file + ".tex")
                os.system("pdflatex " + flag + file + ".tex")
            if "c" not in options:
                os.system("xdg-open " + file + ".pdf &")
    except:
        man()
        do_something = False
