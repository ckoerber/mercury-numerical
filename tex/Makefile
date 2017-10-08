BASE     = MercuryNumerical
STYPATH  = :sty
LTX      = pdflatex
BTX      = bibtex

.PHONY: clean pristine veryclean

all:	${BASE}.pdf
	cp ${BASE}.pdf ../

%.pdf:	%.tex
	TEXINPUTS=${STYPATH} ${LTX} $<

$(BASE).pdf: $(BASE).bbl

%.bbl:  %.bib
	TEXINPUTS=${STYPATH} ${LTX} $*.tex
	BSTINPUTS=${STYPATH} ${BTX} $*

clean:
	-rm -f ${BASE}.aux
	-rm -f ${BASE}.bbl
	-rm -f ${BASE}.blg
	-rm -f ${BASE}.log

pristine: clean
	-rm -f ${BASE}.pdf

veryclean: pristine
