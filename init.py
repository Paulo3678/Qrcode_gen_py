import qrcode
from PIL import Image

url = "urlseusite.com.br"

# GERA O QRCODE
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=40,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# CRIA A IMAGEM DO QRCODE
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode_site.png")