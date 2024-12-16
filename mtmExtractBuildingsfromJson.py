import json, csv, argparse, pprint
from prettytable import PrettyTable
try:
    #TODO
    from aoe2de.mtmExtractPlayersFromJson import Players
except:
    pass

class BuildingsAnalyzer:
    def __init__(self, inputFile):        
        self.buildings = [{},{},{},{},{},{},{},{}]
        self.buildingtypes = []
        self.players = Players(inputFile)
        self.playernames = self.players.getPlayerNames()
        
        with open (inputFile) as p:
            inputData = json.load(p)
        for action in inputData["actions"]:
            if "payload" in action.keys():
                if "building" in action["payload"].keys():
                    if action["payload"]["building"] not in self.buildingtypes:
                        self.buildingtypes.append(action["payload"]["building"])
                    if action["payload"]["building"] in self.buildings[action["player"]-1].keys():
                        self.buildings[action["player"]-1][action["payload"]["building"]]+=1
                    else:
                        self.buildings[action["player"]-1][action["payload"]["building"]]=1
    



    def getListInNewOrder(self, intial_list, byTeam = False):
        if byTeam:
            #print(self.players.teams)
            new_list = []
            for t in self.players.teams:
                for p in t:
                    new_list.append(intial_list[p-1])
            return new_list
        return intial_list

    def getTables(self, byTeam = False, rows=0):
        player_count = len(self.playernames)
        ordered_buildings = self.getListInNewOrder(self.buildings, byTeam)
        ordered_players = self.getListInNewOrder(self.playernames, byTeam)
        the_table = PrettyTable( ["Cladire [AVG]"]+ ordered_players ) 
        
        for btype in self.buildingtypes:
            row = []
            btotal = 0
            for pp in range(player_count):
                if btype in ordered_buildings[pp]:
                    btotal = btotal + ordered_buildings[pp][btype]
            baverage = btotal/len(self.playernames)
            for pp in range(player_count):
                if btype in ordered_buildings[pp]:
                    percent = ordered_buildings[pp][btype] - baverage
                    row.append(f"{ordered_buildings[pp][btype]} [{percent:+.2f}]")
                    btotal = btotal + ordered_buildings[pp][btype]
                else:
                    percent = 0 - baverage
                    row.append(f"0 [{percent:+.2f}]")
            the_table.add_row([f"{btype} [{baverage:.2f}]"] + row)
            
        #print(len(the_table.get_string()))
        tables = []
        current_row = 0
        if rows == 0:
            return [the_table.get_string()]
        else:
            while current_row < len(self.buildingtypes):
                tables.append(the_table.get_string(start=current_row, end = current_row+rows))
                current_row = current_row+rows
            return tables

        

      

if __name__ == '__main__':
    from mtmExtractPlayersFromJson import Players
    parser = argparse.ArgumentParser( 
        prog='extractPlayers',
        description='Extracts Players from JSON')
    parser.add_argument('filename')           # positional argument
    args = parser.parse_args()

    inputFile = args.filename    
    analyzer = BuildingsAnalyzer(inputFile)
    for t in analyzer.getTables(byTeam = True, rows = 3):
        print (len(t))
        print (t)
