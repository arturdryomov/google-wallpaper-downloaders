import base64
import json
import os
import urllib2
import urlparse


REMOTE_URL = "https://www.gstatic.com/prettyearth/"
REMOTE_IDS_PATH = "ids.json"

LOCAL_PATH = "~/Downloads/Wallpapers/Google Maps/"


def download_wallpapers():
    create_wallpapers_path()

    print(":: Downloading Google Maps wallpapers.") 

    for wallpaper_id in get_wallpaper_ids():
        print(wallpaper_id)

        wallpaper_info = get_wallpaper_info(wallpaper_id)

        wallpaper_path = get_wallpaper_path(wallpaper_id)
        wallpaper_bytes = get_wallpaper_bytes(wallpaper_info)

        download_wallpaper(wallpaper_path, wallpaper_bytes)


def create_wallpapers_path():
    if not os.path.exists(get_wallpapers_path()):
        os.makedirs(get_wallpapers_path())


def get_wallpapers_path():
    return os.path.abspath(os.path.expanduser(LOCAL_PATH))


def get_wallpaper_ids():
    with open(get_wallpaper_ids_path()) as wallpaper_ids_file:
        return json.load(wallpaper_ids_file)


def get_wallpaper_ids_path():
    return os.path.join(os.path.dirname(__file__), REMOTE_IDS_PATH)


def get_wallpaper_info(wallpaper_id):
    wallpaper_info_url = get_wallpaper_info_url(wallpaper_id)

    return json.load(urllib2.urlopen(wallpaper_info_url))["dataUri"]


def get_wallpaper_info_url(wallpaper_id):
    return urlparse.urljoin(REMOTE_URL, "{id}.json".format(url=REMOTE_URL, id=wallpaper_id))


def get_wallpaper_path(wallpaper_id):
    wallpapers_path = get_wallpapers_path()
    wallpaper_filename = "{id}.jpg".format(id=wallpaper_id)

    return os.path.join(wallpapers_path, wallpaper_filename)


def get_wallpaper_bytes(wallpaper_info):
    bytes_start_position = wallpaper_info.index(",") + 1

    return base64.b64decode(wallpaper_info[bytes_start_position:])


def download_wallpaper(wallpaper_path, wallpaper_bytes):
    with open(wallpaper_path, "wb") as wallpaper_file:
        wallpaper_file.write(wallpaper_bytes)


if __name__ == "__main__":
    download_wallpapers()
