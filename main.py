import requests
import json


# doc: https://docs.api.jikan.moe



url = "https://api.jikan.moe/v4/"

def topAnimes():


    url_top = "https://api.jikan.moe/v4/top/anime"

    top_animes = requests.get(url_top)
    top_animes = top_animes.json()

    x = 1
    for i in range(0, 20):
        anime_titles = top_animes["data"][i]['title']
        mal_id = top_animes["data"][i]['mal_id']
        print("\n",x,"-",anime_titles, " - (Mal Id:",mal_id,")")
        x += 1


def searchAnime():


    #anime_id = input("\nType the anime ID: ")

    #url_search_id = f"https://api.jikan.moe/v4/anime/{anime_id}"

    anime_name = input("\nType the anime name: ")

    url_search = f"https://api.jikan.moe/v4/anime/?q={anime_name}/Zero&page=1"

    search_anime = requests.get(url_search).json()

    for i in range(0, 4):
        anime_id = search_anime["data"][i]['mal_id']
        anime_url = search_anime["data"][i]['url']
        anime_title = search_anime["data"][0]['title']
        anime_title_english = search_anime["data"][i]['title_english']
        type = search_anime["data"][i]['type']
        episodes = search_anime["data"][i]['episodes']
        status = search_anime["data"][i]['status']
        score = search_anime["data"][i]['score']
        rank = search_anime["data"][i]['rank']
        popularity = search_anime["data"][i]['popularity']
        year = search_anime["data"][i]['year']

        print("\nTitle:",anime_title,"\nTitle(English):",anime_title_english,"\nMal ID:",anime_id, "\nUrl:",anime_url,"\nEpisodes:",episodes,"\nType:",type,"\nSatus:",status,
              "\nScore:",score, "\nRank:",rank,"\nPopularity:",popularity, "\nYear:",year)

        print("\n----------------------------------------------------------------------------------------")




def searchAnimeID():


    anime_id = input("\nType the anime ID: ")

    url_search_id = f"https://api.jikan.moe/v4/anime/{anime_id}"


    search_anime = requests.get(url_search_id).json()

    anime_id = search_anime["data"]['mal_id']
    anime_url = search_anime["data"]['url']
    anime_title = search_anime["data"]['title']
    anime_title_english = search_anime["data"]['title_english']
    type = search_anime["data"]['type']
    episodes = search_anime["data"]['episodes']
    status = search_anime["data"]['status']
    score = search_anime["data"]['score']
    rank = search_anime["data"]['rank']
    popularity = search_anime["data"]['popularity']
    year = search_anime["data"]['year']

    print("\nTitle:", anime_title, "\nTitle(English):", anime_title_english, "\nMal ID:", anime_id, "\nUrl:", anime_url,
          "\nEpisodes:", episodes, "\nType:", type, "\nSatus:", status,
          "\nScore:", score, "\nRank:", rank, "\nPopularity:", popularity, "\nYear:", year)


def search_users():


    username = input("\nType the username: ")

    url_user = f"https://api.jikan.moe/v4/users/{username}"

    user_data = requests.get(url_user)
    user_data = user_data.json()

    mal_id = user_data["data"]['mal_id']
    username = user_data["data"]["username"]
    profile_url = user_data["data"]["url"]
    location = user_data["data"]["location"]

    print("Info:","\nMal ID:",mal_id,"\nUsername:",username,"\n url profile:",profile_url,"\n Location:",location)


if __name__ == '__main__':

    opc = ""
    while opc != "exit":

        print("\n===================================================")
        print("                     Choose an option")
        print("===================================================")
        print("  [1] - Show top animes ")
        print("  [2] - Search anime")
        print("  [3] - Search anime by ID")
        print("  [4] - Search user")
        print("  [exit]")
        print("===================================================")

        opc = input("Choose an option: ")

        if opc == "1":
            topAnimes()
        elif opc == "2":
            searchAnime()
        elif opc == "3":
            searchAnimeID()
        elif opc == "4":
            search_users()
        elif opc == "exit":
            print("\nA sair...")
        else:
            print("\nERROR! - INVALID OPTION!")
