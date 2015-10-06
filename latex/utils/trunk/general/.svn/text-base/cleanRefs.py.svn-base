#!/usr/bin/env python

"""Script to check standard CMS references.
    """
from __future__ import print_function

__version__ = "$Revision: Test$"
#$HeadURL: $
#$Id:$

import re
import shutil
import socket
import sys
import os
import io
import string
import subprocess
import collections


    

def f5(seq, idfun=None): 
    """From http://www.peterbe.com/plog/uniqifiers-benchmark. Fast method to create a unique list while preserving order (otherwise just use a set)
        """
    # order preserving
    if idfun is None:
       def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
       marker = idfun(item)
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
    return result
def checkForDuplicates(checkItems, checkTag):
    # duplicate entry check (use doi as unique marker)
    # python 2.7 and later only
    if (sys.version_info[0] > 2 or (sys.version_info[0]==2  and sys.version_info[1]>6)) :
        chklist = [v[checkTag] for v in (vv[1] for i, vv in checkItems.items()) if checkTag in v]
        if (len(chklist) > len(set(chklist))):
            print('Have duplicate ',checkTag,'s',sep="")
            print([v for v, vv in collections.Counter(chklist).items() if vv > 1])
    else:
        chklist = [v[checkTag] for v in (vv[1] for i, vv in checkItems.iteritems()) if checkTag in v]
        if (len(chklist) > len(set(chklist))):
            print('Have duplicate ',checkTag,'s',sep="")
            for i in range(len(chklist)): #need ordered iterator
                if chklist[i] in chklist[i+1:]:
                    print(chklist[i])

def extractBalanced(text, delim):
    """ Extract a delimited section of text: available opening delimiters are '{', '"', and  '<'.
        Does not check for escaped delimeters. """
    delims = {"{":"}", '"':'"', "<":">"} # matching closing delims
    if not(delim in delims.keys()):
        pout = text.find(',')+1
        pin = 0
    else:
        pin = text.find(delim) + 1
        if pin == 0: 
            print('Bad delim')
        nbraces = 1;
        pout = pin
        while nbraces > 0:
            if pout > len(text): 
                print("extractBalanced >>> Error parsing text: {0}".format(text[pin:pin+min([len(text),15])]))
                return [0, None] # probably unmatched } inside TeX comment string
            if text[pout:pout+2] == '\\'+delim: # look for escaped delim
                pout += 2
            else:
                if text[pout:pout+2] == '\\'+delims[delim]:
                    pout += 2
                else:
                    if text[pout:pout+1] == delims[delim]:
                        nbraces -= 1
                    elif text[pout:pout+1] == delim:
                        nbraces += 1
                    pout += 1
    return [pout, text[pin:pout-1]]

class cleanError(Exception):
    """Base class for exceptions in this module."""
    pass

