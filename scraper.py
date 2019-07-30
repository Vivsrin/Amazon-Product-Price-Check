import requests
from bs4 import BeautifulSoup
import smtplib
import time
from twilio.rest import TwilioRestClient as call

fn="+12054305974"
tn="+919886412259"
src_path="https://sendeyo.com/en/8cebe85ecd"


URL='https://www.amazon.in/Amazon-FireTVStick-Alexa-Voice-Remote-Streaming-Player/dp/B0791YHVMK/ref=sr_1_1?crid=97E1TPD7E967&keywords=fire+stick+tv&qid=1564464314&s=gateway&smid=AT95IG9ONZD7S&sprefix=fire%2Caps%2C1363&sr=8-1'

headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36' }
def check_price():
    page=requests.get(URL, headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    title=soup.find(id="productTitle").getText()
    price=(soup.find(id='priceblock_dealprice').getText())
    p1=price[2:].split(",")
    p2=p1[0]+p1[1]
    converted_price=float(p2)
    if(converted_price<2000.0):
        send_mail()

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('vivekmjs55@gmail.com','yjixlproejlsgcsv')

    subject="price fell down"
    body='Check this amazon link https://www.amazon.in/Amazon-FireTVStick-Alexa-Voice-Remote-Streaming-Player/dp/B0791YHVMK/ref=sr_1_1?crid=97E1TPD7E967&keywords=fire+stick+tv&qid=1564464314&s=gateway&smid=AT95IG9ONZD7S&sprefix=fire%2Caps%2C1363&sr=8-1'

    msg= f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'vivekmjs55@gmail.com',
        'kvpaddu017@gmail.com',
        msg
    )

    client =call("AC9b7b077097e3014d66f9d36c882511a1","194eda29c5f0388fde5c7c1a7e96d368")
    print("call initiated")
    client.calls.create(to=tn,from_=fn,url=src_path,mrthod='GET')
    print('call has been trigerred successfully')
    print('Email has been sent')

    server.quit()

while(True):
    check_price()
    time.sleep(60*60)