# This is a sample Python script.
import json
import os
import requests as requests
from datetime import date
import config


def send_message(api_token, chat_id, msg):
    apiURL = f'https://api.telegram.org/bot{api_token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': msg
    }

    try:
        response = requests.post(apiURL, json=data)
        print(response.text)
    except Exception as e:
        print(e)


def send_photo(api_token, chat_id):
    apiURL = f'https://api.telegram.org/bot{api_token}/sendPhoto?chat_id={chat_id}'
    image1Path = './2022-11-23/photo1.jpg'
    files = {
        'photo': open(image1Path, 'rb')
    }

    try:
        response = requests.post(apiURL, files=files)
        print(response.text)
    except Exception as e:
        print(e)


def send_media(api_token, chat_id, img_dir_path, img_names):
    apiURL = f'https://api.telegram.org/bot{api_token}/sendMediaGroup'

    media_arr = []
    files = {}
    #for img_name in img_names:
    media_arr.append({"type": "photo", "media": "attach://" + img_names[0]})
    files[img_names[0]] = open(img_dir_path + "/" + img_names[0], 'rb')

    data = {
        "chat_id": chat_id,
        "media": json.dumps(media_arr)
    }

    try:
        response = requests.post(apiURL, data=data, files=files)
        print(response.text)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    apiToken = config.var_API_TOKEN
    chatID = config.var_CHAT_ID
    bookmarkFileName = 'bookmark.txt'

    today = date.today()
    str_today = today.strftime("%Y-%m-%d")
    today_img_dir_path = config.var_MEDIA_PATH + '/' + str_today
    bookmark_path = today_img_dir_path + '/' + bookmarkFileName

    # Found start index and create bookmark if not exists
    startIndex = 0
    if not os.path.exists(bookmark_path):
        open(bookmark_path, "x")
    else:
        f = open(bookmark_path, "r")
        startIndex = int(f.read())

    # Fetch all new images and send them
    arr = os.listdir(today_img_dir_path)
    arr.remove(bookmarkFileName)
    arr.sort()

    print(arr[startIndex:])
    send_media(apiToken, chatID, today_img_dir_path, arr[startIndex:])

    # Write new index
    f = open(bookmark_path, "w")
    f.write(str(len(arr)))
    f.close()

    # msg = '/!\ Motion detected END /!\\ \n{} images are currently saved'.format(count_files(today_img_dir_path))

    # send_message(apiToken, chatID, msg)
    # send_photo(apiToken, chatID)
    # send_media(apiToken, chatID)