class cleanRefs:

    def __init__(self, tag, baseDir, verbose, arxiv):
        self._tag = tag
        self._refs = [] # references from paper: bibkey
        self._verbosity = verbose
        self._arxiv = arxiv
        self._bib = {} #dictionary (keyed on bibkey in bib file (same as used in _refs)) which holds the citation tuple (artType, {fieldName:fieldValue}), key is 
        self._rules =[ ('VOLUME',re.compile('[A-G]\s*\d'),'Volume with serial number','Error'),
                       ('VOLUME',re.compile(r'\\bf'), r'Volume with \bf','Error'), # change to be any control sequence
                       ('VOLUME',re.compile('CMS'), 'PAS as article? Please use TECHREPORT','Error'),
                       ('AUTHOR',re.compile('~'), 'Found author string with explicit spacing...normally not good!','Warning'),
                       ('AUTHOR',re.compile('[A-Z]\.[A-Z]'),'Author with adjacent initials','Error'),
                       ('AUTHOR',re.compile('et al\.'), 'Author with explicit et al','Error'),
                       ('AUTHOR',re.compile(r'\\etal'), 'Author with explicit etal','Error'),
                       ('AUTHOR',re.compile(r'Adolphi'), 'Adolphi: this may be an error in attribution for the CMS detector paper. Please check','Warning!'),
                       ('JOURNAL',re.compile('CMS'), 'PAS as article? Please use TECHREPORT','Error'),
                       ('JOURNAL',re.compile('[A-z]\.[A-z].'), 'Missing spaces in journal name','Error'),
                       ('JOURNAL',re.compile('~'), 'Found ~ in a journal name--don\'t override BibTeX','Error'),
                       ('ISSUE',re.compile('.*'), 'Don\'t normally use the ISSUE field','Warning'),
                       ('EPRINT',re.compile('(?<!/)[0-9]{7}'), 'Old style arXiv ref requires the archive class (see http://arxiv.org/help/arxiv_identifier)','Error'),
                       ('TITLE',re.compile('(?i)MadGraph.*v4'), 'MadGraph v5 references are preferred over v4 (unless v4 was what was actually used)','Warning'),                       
                       ('TITLE',re.compile('(?i)MadGraph.*5'), 'Consider using arXiv:1405.0301, MadGraph5_aMC@NLO?','Warning'),                       
                       ('TITLE',re.compile('POWHEG'), 'Is POWHEG (BOX) correctly referenced? See http://powhegbox.mib.infn.it','Warning'),                       
                       ('DOI',re.compile('10.1088/1126-6708/2002/06/029|10.1088/1126-6708/2003/08/007|10.1088/1126-6708/2006/03/092|10.1088/1126-6708/2008/07/029|10.1007/JHEP01\(2011\)053'), 'MC@NLO citation found. Did you get them all? See http://www.hep.phy.cam.ac.uk/theory/webber/MCatNLO/ near the bottom','Warning'),
                       ('DOI',re.compile('doi|DOI'), 'Do not include dx.doi.org','Error'),
                       ('DOI',re.compile(','), 'Only one doi in the DOI field','Error'),
                       ('DOI',re.compile(' '), 'No spaces in the DOI field','Error'),
                       ('COLLABORATION',re.compile(r'Collaboration'), r'Should not normally use Collaboration: already in the format','Error'), 
                       ('LANGUAGE',re.compile('.*'),'Language entry requires loading the babel package, which is not used','Error for APS'),
                       ('PAGES',  re.compile('-'), 'Range in page field: we only use first page','Warning') ] # rules for checking format: field, compiled re, message. (Add severity?)
        self._blankCheck = re.compile(r'^\s+$')
        # field ordering not yet implemented (if ever)
        self._fieldOrder = ('AUTHOR','COLLABORATION','TITLE','DOI','JOURNAL','VOLUME','TYPE','NUMBER','YEAR','PAGES','NOTE','URL','EPRINT','ARCHIVEPREFIX') #SLACCITATION always last
        # self._baseDir = r'C:\Users\George Alverson\Documents\CMS\tdr2\utils\trunk\tmp\\'
        self._baseDir = baseDir

        
    def getRefList(self):
        """Open the aux file and extract the \citation lines, adding the citations contained to an ordered list, which should match the bibtex reference order.
           """
        #\citation{Dawson:1983fw,Beenakker:1996ch,Plehn:2005cq,Beenakker:2009ha}

        # Use \bibcite instead? What about multi-refs?
        #\bibcite{Beenakker:2009ha}{{10}{}{{}}{{}}}
        badrefs = ['REVTEX41Control', 'apsrev41Control']

        file =  os.path.join(self._baseDir,self._tag + '_temp.aux')
        f = io.open(file,'r')
        refs = []
        for line in f:
            if line.startswith('\\citation'):
                newrefs = line[10:len(line)-2].split(',')
                tested = newrefs in badrefs
                if not (newrefs[0] in badrefs):
                    refs.extend(newrefs)
                #print(refs)
        self._refs = f5(refs)
        f.close()

    def getRefs(self):
        """Open the bibfile and scan for "@artType{citation,", where citation matches one we are looking for. Extract the fields
           """
        file = os.path.join(self._baseDir,'auto_generated.bib')
        bibparse = re.compile('^\s*@(\S*)\s*\{',re.MULTILINE) # look for an entire bib entry
        tagparse = re.compile('^\s*(\S*)\s*,',re.MULTILINE) # find the bib tag
        f = io.open(file,'r')
        try:
            bibs = f.read()
        except UnicodeDecodeError:
            print('>>Unicode detected. {0} contains Unicode characters (typically quote marks or ligatures from cut and paste from Word). These are not allowed with the standard BibTex (requires BibTeX8).'.format(file))
            f.close()
            f = io.open(file,'rb')
            text = f.read()
            # check for Unicode characters
            p8 = re.compile(b"[\x80-\xFF]",re.DOTALL)
            pm = p8.findall(text)
            for cand in pm:
                index = text.find(cand)
                print("...Byte {0}: {1}".format(index,text[index:index+25]))
            f.close()
            print('Continuing using Unicode...')
            f = io.open(file,'r',encoding="UTF-8")
            bibs = f.read()
        f.close()
        p = 0
        m = bibparse.search(bibs[p:])
        while m:
            artType = m.group(1).upper()
            [pout, body] = extractBalanced(bibs[p+m.end(0)-1:],'{')
            if (artType != u'COMMENT'):
                t = tagparse.match(body)
                if (t):
                    tag = t.group(1)
                    items = self.parseBody(tag, body[t.end(0):])
                    if tag in self._bib.keys():
                        print(">>> Duplicate entry for {0} being discarded".format(tag))
                    else:
                        self._bib[tag] = (artType, items)
                else:
                    raise cleanError("WARNING: Could not find a tag in string starting with: {0}".format(body.strip()[0:min([len(body.strip()), 25])])) 
            p = p + m.end(0) -1 + pout
            m = bibparse.search(bibs[p:])
        if self._verbosity > 1:
            print("Found {0} entries in the bib file. There were {1} used in the aux file.".format(len(self._bib),len(self._refs)))
            



    def parseBody(self, tag, body):
        """extract the tag and the fields from a citation"""

        # need to protect against "=" inside a URL.
        fieldparse = re.compile('\s*(\S*)\s*=\s*(\S)',re.MULTILINE)
        trim = re.compile('\s{2,}|\n',re.MULTILINE) # what about \r
        p = 0
        m = fieldparse.search(body[p:])
        entry = {}
        while m:
            field = m.group(1).upper()
            [pout, value] = extractBalanced(body[p+m.end(0)-1:],m.group(2))
            value = trim.sub(' ',value)
            entry[field] = value
            p = p + m.end(0) -1 + pout
            m = fieldparse.search(body[p:])

        if self._verbosity > 2:
            for key in entry.keys():
                print("{0}\t: {1}".format(key, entry[key]))

        return entry


    def checkRefs(self):
        """Correlate citations against bib file and check for common errors"""

        print("\n>>> Checking references against CMS rules\n")
        no_collab_rule = re.compile('Collaboration') # to check for a Collaboration as author: not _generally_ okay for papers

        for key in self._refs:
            if not key in self._bib:
                print("Missing bib entry for citation {0}. May be an upper/lower case problem (ignorable)".format(key))
            else:
                #
                # rule-based checks on particular fields
                #
                for rule in self._rules:
                    fieldName = rule[0]
                    if fieldName in self._bib[key][1].keys():
                        m = rule[1].search(self._bib[key][1][fieldName])
                        if m:
                            print("{0}:\t {1} {3}: {2}.".format(key, rule[0], rule[2], rule[3]))
                #
                # ad hoc checks
                #
                if self._bib[key][0]=='TECHREPORT':
                    if not 'URL' in self._bib[key][1].keys():
                        print('{0}:\t Missing URL for Techreport '.format(key))
                if self._bib[key][0]=='ARTICLE':
                    if not 'AUTHOR' in self._bib[key][1].keys():
                        print('{0}:\t Missing AUTHOR '.format(key))
                    else:
                        m = no_collab_rule.search(self._bib[key][1]['AUTHOR'])
                        if m:
                            print("{0}:\t {1} listed as author. Please check this is correct.".format(key, self._bib[key][1]['AUTHOR']))                                           
                    if not 'DOI' in self._bib[key][1].keys():
                        print('{0}:\t Missing DOI '.format(key))
                    if not 'EPRINT' in self._bib[key][1].keys():
                        print('{0}:\t Missing EPRINT '.format(key))
                    if not 'JOURNAL' in self._bib[key][1].keys():
                        print('{0}:\t Missing JOURNAL. Reformat as UNPUBLISHED?'.format(key))
                    else:
                    ## check for wrong number of digits in JHEP volume: must be two
                        if (self._bib[key][1]['JOURNAL']==u'JHEP' or self._bib[key][1]['JOURNAL']==u'J. High Energy Phys.') and not re.match('^[0-9]{2}$',self._bib[key][1]['VOLUME']):
                            print('{0}:\t JHEP volume number given as {1}: should always be exactly two digits (0 left padded).'.format(key,self._bib[key][1]['VOLUME']))
                # number of authors check
                if 'AUTHOR' in self._bib[key][1].keys():
                    etal = re.search(' and others', self._bib[key][1]['AUTHOR']) 
                    authors_list = re.findall(" and ", self._bib[key][1]['AUTHOR'])
                    #print('{0}'.format(self._bib[key][1]['AUTHOR']))
                    nauthors = len(authors_list) + 1
                    if etal:
                        nauthors = nauthors - 1
                    collab = 'COLLABORATION' in self._bib[key][1].keys()
                    # here's the actual test 
                    if (nauthors > 1) and etal and collab:
                        print('{0}:\t Author count. More authors than necessary for a paper with a collaboration. List only the first plus "and others".'.format(key))
                    if (nauthors > 1 and nauthors < 15) and etal and not(collab):
                        print('{0}:\t Author count. Incomplete author list. Include all authors for lists as long as 15'.format(key))
                    if (nauthors > 15) and ~collab:
                        print('{0}:\t Author count. More authors than necessary. Include only the first author plus "and others" for lists longer than 15.'.format(key))
                    if (nauthors==1) and etal and not(collab):
                        print('{0}:\t Author count query. Are there really more than 15 authors for this reference?'.format(key))
                    # diagnostic
                    # print('{0}:\t Number of authors {1} '.format(key, nauthors))

                # check for both url and doi
                if 'DOI' in self._bib[key][1].keys() and 'URL' in self._bib[key][1].keys():
                    print('{0}:\t Both DOI and URL. DOI only is preferred.'.format(key))
                
                # empty/blank field check
                for item in self._bib[key][1].items():
                    if not item[1]:
                        print('{1}: Empty value for field {0}'.format(item[0],key))
                    m = self._blankCheck.search(item[1])
                    if m:
                        print('{1}: Blank value for field {0}'.format(item[0],key))                        
                #print(self.printCite(key))
        # duplicate entry check (use doi as unique marker)
        # python 2.7 and later only
        checkForDuplicates(self._bib,'DOI')
        checkForDuplicates(self._bib,'EPRINT')




    def rewrite(self):
        """Write out a new bib file. Default for now is just to reset the collab field"""

        if self._verbosity > 2:
            print("\n>>>rewrite: Rewriting a new bib file\n")
        outfile = os.path.join(self._baseDir,'auto_generated.bib') # overwrite original
        f = io.open(outfile,'w')


        for key in self._refs:
            if key in self._bib:
                if ('COLLABORATION' in self._bib[key][1].keys() and self._bib[key][1]['COLLABORATION'] in ['CMS', 'ATLAS', 'LHCb', 'ALICE']):
                #print(self.printCite(key))
                    self._bib[key][1]['AUTHOR'] = '{'+self._bib[key][1]['COLLABORATION']+' Collaboration}'
                    del self._bib[key][1]['COLLABORATION']
            # option to filter out arXiv info if published article (PRC); may consider adding 'URL' in addition to 'DOI' for journals (Acta Phys. Polonica) w/o DOIs
                if (not self._arxiv):
                    if ('EPRINT' in self._bib[key][1] and 'DOI' in self._bib[key][1]):
                        del self._bib[key][1]['EPRINT']
                # they also have a hard time figuring out what JINST is...
                    if ('JOURNAL' in self._bib[key][1] and self._bib[key][1]['JOURNAL']==u'JINST'):
                        self._bib[key][1]['JOURNAL']=u'J. Instrum.'
                    if ('JOURNAL' in self._bib[key][1] and self._bib[key][1]['JOURNAL']==u'JHEP'):
                        self._bib[key][1]['JOURNAL']=u'J. High Energy Phys.'
                f.write(self.printCite(key))
            else:
                print("\n> Skipping citation {0}".format(key))
        f.close()
        
    def printCite(self, key):
        """Print out a complete bibtex entry"""
        t = ["\t"+zi[0]+"=\t\""+zi[1]+"\",\n" for zi in self._bib[key][1].items()]
        tt = "".join(t)
        return '@{0}'.format(self._bib[key][0])+'{'+'{0},\n'.format(key)+tt+'}\n'

    def printLog(self):
        print("\n>>> Dumping BibTeX log file\n")
        file =  os.path.join(self._baseDir,self._tag + '_temp.blg')
        f = io.open(file,'r')
        patFlip = re.compile("You've used [0-9]+ entries")
        patFlop = re.compile("\(There were [0-9]+ warnings\)")
        flipFlop = True
        for line in f:
            if (flipFlop):
                flipFlop = not patFlip.match(line)
            else:
                flipFlop = patFlop.match(line)
            if (flipFlop):
                print(line,end=""), 
 




