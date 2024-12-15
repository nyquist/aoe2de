import json, csv

def extractPlayers(inputFile):
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
        # print (playernames)
    return playernames

if __name__=="__main__":
    inputFile = r"C:\CodesPlace\AgeGameAnalize\doi.json"
    print(extractPlayers(inputFile))