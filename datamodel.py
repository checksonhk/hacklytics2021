import pandas as pd

url = "./data/states_covid_history.csv"
df = pd.read_csv(url)

df['date'] = df['date'].astype('datetime64')
cases = df[['date', 'totalTestResultsIncrease', 'negativeIncrease',
            'positiveIncrease', 'deathIncrease', 'hospitalizedIncrease']]
# cases.head(20).style.background_gradient(cmap='Pastel1')

# create percent columns
cases['percent_positive'] = cases['positiveIncrease'] / \
    cases['totalTestResultsIncrease']
cases['percent_negative'] = cases['negativeIncrease'] / \
    cases['totalTestResultsIncrease']
cases['percent_death'] = cases['deathIncrease'] / \
    cases['totalTestResultsIncrease']
cases['percent_hospitalized'] = cases['hospitalizedIncrease'] / \
    cases['totalTestResultsIncrease']
# cases.head(20)

# create percent change columns
cases['positive_pct_change'] = cases['percent_positive'].pct_change()
cases['negative_pct_change'] = cases['percent_negative'].pct_change()
cases['total_cases_pct_change'] = cases['totalTestResultsIncrease'].pct_change()
cases['death_pct_change'] = cases['percent_death'].pct_change()
cases['hospitalized_pct_change'] = cases['percent_hospitalized'].pct_change()
# cases

# filter out old dates
cases = cases[cases['date'] > '2020-03-20']
# cases.head(20).style.background_gradient(cmap="Blues")


# melt daily percent change columns into one dataframe
positive_pct_melt = pd.melt(cases, id_vars=['date'], value_vars=[
                            'positive_pct_change'])
negative_pct_melt = pd.melt(cases, id_vars=['date'], value_vars=[
                            'negative_pct_change'])
death_pct_melt = pd.melt(
    cases, id_vars=['date'], value_vars=['death_pct_change'])
hospitalized_pct_melt = pd.melt(cases, id_vars=['date'], value_vars=[
                                'hospitalized_pct_change'])
total_cases_pct_melt = pd.melt(cases, id_vars=['date'], value_vars=[
                               'total_cases_pct_change'])


cases_melted1 = positive_pct_melt.append(negative_pct_melt, ignore_index=True)
cases_melted2 = cases_melted1.append(death_pct_melt, ignore_index=True)
cases_melted3 = cases_melted2.append(hospitalized_pct_melt, ignore_index=True)
cases_melted = cases_melted3.append(total_cases_pct_melt, ignore_index=True)

print("data processed......")
