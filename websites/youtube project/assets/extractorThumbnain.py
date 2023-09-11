import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

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


        # create a file as utf-8
        f = open('C:\\Users\\Rafael\\Desktop\\youtube.txt', 'w', encoding='utf-8')
        #write the title of the page
        f.write(driver.page_source)
        #close the file
        f.close()




def extractData():
    file = open('C:\\Users\\Rafael\\Desktop\\youtube.txt', 'r', encoding='utf-8')
    data = file.read()
    file.close()

    
    __path = 'C:\\Users\\Rafael\\Desktop\\Code\\fiverr_\\ads\\Website\\learning\\html-css-course\\youtube project\\youtube.json'
    
    if os.path.exists(__path):
        os.remove(__path)



    f = open(__path, 'w', encoding='utf-8')
    f.write('[')
    isFirst=True
    for i in range(0, 10):
        try:
          thumbnail, chanelImage, chanelName, title, stats1, stats2 = getVideoData(data, i)
        except:
          continue
        if isFirst:
            f.write('{\n')
            isFirst=False
        else:
          f.write(',{\n')
        f.write('"thumbnail": "' + thumbnail + '",\n')
        f.write('"chanelImage": "' + chanelImage + '",\n')
        f.write('"chanelName": "' + chanelName + '",\n')
        f.write('"title": "' + title + '",\n')
        f.write('"stats1": "' + stats1 + '",\n')
        f.write('"stats2": "' + stats2 + '"\n')
        f.write('}\n')

      
    f.write(']')
    f.close()


def getVideoData(data, videoNumber):
    d1 = data.split('<div id="dismissible" class="style-scope ytd-rich-grid-media">')[videoNumber+1]
    
    thumbnail = d1.split('src="')[1].split('"')[0]
    chanelImage = d1.split('src="')[2].split('"')[0]
    chanelName = d1.split(' title="')[1].split('"')[0]
    title = d1.split(' title="')[2].split('"')[0]
    stats1 = d1.split('class="style-scope ytd-video-meta-block" hidden="">•</div>')[1].split('ytd-video-meta-block">')[1].split('</span>')[0]
    stats2 = d1.split('class="style-scope ytd-video-meta-block" hidden="">•</div>')[1].split('ytd-video-meta-block">')[2].split('</span>')[0]
    return thumbnail, chanelImage, chanelName, title, stats1, stats2


mr=my_request()
extractData()
