# CPSBC

1. Navigate to the Project Directory:

cd <CPSBC>

2. Install Dependencies:

pip install beautifulsoup
pip install requests
pip install selenium
pip install undetected_chromedriver
pip install psutil
pip install mysql.connect


3. To scrape the site:

    steps:
    1.  get the listing of websie =>
            python Create_links.py
        output file: Output/listings_{filename}.json


    2. get all listings =>
            python get_all_listing.py   
        output file: All_listing.json

    3. Get the data of listing =>
            python main.py
        output file: data.json

    4. create a json data to csv file =>
            python json_helper.py
        output file: Final_Output.csv