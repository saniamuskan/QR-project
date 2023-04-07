import qrcode
from PIL import Image
#pil:light weighed image processing tool which supports many types of image formates.

Logo_link = 'C:\\Users\\Dell\\Downloads\\mvsr.jpg'

logo = Image.open(Logo_link)


basewidth = 100

#adjusting image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
	error_correction=qrcode.constants.ERROR_CORRECT_H
)


url = "https://docs.google.com/spreadsheets/d/1dv3zc3h3Z4DVfm6UDlJu5gD8hX4krqmZG3WKK99WqOY/edit#gid=0"

#adding data in qr code
QRcode.add_data(url)

QRcode.make()


QRcolor = 'orange'

#make image- colour of the qr code.
QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')

#setting qr code size
pos = ((QRimg.size[0] - logo.size[0]) // 2,
	(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)
#paste- to place reshaped image


QRimg.save('mvsr_QR.png')
#qr code is saved in give location.

print('QR code generated!')


#C:\Users\Dell\mvsr_QR.png