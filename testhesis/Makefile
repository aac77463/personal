ifeq ($(shell uname -s),Linux)
    PDFREADER=evince
else
    PDFREADER=open
endif

default: paper

paper:	thesis.tex 
	pdflatex -shell-escape thesis
#	bibtex thesis
	pdflatex -shell-escape thesis
	$(PDFREADER) thesis.pdf &
clean:
	rm -f *.log *.aux *.dvi *.blg
