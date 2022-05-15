import pyqrcode
import png
s= input('enter the data    :   ')       
# https://www.w3schools.com/
res=pyqrcode.create(s)
# res.png('data.png',scale=1)
res.png('data.jpeg',scale=5)
