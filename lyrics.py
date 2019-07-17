
import requests
import json



while True:
    print()
    print("Welcome to the Musixmatch API explorer!")
    print()
    print("MENU OPTIONS")
   
    print("1 - Search for the lyrics of a song")
    print("0 - Exit")
    print()
    choice = input("> ")
    print()

    if choice == "0":
        break

    # see the paramaters for an api method

    # example
    if choice == "1":
        print("Whats's the name of the artist?")
        artist_name = input("> ")
        print("What's the name of the track?")
        track_name = input("> ")
        print()
        api_key="54dce147885b93e7d2bfe74d4be23c21"
        base_url="https://api.musixmatch.com/ws/1.1/"
        api_req=base_url+"matcher.lyrics.get?format=json&callback=callback&q_artist="+artist_name+"&q_track="+track_name+"&apikey="+api_key
        request = requests.get(api_req)
        data = request.json()
        data = data['message']['body']
        print("API Call: " + api_req)
        print()
        print(data['lyrics']['lyrics_body'])

    # check if the user wants to go again
    print()
    print("Again? (y/n)")
    again = input("> ")
    if again == "n":
        break
