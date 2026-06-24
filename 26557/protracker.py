


class Item:
    def __init__(self, name, description, image, craft, price, matches, pickrate, winrate):
        self.name = name
        self.description = description
        self.image = image
        self.craft = craft
        self.price = price
        self.matches = matches
        self.pickrate = pickrate
        self.winrate = winrate
    


class Hero:
    def __init__(self, name, image,
                 carry_matches, carry_winrate,
                 hard_support_matches, hard_support_winrate,
                 mid_matches, mid_winrate,
                 offlane_matches, offlane_winrate,
                 support_matches, support_winrate,
                 all_matches=None, winrate=None, pickrate=None):
        self.name = name
        self.image = image
        self.matches = all_matches
        self.pickrate = pickrate
        self.winrate = winrate
        self.carry_matches = carry_matches
        self.carry_winrate = carry_winrate
        self.hard_support_matches = hard_support_matches
        self.hard_support_winrate = hard_support_winrate
        self.mid_matches = mid_matches
        self.mid_winrate = mid_winrate
        self.offlane_matches = offlane_matches
        self.offlane_winrate = offlane_winrate
        self.support_matches = support_matches
        self.support_winrate = support_winrate
        
        
class Parser():
    def __init__(self):
        pass
    
    
    def parse_heroes(self) -> list[Hero]:
        '''
        Parse heroes from protracker.gg
        '''
        pass
    
    
    def parse_items(self) -> list[Item]:
        '''
        Parse items from protracker.gg
        '''
        pass
    
    
    def run(self):
        items = self.parse_items()
        heroes = self.parse_heroes()
    
    
if __name__ == "__main__":
    parser = Parser()
    parser.run()
        