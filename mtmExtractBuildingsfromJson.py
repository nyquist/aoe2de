import json, csv, argparse
from prettytable import PrettyTable, MARKDOWN, ORGMODE, DOUBLE_BORDER 
from mtmExtractPlayersFromJson import extractPlayers

class BuildingsAnalyzer:
    def __init__(self, inputFile):
        self.all_rows = []
        with open (inputFile) as p:
            inputData = json.load(p)
            playernames = extractPlayers(inputFile)
        
        buildings = [{},{},{},{},{},{},{},{}]
        # print (buildings)
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
    parser = argparse.ArgumentParser( 
        prog='extractPlayers',
        description='Extracts Players from JSON')
    parser.add_argument('filename')           # positional argument
    args = parser.parse_args()

    inputFile = args.filename    
    analyzer = BuildingsAnalyzer(inputFile)
    print (analyzer.getTable("eco"))
    print (analyzer.getTable("mil"))
