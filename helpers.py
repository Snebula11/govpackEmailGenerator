import pandas as pd


# reads a .csv file into a DataFrame from its url
def get_data(url):
    return pd.DataFrame(pd.read_csv(url, keep_default_na=False, na_values=[""]))

checking_info = ['Name', 'party', 'state', 'status', 'district', 'gender', 'education', 'occupation', 'Office',
                 'email_official', 'email_other', 'email_campaign', 'Bio', 'date_of_birth', 'Image', 'website_campaign',
                 'website_official', 'website_personal', 'address_capitol', 'phone_capitol', 'fax_capitol',
                 'address_district', 'phone_district', 'fax_district', 'address_campaign', 'phone_campaign',
                 'twitter_official', 'twitter_personal', 'twitter_campaign', 'youtube_official', 'youtube_personal',
                 'youtube_campaign', 'instagram_official', 'instagram_personal', 'instagram_campaign',
                 'facebook_official', 'facebook_personal', 'facebook_campaign', 'linkedin', 'rumble', 'gab', 'RSS']
