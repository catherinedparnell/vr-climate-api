import pandas as pd
import constants as CONSTANTS

def make_dfs():
    precip_df = pd.read_csv(CONSTANTS.PRECIP_PROJECTION)
    temp_df = pd.read_csv(CONSTANTS.TEMP_PROJECTION)
    sea_level_df = pd.read_csv(CONSTANTS.SEA_LEV_PROJECTION)

    precip_df.index = precip_df[CONSTANTS.YEAR]
    temp_df.index = temp_df[CONSTANTS.YEAR]
    sea_level_df.index = sea_level_df[CONSTANTS.YEAR]

    return [precip_df, temp_df, sea_level_df]

def get_attribute(df, year, scenario):
    return df.loc[[year], [scenario]].iloc[0][scenario]

def get_precip(dfs, year, scenario):
    return get_attribute(dfs[0], year, scenario[0])

def get_temp(dfs, year, scenario):
    return get_attribute(dfs[1], year, scenario[0])

def get_sea_level(dfs, year, scenario):
    return get_attribute(dfs[2], year, scenario[1])

def accumulate_decade(dfs, year, scenario, function):
    total = 0
    for i in range(10):
        total += function(dfs, year + i, scenario)
    return total / 10
