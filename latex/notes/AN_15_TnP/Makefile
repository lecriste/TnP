all:	pdf

pdf:	*.tex
	eval `../tdr runtime -sh`
	tdr -style an b AN-15-TnP 
	acroread ../tmp/AN-15-TnP_temp.pdf &

clean:
	rm -rf ../tmp/*
