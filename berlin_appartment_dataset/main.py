from bs4 import BeautifulSoup
import json
import os

listings_dir = "listings"
files = os.listdir(listings_dir)
counter = 0 # I like to include a counter to print in the terminal to monitor my progress. I hate it when a program just 'runs'.

with open("listings.jsonl", "a", encoding="utf-8") as save:
    for fil in files:
        with open("listings/" + fil, "r", encoding="utf-8") as file:
            content = file.read()
            soup = BeautifulSoup(content, "html.parser")

        # Get address
        spans = soup.find_all("span")
        address = [span.get_text().strip() for span in spans if "Berlin" in span.get_text()][0]

        # Get appartment info
        dls = soup.find_all("dl")
        for dl in dls: # This builds 2 lists, fields (such as floor, size, pets, etc) and info (such as 2nd floor of 2, no pets.)
            dts = [dl.find_all("dt") for dl in dls] # The appartment info fields are kept in dt tags
            dds = [dl.find_all("dd") for dl in dls] # and the rest of the info is kept in the following dd tag.

        info_list = []
        for x in range(len(dls)):
            if len(dts[x]) > 0: # The site uses empty dt and dd tags for layout purposes. This filters them out
                info_list.append([dts[x][0].get_text().strip(), dds[x][0].get_text().strip()]) # and combines the two lists to usable strings pairs.
        
        # A lot of the listings have large white spaces and new lines for layout purposes. 
        # This cleans them out for more readable results.
        for y in info_list: 
            value = y[1].strip()
            value = " ".join(value.split())
            y[1] = value

        sub_dict = {}
        address_fields = ["Postcode", "City"] # The street address isn't necessary. I've included postcode and city for broader datasets.

        total_info = []

        # And finally, combine everything into a single Python dict and save it to file.
        # I always like to save each result to file as I go to prevent data loss in case something goes wrong.
        address_breakdown = address.split(",")
        sub_dict[address_fields[0]] = address_breakdown[-1].strip().split(" ")[0]
        sub_dict[address_fields[1]] = address_breakdown[-1].strip().split(" ")[1].split("\n")[0]

        for info in info_list:
            sub_dict[info[0]] = info[1]

        counter += 1
        print(f"{counter}: Done.") # Honestly, watching the progress just makes me feel better.

        save.write(json.dumps(sub_dict, ensure_ascii=False) + "\n")
