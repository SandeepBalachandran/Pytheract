import pdf2image

def pdf_to_img(pdf_file):
    # return pdf2image.convert_from_path(pdf_file)
    pages = pdf2image.convert_from_path(pdf_file, dpi=200, size=(1654,2340))
    return pages
