from bs4 import BeautifulSoup
import requests


Web = {
    # "Amazon": "https://www.amazon.com/PNY-GeForce-Gaming-Epic-X-Graphics/dp/B09VMMRWHM/ref=sr_1_1_sspa?crid=2Q3GVTC6Q7VHE&keywords=3080+ti&qid=1655251833&sprefix=3080%2Caps%2C218&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE5VlRYRUJSUE1WQVAmZW5jcnlwdGVkSWQ9QTA4MjM2MDMxVjlaS0RWRTBXMjA5JmVuY3J5cHRlZEFkSWQ9QTA3MjMzODQxUUZFVVNRVFA0MUFOJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
    "IMDB": "https://www.imdb.com/title/tt5491994/ratings/?ref_=tt_ov_rt"
    # "PCnation": "https://www.pcnation.com/web/details/9BH960/evga-nvidia-geforce-rtx-3080-graphic-card-10-gb-gddr6x-10g-p5-3897-kl?dfw_tracker=110924-9BH960&mkwid=s_dc&pcrid=524019285072&pkw=&pmt=&plc=&gclid=CjwKCAjw46CVBhB1EiwAgy6M4mVPxT2p1GnlLaTkw1G77EyJ_lQp04ChE1FcYA4wtG-IkGaKbY0MsBoCbCUQAvD_BwE"

}



result = requests.get(Web["IMDB"])
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="9.5")
parent = prices[3].parent
span = parent.find("bigcell")
print(span)
