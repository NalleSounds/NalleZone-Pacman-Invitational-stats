# Dumps Challonge tourney data into a JSON file for less API load
import challonge
import json


def clean(s):
    clean_s = ""
    for ch in s:
        if ch.isalpha():
            clean_s += ch
    return str.lower(clean_s)


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


class Pacmans:
    def __init__(self, username, api_key):
        challonge.set_credentials(username, api_key)
        self.pacmans = None

    def get_tournaments(self):
        tournaments = challonge.tournaments.index()
        self.pacmans = []

        for tournament in tournaments:
            if tournament["game_name"] == "Pokémon Showdown" or tournament["game_name"] == "Pokémon":
                participants = []

                for p in challonge.participants.index(tournament["id"]):
                    participants.append(Participant(p['id'], clean(p['display_name'])))

                # matches = challonge.matches.index(tournament["id"])
                # print(matches)

                pacman = Tournament(tournament['id'], tournament['name'],
                                    tournament['url'], tournament['tournament_type'],
                                    tournament['started_at'], tournament['completed_at'],
                                    tournament['participants_count'], participants)

                # print(pacman.name)
                self.pacmans.append(pacman)

    def get_json(self):
        # If specified, default should be a function that gets called for objects
        # that can’t otherwise be serialized. It should return a JSON encodable
        # version of the object or raise a TypeError. If not specified, TypeError is raised.
        # -- https://docs.python.org/3/library/json.html#json.dump
        return json.dumps(self, indent=2, default=lambda o: getattr(o, '__dict__', str(o)))

    def get_dict(self):
        return json.loads(self.get_json())


pacmans = Pacmans("nallesounds", "u7516BnKalWyIukGmOcYLDZjzRZ0KIEBhOHfztHl")
pacmans.get_tournaments()

print(pacmans.get_dict())

with open("matches.json", 'w') as f:
    f.write(pacmans.get_json())