def main(argv):
    from optparse import OptionParser

    usage = "Usage: %prog [options]  tag"
    pat = re.compile("\$Revision:\s+(\d+)\s+\$")
    global version
    versionOK = pat.search(__version__)
    if versionOK:
        version = versionOK.group(1)
    else:
        version = "Test"
    parser = OptionParser(usage=usage, version=version)
    parser.add_option("-v", "--verbosity", action="count", dest="verbose", default=False,
                        help="trace script execution; repeated use increases the verbosity more")
    parser.add_option("-b",  "--base", action="store", dest="base", help="base of build area", default=r"D:\tdr2\utils\trunk\tmp")
    parser.add_option("-r", "--rewrite", action="store_true", dest="rewrite", default=False, help="rewrites the bib file and overwrites in base directory")
    parser.add_option("--no-arxiv", action="store_false", dest="arxiv", default=True, help="removes arxiv info when doi is supplied; also replaces JINST by J. Instrum.")
    global opts
    (opts, args) = parser.parse_args()
    if opts.verbose:
        print("\tVerbosity = {0}".format(opts.verbose))
        print(opts)
    tag = ""
    if len(args) > 0:
        tag = args[len(args)-1]
    else:
        print("Missing document tag (XXX-YY-NNN). Quitting.")
        exit

        
   
 
    myRefs = cleanRefs(tag, opts.base, opts.verbose, opts.arxiv)
    myRefs.getRefList()
    myRefs.getRefs()
    myRefs.checkRefs()
    myRefs.printLog()

    if (opts.rewrite):
        myRefs.rewrite()

if __name__ == "__main__":
    main(sys.argv[1:])
   
