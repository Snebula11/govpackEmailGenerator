import helpers


def fill_template(data, important_info):
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

    # initialize data we have and we're missing
    data_list = ''
    missing_list = ''

    # create the list of data we have
    for x in data:
        # if we're interested in the data
        if x in important_info:
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
            if helpers.isnan(data[x]):
                missing_list += u'\u2022 ' + new_key + '<br>\n'
            # if we do, list the type of data and it's value
            else:
                if new_key == 'Capitol Address' and '<br>\n' in data[x]:
                    data_list += u'\u2022 ' + new_key + ': ' + str(data[x]).replace('<br>\n', '; ') + '<br>\n'
                else:
                    data_list += u'\u2022 ' + new_key + ': ' + str(data[x]) + '<br>\n'

    # begin putting together the text
    complete_text = data_sentence + data_list

    # if there's any data missing, add it
    if len(missing_list) != 0:
        complete_text += missing_sentence + missing_list

    if helpers.isnan(data['title']):
        return data['name'] + ",<br><br>\n\n" + govpack_sentence + complete_text
    else:
        return data['title'].split(" ")[1] + ' ' + data[
            'family_name'] + ",<br><br>\n\n" + govpack_sentence + complete_text
