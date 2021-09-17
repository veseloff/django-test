from pexels_api import API
from random import choice
is_first_request = True
photos_list = []


def get_picture():
    global is_first_request
    if is_first_request:
        print("=========")
        print("ПЕРВАЯ КАРТИНКА")
        print("=========")
        get_fifty_pictures_kitten(1)
        is_first_request = False
    return choice(photos_list)


def get_fifty_pictures_kitten(page):
    global photos_list
    PEXELS_API_KEY = '563492ad6f91700001000001ddd892d27efb4afa85017bcebb29787d'
    api = API(PEXELS_API_KEY)
    api.search('kitten', page=page, results_per_page=50)
    photos = api.get_entries()
    photos_list = [photo.original for photo in photos]
    # for photo in photos:
    #   print('Photographer: ', photo.photographer)
    #   print('Photo url: ', photo.url)
    #   print('Photo original size: ', photo.original)