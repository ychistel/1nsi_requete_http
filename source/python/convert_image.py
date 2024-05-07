import base64

with open('../html/image.txt',mode='rb') as f:
    img_data = b''
    lignes = f.readlines()
    for ligne in lignes:
        img_data += ligne        

with open("imageToSave.png", "wb") as fh:
    fh.write(base64.decodebytes(img_data))
