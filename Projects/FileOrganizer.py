import os
import shutil

Test_folder= r"C:\Users\HP\OneDrive\Desktop\python\nishantchauhan21-demo\Test_Folder"
Image_file= r"C:\Users\HP\OneDrive\Desktop\python\nishantchauhan21-demo\Test_Folder\Image_file"
Pdf_file= r"C:\Users\HP\OneDrive\Desktop\python\nishantchauhan21-demo\Test_Folder\Pdf_file"
Text_file= r"C:\Users\HP\OneDrive\Desktop\python\nishantchauhan21-demo\Test_Folder\Text_file"
Python_file= r"C:\Users\HP\OneDrive\Desktop\python\nishantchauhan21-demo\Test_Folder\Python_file"

folder= os.listdir(Test_folder)
print(folder)

for file in folder:
    if file.endswith(".png"):

        x= os.path.join(Test_folder,file)
        y= os.path.join(Image_file,file)

        if not os.path.exists(Image_file):
            os.mkdir(Image_file)
            print("New Folder: Image_folder, created Successfully")

        shutil.move(x,y)
        print("Move Successfully!")

    elif file.endswith(".pdf"):
        
        x= os.path.join(Test_folder,file)
        y= os.path.join(Pdf_file,file)

        if not os.path.exists(Pdf_file):
            os.mkdir(Pdf_file)
            print("New Folder: Pdf_folder, created Successfully")
        
        shutil.move(x,y)
        print("Move Successfully!")

    elif file.endswith(".txt"):
        x= os.path.join(Test_folder,file)
        y= os.path.join(Text_file,file)

        if not os.path.exists(Text_file):
            os.mkdir(Text_file)
            print("New Folder: Test_folder, created Successfully")

        shutil.move(x,y)
        print("Move Successfully!")

    elif file.endswith(".py"):
        x= os.path.join(Test_folder,file)
        y= os.path.join(Python_file,file)

        if not os.path.exists(Python_file):
            os.mkdir(Python_file)
            print("New Folder: Test_folder, created Successfully")

        shutil.move(x,y)
        print("Move Successfully!")

