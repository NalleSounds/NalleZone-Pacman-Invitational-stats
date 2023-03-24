import challonge
import json

challonge.set_credentials("nallesounds", "JdWTWzBEcfnXA22dCC3KMZuq0nsaEemnwy2Nujxa")


class Tournament:
    def __init__(self, tid, name, url, tformat, start_at,
                 completed_at, participant_count, participants):
        self.tid = tid
        self.name = name
        self.url = url
        self.tformat = tformat
        self.start_at = start_at.strftime("%Y/%m/%d, %H:%M:%S")
        self.completed_at = completed_at.strftime("%Y/%m/%d, %H:%M:%S")
        self.duration = (completed_at - start_at).total_seconds() / 60
        self.participant_count = participant_count
        self.participants = participants


class Participant:
    def __init__(self, pid, trainer):
        self.pid = pid
        self.trainer = trainer


def clean(s):
    clean_s = ""
    for ch in s:
        if ch.isalpha():
            clean_s += ch
    return str.lower(clean_s)


tournaments = challonge.tournaments.index()

pacmans = []

pacmanJson = ""

for tournament in tournaments:
    if tournament["game_name"] == "Pokémon Showdown" or tournament["game_name"] == "Pokémon":

        participants = challonge.participants.index(tournament["id"])
        partice = []
        particeJson = ""

        for p in participants:
            partice.append(Participant(p['id'], clean(p['display_name'])).__dict__)

        # matches = challonge.matches.index(tournament["id"])
        # print(matches)

        pacman = Tournament(tournament['id'], tournament['name'],
                            tournament['url'], tournament['tournament_type'],
                            tournament['started_at'], tournament['completed_at'],
                            tournament['participants_count'], partice)
        # print(pacman.name)
        pacmans.append(pacman)

        pacmanJson += ",\n" + json.dumps(pacman.__dict__)

with open("matches.json", 'w') as f:
    f.write(pacmanJson[2:])

print("hello cummers")
