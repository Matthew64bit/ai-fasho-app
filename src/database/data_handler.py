import os
import cv2
import uuid
from src.utils.text_formatter import format_counter, format_time
from src.utils.image_fromatter import stitch_images
import json

FILEPATH = f"C:\\Users\\{os.getlogin()}\\Pictures\\"

def organize(conn, cur):
    print("Chose image format:\n1 for APPLE || 2 for WINDOWS")
    choice = int(input())

    if choice == 1:
        data = organize_windows()


def organize_windows():
    print("Please input start date and time in following format:\nYYYY MM DD")
    date = input().split(' ')

    print("Please input starting counter, if no value inserted default value is 0")
    counter = int(input())
    if counter is None:
        counter = 0

    data = []
    bookmark = None
    for h in range(0, 24):
        for m in range(0, 60):
            for s in range(0, 60):
                ss, mm, hh = format_time(s), format_time(m), format_time(h)
                if os.path.exists("{}Screenshots\\Screenshot {}-{}-{} {}{}{}.png".format(FILEPATH, date[0], date[2], date[1], hh, mm, ss)):
                    cid = uuid.uuid4()
                    data.append(cid)
                    # TODO - Image pair for windows


                    bookmark, item = read_article(bookmark)
                    data.append(item)
    return data


def organize_apple():
    print("Please input starting index of picture:")
    idx = int(input())
    if idx is None:
        idx = 0

    data = []
    bookmark = None
    while idx < 9999:
        my_path = "{}Screenshots\\IMG_{}.png".format(FILEPATH, format_counter(idx))
        if os.path.exists(my_path):
            cid = str(uuid.uuid4())

            img1 = cv2.imread("{}Screenshots\\IMG_{}.png".format(FILEPATH, format_counter(idx)))
            img2 = cv2.imread("{}Screenshots\\IMG_{}.png".format(FILEPATH, format_counter(idx + 1)))
            idx += 2

            stitch = stitch_images(img1, img2)
            cv2.imwrite("{}Clothes\\{}.png".format(FILEPATH, cid), stitch)

            # TODO - Bookmark
            bookmark, item = read_article(bookmark)
            item["id"] = cid
            data.append(item)
        else:
            idx += 1
    return data

def clean_newlines(obj):
    if isinstance(obj, dict):
        return {k: clean_newlines(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [clean_newlines(elem) for elem in obj]
    elif isinstance(obj, str):
        return obj.strip()  # This removes the \n and leading/trailing spaces
    return obj


def data_to_json(data):
    clean_data = clean_newlines(data)
    with open(f"{FILEPATH}clothes.json", "w") as f:
        json.dump(clean_data, f, indent = 4)


def read_article(bookmark=None):
    idx = 0
    val = []
    if bookmark is not None:
        with open(f"{FILEPATH}clothes.txt", "r") as f:
            f.seek(bookmark)
            while idx < 10:
                line = f.readline()
                if ' ' in line:
                    val.append(line.split(' '))
                else:
                    val.append(line)
                idx += 1
            line = f.readline()
            line = f.readline()
            bookmark = f.tell()
    else:
        with open(f"{FILEPATH}clothes.txt", "r") as f:
            while idx < 10:
                line = f.readline()
                if ' ' in line:
                    val.append(line.split(' '))
                else:
                    val.append(line)
                idx += 1
            line = f.readline()
            line = f.readline()
            bookmark = f.tell()
    return bookmark, {
        "id": None,
        "brand": val[0],
        "category": val[1],
        "gender": val[2],
        "style": val[3],
        "fit": val[4],
        "model": val[5],
        "colours": val[6],
        "season": val[7],
        "price": val[8],
        "url": val[9]
    }
