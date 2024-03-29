import qrcode
from PIL import Image

def generate_customized_qr_code(data, fill="black", back="white", box_size=10, border=4, logo=None):
    qr = qrcode.QRCode(version=1, box_size=box_size, border=border)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=fill, back_color=back)
    if logo:
        logo_img = Image.open(logo)
        max_size = (qr_img.size[0] // 4, qr_img.size[1] // 4)
        logo_img.thumbnail(max_size)
        logo_pos = (qr_img.size[0] - logo_img.size[0] - border, qr_img.size[1] - logo_img.size[1] - border)
        qr_img.paste(logo_img, logo_pos, mask=logo_img)
    return qr_img

name = input("What is your QR code name?: ")
website_link = input("Please enter a link for the QR code: ")
fillcolor = input("Please enter fill color of the QR code: ")
backcolor = input("Please enter back color of the QR code: ")
yesno = input("Do you want to use logo? ")
if yesno.lower() == "yes":
    logo1 = input("What is the name of the logo?: ")
    qr_code = generate_customized_qr_code(website_link, fill=fillcolor, back=backcolor, logo=logo1)
else:
    qr_code = generate_customized_qr_code(website_link, fill=fillcolor, back=backcolor)
qr_code.save(f"{name}_QR_code.png")
print("QR code generated successfully!")