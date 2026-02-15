import requests
import json
from time import sleep
import random as rnd

def get_title(url):
    header = {"User-Agent": "MyAnimeDatabseBot MADbot - github.com/Mediocrates78"}
    response = requests.get(url, headers=header)
    return [response.status_code, response.json()]

def clean_dic(raw_dic): # Cleaning that dirty dic. I'm not including any image files. I don't want any dic pics.
    fields = ["mal_id", "url", "title", "title_english", "title_japanese", "type", "source",
        "episodes", "status", "aired", "duration", "rating", "score", "scored_by", "rank",
        "popularity", "members", "favorites", "synopsis", "season", "year", "producers", 
        "licensors", "studios", "genres", "themes", "demographics"]
    
    sub_dic = {} # Compiling the data from raw_dic into a nice clean dic
    for field in fields:
        sub_dic[field] = raw_dic["data"][field]

    strip_fields = ["producers", "licensors", "studios", "genres", "themes", "demographics"]
    for stripper in strip_fields: # These fields are docked inside another dic so I just want to strip out the names.
        sub_dic[stripper] = [s["name"] for s in sub_dic[stripper]]

    return sub_dic

def rest(length):
    sleep(length + rnd.uniform(2.5, 3.5))

def error_log(id, code):
    with open("error_log.txt", "a", encoding="utf-8")as file:
        if code == 404:
            comment = "File missing."
        elif code == 429:
            comment = "Too many requests."
        else:
            comment = "Unknown error."
        file.write(f"Error: {code} - {comment}\n")
        print(f"Error: {id} - {code} - {comment}\n")
    

# Get a complete list of all anime in MAL in alphabetical order by ID number.
with open("title_ids.txt", "r", encoding="utf-8") as ids_file:
    titles_list = ids_file.readlines()
    ids_list = [title.split(" | ")[1].strip() for title in titles_list]

counter = 0
with open("big_dic.jsonl", "a", encoding="utf-8") as big_dic: # I want the biggest, most comprehensive dic I can get.
    for mal_id in ids_list:
        url = f"https://api.jikan.moe/v4/anime/{mal_id}"
        attempt = 0

        rest(0)
        code, anime_dic = get_title(url)
        while True:
            if code == 200:
                cleaned_data = clean_dic(anime_dic)
                big_dic.write(json.dumps(cleaned_data, ensure_ascii=False) + "\n") # big_dic... json's dumps... I think I'll leave that one alone.
                counter += 1
                print(f"{counter}: {mal_id} - {cleaned_data["title"]}")
                break

            # I completely recycled my error handling from my Anime Title Scraper project.
            # No sence in writing the same code twice.
            elif code == 404: 
                error_log(mal_id, code)
                break

            elif code == 429:
                error_log(mal_id, code)
                if attempt >= 5:
                    break
                else:
                    rest(60 * (2 ** (attempt + 1)))
                    attempt += 1

            else:
                error_log(mal_id, code)
                if attempt >= 5:
                    break
                else:
                    rest(0)
                    attempt += 1

