import pandas as pd
import helpers


def fill_template(df):
    all_emails = []

    # initialize sentences to fill it out
    govpack_sentence = "I hope this email finds you well. I'm a researcher with Govpack, an open-source " \
                       "technology that aggregates data on state- and local-level elected officials, allowing local " \
                       "newspapers to easily build candidate profiles and election guides. I'm in the process of " \
                       "data collection, and I wanted to make sure that I have complete, accurate data to fill out " \
                       "your profile.<br><br>\n\n"

    data_sentence = "This is the information I've collected:<br>\n"
    missing_sentence = "<br>\nI'm missing some information too, and I'm hoping you could help me fill in the gaps. " \
                       "I want to make sure that my data is equally robust for every public official. " \
                       "<br><br>\n\nHere's the information I'm still looking for:<br>\n"
    closing_sentence = "<br>\nThank you so much for helping us build the most complete dataset possible. " \
                       "Please reach out with any questions, in addition to a confirmation of our existing data and " \
                       "filling in what we do not have.<br><br>\n\n" \
                       "Sincerely,<br>\n" \
                       "Govpack Research Team"

    for row in df.index:

        data_list = ''
        missing_list = ''

        for header in helpers.checking_info:
            # creating a string with our header
            new_header = header.replace('_', ' ')
            new_header = new_header.title()

            # managing linkedin and RSS
            if new_header == 'Linkedin':
                new_header = 'LinkedIn'
            if new_header == 'Rss':
                new_header = 'RSS'

            # making two-word columns read properly
            split_header = new_header.split()
            if len(split_header) == 2:
                split_header.reverse()
                new_header = ' '.join(split_header)

            # if there isn't a value, add it to the list of missing values
            if pd.isna(df[header][row]):
                missing_list += u'\u2022 ' + new_header + '<br>\n'

            # if there is a value (and it's not 'n/a'), add it to the list we have
            elif df[header][row] != 'n/a':
                if new_header == 'Capitol Address' and '\n' in df[header][row]:
                    data_list += u'\u2022 ' + new_header + ': ' + str(df[header][row]).replace('\n', '; ') + '<br>\n'
                else:
                    data_list += u'\u2022 ' + new_header + ': ' + str(df[header][row]) + '<br>\n'

        complete_text = data_sentence + data_list

        # if there's any data missing, add it
        if len(missing_list) != 0:
            complete_text += missing_sentence + missing_list

        complete_text = df['Name'][row] + ",<br><br>\n\n" + govpack_sentence + complete_text + closing_sentence

        all_emails.append(complete_text)

    df = pd.DataFrame(all_emails, columns=['completed emails'])

    return df
