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
import posixpath
import urllib
import urllib2
import urlparse


REMOTE_URL = "https://storage.googleapis.com/chromeos-wallpaper-public/"
REMOTE_MANIFEST = "manifest_en.json"

LOCAL_PATH = "~/Downloads/Wallpapers/Chrome OS/"


def download_wallpapers():
    create_wallpapers_path()

    print(":: Downloading Chrome OS wallpapers.")

    for wallpaper_info in get_wallpapers_info()["wallpaper_list"]:
        wallpaper_url = get_wallpaper_url(wallpaper_info)
        wallpaper_path = get_wallpaper_path(wallpaper_url)

        print(wallpaper_url)

        download_wallpaper(wallpaper_url, wallpaper_path)


def create_wallpapers_path():
    wallpapers_path = get_wallpapers_path()

    if not os.path.exists(wallpapers_path):
        os.makedirs(wallpapers_path)


def get_wallpapers_path():
    return os.path.abspath(os.path.expanduser(LOCAL_PATH))


def get_wallpapers_info():
    return json.load(urllib2.urlopen(get_wallpapers_info_url()))


def get_wallpapers_info_url():
    return urlparse.urljoin(REMOTE_URL, REMOTE_MANIFEST)


def get_wallpaper_url(wallpaper_info):
    return wallpaper_info["base_url"] + "_high_resolution.jpg"


def get_wallpaper_path(wallpaper_url):
    wallpapers_path = get_wallpapers_path()
    wallpaper_filename = get_wallpaper_filename(wallpaper_url)

    return os.path.join(wallpapers_path, wallpaper_filename)


def get_wallpaper_filename(wallpaper_url):
    return posixpath.basename(urlparse.urlsplit(wallpaper_url).path)


def download_wallpaper(wallpaper_url, wallpaper_path):
    wallpaper_contents = urllib2.urlopen(urllib.quote(wallpaper_url, safe=":/"))

    with open(wallpaper_path, "wb") as wallpaper_file:
        wallpaper_file.write(wallpaper_contents.read())


if __name__ == "__main__":
    download_wallpapers()
