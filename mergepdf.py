def mergepdf():
        #The two pdf must be in the working directory. Do not forget to install the PyPDF2 module.
        import PyPDF2
        print('insert name first pdf.DO NOT FORGET THE .pdf!')
        name1=str(input())
        print('insert name second pdf')
        name2=input()
        pdf1File=open(name1,'rb')
        pdf2File=open(name2,'rb')
        pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
        pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
        pdfWriter = PyPDF2.PdfFileWriter()

        for pageNum in range(pdf1Reader.numPages):
                pageObj = pdf1Reader.getPage(pageNum)
                pdfWriter.addPage(pageObj)

        for pageNum in range(pdf2Reader.numPages):
                pageObj = pdf2Reader.getPage(pageNum)
                pdfWriter.addPage(pageObj)

        pdfOutputFile = open('merger.pdf' , 'wb')
        pdfWriter.write(pdfOutputFile)
        pdfOutputFile.close()
        pdf1File.close()
        pdf2File.close()
        print('The mergered pdf File is in the working directory and is saved with the name merger.pdf')

mergepdf()
        
