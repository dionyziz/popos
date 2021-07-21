SOURCES := $(shell find . -iname '*.tex' -o -iname '*.bib' -o -iname '*.sty' -o -iname '*.cls' -o -ipath '*figures/*.pdf')

.PHONY: all clean

all: popos.pdf

popos.pdf: $(SOURCES)
	rm -f *.glsdefs
	pdflatex --halt-on-error popos.tex
	bibtex popos
	pdflatex --halt-on-error popos.tex
	pdflatex --halt-on-error popos.tex

clean:
	rm -f *.aux *.log *.out *.cfg *.glo *.idx *.toc *.ilg *.ind *.lof *.lot *.bbl *.blg *.gls *.cut *.hd *.dvi *.ps *.thm *.rpi *.d *.fls *.pyc *.fdb_latexmk *.sls *.slo *.slg *.glsdefs *.gls *.glg *.glo *.ist
	rm -Rf latex.out
	rm -Rf popos.pdf
