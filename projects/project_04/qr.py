import qrcode
import datetime
qr = qrcode.make("https://harshpreet-singh.netlify.app")
now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# filename = f"screenshots\\screenshot_{now}.jpg"
qr.save(f"codes\\qr_code_{now}.png")
# qr.show()