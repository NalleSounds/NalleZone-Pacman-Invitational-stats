import challonge

challonge.set_credentials("nallesounds", "JdWTWzBEcfnXA22dCC3KMZuq0nsaEemnwy2Nujxa")

class Tournament:

    def __init__(self, tid, name, url, tformat, start_at,
     completed_at, participant_count):
        self.tid = tid
        self.name = name
        self.url = url
        self.tformat = tformat
        self.start_at = start_at
        self.completed_at = completed_at
        self.participant_count = participant_count

tournaments = challonge.tournaments.index()
pacmans = []

for tournament in tournaments:
    if tournament["game_name"] == "Pokémon Showdown" or tournament["game_name"] == "Pokémon":
        print(tournament)

