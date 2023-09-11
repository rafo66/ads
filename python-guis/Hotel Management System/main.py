import tkinter as tk
from tkinter import ttk
from tkinter import *


class HotelManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hotel Management System")
        self.geometry("1080x720")
        self.configure(bg="white")
        self.create_widgets()


    def create_widgets(self):
        self.create_tabs_main_page()

    def create_tabs_main_page(self):
        self.main_page = Frame(self, bg="#F5F5F5")
        self.main_page.pack(fill="both", expand=True)





        self.rightView = Frame(self.main_page, bg="#F5F5F5")
        self.rightView.pack(fill="both", expand=True, side=RIGHT)


        # rounded corners
        self.rightViewDateFrame = Frame(self.rightView, bg="white", highlightbackground="grey", highlightthickness=1)
        self.rightViewDateFrame.pack(fill="x", side=TOP, padx=(0,20), pady=(20,0))

        self.rightViewTitle = Label(self.rightViewDateFrame, text="August", font=("Arial", 14), foreground="#757575", background="white")
        self.rightViewTitle.pack(fill="both", expand=True, padx=20, pady=(25, 0))

        self.rightViewTitle = Label(self.rightViewDateFrame, text="30", font=("Arial", 40), foreground="#757575", background="white")
        self.rightViewTitle.pack(fill="both", expand=True, padx=20)

        self.rightViewTitle = Label(self.rightViewDateFrame, text="2023", font=("Arial", 14), foreground="#757575", background="white")
        self.rightViewTitle.pack(fill="both", expand=True, padx=20, pady=(0, 25))











        self.leftView = Frame(self.main_page, bg="#F5F5F5")
        self.leftView.pack(fill="both", expand=True, side=LEFT)
        self.leftView.rowconfigure(0, weight=1)
        self.leftView.rowconfigure(1, weight=4)
        self.leftView.columnconfigure(0, weight=1)


        self.topLeftView = Frame(self.leftView, bg="#F5F5F5")
        self.topLeftView.grid(row=0, column=0, sticky="n", padx=5, pady=5)
        self.topLeftView.grid_columnconfigure(0, weight=1)
        self.topLeftView.grid_columnconfigure(1, weight=1)
        self.topLeftView.grid_columnconfigure(2, weight=1)
        self.topLeftView.grid_columnconfigure(3, weight=1)
        self.topLeftView.grid_rowconfigure(0, weight=1)

      

        self.generateTopLeftViewItems()

        







        self.bottomLeftView = Frame(self.leftView, bg="#F5F5F5")
        self.bottomLeftView.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.bottomLeftView.columnconfigure(0, weight=1)
        self.bottomLeftView.columnconfigure(1, weight=1)

        




        self.room_status_tab = Frame(self.bottomLeftView, bg="white", highlightbackground="grey", highlightthickness=1)
        self.room_status_tab.pack(fill="both", expand=True, side=RIGHT, padx=5, pady=5)

        self.room_status_tab.grid_rowconfigure(0, weight=1)
        self.room_status_tab.grid_rowconfigure(1, weight=4)
        self.room_status_tab.grid_columnconfigure(0, weight=1)

        self.titleTab = Frame(self.room_status_tab,  background="white")
        self.titleTab.grid(row=0, column=0, sticky="nsew", pady=0)
        self.room_status_tab_title = Label(self.titleTab, text="Room Status", font=("Arial", 20), background="white")
        # align left
        self.room_status_tab_title.pack(expand=True, side=LEFT, anchor="w")
        

        self.room_status_graph_tab = Frame(self.room_status_tab, background="white")
        self.room_status_graph_tab.grid(row=1, column=0, sticky="new", pady=0)
        # create a canvas and draw a graph
        self.canvas = Canvas(self.room_status_graph_tab, width=200, height=200, background="white")
        self.canvas.pack(fill="both", expand=True, side=TOP, pady=0)
        self.draw_graph()





        self.booking_tab = Frame(self.bottomLeftView)
        self.booking_tab.pack(fill="both", expand=True, side=LEFT, padx=5, pady=5)


        # new room button
        self.new_room_button = Button(self.booking_tab, text="New Room", font=("Arial", 14), background="#03A9F4", foreground="white", activebackground="#03A9F4", activeforeground="white", borderwidth=0)
        self.new_room_button.pack(fill="x", side=TOP, pady=(0, 10))

        # new reservation button
        self.new_reservation_button = Button(self.booking_tab, text="New Reservation", font=("Arial", 14), background="#03A9F4", foreground="white", activebackground="#03A9F4", activeforeground="white", borderwidth=0)
        self.new_reservation_button.pack(fill="x", side=TOP, pady=(0, 10))

        # new check out button
        self.new_check_out_button = Button(self.booking_tab, text="Check Out", font=("Arial", 14), background="#03A9F4", foreground="white", activebackground="#03A9F4", activeforeground="white", borderwidth=0)
        self.new_check_out_button.pack(fill="x", side=TOP, pady=(0, 10))

        # new call service button
        self.new_call_service_button = Button(self.booking_tab, text="Call Service", font=("Arial", 14), background="#03A9F4", foreground="white", activebackground="#03A9F4", activeforeground="white", borderwidth=0)
        self.new_call_service_button.pack(fill="x", side=TOP, pady=(0, 10))

        


    def generateTopLeftViewItems(self):
        self.topLeftViewItems = []
        
        self.topLeftViewItems.append(TopLeftViewItem(self.topLeftView, 0, "Current In House \n ", 59, 137))
        self.topLeftViewItems.append(TopLeftViewItem(self.topLeftView, 1, "Expected Arrivals \n ", 8, 20))
        self.topLeftViewItems.append(TopLeftViewItem(self.topLeftView, 2, "Expected Departures \n ", 16, 32))
        self.topLeftViewItems.append(TopLeftViewItem(self.topLeftView, 3, "End Of Day \n ", 51, 25))

    def draw_graph(self):
        data = {
            "Available": 20,
            "Single": 10,
            "Double": 15,
            "Family": 6
        }

        colors = {
            "Single": "#03A9F4",
            "Double": "#F44336",
            "Family": "#FF9800",
            "Available": "#607D8B"
        }

        # create a circle 
        self.canvas.create_oval(30, 30, 190, 190, fill="white", outline="white")
        curentAngle = 0
        # for each key in data
        for key in data:
            # calculate the angle
            angle = data[key] * 360 / sum(data.values())
            # draw the arc
            self.canvas.create_arc(30, 30, 190, 190, start=curentAngle, extent=angle, fill=colors[key], outline="white")

            # draw legend
            rectSize = [30, 20]
            # get index of the key
            rectPos = [210, 60+list(data.keys()).index(key)*25]
            self.canvas.create_rectangle(rectPos[0], rectPos[1], rectPos[0] + rectSize[0], rectPos[1] + rectSize[1], fill=colors[key], outline="white")

            # draw text
            displayedText = str(key) + " (" + str(data[key]) + ")"
            self.canvas.create_text(rectPos[0] + rectSize[0] + 10, rectPos[1] + rectSize[1]/2, text=displayedText, anchor="w", fill="black")
            curentAngle += angle

    
            



