import re
import os
import string
import glob

def main(argv):
	import sys
	from optparse import OptionParser

	usage = "Usage: %prog  tex-file commands-file"
	global opts
	parser = OptionParser(usage=usage)
	(opts, args) = parser.parse_args()
	texfile = args[0]
	cmdfile = args[1]

	p = re.compile('\\\\(re)*newcommand\s*{\s*(.*?)\s*}') # consider looking for \def as well
	cmds = dict()
	with open(cmdfile) as fin:
		body = fin.read()
		m = p.findall(body)
	cmds = {c[1]:0 for c in m} 

	with open(texfile) as tex:
		body = tex.read()
		for cmd in cmds.keys():
			#print(">Looking for {}".format(cmd))
			m = re.findall('('+cmd.replace('\\','\\\\')+')'+'[^a-zA-Z]',body)
			if m: #need to protect backslashes as they get interpreted as control characters otherwise
				cmds[cmd] = len(m)

	unused = [key for key in cmds.keys() if cmds[key] == 0]
	print("Commands unused in main TeX file: ")
	for u in unused:
		print(u)

	used = [key for key in cmds.keys() if cmds[key] != 0]
	print("----------------\nCommand name stems found in main TeX file: ")
	used = sorted(used, key = lambda x: cmds[x])
	for u in used:
		print('{:>2} occurrences of {}'.format(cmds[u], u))
	print("----------------\nCommands not used in main TeX file: ")
	unused = [key for key in cmds.keys() if cmds[key] == 0]
	unused = sorted(unused)
	for u in unused:
		print(u)







if __name__ == "__main__":
	import sys
	main(sys.argv[1:])

