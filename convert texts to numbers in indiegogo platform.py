for index, row in df.iterrows():
    if row['R_RANGE'] == 'Ships worldwide.':
        df.loc[index, 'R_RANGE_SCORE'] = 1
    elif row['R_RANGE'] == 'Ships to United States of America':
        df.loc[index, 'R_RANGE_SCORE'] = 2
    elif row['R_RANGE'] == 'Ships to European Union, United States of America, United Kingdom':
        df.loc[index, 'R_RANGE_SCORE'] = 3
    elif row['R_RANGE'] == 'Ships to many locations.':
        df.loc[index, 'R_RANGE_SCORE'] = 4
    elif row['R_RANGE'] == 'Ships to Italy':
        df.loc[index, 'R_RANGE_SCORE'] = 5
    elif row['R_RANGE'] == 'Ships to France':
        df.loc[index, 'R_RANGE_SCORE'] = 6
    elif row['R_RANGE'] == 'Ships to United States of America, Canada':
        df.loc[index, 'R_RANGE_SCORE'] = 7
    elif row['R_RANGE'] == 'Ships to United Kingdom, Germany':
        df.loc[index, 'R_RANGE_SCORE'] = 8
    elif row['R_RANGE'] == 'Ships to European Union, Canada, United States of America':
        df.loc[index, 'R_RANGE_SCORE'] = 9
    elif row['R_RANGE'] == 'Ships to European Union, United States of America':
        df.loc[index, 'R_RANGE_SCORE'] = 10
    elif row['R_RANGE'] == 'Ships to European Union, Italy':
        df.loc[index, 'R_RANGE_SCORE'] = 11
    elif row['R_RANGE'] == 'Ships to United States of America, Antarctica':
        df.loc[index, 'R_RANGE_SCORE'] = 12
    elif row['R_RANGE'] == 'Ships to United States of America, Hong Kong':
        df.loc[index, 'R_RANGE_SCORE'] = 13
    elif row['R_RANGE'] == 'Ships to Canada':
        df.loc[index, 'R_RANGE_SCORE'] = 14
    elif row['R_RANGE'] == 'Ships to European Union, United States of America, Canada, Australia':
        df.loc[index, 'R_RANGE_SCORE'] = 15
    elif row['R_RANGE'] == "Ships to United States of America, Hong Kong":
        df.loc[index, 'R_RANGE_SCORE'] = 16
    elif row['R_RANGE'] == "Ships to Australia, Canada, Denmark, United Kingdom":
        df.loc[index, 'R_RANGE_SCORE'] = 17
    elif row['R_RANGE'] == "Ships to European Union, Japan, Malaysia, Vietnam":
        df.loc[index, 'R_RANGE_SCORE'] = 18
    elif row['R_RANGE'] == "Ships to European Union, Italy, United States of America, Canada":
        df.loc[index, 'R_RANGE_SCORE'] = 19
    elif row['R_RANGE'] == "Ships to European Union, United States of America, Australia, Canada, United Kingdom":
        df.loc[index, 'R_RANGE_SCORE'] = 20
    elif row['R_RANGE'] == "Ships to United States of America, Canada, Hong Kong, Malaysia, Singapore":
        df.loc[index, 'R_RANGE_SCORE'] = 21
    elif row['R_RANGE'] == "Ships to United States of America, Australia, Canada, Germany, United Kingdom":
        df.loc[index, 'R_RANGE_SCORE'] = 22
    elif row['R_RANGE'] == "Ships to European Union, United States of America, People's Republic of China, Canada, Mexico":
        df.loc[index, 'R_RANGE_SCORE'] = 23
    elif row['R_RANGE'] == "24":
        df.loc[index, 'R_RANGE_SCORE'] = 24