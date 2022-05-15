import pyqrcode
print(pyqrcode)
res=pyqrcode.create('0123456780')   #o/p comes in binary string
print(res)
print('-----------------------')
# leading 0 is not allowed   like---0123456789
res1=pyqrcode.create(123456780)     #o/p comes in normal string
print(res1)
print('-----------------------')
res2=pyqrcode.create('hello')
print(res2)
print('-----------------------')
hello='hii'
res3=pyqrcode.create(hello)
print(res3)
res3.show()
print('-----------------------')
res4=pyqrcode.create('hello'.upper())
print(res4)
print('-----------------------')