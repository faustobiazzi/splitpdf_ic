from pyPdf import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("teste.pdf", "rb"))

for i in xrange(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    output.addPage(inputpdf.getPage(i+1))
    if (i%2 == 0):
        with open("document-page%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)
 
