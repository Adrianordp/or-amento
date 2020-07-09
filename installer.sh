pyinstaller -D \
        --add-data="fontawesome.sty:." \
        --add-data="fontawesomesymbols-xeluatex.tex:." \
        --add-data="fontawesomesymbols-generic.tex:." \
        --add-data="fontawesomesymbols-pdftex.tex:." \
        main.pyw
