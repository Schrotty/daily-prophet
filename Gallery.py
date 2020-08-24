import tkinter

from PIL import Image, ImageTk


class Gallery:
    def __init__(self, media):
        self.master = tkinter.Tk()
        self.width, self.height = self.master.winfo_screenwidth(), self.master.winfo_screenheight()

        self.canvas = tkinter.Canvas(self.master, width=self.width, height=self.height, highlightthickness=0)
        self.canvas.pack()
        self.canvas.configure(background='black')

        self.display(media)

    def display(self, media):
        self.master.overrideredirect(1)
        self.master.geometry("%dx%d+0+0" % (self.width, self.height))
        self.master.focus_set()
        self.master.bind("<Escape>", lambda f: (f.widget.withdraw(), f.widget.quit()))

        img_width, img_height = media.size
        ratio = min(self.width / img_width, self.height / img_height)
        img_width = int(img_width * ratio)
        img_height = int(img_height * ratio)
        pil_image = media.resize((img_width, img_height), Image.ANTIALIAS)

        image = ImageTk.PhotoImage(pil_image)
        self.canvas.create_image(self.width / 2, self.height / 2, image=tkinter.PhotoImage(file="C:\\Users\\ruben\\Pictures\\dr_finklestein.gif"))

        self.master.mainloop()


if __name__ == "__main__":
    Gallery(Image.open("C:\\Users\\ruben\\Pictures\\dr_finklestein.gif"))
