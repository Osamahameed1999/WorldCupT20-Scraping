
# Web Scraping World T20 2023 Summary Data from ESPNcricinfo

This project involves web scraping data from ESPNcricinfo website using Python and its 

libraries - pandas, requests, and Beautiful Soup. The goal of this project is to obtain 

the summary data for the World T20 2023 tournament. 





## Table of Contents

- Installation

- Usage

- Data

- License 

- Conlusion
## Installation

To use this program, you'll need to have Python 3 and the following libraries installed:

- requests
- beautifulsoup4
- pandas
        
        
You can install these libraries by running the following command in your terminal:

    pip install requests beautifulsoup4 pandas



## Usage

To run the program, simply execute the following command in your terminal:

    python web_scraping.py

The program will extract the results of the ICC World T20 2023 cricket tournament from the 

ESPNcricinfo website and save them to a CSV file called icc_world_cup_results.csv.
## Data

The program extracts the following data for each match:

- Team 1

- Team 2
- Winner
- Margin
- Ground
- Match Date

The data is saved to a CSV file in the following format:


| Team 1          | Team 2         | Winner       | Margin           | Ground             | Match Date    |
| ---------------| --------------| -------------|------------------|-------------------|--------------|
| India           | Pakistan       | India        | 10 runs          | Melbourne          | 20 October    |
| Australia       | South Africa   | Australia    | 6 wickets        | Sydney             | 21 October    |
| Sri Lanka       | West Indies    | West Indies | 8 wickets        | Adelaide           | 22 October    |
| England         | New Zealand   | England      | 4 runs           | Perth              | 23 October    |
| Pakistan        | South Africa  | South Africa | 5 wickets       | Sydney             | 24 October    |


## License

This project is licensed under the MIT License. Feel free to use and modify this code as   

per your requirement.
## Conclusion

In this project, we used Python and its libraries - pandas, requests, and Beautiful Soup - 

to scrape summary data for the upcoming World T20 2023 tournament from the ESPNcricinfo 

website. We retrieved the HTML content of the webpage, parsed it using Beautiful Soup, and 

converted the summary data into a pandas DataFrame. The resulting DataFrame can be used 

for further analysis or visualization, or saved to a CSV file for later use.
