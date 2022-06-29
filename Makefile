TARGET := popos

all:
	latexmk -pdf -latexoption=-halt-on-error \
		-latexoption=-file-line-error \
		-latexoption=-interaction=nonstopmode \
		-latexoption=-synctex=1 $(TARGET).tex

clean:
	rm -f $(TARGET).pdf *~ .*~
	rm -f *.aux *.bbl *.blg *.fdb_latexmk *.fls *.log *.out *.synctex.gz

.PHONY: all clean
