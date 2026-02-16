# Dave-Ronnert-Portfolio


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
- 'title_ids.txt' - The output file from MAL Title Scraper and input file for MADbot.
- 'main.py' - The main runnable Python script
- 'title_ids.txt' - The output of the run script including all 29,635 titles saves in the format: Title | MAL_ID | URL
- 'error_log.txt' - An empty file since I didn't encounter any errors to log while running this script, but I felt it would be prudent to include all files associated with this project.

The output of this project will be used in my next project which is to use Jikan (MAL's unofficial API) to build a complete database of MAL's entire catalogue for data analysis purposes.
Feel free to run and modify this code for yourself.

### Prerequisites:
- Requests
- BeautifulSoup (BS4)

---
## MADbot MyAnimeDataset bot
The followup project from my MAL title scraper. This project is to create a full dataset of all anime listed on My Anime List's website using Jikan (MAL's unofficial API). I can then go on and use this dataset for Data Analysis on anime as a whole, tracking trends and answering the long standing question, "Has anime gotten worse?" Jikan has a request limit of 3/sec or 60/min. Since I was pulling almost 30,000 titles, I decided to steer well clear of the 1/second maximum and give myself an average 3 second interval between requests. This added significantly to the run time but I was pushing more for stability than speed. Discovering a major issue and restarting / rerunning would take longer than simply taking a little longer and have it run correctly the first time.

### Key Features
- **Uses Jikan** and the title_ids.txt file from my previous project to construct a dataset of MAL's entire catalogue.
- Recycles code from the previous project to **prevent needlessly rewriting the same code again**.
- Saves each anime's data in a **separate Json dictionary** for later retrieval and compilation.
- keeps the aired dates in a dictionary format to make it **more compatible with Python's time library**.

### Tech Stack
- **Python**
- **requests** - to interact with Jikan.
- **Json** - To save the data to a jsonl file for easy compilation later.
- **time**, **random** - for polite pauses between requests.

### What I learned during this project
- **Interacting with an API**.
- **Sorting and cleaning** the 'data' dictionary.
- **Preparing for and executing a large pull** from an API (the entire pull took approximately 30 hours to complete)

### Files Included
- main.py - The executable Python file.
- big_dic.jsonl - the collection of json dictionaries, one for each title.
- Error_log.txt - The error log recorded during the pull. In total 34 errors recorded, all code:500.

The output for this project is full of useful data which can be analyzed with Python libraries such as Pandas or MatPlotLib to track trends, possible predictions as to what types of anime might be popular in the future and see the growing pressure on the anime industry as a whole with ever increasing numbers of anime released each year.

### Prerequisites
- Requests
