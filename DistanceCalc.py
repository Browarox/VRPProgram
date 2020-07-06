# from bingmaps import apiservices
from pybingmaps import pybingmaps as bm
key = "Akaz-7y6btktEEz0ZbAaDESm0ZYYPbx-_UXcf2XBmQlTF_UM-0srnnPQ4Eu058Yi"
bing = bm.Bing(api_key=key)


def distance_calc(start, end):
    bing.route(start, end)
    return format(bing.travelDistance(start, end), '.3f')   # dodałem format, żeby były 3 cyfry po przecinku


if __name__ == '__main__':
    print(distance_calc((50.07031, 20.01635), (50.02911, 19.925505)))
