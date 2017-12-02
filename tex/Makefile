BASE     = MercuryNumerical
STYPATH  = :sty
LTX      = pdflatex
BTX      = bibtex

.PHONY: clean pristine veryclean



%.pdf:	%.tex
	TEXINPUTS=${STYPATH} ${LTX} $<
	TEXINPUTS=${STYPATH} ${LTX} $<

all:	${BASE}.pdf
	cp ${BASE}.pdf ../

clean:
	-rm -f ${BASE}.aux
	-rm -f ${BASE}.bbl
	-rm -f ${BASE}.blg
	-rm -f ${BASE}.log
	-rm -f ${BASE}.tdo
	-rm -f ${BASE}.pdf
	-rm -f ${BASE}.out


pristine: clean
	-rm -f ${BASE}.pdf

veryclean: pristine
