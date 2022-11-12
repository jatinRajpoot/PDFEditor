from PyPDF2 import PdfReader, PdfMerger
import os

def mergerpdf(fileslist:list,instance) :
    merged_file_path="D:\\Projects\\pdftools\\static\\"+instance+".pdf"
    merger = PdfMerger()
    for pdf in fileslist:
        merger.append(pdf)
    merger.write(merged_file_path)
    merger.close()
    for removepath in fileslist:
        os.remove(removepath)

