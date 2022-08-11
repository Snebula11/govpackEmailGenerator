# imports function that creates the email
import helpers
import fill_template as ft

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # user input: take state to generate all emails for
    # inp = input("Type the postal abbr. for the state you need emails: ").upper()

    for inp in helpers.states.keys():
        output_filepath = 'emails/' + inp.lower() + '_emails.csv'

        url = 'https://raw.githubusercontent.com/Snebula11/oklahama-cleaner/main/data/' \
              + inp.upper() \
              + '/' \
              + inp.lower() \
              + '_output.csv'
        df = helpers.get_data(url)

        print(f'making {inp} emails')

        ft.fill_template(df).to_csv(output_filepath, index=False, encoding='utf-8')
