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
        self.loadimage = tk.PhotoImage(file="C:\\Users\\Ayush\\Desktop\\prog\\acti.png")
        self.hi_there = tk.Button(self, image=self.loadimage, bg="white")
        # self.hi_there["command"] = self.start_it
        self.hi_there["border"] = "2"
        self.hi_there.grid(row=0, column=0, padx=20,pady=20)

        self.loadimage1 = tk.PhotoImage(file="C:\\Users\\Ayush\\Desktop\\prog\\climate.png")
        self.hi1_there = tk.Button(self, image=self.loadimage1, bg="white")
        # self.hi1_there["command"] = self.start_it
        self.hi1_there["border"] = "2"
        self.hi1_there.grid(row=0, column=1, padx=20,pady=20)

        self.loadimage2 = tk.PhotoImage(file="C:\\Users\\Ayush\\Desktop\\prog\\poa.png")
        self.hi2_there = tk.Button(self, image=self.loadimage2, bg="white")
        # self.hi2_there["command"] = self.start_it
        self.hi2_there["border"] = "2"
        self.hi2_there.grid(row=0, column=2, padx=20,pady=20)

        self.loadimage3 = tk.PhotoImage(file="C:\\Users\\Ayush\\Desktop\\prog\\visa.png")
        self.hi3_there = tk.Button(self, image=self.loadimage3, bg="white")
        # self.hi3_there["command"] = self.start_it
        self.hi3_there["border"] = "2"
        self.hi3_there.grid(row=0, column=3, padx=20,pady=20)

        self.loadimage4 = tk.PhotoImage(file="C:\\Users\\Ayush\\Desktop\\prog\\india.png")
        self.hi4_there = tk.Button(self, image=self.loadimage4, bg="white")
        # self.hi4_there["command"] = self.start_it
        self.hi4_there["border"] = "2"
        self.hi4_there.grid(row=0, column=4, padx=20,pady=20)

        self.loadimage5 = tk.PhotoImage(file="C:\\Users\\Ayush\\Desktop\\prog\\itinerary.png")
        self.hi5_there = tk.Button(self, image=self.loadimage5, bg="white")
        # self.hi5_there["command"] = self.start_it
        self.hi5_there["border"] = "2"
        self.hi5_there.grid(row=0, column=5, padx=20,pady=20)

        self.loadimage6 = tk.PhotoImage(file="C:\\Users\\Ayush\\Desktop\\prog\\identify.png")
        self.hi6_there = tk.Button(self, image=self.loadimage6, bg="white")
        # self.hi6_there["command"] = self.start_it
        self.hi6_there["border"] = "2"
        self.hi6_there.grid(row=1, column=0, padx=20,pady=20)

        self.loadimage7 = tk.PhotoImage(file="C:\\Users\\Ayush\\Desktop\\prog\\duration.png")
        self.hi7_there = tk.Button(self, image=self.loadimage7, bg="white")
        # self.hi7_there["command"] = self.start_it
        self.hi7_there["border"] = "2"
        self.hi7_there.grid(row=1, column=1, padx=20,pady=20)

        self.loadimage8 = tk.PhotoImage(file="C:\\Users\\Ayush\\Desktop\\prog\\distance.png")
        self.hi8_there = tk.Button(self, image=self.loadimage8, bg="white")
        # self.hi8_there["command"] = self.start_it
        self.hi8_there["border"] = "2"
        self.hi8_there.grid(row=1, column=2, padx=20,pady=20)

        self.loadimage9 = tk.PhotoImage(file="C:\\Users\\Ayush\\Desktop\\prog\\emergency.png")
        self.hi9_there = tk.Button(self, image=self.loadimage9, bg="white")
        # self.hi9_there["command"] = self.start_it
        self.hi9_there["border"] = "2"
        self.hi9_there.grid(row=1, column=3, padx=20,pady=20)
        
        self.loadimage10 = tk.PhotoImage(file="C:\\Users\\Ayush\\Desktop\\prog\\airport.png")
        self.hi10_there = tk.Button(self, image=self.loadimage10, bg="white")
        # self.hi10_there["command"] = self.start_it
        self.hi10_there["border"] = "2"
        self.hi10_there.grid(row=1, column=4, padx=20,pady=20)

        self.loadimage11 = tk.PhotoImage(file="C:\\Users\\Ayush\\Desktop\\prog\\india1.png")
        self.hi11_there = tk.Button(self, image=self.loadimage11, bg="white")
        # self.hi11_there["command"] = self.start_it
        self.hi11_there["border"] = "2"
        self.hi11_there.grid(row=1, column=5, padx=20,pady=20)



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
