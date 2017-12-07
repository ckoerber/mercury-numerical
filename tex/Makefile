BASE     = MercuryNumerical
LTX      = pdflatex
BTX      = bibtex
THISBIB  = References.bib

.DEFAULT_GOAL := ${BASE}.pdf

%.pdf:	%.tex %.bbl
	${LTX} $<
	${LTX} $<

%.bbl:	%.aux ${THISBIB}
	${BTX} $<

%.aux:	%.tex
	${LTX} $<

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

