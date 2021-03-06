# imports function that creates the email
import helpers
import fill_template as ft
import csv

# the data we want to double check with candidates, based on state
ct_info = ['name', 'Facebook (Official)', 'Facebook (Personal)', 'Facebook (Campaign)', 'Twitter (Official)',
           'Twitter (Personal)', 'Twitter (Campaign)', 'email', 'birth_date', 'capitol_address', 'capitol_voice',
           'district_address', 'district_voice', 'youtube', 'Instagram (Official)', 'Instagram (Personal)',
           'Instagram (Campaign)']

ok_info = ['name', 'Facebook (Official)', 'Facebook (Personal)', 'Facebook (Campaign)', 'Twitter (Official)',
           'Twitter (Personal)', 'Twitter (Campaign)', 'email', 'birth_date', 'capitol_address', 'capitol_voice',
           'district_address', 'district_voice', 'youtube', 'Instagram (Official)', 'Instagram (Personal)',
           'Instagram (Campaign)', 'Campaign mailing address', 'Campaign phone', 'LinkedIn']

# the link to state-specific data hosted on github
ct_url = 'https://raw.githubusercontent.com/Snebula11/govpackEmailGenerator/main/ct_test_data.csv'
ca_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/out.csv'
ok_url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/out_ctcl.csv'

# available states
available_states = ['CT', 'CA', 'OK']


# takes a dataframe, the name of the file to output to, and the list of headers we want to double-check
# outputs to filename 'outp' as a N x 1 array of emails
def output_data(dataframe, outp, info):
    with open(outp, mode='w') as output:
        writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        for i in gp_df.index:
            writer.writerow([ft.fill_template(dataframe, i, info)])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # user input: take state to generate all emails for
    while True:
        inp = input("Type the postal abbr. for the state you need emails: ").upper()
        if inp not in available_states:
            print("Sorry, we can't generate emails for that state. Make sure there were no typos, and try again!")
        else:
            break

    if inp == 'CT':
        gp_df = helpers.get_data(ct_url)
        output_data(gp_df, 'emails/ct_emails.csv', ct_info)
    elif inp == 'CA':
        gp_df = helpers.get_data(ca_url)
        output_data(gp_df, 'emails/ca_emails.csv', ct_info)
    elif inp == 'OK':
        gp_df = helpers.get_data(ok_url)
        output_data(gp_df, 'emails/ok_emails.csv', ok_info)
