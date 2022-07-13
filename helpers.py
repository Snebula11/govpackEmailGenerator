import subprocess


# checks whether we have the value (as represented by Pandas DataFrame)
def isnan(num):
    return num != num


# goal: automatically copy output to clipboard (essentially copy it)
def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))
