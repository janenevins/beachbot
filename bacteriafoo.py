import csv
import requests
from utils.datehelper import fix_date_string

SRC_DATA_URL = 'https://data.smcgov.org/api/views/kpd9-xf4h/rows.csv?accessType=DOWNLOAD'


def __sortfoo(somerecord): #this creats the key to sort by the date
    a = somerecord['Process Date']
    b = fix_date_string(a)
    return b


def get_data(): #this function downloads the data and creates a list of dictionaries
    resp = requests.get(SRC_DATA_URL)
    txt = resp.text
    lines = txt.splitlines()
    results = list(csv.DictReader(lines))
    return results



def get_beach_names(): #this works in the interactive shell, but the function doesn't work when I paste it in
    rows = get_data()
    names = []
    for r in rows:
        names.append(r['Site Name'])

    return sorted(list(set(names)))

def get_beach_results(beachname): #this sorts all the records by Process Date
    all_rows = get_data()
    filtered_rows = []

    for row in all_rows:
        if row['Site Name'] == beachname.upper(): #Getting an error because in this beachname is a list? list object has no attribute upper
            filtered_rows.append(row)

    return sorted(filtered_rows, key=__sortfoo, reverse=True)
