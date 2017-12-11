zip:
	make -C tex/ clean
	zip -r tex tex

clean:
	$(RM) tex.zip