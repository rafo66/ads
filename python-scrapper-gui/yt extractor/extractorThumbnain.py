import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import http.client
from PIL import ImageTk
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import PIL.Image


class my_request():
    def __init__(self):
        self.request()


    def request(self):
        _path = 'C:\\Users\\Rafael\\Downloads\\chromedriver_win32\\chromedriver.exe'
        option = Options()
        option.add_argument('--headless')
        option.add_argument('--disable-gpu')
        option.add_argument('--log-level=3')
        # simulate us location
        option.add_argument('--lang=en-US')
        s = Service(ChromeDriverManager().install())

        driver = webdriver.Chrome(service=s, options=option)

        baseurl = 'https://youtube.com'

        driver.get(baseurl)
        time.sleep(5)


        f = open('source.txt', 'w', encoding='utf-8')
        f.write(driver.page_source)
        f.close()



import tkinter as tk
from tkinter import ttk
from tkinter import *




class my_gui():
    def __init__(self):
        self.curentIndex = -1
        self.titles = [
    "Miley Cyrus - Used To Be Young (Official Video)",
    "Kung Fu Panda | Who Are You",
    "REACTING TO MY MOST POPULAR VIDEOS",
    "Acoustic 2023 ⧸ The Best Acoustic Covers of Popular Songs 2023 - English Love Songs Cover ♥"
        ]

        self.thumbnails = [
    "C:\\Users\\Rafael\\Desktop\\Code\\fiverr_\\ads\\Website\\learning\\html-css-course\\youtube project\\assets\\thumbnail1.jpg",
    "hq720.webp",
    "hq720 (1).webp",
    "hq720 (2).webp",
    "hq720 (3).webp"
        ]

        self.path = "C:\\Users\\Rafael\\Desktop\\Code\\fiverr_\\ads\\Website\\learning\\html-css-course\\youtube project\\assets\\thumbnail1.jpg"
        
        
        self.root = tk.Tk()
        self.root.title('Youtube Extractor')
        self.root.geometry('720x480')
        self.root.resizable(False, False)
        self.root.config(bg='black')
        self.createWidgets()
        self.root.mainloop()


    def createWidgets(self):
        self.createThumbnails()
        self.createTexts()
        self.createButtons()
        self.root.update()


    def createThumbnails(self):

        # convert to png
        im = PIL.Image.open(self.path)
        im.save(self.path+'.png')



        photo = tk.PhotoImage(file=self.path+'.png')
        #image2 = photo.subsample(3, 3)
        if self.curentIndex==-1:
            image2 = photo.subsample(3, 3)
        else:
            image2 = photo.subsample(2, 2)
        
        self.label=tk.Label(image=image2)
        self.label.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor='center')

    def createTexts(self):
        self.title = tk.Label(self.root, text='Random Video', font=('Verdana', 20), fg='black')
        self.title.place(relx=0.3, rely=0.1, anchor='center')

        self.videoTitle = tk.Label(self.root, text='Video Title', font=('Verdana', 15), fg='black')
        self.videoTitle.place(relx=0.5, rely=0.8, anchor='center')

    def createButtons(self):
        self.refreshButton = tk.Button(self.root, text='Refresh', font=('Verdana', 15), fg='black', command=self.refresh)
        self.refreshButton.place(relx=0.7, rely=0.1, anchor='center')

    def refresh(self):
        self.curentIndex+=1
        if self.curentIndex==len(self.titles):
            self.curentIndex=0

        self.path = self.thumbnails[self.curentIndex+1]
        self.createWidgets()


        self.videoTitle.config(text=self.titles[self.curentIndex])




        self.root.update()


    '''def refresh(self):
        __path = 'C:\\Users\\Rafael\\Desktop\\Code\\fiverr_\\ads\\Website\\learning\\html-css-course\\youtube project\\youtube.json'
        # read the json file
        jsonFile = open(__path, 'r', encoding='utf-8')
        data = jsonFile.read()
        jsonFile.close()
        # convert the json file to a python dictionary
        data = json.loads(data)
        # loop through the dictionary
        for i in range(0, 4):
            # get the thumbnail
            thumbnailURL = data[i]['thumbnail']
            # get the chanel image
            chanelImageURL = data[i]['chanelImage']
            # get the chanel name
            chanelName = data[i]['chanelName']
            # get the title
            title = data[i]['title']
            # get the stats1
            stats1 = data[i]['stats1']
            # get the stats2
            stats2 = data[i]['stats2']
            # update the gui
            self.thumbnails[i].config(image=thumbnailURL)
            self.chanelImages[i].config(image=chanelImageURL)
            self.chanelNames[i].config(image=chanelName)
            self.titles[i].config(text=title)
            self.stats1[i].config(text=stats1)
            self.stats2[i].config(text=stats2)
            self.root.update()
    '''



import json
app=my_gui()