**INSTALLATION**

Just add the path to your $PATH. Example:

    export PATH="/home/username/ltex:$PATH"

**USAGE**

Usage: 

    ltex.py <option> file

`<option>` is either
`-m`: if need to compile with the minted package
`-p`: for only pdf creation
`-b`: compiles with the bibliography
`-r`: compiles with the references to figures, tables, etc...
`-c`: doesn't open the pdf afterward
`-g`: compiles with the glossary 
`-i`: compiles with the index 
`--help`: display man

Examples:
You have a `tex` source containing a file `main.tex` and two other files included in `main.tex`: `file1.tex` and `file2.tex`.
- You just want to compile your tex file. Then execute:

    ltex.py main.tex

But if you don't have time, you can equivalently execute

    ltex.py main.

or 
    
    ltex.py main

- Imagine you have some hypertext references to figures, tables, etc. Then you need to compile your files twice, or just run:

       ltex.py -r main
    
- If you have a bibliography, the process is painful. You would need to compile once with pdflatex, then with bibtex, then twice with pdflatex. With `ltex.py`, just run

       ltex.py -b main

- You use the `minted` package ? Easy ! Add the `-m` option, e.g.:

       ltex.py -bm main

(of course, you can combine options.)