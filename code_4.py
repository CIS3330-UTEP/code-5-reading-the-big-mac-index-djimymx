import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)
#print(type(df['iso_a3'][0]))

def get_big_mac_price_by_year(year,country_code):
    
    #Changes the date format to year and converts the country code to lowercase vectorized
    df['date'] = df['date'].str[:4] # Extract year from date
    df['iso_a3'] = df['iso_a3'].str.lower() # Convert country code to lowercase

    ### changes the date format to year and converts the country code to lowercase using a loop ###
    # # Extract year from date
    # dates = []
    # for date in df['date']:
    #     dates.append(date[:4])
    # df['date'] = dates
    
    # # Convert country code to lowercase
    # isos = []
    # for iso in df['iso_a3']:
    #     isos.append(iso.lower())
    # df['iso_a3'] = isos

    query = f"date == '{year}' and iso_a3 == '{country_code}'"
    price_by_year = df.query(query)
    mean_price = round(price_by_year['dollar_price'].mean(),2)
    return mean_price

def get_big_mac_price_by_country(country_code):

    df['iso_a3'] = df['iso_a3'].str.lower() # Convert country code to lowercase

    query = f"iso_a3 == '{country_code}'"
    price_by_country = df.query(query)
    mean_price = round(price_by_country['dollar_price'].mean(),2)
    return mean_price

def get_the_cheapest_big_mac_price_by_year(year):

    df['date'] = df['date'].str[:4] # Extract year from date
    df['iso_a3'] = df['iso_a3'].str.upper() # Convert country code to uppercase

    query = f"date == '{year}'"
    min_price_by_year = df.query(query)
    min_idx = min_price_by_year['dollar_price'].idxmin()
    min_price = round(min_price_by_year['dollar_price'].min(),2)
    return f"{df['name'][min_idx]}({df['iso_a3'][min_idx]}): ${min_price}"

def get_the_most_expensive_big_mac_price_by_year(year):
    df['date'] = df['date'].str[:4] # Extract year from date
    df['iso_a3'] = df['iso_a3'].str.upper() # Convert country code to uppercase

    query = f"date == '{year}'"
    max_price_by_year = df.query(query)
    max_idx = max_price_by_year['dollar_price'].idxmax()
    max_price = round(max_price_by_year['dollar_price'].max(),2)
    return f"{df['name'][max_idx]}({df['iso_a3'][max_idx]}): ${max_price}"

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2010,'arg')
    print(result_a)

    result_b = get_big_mac_price_by_country('mex')
    print(result_b)

    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    print(result_c)

    result_d = get_the_most_expensive_big_mac_price_by_year(2014)
    print(result_d)
   