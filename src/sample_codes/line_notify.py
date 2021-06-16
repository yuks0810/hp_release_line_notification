import requests

line_notify_token = '5T7DYnwuIMLSNqvsyXSYnIGMPAoNJZidwIw6jRhNhAf'
line_notify_api = 'https://notify-api.line.me/api/notify'
message = '送信てすとーーーー。' #送るメッセージ


payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token} 
line_notify = requests.post(line_notify_api, data=payload, headers=headers)
