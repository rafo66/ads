'''

Scrapes amazon.com for product information and saves it to a csv file.

'''


import requests
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
# write to excel
import xlsxwriter

import json



class Scrapper():
  def __init__(self, querry):
      chrome_driver_path = 'C:\\Users\\Rafael\\Downloads\\chromedriver_win32\\chromedriver.exe'
      option = Options()
      #option.add_argument('--headless')
      #option.add_argument('--disable-gpu')
      option.add_argument('--log-level=3')
      option.add_argument('--lang=en-US')
      s = Service(ChromeDriverManager().install())
      driver = webdriver.Chrome(service=s, options=option)
      
      baseurl = 'https://www.youtube.com/results?search_query=' + querry
      driver.get(baseurl)

      
      cookies_button = driver.find_element(By.XPATH ,'/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')

      print("loadeed")

      cookies_button.click()
      
      self.processThumbnails(driver)

  def processThumbnails(self, driver):

      '''
      $x("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[2]/div[1]/div/div[1]/div/h3/a")[0].innerText

      '''

      input("press enter to continue")

      self.titles = []
      self.authors = []
      self.views = []
      self.dates = []
      self.links = []


      for i in range(1, 100):
          try:
            celement = driver.find_element(By.XPATH ,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[' + str(i) + ']/div[1]/div/div[1]/div/h3/a')
            # first element of the array
            self.titles.append(celement.text)
            self.links.append(celement.get_attribute('href'))
          except:
            print("end of list")
            break

      # get all elements with id channel-name
      i=0
      elements_metadata = driver.find_elements(By.ID, 'metadata')
      for meta in elements_metadata:
        try:
            if meta.text != '':
              print(meta.text, i)
              views, date = meta.text.split('\n')
              self.dates.append(date)
              self.views.append(views.replace('views', ''))
        except:
          pass



      # populate style-scope ytd-channel-name
      elements_authors = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-channel-name')
      # get 'a' child element
      for author in elements_authors:
        if author.text != '':
            print(author.text)
            self.authors.append(author.text)

      # remove first element
      self.authors.pop(0)


      self.exportToXlsx()
      self.exportToCsv()
      self.exportToJson()

  def exportToXlsx(self):

    if os.path.exists('titles.xlsx'):
      os.remove('titles.xlsx')

    xlsxwriter.Workbook('titles.xlsx')
    workbook = xlsxwriter.Workbook('titles.xlsx')
    worksheet = workbook.add_worksheet()
    
    columnTitles = ['Title', 'Author', 'Views', 'Date', 'Link']

    self.populateColumnsTitle(columnTitles, worksheet)
    self.populateColumns(worksheet, self.titles, 0)
    self.populateColumns(worksheet, self.authors, 1)
    self.populateColumns(worksheet, self.views, 2)
    self.populateColumns(worksheet, self.dates, 3)
    self.populateColumns(worksheet, self.links, 4)

    # set first column width to the max length of the titles
    print(max(self.titles, key=len))
    print(int(len(max(self.titles, key=len)) * 1.5))

    charSize = 0.8
    worksheet.set_column(0, 0, int(len(max(self.titles, key=len)) * charSize))
    worksheet.set_column(1, 1, int(len(max(self.authors, key=len)) * charSize))
    worksheet.set_column(2, 2, int(len(max(self.views, key=len)) * charSize))
    worksheet.set_column(3, 3, int(len(max(self.dates, key=len)) * charSize))
    worksheet.set_column(4, 4, int(len(max(self.links, key=len)) * charSize))

    # style 1st row as size 20
    cell_format = workbook.add_format({'bold': True, 'font_color': 'white', 'bg_color': 'black', 'font_size': 20})
    worksheet.set_row(0, None, cell_format)

    # style all rows except 1st
    cell_format = workbook.add_format({'bold': False, 'font_color': 'black', 'bg_color': 'white', 'font_size': 16})
    for i in range(1, len(self.titles)):
      worksheet.set_row(i, None, cell_format)

    workbook.close()
    os.startfile('titles.xlsx')

  def populateColumnsTitle(self, columnTitles, worksheet):
    row = 0
    col = 0

    for title in columnTitles:
      worksheet.write(row, col, title)
      col += 1

  def populateColumns(self, worksheet, columnValues, columnIndex):
    col = columnIndex
    row = 1

    for value in columnValues:
      worksheet.write(row, col, value)
      row += 1


  def exportToCsv(self):
    if os.path.exists('titles.csv'):
      os.remove('titles.csv')

    with open('titles.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(["Title", "Author", "Views", "Date", "Link"])
      for i in range(0, len(self.titles)):
        try:
          writer.writerow([self.titles[i], self.authors[i], self.views[i], self.dates[i], self.links[i]])
        except:
          pass
    os.startfile('titles.csv')

  def exportToJson(self):
    if os.path.exists('titles.json'):
      os.remove('titles.json')

    with open('titles.json', 'w', encoding='utf-8') as f:
      json.dump({'titles': self.titles, 'authors': self.authors, 'views': self.views, 'dates': self.dates, 'links': self.links}, f, ensure_ascii=False, indent=4)
    os.startfile('titles.json')



  


scrapper = Scrapper('music')
