import requests
from bs4 import BeautifulSoup

line_notify_token = '5T7DYnwuIMLSNqvsyXSYnIGMPAoNJZidwIw6jRhNhAf'
line_notify_api = 'https://notify-api.line.me/api/notify'
 
URL = 'https://www.levanga.com/schedule/list/?scheduleMonth=5'
headers = {"User-Agent": "hoge"}

resp = requests.get(URL, timeout=1, headers=headers)
r_text = resp.text

b_soup = BeautifulSoup(r_text, 'html.parser')
schedules = b_soup.select("table[class='schedule-detail']")

message = "\n"
for idx, schedule in enumerate(schedules):
    date = schedule.select_one("td[class='day-box']").p.text
    team_name = schedule.select_one("td[class='team-name pc']").p.text
    staduim_name = schedule.select_one("p[class='stadium-name']").text
    pref = schedule.select_one("p[class='pref']").text
    score_left = schedule.select_one("span[class='score score-left']").text
    score_right = schedule.select_one("span[class='score score-right']").text
    game_info = schedule.select_one("[class='result-selector-box']").ul.li.a.get('href')

    add_message = f'No.{idx+1}\n日程: {date}\nチーム名: {team_name}\nスタジアム: {staduim_name}\n都道府県: {pref}\nスコア: {score_left}-{score_right}\n試合情報: {game_info}\n\n'
    message += add_message


payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token} 
line_notify = requests.post(line_notify_api, data=payload, headers=headers)
