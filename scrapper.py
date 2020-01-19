'''Felt cute, might delete later'''


import requests
from bs4 import BeautifulSoup as bs
import smtplib as mail

URL = 'https://www.amazon.in/dp/B07TVTHPRG/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B07TVTHPRG&pd_rd_w=RQLjM&pf_rd_p=357151f8-058c-46f1-b7d1-fa3647ce3999&pd_rd_wg=QoYWv&pf_rd_r=D7DY0QM8M1QA3SJEZXE5&pd_rd_r=681fdd87-9de3-4c78-8e9c-83af9320bfce&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE1S09FVU9BN0NTRiZlbmNyeXB0ZWRJZD1BMDQwNjUzOTM3QlpBRDVJNFJZVEUmZW5jcnlwdGVkQWRJZD1BMDY0MjAzNzJJVFkwU0gzSk5UOTMmd2lkZ2V0TmFtZT1zcF9kZXRhaWwmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

headers = { "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

def check_price():
	page = requests.get(URL, headers=headers)

	soup = bs(page.content, 'html.parser')

	#print(soup.prettify())

	title = soup.find(id="productTitle").get_text()

	price = soup.find(id="priceblock_dealprice").get_text()
	converted = float(''.join( i for i in price if i.isnumeric() or i=='.'))

	if converted<2000.00:
		send_email()

	print('price=',converted)
	print(title.strip())


def send_email():
	server = mail.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('iamsadhu98@gmail.com', 'Animesh1998')
	subject = "Price Fell down"
	body = 'Check the link below https://www.amazon.in/dp/B07TVTHPRG/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B07TVTHPRG&pd_rd_w=RQLjM&pf_rd_p=357151f8-058c-46f1-b7d1-fa3647ce3999&pd_rd_wg=QoYWv&pf_rd_r=D7DY0QM8M1QA3SJEZXE5&pd_rd_r=681fdd87-9de3-4c78-8e9c-83af9320bfce&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE1S09FVU9BN0NTRiZlbmNyeXB0ZWRJZD1BMDQwNjUzOTM3QlpBRDVJNFJZVEUmZW5jcnlwdGVkQWRJZD1BMDY0MjAzNzJJVFkwU0gzSk5UOTMmd2lkZ2V0TmFtZT1zcF9kZXRhaWwmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

	msg = f"Subject:{subject}\n\n{body}"

	server.sendmail(
		'iamsadhu98@gmail.com',
		'stant581@gmail.com',
		msg
		)

	print("Hey, Email has been sent")

	server.quit()

while True:
	check_price()
	time.sleep(60)