class TopLeftViewItem():
    def __init__(self, parent, col, title, number_rooms, total_pax):
        self.parent = parent
        self.col = col
        self.title = title
        self.number_rooms = number_rooms
        self.total_pax = total_pax
        self.create()

    def create(self):
        self.topLeftViewItem = Frame(self.parent, bg="grey", width=150, highlightbackground="red", highlightthickness=1)

        # expand=True, side=LEFT
        self.topLeftViewItem.grid(row=0, column=self.col, sticky="new", padx=15, pady=5)

        self.topLeftViewItem.rowconfigure(0, weight=2)
        self.topLeftViewItem.rowconfigure(1, weight=1)
        self.topLeftViewItem.columnconfigure(0, weight=1)

        self.topLeftViewItemMain = Frame(self.topLeftViewItem, bg="white", height=90)
        self.topLeftViewItemMain.grid(row=0, column=0, sticky="nsew", pady=1, padx=1)





        # bold
        # set fixed width to 500 px and override the weight
        self.topLeftViewItemTitleFrame = Frame(self.topLeftViewItemMain, bg="blue", width=500)
        self.topLeftViewItemTitleFrame.pack(fill="x", side=TOP, pady=(0, 15))
        
        self.topLeftViewItemTitle = Label(self.topLeftViewItemTitleFrame, text=self.title, font=("Arial", 18), background="white", width=200)
        # align left
        self.topLeftViewItemTitle.pack(side=LEFT, anchor="w")





        self.number_rooms_colors = [
            "#03A9F4",
            "#F44336",
            "#FF9800",
            "#607D8B"
        ]

        self.topLeftViewItemNumberRooms = Label(self.topLeftViewItemMain, text=self.number_rooms, font=("Arial", 50), foreground=self.number_rooms_colors[self.col], background="white")
        self.topLeftViewItemNumberRooms.pack(fill="x", side=TOP)

        self.topLeftViewItemNumberRoomsText = Label(self.topLeftViewItemMain, text="Rooms", font=("Arial", 20), background="white", foreground="#757575")
        self.topLeftViewItemNumberRoomsText.pack(fill="x", side=TOP, pady=(0, 30))



        self.topLeftViewItemPax = Frame(self.topLeftViewItem, bg="white", height=50)
        # apply pady only on the top
        self.topLeftViewItemPax.grid(row=1, column=0, sticky="nsew", pady=(0,1), padx=1)
      
        self.topLeftViewItemTotalPaxText = Label(self.topLeftViewItemPax, text="Total Pax :", font=("Arial", 14), background="white", foreground="#757575")
        self.topLeftViewItemTotalPaxText.place(x=0, rely=0.5, anchor="w")

        self.topLeftViewItemTotalPax = Label(self.topLeftViewItemPax, text=self.total_pax, font=("Arial", 16), background="white")
        self.topLeftViewItemTotalPax.place(x=120, rely=0.5, anchor="center")




if __name__ == "__main__":
    app = HotelManagementSystem()
    app.mainloop()