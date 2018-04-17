BASE     = response
LTX      = pdflatex
REV      = $(shell git log -n 1 --pretty=format:"%H")

.DEFAULT_GOAL := ${BASE}.pdf

%.pdf:	%.tex
	${LTX} $<
	${LTX} $<

.PHONY: diff
diff:
	latexdiff-vc --git --pdf -r ${REV} ${BASE}.tex
	$(RM) ${BASE}-diff${REV}.blg
	$(RM) ${BASE}-diff${REV}.tex
	$(RM) ${BASE}-diff${REV}.out

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
	$(RM) ${BASE}-diff${REV}.blg
	$(RM) ${BASE}-diff${REV}.tex
	$(RM) ${BASE}-diff${REV}.out
	$(RM) ${BASE}-diff${REV}.pdf

.PHONY: cleanTex
cleanTex:
	$(RM) ${BASE}.aux
	$(RM) ${BASE}.blg
	$(RM) ${BASE}.log
	$(RM) ${BASE}.tdo
	$(RM) ${BASE}.out
	$(RM) ${BASE}.pdf
	$(RM) ${BASE}.synctex.gz
	$(RM) "${BASE}.synctex(busy)"
	$(RM) ${BASE}-diff${REV}.blg
	$(RM) ${BASE}-diff${REV}.tex
	$(RM) ${BASE}-diff${REV}.out
	$(RM) ${BASE}-diff${REV}.pdf