import subprocess
import pandas as pd


# reads a .csv file into a DataFrame from its url
def get_data(url):
    return pd.DataFrame(pd.read_csv(url, keep_default_na=False, na_values=[""]))


# goal: automatically copy output to clipboard (essentially copy it)
def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))
