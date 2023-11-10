all: paper.pdf

paper.pdf: paper.tex paper.bib
	pdflatex -shell-escape paper.tex
	bibtex paper
	pdflatex -shell-escape paper.tex
	pdflatex -shell-escape paper.tex

.PHONY: spellcheck
spellcheck: aspell.conf
	aspell --conf ./aspell.conf --check paper.tex

clean:
	rm -f *.pdf
	rm -f *.log *.aux *.out
	rm -f *.blg *.bbl
