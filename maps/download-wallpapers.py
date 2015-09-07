#!/usr/bin/env python2

'''
Copyright 2014 Artur Dryomov

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


import json
import os
import urllib2
import urlparse


REMOTE_URL = "https://earthview.withgoogle.com/download/"
REMOTE_IDS_PATH = "ids.json"

LOCAL_PATH = "wallpapers"


def download_wallpapers():
    create_wallpapers_path()

    print(":: Downloading Google Maps wallpapers.")

    for wallpaper_id in get_wallpaper_ids():
        print(wallpaper_id)

        wallpaper_url = get_wallpaper_url(wallpaper_id)
        wallpaper_path = get_wallpaper_path(wallpaper_id)

        download_wallpaper(wallpaper_url, wallpaper_path)


def create_wallpapers_path():
    wallpapers_path = get_wallpapers_path()

    if not os.path.exists(wallpapers_path):
        os.makedirs(wallpapers_path)


def get_wallpapers_path():
    wallpapers_path = os.path.dirname(os.path.realpath(__file__))

    return os.path.abspath(os.path.join(wallpapers_path, LOCAL_PATH))


def get_wallpaper_ids():
    with open(get_wallpaper_ids_path()) as wallpaper_ids_file:
        return json.load(wallpaper_ids_file)


def get_wallpaper_ids_path():
    return os.path.join(os.path.dirname(__file__), REMOTE_IDS_PATH)


def get_wallpaper_url(wallpaper_id):
    return urlparse.urljoin(REMOTE_URL, get_wallpaper_name(wallpaper_id))


def get_wallpaper_path(wallpaper_id):
    wallpapers_path = get_wallpapers_path()
    wallpaper_name = get_wallpaper_name(wallpaper_id)

    return os.path.join(wallpapers_path, wallpaper_name)


def get_wallpaper_name(wallpaper_id):
    return "{id}.jpg".format(id=wallpaper_id)


def download_wallpaper(wallpaper_url, wallpaper_path):
    with open(wallpaper_path, "wb") as wallpaper_file:
        wallpaper_file.write(urllib2.urlopen(wallpaper_url).read())


if __name__ == "__main__":
    download_wallpapers()
