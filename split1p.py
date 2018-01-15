from pyPdf import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("escaneado.pdf", "rb"))

for i in xrange(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("separados\document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)
