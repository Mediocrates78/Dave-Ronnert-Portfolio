import requests
from bs4 import BeautifulSoup
from string import ascii_uppercase
from time import sleep
import random as rnd

def get_request(url):
    headers = {
        "USER-AGENT": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
        "ACCEPT": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        "ACCEPT-LANGUAGE": 'en-AU,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'
        }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    return [response.status_code, soup]

# Allowing for a minimum average of 3 seconds between any requests to keep from flooding the site.
# For minimum time, just add 0 to any pause request. Other than that, I'm allowing for flexible pause times.
def pause(length): 
    sleep(rnd.uniform(2.5, 3.5) + length)

# This extracts the Title, MAL ID and specific URL for anime listed on MAL's alphabetical anime search pages.
# It only exracts from publicly accessable pages.
def get_title_deets(raw_html):
    table = raw_html.find_all("table")[1]
    trs = table.find_all("tr")[1:]
    a_tags = [tr.find_all("a")[1] for tr in trs]
    titles = [tag.get_text(strip=True) for tag in a_tags]
    urls = [str(tag).split('href=')[1].split(" ")[0].strip() for tag in a_tags]
    id_nos = [no.split("/")[-2] for no in urls]
    return [titles, id_nos, urls]

def error_log(code):
    with open("error_log.txt", "a", encoding="utf-8")as file:
        if code == 404:
            comment = "File missing."
        elif code == 429:
            comment = "Too many requests."
        else:
            comment = "Unknown error."
        file.write(f"Error: {code} - {comment}\n")
        print(f"Error: {code} - {comment}\n") # Just a quick print into the terminal in case something goes wrong, I don't have to guess.


html = "https://myanimelist.net/anime.php?letter="
letters = "." + ascii_uppercase

with open("title_ids.txt", "a", encoding="utf-8") as file:
    for letter in letters:
        show = 0
        attempt = 0
        while True:
            if show == 0: # basically, if it's the first page listed for that letter.
                url = html + letter
            else:
                url = html + letter + "&show=" + str(show)
            pause(0)
            code, page = get_request(url)
            if code == 200: # If the page is there and works, run the script
                attempt = 0 # Automatically reset the attempt counter for the errors
                titles, ids, urls = get_title_deets(page)
                for t in range(len(titles)):
                    # Scrub through and save this info to a txt file for later reference.
                    file.write(f"{titles[t]} | {ids[t]} | {urls[t]}\n")
                print(f"{url}: {len(titles)}\n")
                # A visual aid in the terminal to monitor progress.
                # I don't like when a program just 'runs'. I prefer to know what's going on.
                if len(titles) < 50:
                    break
                show += 50

            elif code == 404:
                error_log(code)
                pass
            elif code == 429: # This allows for 5 attempts to wait out a code 429 (too many requests).
                error_log(code)
                if attempt >= 5:
                    break # If it's made 5 attempts, shut down the whole code and wait for assistence.
                else:
                    # Otherwise, it waits an initial 2 minutes which increases exponentially with each subsequent attempt.
                    pause(60 * (2 ** (attempt + 1)))
                    attempt += 1
            else:
                error_log(code)
                if attempt >= 5:
                    break
                else:
                    # This should cover any server-side issues, such as code 500. Just wait a sec and try again.
                    #If it doesn't resolve itself after 5 attempts, there's clearly an issue and move on.
                    attempt += 1
            