from pdfrw import PdfReader

file = PdfReader('GRE OV.pdf')

#print(file.Info)

'''
print(file.Root)
f = open('txtfile/Root file.txt','w',encoding='UTF-8')
for s in file.Root:
    f.writelines(s)
f.close()
'''

print(file.Encrypt)
f = open('txtfile/Encrypt file.txt','w',encoding='UTF-8')
fencrypt = print(file.Encrypt)
for s in fencrypt:
    f.writelines(s)
f.close()