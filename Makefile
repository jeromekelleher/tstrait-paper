all: paper.pdf

paper.pdf: paper.tex paper.bib
	pdflatex -shell-escape paper.tex
	bibtex paper
	pdflatex -shell-escape paper.tex
	pdflatex -shell-escape paper.tex

paper.ps: paper.dvi
	dvips paper

paper.dvi: paper.tex paper.bib
	latex paper.tex
	bibtex paper
	latex paper.tex
	latex paper.tex

.PHONY: spellcheck
spellcheck: aspell.conf
	aspell --conf ./aspell.conf --check paper.tex

clean:
	rm -f *.pdf
	rm -f illustrations/*.pdf
	rm -f illustrations/*.svg
	rm -f *.log *.dvi *.aux
	rm -f *.blg *.bbl

mrproper: clean
	rm -f *.ps *.pdf
