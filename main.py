import subprocess
import pandas as pd
import csv


# the data we want to double check with candidates
ct_info = ['name', 'Facebook (Official)', 'Facebook (Personal)', 'Facebook (Campaign)', 'Twitter (Official)',
           'Twitter (Personal)', 'Twitter (Campaign)', 'email', 'birth_date', 'capitol_address', 'capitol_voice',
           'district_address', 'district_voice', 'youtube', 'Instagram (Official)', 'Instagram (Personal)',
           'Instagram (Campaign)']

# getting our data and reading into DataFrame
gp_data = pd.read_csv(r'/Users/benswedberg/Desktop/test1.csv')
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


# checks whether we have the value (as represented by Pandas DataFrame)
def isnan(num):
    return num != num


# goal: automatically copy output to clipboard (essentially copy it)
def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))


# actually generates the email
def fill_template(data):
    # initialize sentences to fill it out
    govpack_sentence = "I hope this email finds you well. I'm a researcher with Govpack, an open-source " \
                       "technology that aggregates data on state- and local-level elected officials, allowing local " \
                       "newspapers to easily build candidate profiles and election guides. I'm in the process of " \
                       "data collection, and I wanted to make sure that I have complete, accurate data to fill out " \
                       "your profile.\n\n"

    data_sentence = "This is the information I've collected:\n"
    missing_sentence = "\nI'm missing some information too, and I'm hoping you could help me fill in the gaps. " \
                       "I want to make sure that my data is equally robust for every public official. " \
                       "\n\nHere's the information I'm still looking for:\n"

    # initialize data we have and we're missing
    data_list = ''
    missing_list = ''

    # create the list of data we have
    for x in data:
        # if we're interested in the data
        if x in ct_info:
            # create a new key that simply parses and capitalizes the header
            new_key = x.replace('_', ' ')
            new_key = new_key.replace('voice', 'phone')
            new_key = new_key.title()
            # changing our  social media headers
            if '(' in new_key:
                new_key = new_key.replace('(', '')
                new_key = new_key.replace(')', '')
                new_key_list = new_key.split(" ")
                new_key_list.reverse()
                new_key = " ".join(new_key_list)
            # if we don't have the data, add it to the list of missing data
            if isnan(data[x]):
                missing_list += u'\u2022 ' + new_key + '\n'
            # if we do, list the type of data and it's value
            else:
                if new_key == 'Capitol Address' and '\n' in data[x]:
                    data_list += u'\u2022 ' + new_key + ': ' + str(data[x]).replace('\n', '; ') + '\n'
                else:
                    data_list += u'\u2022 ' + new_key + ': ' + str(data[x]) + '\n'

    # begin putting together the text
    complete_text = data_sentence + data_list

    # if there's any data missing, add it
    if len(missing_list) != 0:
        complete_text += missing_sentence + missing_list

    return data['title'].split(" ")[1] + ' ' + data['family_name'] + ",\n\n" + govpack_sentence + complete_text


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('ct_output.csv', mode='w') as ct_output:
        ct_writer = csv.writer(ct_output, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        for candidate in candidate_dict.values():
            ct_writer.writerow([fill_template(candidate)])
