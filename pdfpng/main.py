import sys, fitz  # import the bindings
# fname = sys.argv[1]  # get filename from command line
# doc = fitz.open(r'D:\PROGRAMING\+PROJECT+\google docs ocr\New folder\a.pdf')  # open document
# for page in doc:  # iterate through the pages
#     pix = page.get_pixmap()  # render page to an image
#     pix.save(fr"D:\PROGRAMING\+PROJECT+\google docs ocr\New folder\page{page.number}.png" )  # store image as a PNG
    
    
def extract_png(pdf_path, png_path):
    doc = fitz.open(pdf_path)
    c = 0
    for page in doc:  # iterate through the pages
        pix = page.get_pixmap()  # render page to an image
        pix.save(png_path+f'{c}.png')
        c+=1
    return c