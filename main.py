import requests
import os
from bs4 import BeautifulSoup
import datetime


def read_text_file(file_path):
    f = open(file_path, 'r', encoding='UTF-8')
    data = f.read()
    return data


def create_latest_news_message(b_soup):
    '''
    最新ニュースがあれば、メッセージを作成する処理

    return:
        もし、message内容に更新があれば、messageを返す。
        一つもアップデートがなければ `None` をmessageに入れて返す。
    '''
    list_cards = b_soup.select("li[class='list-card']")
    # 今日の日付取得
    date_today = str(datetime.datetime.now().strftime('%Y-%m-%d'))

    message = "\n"
    update_news_counter = 0
    for card in list_cards:
        if card.select_one('p[class="update"]').text == date_today:
            # 今日の日付にアップデートされたニュースだけmessageに追加する
            message += f'##新着##\n  {str(card.p.text)}\n'
            message += f'{card.a.get("href")}\n\n'

            update_news_counter += 1

    if update_news_counter == 0:
        message = None

    return message


def post_to_line(message, line_notify_token):
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)


if __name__ == "__main__":
    line_notify_token = os.environ["LINE_TOKEN"]
    line_notify_api = 'https://notify-api.line.me/api/notify'

    URL = 'https://www.levanga.com/news/'
    headers = {"User-Agent": "hoge"}
    resp = requests.get(URL, timeout=10, headers=headers)
    r_text = resp.text
    b_soup = BeautifulSoup(r_text, 'html.parser')

    # 通知用のメッセージ作成
    # 新しいNewsがなければ None がmessageの中に入っている。
    message = create_latest_news_message(b_soup)

    if message != None:
        message += "\n\nニュース一覧: https://www.levanga.com/news/"
        print("最新のニュースが更新されています。")
        print("############最新ニュース############")
        print(message)
        
    else:
        print("最新ニュースは更新されていません。")
        message = '本日は最新のニュースはありません。\nニュース一覧: https://www.levanga.com/news/'
    
    post_to_line(message, line_notify_token)




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
