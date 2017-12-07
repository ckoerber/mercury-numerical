BASE     = MercuryNumerical
LTX      = pdflatex
BTX      = bibtex

.DEFAULT_GOAL := ${BASE}.pdf

%.pdf:	%.tex
	TEXINPUTS=${STYPATH} ${LTX} $<
	TEXINPUTS=${STYPATH} ${LTX} $<

.PHONY: clean
clean:
	$(RM) ${BASE}.aux
	$(RM) ${BASE}.bbl
	$(RM) ${BASE}.blg
	$(RM) ${BASE}.log
	$(RM) ${BASE}.tdo
	$(RM) ${BASE}.out
	$(RM) ${BASE}.pdf
	$(RM) ${BASE}.synctex.gz

