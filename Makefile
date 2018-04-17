zip:
	make -C tex/ clean
	zip -r tex tex

clean:
	$(RM) tex.zip
	$(RM) arxiv.zip

arxiv:
	make -C tex/ arxiv
	mv tex/arxiv.zip .

response:
	make -C ped-response