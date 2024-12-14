import json, csv
from prettytable import PrettyTable 

inputFile = r"C:\CodesPlace\AgeGameAnalize\24Dec13.json"
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
    myTable = PrettyTable(["Cladire"]+ playernames) 
    for btype in buildingtypes:
        row = []
        for pp in range(8):
            if btype in buildings[pp]:
                # print (buildings[pp][btype])
                row.append(buildings[pp][btype])
            else:
                # print (0)
                row.append(0)
        myTable.add_row([btype] + row)   
    print(myTable)  

