import qrcode

url= input("Enter Your URL Here: ")
filename= input("Enter Your FileName Here: ")

if not filename.endswith (".png"):
    filename= filename + ".png"

img= qrcode.make(url)
img.save(filename)

print(f"QR Code '{filename}' generated successfully!")









