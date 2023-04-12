{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "65283a58",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Importing Libararies\n",
    "\n",
    "from pip._vendor import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "86f68c11",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Setting URL as Variable\n",
    "\n",
    "URL =\"https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=14450;type=tournament\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "583a5d55",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Defining Header with your User Agent\n",
    "\n",
    "HEADER = ({'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36', 'Accept-Language' : 'en-US, en;q=0.5'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "505e5293",
   "metadata": {},
   "outputs": [],
   "source": [
    "#HTTP Request \n",
    "\n",
    "webpage = requests.get(URL, headers=HEADER)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "33e622d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Soup objectr containing all webpage data \n",
    "\n",
    "soup = BeautifulSoup(webpage.content, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ed8ab69c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Fetch the Data Table\n",
    "\n",
    "table = soup.find('table', class_='engineTable')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0e11bad5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Define the Data Dictionary containing table attributes \n",
    "\n",
    "data_dict = {'Team 1': [] , 'Team 2': [] , 'Winner': [] , 'Margin': [] , 'Ground': [] , 'Match Date': [] }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "81b7ca31",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Fecth rows and columns from the table \n",
    "\n",
    "for row in table.find_all(\"tr\")[1:]:\n",
    "    cells = row.find_all(\"td\")\n",
    "    if len(cells) == 0:\n",
    "        continue\n",
    "    team1 = cells[0].text.strip()\n",
    "    team2 = cells[1].text.strip()\n",
    "    winner = cells[2].text.strip()\n",
    "    margin = cells[3].text.strip()\n",
    "    ground = cells[4].text.strip()\n",
    "    match_date = cells[5].text.strip()\n",
    "    data_dict[\"Team 1\"].append(team1)\n",
    "    data_dict[\"Team 2\"].append(team2)\n",
    "    data_dict[\"Winner\"].append(winner)\n",
    "    data_dict[\"Margin\"].append(margin)\n",
    "    data_dict[\"Ground\"].append(ground)\n",
    "    data_dict[\"Match Date\"].append(match_date)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "60e2f680",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Team 1        Team 2        Winner      Margin     Ground  \\\n",
      "0        Namibia     Sri Lanka       Namibia     55 runs    Geelong   \n",
      "1    Netherlands        U.A.E.   Netherlands   3 wickets    Geelong   \n",
      "2       Scotland   West Indies      Scotland     42 runs     Hobart   \n",
      "3        Ireland      Zimbabwe      Zimbabwe     31 runs     Hobart   \n",
      "4        Namibia   Netherlands   Netherlands   5 wickets    Geelong   \n",
      "5      Sri Lanka        U.A.E.     Sri Lanka     79 runs    Geelong   \n",
      "6        Ireland      Scotland       Ireland   6 wickets     Hobart   \n",
      "7    West Indies      Zimbabwe   West Indies     31 runs     Hobart   \n",
      "8    Netherlands     Sri Lanka     Sri Lanka     16 runs    Geelong   \n",
      "9        Namibia        U.A.E.        U.A.E.      7 runs    Geelong   \n",
      "10       Ireland   West Indies       Ireland   9 wickets     Hobart   \n",
      "11      Scotland      Zimbabwe      Zimbabwe   5 wickets     Hobart   \n",
      "12     Australia   New Zealand   New Zealand     89 runs     Sydney   \n",
      "13   Afghanistan       England       England   5 wickets      Perth   \n",
      "14       Ireland     Sri Lanka     Sri Lanka   9 wickets     Hobart   \n",
      "15         India      Pakistan         India   4 wickets  Melbourne   \n",
      "16    Bangladesh   Netherlands    Bangladesh      9 runs     Hobart   \n",
      "17  South Africa      Zimbabwe     no result                 Hobart   \n",
      "18     Australia     Sri Lanka     Australia   7 wickets      Perth   \n",
      "19       England       Ireland       Ireland      5 runs  Melbourne   \n",
      "20   Afghanistan   New Zealand     abandoned              Melbourne   \n",
      "21    Bangladesh  South Africa  South Africa    104 runs     Sydney   \n",
      "22         India   Netherlands         India     56 runs     Sydney   \n",
      "23      Pakistan      Zimbabwe      Zimbabwe       1 run      Perth   \n",
      "24   Afghanistan       Ireland     abandoned              Melbourne   \n",
      "25     Australia       England     abandoned              Melbourne   \n",
      "26   New Zealand     Sri Lanka   New Zealand     65 runs     Sydney   \n",
      "27    Bangladesh      Zimbabwe    Bangladesh      3 runs   Brisbane   \n",
      "28   Netherlands      Pakistan      Pakistan   6 wickets      Perth   \n",
      "29         India  South Africa  South Africa   5 wickets      Perth   \n",
      "30     Australia       Ireland     Australia     42 runs   Brisbane   \n",
      "31   Afghanistan     Sri Lanka     Sri Lanka   6 wickets   Brisbane   \n",
      "32       England   New Zealand       England     20 runs   Brisbane   \n",
      "33   Netherlands      Zimbabwe   Netherlands   5 wickets   Adelaide   \n",
      "34    Bangladesh         India         India      5 runs   Adelaide   \n",
      "35      Pakistan  South Africa      Pakistan     33 runs     Sydney   \n",
      "36       Ireland   New Zealand   New Zealand     35 runs   Adelaide   \n",
      "37     Australia   Afghanistan     Australia      4 runs   Adelaide   \n",
      "38       England     Sri Lanka       England   4 wickets     Sydney   \n",
      "39   Netherlands  South Africa   Netherlands     13 runs   Adelaide   \n",
      "40    Bangladesh      Pakistan      Pakistan   5 wickets   Adelaide   \n",
      "41         India      Zimbabwe         India     71 runs  Melbourne   \n",
      "42   New Zealand      Pakistan      Pakistan   7 wickets     Sydney   \n",
      "43       England         India       England  10 wickets   Adelaide   \n",
      "44       England      Pakistan       England   5 wickets  Melbourne   \n",
      "\n",
      "      Match Date  \n",
      "0   Oct 16, 2022  \n",
      "1   Oct 16, 2022  \n",
      "2   Oct 17, 2022  \n",
      "3   Oct 17, 2022  \n",
      "4   Oct 18, 2022  \n",
      "5   Oct 18, 2022  \n",
      "6   Oct 19, 2022  \n",
      "7   Oct 19, 2022  \n",
      "8   Oct 20, 2022  \n",
      "9   Oct 20, 2022  \n",
      "10  Oct 21, 2022  \n",
      "11  Oct 21, 2022  \n",
      "12  Oct 22, 2022  \n",
      "13  Oct 22, 2022  \n",
      "14  Oct 23, 2022  \n",
      "15  Oct 23, 2022  \n",
      "16  Oct 24, 2022  \n",
      "17  Oct 24, 2022  \n",
      "18  Oct 25, 2022  \n",
      "19  Oct 26, 2022  \n",
      "20  Oct 26, 2022  \n",
      "21  Oct 27, 2022  \n",
      "22  Oct 27, 2022  \n",
      "23  Oct 27, 2022  \n",
      "24  Oct 28, 2022  \n",
      "25  Oct 28, 2022  \n",
      "26  Oct 29, 2022  \n",
      "27  Oct 30, 2022  \n",
      "28  Oct 30, 2022  \n",
      "29  Oct 30, 2022  \n",
      "30  Oct 31, 2022  \n",
      "31   Nov 1, 2022  \n",
      "32   Nov 1, 2022  \n",
      "33   Nov 2, 2022  \n",
      "34   Nov 2, 2022  \n",
      "35   Nov 3, 2022  \n",
      "36   Nov 4, 2022  \n",
      "37   Nov 4, 2022  \n",
      "38   Nov 5, 2022  \n",
      "39   Nov 6, 2022  \n",
      "40   Nov 6, 2022  \n",
      "41   Nov 6, 2022  \n",
      "42   Nov 9, 2022  \n",
      "43  Nov 10, 2022  \n",
      "44  Nov 13, 2022  \n"
     ]
    }
   ],
   "source": [
    "#Save the content into a CSV \n",
    "\n",
    "df = pd.DataFrame(data_dict)\n",
    "df.to_csv('icc_world_cup_results.csv', index=False)\n",
    "print(df)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
