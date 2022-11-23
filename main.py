# This is a sample Python script.
import json
import os
import requests as requests
from datetime import date
import config

def sendMessage(apiToken, chatId, msg):
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    data = {
        'chat_id': chatID,
        'text': msg
    }

    try:
        response = requests.post(apiURL, json=data)
        print(response.text)
    except Exception as e:
        print(e)


def sendPhoto(apiToken, chatId):
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendPhoto?chat_id={chatId}'
    image1Path = './2022-11-23/photo1.jpg'
    files = {
        'photo': open(image1Path, 'rb')
    }

    try:
        response = requests.post(apiURL, files=files)
        print(response.text)
    except Exception as e:
        print(e)


def sendMedia(apiToken, chatId):
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMediaGroup'
    image1Path = './2022-11-23/photo1.jpg'
    image2Path = './2022-11-23/photo2.jpg'

    data = {
        "chat_id": chatId,
        "media": json.dumps([
            {"type": "photo", "media": "attach://photo1.jpg"},
            {"type": "photo", "media": "attach://photo2.jpg"}
        ])
    }

    files = {
        "photo1.jpg": open(image1Path, 'rb'),
        "photo2.jpg": open(image2Path, 'rb')
    }

    try:
        response = requests.post(apiURL, data=data, files=files)
        print(response.text)
    except Exception as e:
        print(e)


def count_files(dir_path):
    count = 0
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    return count


if __name__ == '__main__':

    apiToken = config.var_API_TOKEN
    chatID = config.var_CHAT_ID

    today = date.today()
    str_today = today.strftime("%Y-%m-%d")
    today_img_dir_path = config.var_MEDIA_PATH + '/' + str_today

    msg = '/!\ Motion detected END /!\\ \n{} images are currently saved'.format(count_files(today_img_dir_path))

    sendMessage(apiToken, chatID, msg)
    # sendPhoto(apiToken, chatID)
    # sendMedia(apiToken, chatID)
