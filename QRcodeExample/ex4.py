import pyqrcode 
import png 
from pyqrcode import QRCode 
  
  
# String which represents the QR code 
s = "Gaurav Sharma"
  
# Generate QR code 
url = pyqrcode.create(s) 
print(url)  
# Create and save the svg file naming "myqr.svg" 
# url.svg("myqr.svg", scale = 8) 
  
# Create and save the png file naming "myqr.png" 
url.png('myqr.png', scale = 6,module_color=[0, 0, 0, 128],background=[255, 000, 000,000]) 