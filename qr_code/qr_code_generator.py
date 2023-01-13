import qrcode 
img = qrcode.make('Some data here')
# type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
print("Done")

''' Using class QRcode'''
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=8,
    border=6,
    
)

qr.add_data("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")
qr.make(fit=True)
img2 = qr.make_image()
img2.save("qr01.png")