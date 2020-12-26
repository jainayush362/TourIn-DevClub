import tkinter as tk #FOR GUI Development
import tkinter.messagebox


class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        #wishme()
        self.create_widgets()

    def createCanvas(self, canvas_width, canvas_height):
        canvas = tk.Canvas(self.master, width=canvas_width, height=canvas_height)
        return canvas

    def addImage(self, canvas, filename, image_x, image_y, direction=tk.NW):
        self.img = tk.PhotoImage(file=filename) # Create PhotoImage object
        canvas.create_image(image_x, image_y, anchor=direction, image=self.img) # Create the image on our canvas
        return canvas

    def create_widgets(self):
        self.loadimage = tk.PhotoImage(file="C:\\Users\\Ayush\\Desktop\\pro\\rounded.png")
        self.hi_there = tk.Button(self, image=self.loadimage)
        # self.hi_there["command"] = self.start_it
        self.hi_there["border"] = "0"
        self.hi_there.pack(side="left")

        self.hi1_there = tk.Button(self, image=self.loadimage)
        # self.hi1_there["command"] = self.start_it
        self.hi1_there["border"] = "0"
        self.hi1_there.pack(side="left")

        self.hi2_there = tk.Button(self, image=self.loadimage)
        # self.hi1_there["command"] = self.start_it
        self.hi2_there["border"] = "0"
        self.hi2_there.pack(side="left")


        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")


if __name__ == "__main__":

    root = tk.Tk()
    app = Application(master=root)
    canvas = app.createCanvas(700, 450)
    canvas = app.addImage(canvas,"C:\\Users\\Ayush\\Desktop\\pro\\backgroundimg.png", 0, 0)
    canvas.pack()
    app.mainloop()
