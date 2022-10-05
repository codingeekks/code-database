#pip install qrcode[pil]
import qrcode
img=qrcode.make("message")
img.save("pic.png") 