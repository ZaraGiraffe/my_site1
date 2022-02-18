import folium
from geopy.geocoders import Nominatim
import requests
import json
import os

PATH = "templates/map.html"
TOKEN = "Bearer AAAAAAAAAAAAAAAAAAAAAH4VZQEAAAAAov60xmwpdz%2BzoABDW7wBfq7kYSM%3DTGScFHiSQ3T57NmKIc7yVVqCHfxviEfYV8nVzpSLywFtZSSDqb"
templ_ids = "https://api.twitter.com/1.1/friends/ids.json?cursor=-1&screen_name={}&count=100"
templ_loc = "https://api.twitter.com/2/users?ids={}&user.fields=location"


def get_ids(name):
    string = templ_ids.format(name)
    get = requests.get(string, headers={"authorization": TOKEN})
    dct = json.loads(get.text)
    return dct['ids']


def location(ID):
    string = templ_loc.format(ID)
    get = requests.get(string, headers={"authorization": TOKEN})
    dct = json.loads(get.text)
    return dct['data'][0]


def create_map(name):
    data = []
    try:
        try:
            mas = get_ids(name)
        except:
            with open(PATH, 'w') as file:
                html = '{% extends "layout.html" %} {% block body %} <h2> invalid username </h2> {% endblock %}'
                file.write(html)
            return
        for i in mas:
            data.append(location(i))
    except:
        pass
    map = folium.Map()
    html = """<h4>{}</h4>
    username: {},<br>
    """
    geolocator = Nominatim(user_agent="zararaza")
    data2 = []
    for i in data:
        try:
            loc = geolocator.geocode(i["location"])
            data2.append(((loc.latitude, loc.longitude), i))
        except:
            pass
    fg = folium.FeatureGroup(name="friends")
    for i in data2:
        iframe = folium.IFrame(html=html.format(i[1]['name'], i[1]['username']), width=300, height=100)
        fg.add_child(folium.Marker(location=i[0], popup=folium.Popup(iframe)))
    map.add_child(fg)
    map.add_child(folium.LayerControl())
    os.remove(PATH)
    map.save(PATH)
