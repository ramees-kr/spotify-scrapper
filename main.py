import requests
import json
from pprint import pprint

def get_data(file_name,data_key):
    with open(file_name) as file:
        data = json.load(file)
    return data[data_key]

def get_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }             
    
    data = get_data('settings.json','credentials')

    response = requests.post(url, headers=headers, data=data)
    pprint(response.json())

    return response.json()['access_token']

def get_playlist(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?fields=items(track(href,name))"
    payload = {}
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

def main():
    token = get_token()
    print(token)

    get_playlist(token)
    #print(playlist)


if __name__ == '__main__':
    main()