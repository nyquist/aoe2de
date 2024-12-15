import json, csv
from prettytable import PrettyTable, MARKDOWN, ORGMODE, DOUBLE_BORDER 


class BuildingsAnalyzer:
    def __init__(self, inputFile):
        self.all_rows = []
        with open (inputFile) as p:
            inputData = json.load(p)
            playernames =[1,1,1,1,1,1,1,1]
            for player in inputData["players"]:
                if isinstance(player,dict):
                    print (player["name"], player["number"])
                    playernames[player["number"]-1]=player["name"]
                    for pl in player["team"]:
                        if isinstance(pl,dict):
                            print (pl["name"], pl["number"])
                            playernames[pl["number"]-1]=pl["name"]
                            for pl3 in pl["team"]:
                                if isinstance(pl3,dict):
                                    print (pl3["name"], pl3["number"])
                                    playernames[pl3["number"]-1]=pl3["name"]
                                    for pl4 in pl3["team"]:
                                        if isinstance(pl4,dict):
                                            print (pl4["name"], pl4["number"])
                                            playernames[pl4["number"]-1]=pl4["name"]
        print (playernames)
        
        buildings = [{},{},{},{},{},{},{},{}]
        print (buildings)
        buildingtypes = []
        for action in inputData["actions"]:
            if "payload" in action.keys():
                if "building" in action["payload"].keys():
                    if action["payload"]["building"] not in buildingtypes:
                        buildingtypes.append(action["payload"]["building"])
                    if action["payload"]["building"] in buildings[action["player"]-1].keys():
                        buildings[action["player"]-1][action["payload"]["building"]]+=1
                    else:
                        buildings[action["player"]-1][action["payload"]["building"]]=1
        # for pp in range(8):
        #     print(f"\n{playernames[pp]} buildings:")
        #     for key, value in buildings[pp].items():
        #         print (key, value)
        # print (buildingtypes)
        #R = "\033[0;33;40m" #Y
        #G = "\033[0;32;40m" # GREEN
        self.all_rows.append(["Cladire"] + playernames )
        ecoTable = PrettyTable( ["Cladire"]+ playernames ) 
        milTable = PrettyTable( ["Cladire"]+ playernames ) 
        for btype in buildingtypes:
            row = []
            for pp in range(8):
                if btype in buildings[pp]:
                    row.append(buildings[pp][btype])
                else:
                    row.append(0)
            if btype in ['Barracks', 'Stable', 'Castle', 'Siege Workshop', 'Archery Range', 'University', 'Blacksmith', 'Monastery', 'Watch Tower']:
                ecoTable.add_row([btype] + row)
            else:
                milTable.add_row([btype] + row)
            self.all_rows.append([btype] + row)
        print(ecoTable)
        print(milTable)
        self.milTable = milTable
        self.ecoTable = ecoTable
        #print(self.all_rows)
        
    
    def getRows(self):
        return self.all_rows
    
    def getTable(self, table_type="mil"):
        if table_type == "mil":
            mtable = self.milTable
        else:
            mtable = self.ecoTable
        mtable.set_style(MARKDOWN)
        return mtable.get_string()
      

if __name__ == '__main__':
    print ("Need to fix passing file_name. Try using it as a module")
    analyzer = BuildingsAnalyzer("AgeIIDE_Replay_358345344.aoe2record.json")
    print (analyzer.getTable("eco"))
