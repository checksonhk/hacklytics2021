import numpy as np
import pandas as pd
import time
from datetime import datetime, timedelta

def reindex(df, var, index_ = 10):
    ''' creates a data series which shifts data so that the day
    where the criteria index_ is reached is at index 0
    Note cases are indexed to weekly total, while deaths to cumulative total'''
    dta = df.copy()

    # First we need to identify the day at which the minimum number of cases/deaths is reached
    # some countries have no data so the try/except allows the function to
    # ignore them
    try:
        first_day = dta[dta[var] > index_].index[0]

    # The cumulative cases/deaths data are then shifted back so that the first
    # day index_ is exceeded becomes index 0
        dta[var] = dta[var].shift(-first_day)
    except BaseException:
        dta[var] = np.nan
    return dta