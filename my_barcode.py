
# Install the required Library Using 
# pip install "python-barcode[images]"


import barcode
from barcode.writer import ImageWriter

barcode_format = barcode.get_barcode_class("code128")
generated_barcode = barcode_format("708191", writer=ImageWriter())
generated_barcode.save("barcode")