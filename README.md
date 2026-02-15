# Dave-Ronnert-Portfolio
Dave Ronnert's coding portfolio

## MyAnimeList Title Scraper project

I wanted to start with a project which matches my interests and being a fan of anime, I decided to start with a simple anime title srcaper from MyAnimeList (MAL).
I tried to be as ethical about my script as possible, only taking data from publicly available pages and giving the site a random pause between requests of between 2.5 and 3.5 seconds.

### Key Features:
- Scrapes **publicly accessible** pages on MAL for the **Title**, **MAL_ID** and **URL** for each anime listed on the site.
- **Handles and logs any error codes** which occur during the scraping process including 404, 429 and 500.
- **Saves the information incrementally** to an external txt file (title_ids.txt) as it goes in case of crash or failure during runtime.
- Output: 29.635 titles as of mid-February 2026.

### Tech Stack
- **Python**
- **requests** and **BeautifulSoup** - For Web Scraping.
- **time**, **random** - For polite pauses between requests.
- **string.ascii_uppercase** - for quick alphabetical list.

### What I learned during this project
- Extracting data from **tabled information** on a website rather than simple paragraphs and a_tags.
- **Robust parsing of HTML** rather than just endless string splits.
- **Handling pagination** for scraping purposes.
- Adding **error logging and handling**.
- **Ethical scraping practices**, using realistic headers and **respect for the website**.

### Files Included
- 'main.py' - The main runnable Python script
- 'title_ids.txt' - The output of the run script including all 29,635 titles saves in the format: Title | MAL_ID | URL
- 'error_log.txt' - An empty file since I didn't encounter any errors to log while running this script, but I felt it would be prudent to include all files associated with this project.

The output of this project will be used in my next project which is to use Jikan (MAL's unofficial API) to build a complete database of MAL's entire catalogue for data analysis purposes.
Feel free to run and modify this code for yourself.

### Prerequisites:
- Requests
- BeautifulSoup (BS4)
