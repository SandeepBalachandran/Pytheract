import pdf2image

def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)