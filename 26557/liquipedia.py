import requests 
from bs4 import BeautifulSoup as bs


class Liquipedia:
    def __init__(self, url):
        self.url = url
        self.teams = []
        self.headers = {
            'Host': 'liquipedia.net',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:155.0) Gecko/20100101 Firefox/155.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Referer': 'https://liquipedia.net/dota2/Main_Page',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Priority': 'u=0, i'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def parse_teams(self):
        response = self.session.get(self.url)
        data = bs(response.content, 'lxml')
        teams_block = data.find(class_="lp-container-fluid")
        teams = teams_block.find_all(class_="team-template-text")
        teams_urls = [team.find('a')['href'] for team in teams]
        for team_url in teams_urls[:1]:
            roster = []
            team_name = team_url.split('/')[-1]
            json_data = self.session.get(f"https://liquipedia.net/dota2/api.php?action=parse&page={team_name}&format=json").json()['parse']['text']['*']
            soup = bs(json_data, 'lxml')
            for t in soup.find_all("table"):
                rows = t.select("tr")
                if not rows:
                    continue
                head = [c.get_text(" ", strip=True) for c in rows[0].find_all(["td", "th"])]
                if "ID" in head and "Position" in head:
                    for row in rows[1:]:
                        cells = [c.get_text(" ", strip=True) for c in row.find_all(["td", "th"])]
                        if len(cells) >= 3 and cells[0] and cells[0] != "ID":
                            roster.append((cells[0], cells[2]))  # (id, position)
                    break

            print(roster, team_name)

    def get_players(self):
        pass


class Player:
    def __init__(self, name, nickname, team, roster=False):
        self.name = name
        self.nickname = nickname
        self.team = team
        self.roster = roster

    def update_name(self):
        pass

    def update_nickname(self):
        pass

    def update_team(self):
        pass

    def update_roster(self):
        pass



class Update:
    pass


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.roster = None
        self.tournaments = []

    def update_roster(self):
        pass

    def update_players(self):
        pass

    def update_tournaments(self):
        pass
        

parser = Liquipedia('https://liquipedia.net/dota2/Portal:Teams')
teams = parser.parse_teams()