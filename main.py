import requests
import os
from bs4 import BeautifulSoup


def create_latest_news_log(log_txt, file_path):
    f = open(file_path, 'w')
    f.write(str(log_txt))
    f.close()


def read_text_file(file_path):
    f = open(file_path, 'r', encoding='UTF-8')
    data = f.read()
    return data


def create_latest_news_message(b_soup):
    '''
    最新ニュースがあれば、メッセージを作成する処理
    '''
    list_cards = b_soup.select("li[class='list-card']")

    message = "\n"
    for idx, card in enumerate(list_cards):
        if idx >= 1:
            # 最初の１つ目のみ最新なのでmessage作成する
            continue

        message += f'##新着##\n  {str(card.p.text)}\n'
        message += f'{card.a.get("href")}\n\n'

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

    # 最後に取得したニュース
    latest_news = read_text_file("db/log/check_logs/latest_news_log.txt")

    # 通知用のメッセージ
    message = create_latest_news_message(b_soup)

    if message != latest_news:
        print("最新のニュースが更新されています。")
        print("############最新ニュース############")
        print(message)
        create_latest_news_log(
            message, "db/log/check_logs/latest_news_log.txt")
        post_to_line(message, line_notify_token)
    else:
        print("最新ニュースは更新されていません。")

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
