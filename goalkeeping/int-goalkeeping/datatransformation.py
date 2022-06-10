# ANALYZE GOALKEEPER DATA

# Author : M1H
# Last Edited : 2022-06-10

# Source Data coming from : Statsbomb

# Specifically developed to get and transform soccer data on Goalkeeper actions to analyze GK performance and build models.

# ------------------------------

import pandas as pd
import glob

class GetStatsbombData:
    def __init__(self):
        self.competition_file = '/Users/matthiashugli/Virtualenvs/youth-base/youth-base/goalkeeping/open-data/data/competitions.json'

    def get_competition(self, league_name):
        # AVAILABLE LEAGUES
        # league_name = input("Choose League: Champions League, \
        #                         FA Women's Super League, FIFA World Cup, \
        #                             La Liga, NWSL, Premier League, UEFA Euro, Women's World Cup")
        comp_file = pd.read_json(self.competition_file)
        competitions = pd.DataFrame(comp_file)
        self.competition_ids = str(competitions[competitions['competition_name'] == (league_name)]['competition_id'].unique()[0])
        
    def get_match_id(self):
        match_files = '/Users/matthiashugli/Virtualenvs/youth-base/youth-base/goalkeeping/open-data/data/matches/' \
            + self.competition_ids + '/*.json'
        matches = pd.DataFrame()
        for filename in glob.glob(match_files):
            file = pd.read_json(filename)
            df = pd.DataFrame(file)
            matches = pd.concat([matches, df])
            self.match_ids = pd.Series(matches['match_id']).tolist()    

    def get_event_files(self, league_name):
        self.get_competition(league_name=league_name)
        self.get_match_id()
        event_path = '/Users/matthiashugli/Virtualenvs/youth-base/youth-base/goalkeeping/open-data/data/events/'
        events = pd.DataFrame()
        for i in self.match_ids:
            filename = event_path + str([i][0]) + '.json'
            file = pd.read_json(str(filename))
            df = pd.DataFrame(file)
            df['event_name'] = [v['name'] for k, v in df['type'].items()]
            df['event_detail'] = [v['name'] for k, v in df['play_pattern'].items()]
            df.drop(['type', 'play_pattern'], axis=1, inplace=True)
            events = pd.concat([events, df])
        
        return events