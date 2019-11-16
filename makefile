%.pdf: %.tex
	xelatex -shell-escape -8bit $<
	xelatex -shell-escape -8bit $<
clean:
	rm -r *.aux *.log _minted-* *.toc
