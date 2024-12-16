import json, csv, argparse

def extractPlayers(inputFile):
    with open (inputFile) as p:
        inputData = json.load(p)
        playernames =[1,1,1,1,1,1,1,1]
        for player in inputData["players"]:
            if isinstance(player,dict):
                playernames[player["number"]-1]=player["name"]
                for pl in player["team"]:
                    if isinstance(pl,dict):
                        playernames[pl["number"]-1]=pl["name"]
                        for pl3 in pl["team"]:
                            if isinstance(pl3,dict):
                                playernames[pl3["number"]-1]=pl3["name"]
                                for pl4 in pl3["team"]:
                                    if isinstance(pl4,dict):
                                        playernames[pl4["number"]-1]=pl4["name"]
    return playernames

if __name__=="__main__":
    parser = argparse.ArgumentParser( 
        prog='extractPlayers',
        description='Extracts Players from JSON')
    parser.add_argument('filename')           # positional argument
    args = parser.parse_args()

    inputFile = args.filename
    print(extractPlayers(inputFile))
