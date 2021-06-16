import requests
from bs4 import BeautifulSoup

line_notify_token = '5T7DYnwuIMLSNqvsyXSYnIGMPAoNJZidwIw6jRhNhAf'
line_notify_api = 'https://notify-api.line.me/api/notify'
 
URL = 'https://www.levanga.com/news/'
headers = {"User-Agent": "hoge"}

resp = requests.get(URL, timeout=1, headers=headers)
r_text = resp.text

b_soup = BeautifulSoup(r_text, 'html.parser')
list_cards = b_soup.select("li[class='list-card']")

message = "\n"
for idx, card in enumerate(list_cards):
    message += f'{idx+1}: {str(card.p.text)}\n'
    message += f'{card.a.get("href")}\n\n'

payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token} 
line_notify = requests.post(line_notify_api, data=payload, headers=headers)


# for i in range(1,12):

# URL = f'https://www.levanga.com/schedule/list/?scheduleYear=2021&scheduleMonth={i}'
# headers = {"User-Agent": "hoge"}

# resp = requests.get(URL, timeout=1, headers=headers)
# r_text = resp.text

# b_soup = BeautifulSoup(r_text, 'html.parser')
# elms = b_soup.select("p[class='title']")

# message = "\n"
# for idx, elm in enumerate(elms):
#     message += f'{idx+1}: {str(elm.text)}\n\n'


# payload = {'message': message}
# headers = {'Authorization': 'Bearer ' + line_notify_token} 
# line_notify = requests.post(line_notify_api, data=payload, headers=headers)
