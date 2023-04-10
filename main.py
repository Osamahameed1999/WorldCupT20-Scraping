

from pip._vendor import requests
from bs4 import BeautifulSoup
import pandas as pd

URL ="https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=14450;type=tournament"

HEADER = ({'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36', 'Accept-Language' : 'en-US, en;q=0.5'})

webpage = requests.get(URL, headers=HEADER)

print(webpage)

soup = BeautifulSoup(webpage.content, "html.parser")

print(soup)



all_data = soup.find('table', class_='engineTable')


print(all_data)

rows = all_data.find_all('tr')

data_dict = {'Team 1': [] , 'Team 2': [] , 'Winner': [] , 'Margin': [] , 'Ground': [] , 'Match Date': [] }

print(rows)


for row in rows:
    cells = row.find_all('td')

    for cell in cells: 
            teamA = cell.text.strip()
            teamB = cell.text.strip()
            winner = cell.text.strip()
            margin = cell.text.strip()
            ground = cell.text.strip()
            match_date= cell.text.strip()

            data_dict['Team 1'].append(teamA)
            data_dict['Team 2'].append(teamB)
            data_dict['Winner'].append(winner)
            data_dict['Margin'].append(margin)
            data_dict['Ground'].append(ground)
            data_dict['Match Date'].append(match_date)



print(data_dict)





