# two important python modules
import csv

import pandas as pd

# imports function that creates the email
import fill_template as ft

# the data we want to double check with candidates, based on state
ct_info = ['name', 'Facebook (Official)', 'Facebook (Personal)', 'Facebook (Campaign)', 'Twitter (Official)',
           'Twitter (Personal)', 'Twitter (Campaign)', 'email', 'birth_date', 'capitol_address', 'capitol_voice',
           'district_address', 'district_voice', 'youtube', 'Instagram (Official)', 'Instagram (Personal)',
           'Instagram (Campaign)']

# the link to state-specific data hosted on github
ct_url = '~/Desktop/govpackEmailGenerator/ct_test_data.csv'
ca_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/out.csv'
ok_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/out_ctcl.csv'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # available states, urls & info
    available_states = ["Connecticut", "California", "Oklahoma"]
    relevant_info = None
    url = None

    # user input: take state to generate all emails for
    while True:
        inp = input("Type the state you want to generate emails for: ")
        inp = inp.title()
        if inp not in available_states:
            print("Sorry, we can't generate emails for that state. Make sure there were no typos, and try again!")
        else:
            break

    if inp == 'Connecticut':
        url = ct_url
        relevant_info = ct_info
    elif inp == 'California':
        url = ca_url
        relevant_info = ct_info
    elif inp == 'Oklahoma':
        url = ok_url
        relevant_info = ct_info

    gp_data = pd.read_csv(url)
    gp_df = pd.DataFrame(gp_data)

    with open('output.csv', mode='w') as output:
        writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        for i in gp_df.index:
            writer.writerow([ft.fill_template(gp_df, i, relevant_info)])
