# ANALYZE GOALKEEPER DATA

# Author : M1H
# Last Edited : 2022-06-10

# Source Data coming from : Statsbomb

# Specifically developed to get and transform soccer data on Goalkeeper actions to analyze GK performance and build models.

# ------------------------------

import pandas as pd
import numpy as np
import glob

class GetStatsbombData:
    def __init__(self):
        self.competition_file = '/Users/matthiashugli/Virtualenvs/youth-base/youth-base/goalkeeping/open-data/data/competitions.json'
        self.event_path = '/Users/matthiashugli/Virtualenvs/youth-base/youth-base/goalkeeping/open-data/data/events/'
        self.match_path = '/Users/matthiashugli/Virtualenvs/youth-base/youth-base/goalkeeping/open-data/data/matches/'

    def get_competition(self, league_name):
        # AVAILABLE LEAGUES
        # league_name = input("Choose League: Champions League, \
        #                         FA Women's Super League, FIFA World Cup, \
        #                             La Liga, NWSL, Premier League, UEFA Euro, Women's World Cup")
        comp_file = pd.read_json(self.competition_file)
        competitions = pd.DataFrame(comp_file)
        self.competition_ids = str(competitions[competitions['competition_name'] == (league_name)]['competition_id'].unique()[0])
        
    def get_match_id(self):
        match_files = self.match_path + self.competition_ids + '/*.json'    
        matches = pd.DataFrame()
        for filename in glob.glob(match_files):
            file = pd.read_json(filename)
            df = pd.DataFrame(file)
            matches = pd.concat([matches, df])
            self.match_ids = pd.Series(matches['match_id']).tolist()    

    def get_event_files(self, league_name):
        self.get_competition(league_name=league_name)
        self.get_match_id()
        events = pd.DataFrame()
        for i in self.match_ids:
            filename = self.event_path + str([i][0]) + '.json'
            file = pd.read_json(str(filename))
            df = pd.DataFrame(file)
            df['event_name'] = [v['name'] for k, v in df['type'].items()]
            df['event_detail'] = [v['name'] for k, v in df['play_pattern'].items()]
            df.drop(['type', 'play_pattern'], axis=1, inplace=True)
            events = pd.concat([events, df])
        
        return events


class ShotDistance:
    def create_gk_shot_dataframe(self, df):
        gk_df = df[df['event_name'] == 'Goal Keeper']
        shot_df = df[df['event_name'] == 'Shot']
        shot_id = shot_df[['id', 'related_events']].explode('related_events').dropna(subset=['related_events'])

        merge_gk = shot_id.merge(gk_df[['id', 'event_name', 'goalkeeper', 'location']], how='left', left_on='related_events', right_on='id') \
                    .dropna() \
                        .drop(columns=['id_y']) \
                            .merge(shot_df[['id', 'minute', 'second', 'event_name', 'shot', 'location']], how='left', left_on='id_x', right_on='id')

        gk_exp = merge_gk['goalkeeper'].apply(pd.Series)[['outcome', 'type', 'position', 'technique', 'body_part']]
        shot_exp = merge_gk['shot'].apply(pd.Series)[['outcome', 'type', 'technique', 'body_part']]

        merge_df = pd.DataFrame()
        for column in gk_exp:
            exp_col = pd.concat([gk_exp.drop([column], axis=1), gk_exp[column].apply(pd.Series)], axis=1).rename(columns={'name': 'gk_' + column}).drop(['id'], axis=1)
            merge_df = pd.concat([merge_df, exp_col['gk_' + column]], axis=1)


        for column in shot_exp:
            exp_col = pd.concat([shot_exp.drop([column], axis=1), shot_exp[column].apply(pd.Series)], axis=1).rename(columns={'name': 'shot_' + column}).drop(['id'], axis=1)
            merge_df = pd.concat([merge_df, exp_col['shot_' + column]], axis=1)

        self.gk_shots = pd.concat([merge_gk.drop(['goalkeeper', 'shot'], axis=1), merge_df, merge_gk['shot'].apply(pd.Series)[['statsbomb_xg', 'one_on_one']]], axis=1)

        return self.gk_shots

    def create_shot_model(self, df):
        df = self.create_gk_shot_dataframe(df=df)
        shot_model = df.loc[(df['gk_type'].isin(['Goal Conceded', 'Shot Saved'])) \
                & (df['shot_type'] == 'Open Play') \
                    & (df['gk_position'] != 'Prone')] \
                        [['id', 'location_x', 'location_y', 'gk_type', 'gk_technique', 'shot_outcome', 'shot_technique', 'shot_body_part', 'statsbomb_xg']]\
                            .reset_index()
        shot_model['gk_pos_x'] = [i[1] for i in shot_model['location_x']]
        shot_model['gk_pos_x'] = 80 - shot_model['gk_pos_x']
        shot_model['gk_pos_y'] = [i[0] for i in shot_model['location_x']]
        shot_model['gk_pos_y'] = 120 - shot_model['gk_pos_y']
        shot_model['shot_pos_x'] = [i[1] for i in shot_model['location_y']] # Pitch Rotation transforms y to x value
        shot_model['shot_pos_y'] = [i[0] for i in shot_model['location_y']] # Pitch Rotation transforms x to y value

        temp_df = pd.DataFrame()
        for i in range(len(shot_model)):
            # GK Distance to Shot
            gk_dis = pd.Series(np.hypot([int(shot_model['gk_pos_x'][i]) - int(shot_model['shot_pos_x'][i])], \
                                        [int(shot_model['gk_pos_y'][i]) - int(shot_model['shot_pos_y'][i])])[0], name='gk_dis').astype(int)
            # # Shot Distance to Goal Line
            shot_dis_gl = pd.Series(np.hypot([40 - int(shot_model['shot_pos_x'][i])], \
                                            [120 - int(shot_model['shot_pos_y'][i])])[0], name='shot_dis_gl').astype(int)
            # # Angle of the Shot from the Goal Line
            shot_angle = np.rad2deg(np.arccos([40 - int(shot_model['shot_pos_x'][i])] / shot_dis_gl)).astype(int)
            shot_angle = [x - 90 if x > 90 else x for x in shot_angle][0]
            shot_angle = pd.Series(shot_angle, name='shot_angle')

            temp_df = pd.concat([temp_df, pd.concat([gk_dis*0.9, shot_dis_gl*0.9, shot_angle], axis=1)])


        shot_model = pd.concat([shot_model, temp_df.reset_index()], axis=1)                        
        
        return shot_model[['gk_type', 'gk_technique', 'shot_body_part', 'statsbomb_xg', 'gk_dis', 'shot_dis_gl', 'shot_angle']]