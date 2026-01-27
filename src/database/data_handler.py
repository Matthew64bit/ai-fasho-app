import os
import cv2
import uuid
import json
import datetime
from . import crud
from src.utils.text_formatter import format_counter, format_time
from src.utils.image_fromatter import stitch_images
from src.my_logger import logger

logger.set_log_file(__name__)
FILEPATH = f'C:\\Users\\{os.getlogin()}\\Pictures\\'
debug_val = 0


def organize(conn, cur):
    print('Chose image format:\n1 for APPLE || 2 for WINDOWS')
    choice = int(input())

    if choice == 1:
        data = organize_apple()
    elif choice == 2:
        data = organize_windows()
    else:
        raise ValueError('Index out of bounds')
    try:
        for d in data:
            crud.create(conn, cur, d)
        logger.info(f'Inserted {len(data)} items successfully!')

    except Exception as e:
        logger.error(f'Encountered an error: {str(e)}')


def organize_windows():
    print('Please input start date and time in following format:\nYYYY MM DD')
    date = input().split(' ')

    images = []
    data = []
    bookmark = None
    for h in range(0, 24):
        for m in range(0, 60):
            for s in range(0, 60):
                ss, mm, hh = format_time(s), format_time(m), format_time(h)
                if os.path.exists('{}Screenshots\\Screenshot {}-{}-{} {}{}{}.png'.format(FILEPATH, date[0], date[2], date[1], hh, mm, ss)):
                    images.append(cv2.imread('{}Screenshots\\Screenshot {}-{}-{} {}{}{}.png'.format(FILEPATH, date[0], date[2], date[1], hh, mm, ss)))

    idx = 0
    while idx < len(images):
        stitch = stitch_images(images[idx], images[idx + 1])
        cid = str(uuid.uuid4())
        cv2.imwrite('{}Clothes\\{}.png'.format(FILEPATH, cid), stitch)

        bookmark, item = read_article(bookmark)
        item['id'] = cid
        data.append(item)

        idx+= 2


    return data


def organize_apple():
    print('Please input starting index of picture:')
    idx = int(input())
    if idx is None:
        idx = 0

    data = []
    bookmark = None
    while idx < 9999:
        my_path = '{}Screenshots\\IMG_{}.png'.format(FILEPATH, format_counter(idx))
        if os.path.exists(my_path):
            cid = str(uuid.uuid4())

            img1 = cv2.imread('{}Screenshots\\IMG_{}.png'.format(FILEPATH, format_counter(idx)))
            img2 = cv2.imread('{}Screenshots\\IMG_{}.png'.format(FILEPATH, format_counter(idx + 1)))
            idx += 2

            stitch = stitch_images(img1, img2)
            cv2.imwrite('{}Clothes\\{}.png'.format(FILEPATH, cid), stitch)

            bookmark, item = read_article(bookmark)
            item['id'] = cid
            data.append(item)
        else:
            idx += 1
    return data


def data_to_json(data):
    date = str(datetime.datetime.now().date())
    with open(f'{FILEPATH}{date}.json', 'w') as f:
        json.dump(data, f, indent = 4)


def read_article(bookmark=None):
    idx = 0
    val = []

    if bookmark is not None:
        with open(f'{FILEPATH}clothes.txt', 'r') as f:
            f.seek(bookmark)
            while idx < 10:
                line = f.readline()
                if ' ' in line:
                    val.append([x.strip() for x in line.split(' ')])
                else:
                    val.append(line.strip())
                idx += 1
            line = f.readline()
            bookmark = f.tell()
    else:
        with open(f'{FILEPATH}clothes.txt', 'r') as f:
            while idx < 10:
                line = f.readline()
                if ' ' in line:
                    val.append([x.strip() for x in line.split(' ')])
                else:
                    val.append(line.strip())
                idx += 1
            line = f.readline()
            bookmark = f.tell()

    if type(val[6]) != list:
        val[6] = [val[6]]

    return bookmark, {
        'id': None,
        'brand': val[0],
        'category': val[1],
        'gender': val[2],
        'style': val[3],
        'fit': val[4],
        'model': val[5],
        'colours': val[6],
        'season': val[7],
        'price': val[8],
        'url': val[9]
    }
