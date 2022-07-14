import pandas as pd


def fill_template(gp_df, index, important_info):
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

    # initialize data we have and we're missing
    data_list = ''
    missing_list = ''

    for column in gp_df:
        if column in important_info:
            new_phrase = column.replace('_', ' ')
            new_phrase = new_phrase.replace('voice', 'phone')
            if new_phrase != 'LinkedIn':
                new_phrase = new_phrase.title()
            if '(' in new_phrase:
                new_phrase = new_phrase.replace('(', '')
                new_phrase = new_phrase.replace(')', '')
                new_phrase_list = new_phrase.split(" ")
                new_phrase_list.reverse()
                new_phrase = " ".join(new_phrase_list)
                # if we don't have the data, add it to the list of missing data
            if pd.isna(gp_df[column][index]):
                missing_list += u'\u2022 ' + new_phrase + '<br>\n'
                # if we do, list the type of data and it's value
            elif gp_df[column][index] != 'n/a':
                if new_phrase == 'Capitol Address' and '\n' in gp_df[column][index]:
                    data_list += u'\u2022 ' + new_phrase + ': ' + str(gp_df[column][index]).replace('\n', '; ') + \
                                 '<br>\n'
                else:
                    data_list += u'\u2022 ' + new_phrase + ': ' + str(gp_df[column][index]) + '<br>\n'

    # begin putting together the text
    complete_text = data_sentence + data_list

    # if there's any data missing, add it
    if len(missing_list) != 0:
        complete_text += missing_sentence + missing_list

    if pd.isna(gp_df['title'][index]):
        return gp_df['name'][index] + ",<br><br>\n\n" + govpack_sentence + complete_text + closing_sentence
    else:
        return gp_df['title'][index].split(" ")[1] + ' ' + gp_df['family_name'][index] + ",<br><br>\n\n" + \
               govpack_sentence + complete_text + closing_sentence
