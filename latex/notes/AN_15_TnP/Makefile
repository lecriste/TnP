all:	pdf

pdf:	*.tex
	#eval `../../tdr runtime -tcsh`
	tdr -style an b AN_EarlyBHadron2015 
	open ../tmp/AN_EarlyBHadron2015_temp.pdf

clean:
	rm -rf ../tmp/*
