from tkinter import Button, Entry, Tk
from tkinter import Label
from tkinter import StringVar
from tkinter.filedialog import asksaveasfilename, asksaveasfile
from pytube import YouTube


'''Display Window
In this case TK from tkinter is used to create the resizable window'''
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("My Magic Wand")

'''Use label to display text that cannot be modified by end user'''
Label(root, text= 'Youtube Video Downloader', font='arial 20 bold').pack()

'''Create Field to Enter Link'''

link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x = 160 , y = 60)

link_enter = Entry(root, width = 70, textvariable = link) .place( x = 32, y = 90)

def Downloader():
    '''This is what will be called for the code to work'''
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)

    '''Prompt the user where they want to save the video downloaded'''
    file = asksaveasfile(initialfile = 'video.mp4',
    defaultextension = " .mp4", filetypes = ["All Files"])
    


Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()

