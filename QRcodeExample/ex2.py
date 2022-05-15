import pyqrcode
print(pyqrcode)
res=pyqrcode.create('0123456780')  
print(res.text())
print('-----------------------')
print(res.terminal())
print(res.terminal(module_color='red', background='yellow'))
