<<<<<<< HEAD
from statistics import harmonic_mean
from tools_oop import HamrobazarScraper, Hamrobazaar
=======
from tools_oop import HamrobazarScraper
>>>>>>> c57be8bc94be7c6d2a12b67d56d2690890a9cdb3
import pandas as pd
import winsound
import time

# main URL:
hamrobazar_url = "https://hamrobazaar.com/category/computers-peripherals/4cce4a7c-431b-474d-8b58-4fd2ddc191cf"

# Track the timer:
start_time = time.time()


# Time interval between each request made to the server. i"ve set the default value to 5 seconds:
# Decrease the time interval if you want a bit faster scraping, however I discourage you to do so as it may hurt the server or may throw an error:
time_interval = 5


category_name = HamrobazarScraper(hamrobazar_url).category_name()
print(f"Category | {category_name}\n--------------------------------")
hamrobazar = HamrobazarScraper(hamrobazar_url).hamrobazar_automation(time_interval)


# # Extracting to Json and Excel via Pandas dataframe:
# Index 0 extracts products' name, 1 extracts products' link and -1 (last index) extracts products' links:
d = {'Names': hamrobazar[0], "Prices": hamrobazar[1], "Links": hamrobazar[-1]}
df = pd.DataFrame(data=d)
df.to_json(f"Sample Hamrobazar {category_name} database.json", indent=4)
df.to_excel(f"Sample Hamrobazar {category_name} database.xlsx", index=False)



# Play the sound after the completion of Scraping process:
winsound.PlaySound('notification.mp3', winsound.SND_FILENAME)


# Calculating time of completion:
time_took = time.time() - start_time
time_in_seconds = round(time_took, 2)
time_in_minutes = round(time_in_seconds/60, 2)
print(f'Took {time_in_seconds} seconds.....')
print(f"Took {time_in_minutes} minutes.....")
