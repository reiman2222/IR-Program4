#Tyler Rodgers, Chase Moore, Jack Edwards

import re

#a Document object represents a document in the cran collection.
class Document:
    def __init__(self):
        self.author    = ''
        self.title     = ''
        self.body_text = ''
        self.number = -1

    # Creates document object
    @staticmethod
    def buildDocument(initAuth, initTitle, initBody, num):
        d = Document()
        d.author    = initAuth
        d.title     = initTitle
        d.body_text = initBody
        d.number    = num
        return d

#END CLASS


#getRawText returns the contents of file filename.
def getRawText(filename):
    f = open(filename, 'r')
    fileText = f.read()
    return fileText

#parseCorpus returns a list of Documetns representing each document
#in the cran corpus. courpus is the cran corpus as a sting.
def parseCorpus(corpus):
    docList = []
    docs = []
    #corpus split on entries
    re_entry = re.compile("\.I ")
    docs = re.split(re_entry, corpus)

    del(docs[0])
    #getArticleInformation(docs[0])

    for entry in docs:
        docList.append(getArticleInformation(entry))

    return docList

    
#getArticleInformation returns a Document object generated from string unprocessedDocs.
def getArticleInformation(unprocessedDocs):
    doc_buster = re.compile("\.[A-Z]\n")
    doc_attributes = re.split(doc_buster, unprocessedDocs)

    # build a document using the relevant information and return it
    return Document.buildDocument(doc_attributes[2],doc_attributes[1],doc_attributes[4],int(doc_attributes[0]))


#######################################
#                MAIN                 #
#######################################

#read corpus and generate a list of files
theFile = getRawText('corpus/cran.all.1400')
docList = parseCorpus(theFile)

print('begining to write files')

for doc in docList:
	f = open('docs/' + str(doc.number) + '.txt', 'w+')
	f.write(doc.author)
	f.write(str(doc.number) + '\n')
	f.write(doc.body_text)

