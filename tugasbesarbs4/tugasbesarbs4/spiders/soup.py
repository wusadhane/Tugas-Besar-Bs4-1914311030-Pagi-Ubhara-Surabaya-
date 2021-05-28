import requests
from bs4 import BeautifulSoup
import speech_recognition as sr
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

r=requests.get("https://www.wavsource.com/people/people.htm", headers=headers)


soup = BeautifulSoup(r.text, 'html.parser')
link = 'https://www.wavsource.com/people/'+soup.select('option:nth-child(7)')[0].get('value')




r =requests.get(link, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')


for items in range(0,63):
    pertama= soup.select('.c1 script')[items].string
    pertama = pertama.replace('s2p(','').replace(')','').replace('\'','').strip()
    pertama = pertama.split(',')
    pertama = 'https://www.wavsource.com/snds_2020-10-01_3728627494378403/'+pertama[0]+'/'+pertama[1]
    
    with requests.Session() as req:
        name = re.search(r"([^\/]+$)", pertama).group()
        print(f"Downloading File {name}")
        headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
        }
        download = req.get(pertama, headers=headers)
        
        if download.status_code == 200:
            print ("berhasil didownload")
            with open('hasil/'+name, 'wb') as f:
                f.write(download.content)
        else:
            print(f"Download Failed For File {name}")

        if items == 2 or items == 11:
            print('errot file yang ini \n')
            continue

        recog = sr.Recognizer()

        

        # open the file
        with sr.AudioFile('hasil/'+name) as source:
            # listen for the data (load audio to memory)
            
        
            try:
                audio_data = recog.record(source)
            except:
                print("File Tidak Bisa Di masukin record (gaktau kenapa)")
            
            # recognize (convert from speech to text)
            try:
                text = recog.recognize_google(audio_data)
                print("File Musik Tersebut Terbilang : ")
                print(text)
            except:
                print('Suaranya terlalu bagus')
            print('\n')