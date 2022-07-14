import subprocess
import pandas as pd


# checks whether we have the value (as represented by Pandas DataFrame)
def isnan(num):
    return num != num


# reads a .csv file into a DataFrame from its url
def get_data(url):
    return pd.DataFrame(pd.read_csv(url))


# goal: automatically copy output to clipboard (essentially copy it)
def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))
