BASE     = MercuryNumerical
LTX      = pdflatex
BTX      = bibtex

.DEFAULT_GOAL := ${BASE}.pdf

%.pdf:	%.tex
	TEXINPUTS=${STYPATH} ${LTX} $<
	TEXINPUTS=${STYPATH} ${LTX} $<

.PHONY: clean
clean:
	-rm -f ${BASE}.aux
	-rm -f ${BASE}.bbl
	-rm -f ${BASE}.blg
	-rm -f ${BASE}.log
	-rm -f ${BASE}.tdo
	-rm -f ${BASE}.out
	-rm -f ${BASE}.pdf

