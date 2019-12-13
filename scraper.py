import requests
from bs4 import BeautifulSoup
import smtplib

# define the URL of the product that we need to track
URL = " https://www.amazon.it/Anycubic-Stampante-schermo-Printer-115x65x155/dp/B07QDYYDDB/ref=sr_1_2_sspa?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=stampante+3d&qid=1576225644&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNDdBTFhNWVdPNDdIJmVuY3J5cHRlZElkPUEwNTE2OTcxM1EwVkVYNzJVMTQyVyZlbmNyeXB0ZWRBZElkPUEwOTQ3Mjg5UVhJSFhPTVBZV1pLJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==  "

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0"}

# this function will check the prize of the product
def check_prize():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    prize = soup.find(id="priceblock_ourprice_row").get_text()
    prize_ = float(prize[8:13])
    print(prize_)
    if prize_ > 300:
        send_email()

# defining the send email function
def send_email():

    # creating a connection between us and gmail
    connection_server = smtplib.SMTP("smtp.gmail.com", 587)
    connection_server.ehlo()

    # encrypt the connection
    connection_server.starttls()
    connection_server.ehlo()
    connection_server.login("email", "password")

    # define the message texts
    subject = " HEY THE PRODUCT HAS A FALLDOWN PRIZE: "
    body = " go to the amazon link : https://www.amazon.it/Anycubic-Stampante-schermo-Printer-115x65x155/dp/B07QDYYDDB/ref=sr_1_2_sspa?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=stampante+3d&qid=1576225644&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNDdBTFhNWVdPNDdIJmVuY3J5cHRlZElkPUEwNTE2OTcxM1EwVkVYNzJVMTQyVyZlbmNyeXB0ZWRBZElkPUEwOTQ3Mjg5UVhJSFhPTVBZV1pLJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==  "
    msg = f"subject:{subject},\n\n{body}"

    # sending the email
    connection_server.sendmail(
        "email that send",
        "email that recieve",
        msg
    )
    print("the mail has been send ")
    connection_server.quit()

check_prize()
