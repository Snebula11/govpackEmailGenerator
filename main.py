# two important python modules
import pandas as pd
import csv

# imports function that creates the email
import fill_template as ft

# the data we want to double check with candidates, based on state
ct_info = ['name', 'Facebook (Official)', 'Facebook (Personal)', 'Facebook (Campaign)', 'Twitter (Official)',
           'Twitter (Personal)', 'Twitter (Campaign)', 'email', 'birth_date', 'capitol_address', 'capitol_voice',
           'district_address', 'district_voice', 'youtube', 'Instagram (Official)', 'Instagram (Personal)',
           'Instagram (Campaign)']

# the link to state-specific data hosted on github
ct_url = 'https://raw.githubusercontent.com/Snebula11/govpackEmailGenerator/main/ct_test_data.csv'
ca_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/out.csv'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # available states, urls & info
    available_states = ["Connecticut", "California"]
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

    gp_data = pd.read_csv(url)
    gp_df = pd.DataFrame(gp_data)

    # creating our dictionary of candidates
    candidate_dict = {}

    # initializing our dictionary of candidates
    for curr_can_index in gp_df.index:
        # sets key:value pair as 'candidate name':empty_dictionary
        candidate_dict[gp_df['name'][curr_can_index]] = {}
        for curr_column in gp_df.columns:
            # for each data point, we update the empty_dictionary
            candidate_dict[gp_df['name'][curr_can_index]][curr_column] = gp_df[curr_column][curr_can_index]

    with open('output.csv', mode='w') as output:
        writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        for candidate in candidate_dict.values():
            writer.writerow([ft.fill_template(candidate, relevant_info)])
