import json, csv, argparse, pprint


class Players:
    def __init__(self, inputFile):
        self.teams = []
        self.players = []
        with open(inputFile) as p:
            inputData = json.load(p)
            players = [1, 1, 1, 1, 1, 1, 1, 1]
            for pl1 in inputData["players"]:
                if isinstance(pl1, dict):
                    if pl1["team_id"] not in self.teams:
                        self.teams.append(pl1["team_id"])
                    players[pl1["number"] - 1] = {
                        "name": pl1["name"],
                        "color": pl1["color"],
                        "civ": pl1["civilization"],
                        "number": pl1["number"],
                        "team": self.teams.index(pl1["team_id"]) + 1,
                    }
                    # print(player["team"])
                    for pl2 in pl1["team"]:
                        if isinstance(pl2, dict):
                            if pl1["team_id"] not in self.teams:
                                self.teams.append(pl1["team_id"])
                            players[pl2["number"] - 1] = {
                                "name": pl2["name"],
                                "color": pl2["color"],
                                "civ": pl2["civilization"],
                                "number": pl2["number"],
                                "team": self.teams.index(pl2["team_id"]) + 1,
                            }
                            for pl3 in pl2["team"]:
                                if isinstance(pl3, dict):
                                    if pl1["team_id"] not in self.teams:
                                        self.teams.append(pl1["team_id"])
                                    players[pl3["number"] - 1] = {
                                        "name": pl3["name"],
                                        "color": pl3["color"],
                                        "civ": pl3["civilization"],
                                        "number": pl3["number"],
                                        "team": self.teams.index(pl3["team_id"]) + 1,
                                    }
                                    for pl4 in pl3["team"]:
                                        if isinstance(pl4, dict):
                                            if pl1["team_id"] not in self.teams:
                                                self.teams.append(pl1["team_id"])
                                            players[pl4["number"] - 1] = {
                                                "name": pl4["name"],
                                                "color": pl4["color"],
                                                "civ": pl4["civilization"],
                                                "number": pl4["number"],
                                                "team": self.teams.index(pl4["team_id"])
                                                + 1,
                                            }
        
        for p in players:
            if p != 1:
                self.players.append(p)
        

    def getPlayerNames(self):
        return [x["name"] for x in self.players]

    def getPlayerInfo(self, player_number):
        for x in self.players:
            if x["number"] == player_number:
                return x


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="extractPlayers", description="Extracts Players from JSON"
    )
    parser.add_argument("filename")  # positional argument
    args = parser.parse_args()

    inputFile = args.filename
    players = Players(inputFile)
    print(players.getPlayerNames())
    print(players.getPlayerInfo(1))
