import PyPDF2
'''
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('main.pdf')
pdf_combiner(inputs)
'''
main_pdf = PyPDF2.PdfFileReader(open('main.pdf','rb'))
watermark_image = PyPDF2.PdfFileReader(open('watermark.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = main_pdf.getPage(i)
    page.mergePage(watermark_image.getPage(0))
    output.addPage(page)

    with open('watermarked_pdf.pdf', 'wb') as file:
        output.write(file)
