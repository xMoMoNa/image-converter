from tkinter import *
from tkinter import filedialog
from PIL import Image
import os
from os import system
import customtkinter
from customtkinter import CTkImage
from CTkMessagebox import CTkMessagebox
system('cls')

customtkinter.set_default_color_theme("green")
###############################################################################################################################
def browseFile():
    global inputPathTrimed
    global inputPath
    global viwePic
    inputPath = filedialog.askopenfilename(filetypes=[("png","*.png"), ("ico","*.ico")])
    if(inputPath):
        inputPathTrimed.set(inputPath)
        image=Image.open(inputPath)
        viwePic.configure(image=CTkImage(image, image, size=(128,128)))


#############################browseDirect#########################################<>
def browseDirect():
    global outPutPath
    outPutPath=filedialog.askdirectory()
    outPutPathTrimed.set(outPutPath)


#############################btnconv#########################################
def btnconv():
    global outPutPath, inputPath
    maxDimension= resOption[resValu.get()]
    if(os.path.exists(inputPath)):
        png_image = Image.open(inputPath)
        png_image.thumbnail([maxDimension,maxDimension])
        name=inputPath.split("/")[-1]
        name=name.split(".")[0]
    else:
        CTkMessagebox(message="Please select file", title="Error", icon="cancel")
        return

    if(sameName.get() and outPutPath):
        png_image.save(f"{outPutPath}\\{name}.ico", format='ICO', sizes=[(png_image.width, png_image.height)])
    else:
        outPutPath= filedialog.asksaveasfile(initialfile=name, defaultextension=".ico", filetypes=[("ico","*.ico")])
        if(outPutPath):
            png_image.save(outPutPath.name,format='ICO', sizes=[(png_image.width, png_image.height)])
    if(outPutPath):
        CTkMessagebox(message="success", title="Done",icon="check")  
    
     
###############################################################################################################################


main = customtkinter.CTk()
main.title("convert to ico")
main.resizable(0,0)
main.iconbitmap("D:\program_document\python\pythonImageConverter\image\pngToIco.ico")

inputPath = ""
inputPathTrimed=StringVar(value="")
outPutPath = ""
outPutPathTrimed=StringVar(value= "")

viwePic=customtkinter.CTkLabel( 
    main, 
    text="",
    bg_color="transparent",
    width= 128,
    height=128)
viwePic.grid(column=0, row=0, rowspan=3, padx=5, pady=5)

btn_inputPath = customtkinter.CTkButton(main, font=('adobe', 16), text="Browse file", command=browseFile)
btn_inputPath.grid(column=1, row=0, padx=5)

btn_outPut = customtkinter.CTkButton(main, text="Browse Folder", font=('adobe', 16), command=browseDirect)
btn_outPut.grid(column=1, row=1, padx= 5)


frm_inputPath=customtkinter.CTkScrollableFrame(main, height=16, width=270, orientation="horizontal", bg_color="transparent", fg_color="transparent")
frm_inputPath.grid(column=2, row=0)
lbl_inputPath = customtkinter.CTkLabel(frm_inputPath, anchor='w', font=('adobe', 16),textvariable=inputPathTrimed )
lbl_inputPath.pack()

frm_outPutPath=customtkinter.CTkScrollableFrame(main, height=16, width=270, orientation="horizontal", bg_color="transparent", fg_color="transparent")
frm_outPutPath.grid(column=2, row=1, sticky = 'news')
lbl_outPutPath = customtkinter.CTkLabel(frm_outPutPath, anchor='w', font=('adobe', 16),textvariable=outPutPathTrimed)
lbl_outPutPath.pack()


btn_convert = customtkinter.CTkButton(main, font=('adobe', 16), text="Convert", command=btnconv)
btn_convert.grid(column=2, row=2, columnspan=2, sticky='news', padx=5, pady=5)


frm_option = customtkinter.CTkFrame(main, bg_color="transparent", fg_color="transparent")
frm_option.grid(column=1, row=2, padx=5, pady=5)
sameName=BooleanVar(value=True)
chk_sameName=customtkinter.CTkCheckBox(frm_option, text="use same name\nand folder", variable=sameName, checkbox_height=24, checkbox_width=24)
chk_sameName.pack( anchor = 'w')
 
resOption={'64x64':64,
           '128x128':128,
           '256x256':256
           }
resValu=StringVar()
resValu.set('256x256')
cmb_resolution = customtkinter.CTkOptionMenu(frm_option,  variable=resValu ,values= list(resOption.keys()))
cmb_resolution.pack()
print(frm_option.cget("width"))
main.mainloop()