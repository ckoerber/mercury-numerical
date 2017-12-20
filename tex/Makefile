BASE     = MercuryNumerical
LTX      = pdflatex
BTX      = bibtex
THISBIB  = References.bib
REV      = $(shell git log -n 1 --pretty=format:"%H")

.DEFAULT_GOAL := ${BASE}.pdf

%.pdf:	%.tex %.bbl
	${LTX} $<
	${LTX} $<

%.bbl:	%.aux ${THISBIB}
	${BTX} $<

%.aux:	%.tex
	${LTX} $<

.PHONY: diff
diff:
	latexdiff-vc --git --pdf -r ${REV} ${BASE}.tex
	rm -f ${BASE}-diff${REV}.tex
	rm -f ${BASE}-diff${REV}.out

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
	$(RM) "${BASE}.synctex(busy)"

