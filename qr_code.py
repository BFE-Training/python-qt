
# Install the required Library Using 
# pip install segno

import segno

my_qrcode = segno.make("Bangla Fighter Engineering")
my_qrcode.save("my-qrcode.png", scale=12)
