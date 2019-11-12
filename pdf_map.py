def return_infile():
    from PyPDF2 import PdfFileReader
    def return_infile():
        infile = "C:\\Users\\mark.nations\\Desktop\\H-15\\h15.pdf"
        return infile
    
    infile = return_infile()
    pdf = PdfFileReader(open(infile, "rb"), strict=False)
    fields = pdf.getFields()
    return PdfFileReader, fields, infile, pdf, return_infile

PdfFileReader, fields, infile, pdf, return_infile = return_infile()

