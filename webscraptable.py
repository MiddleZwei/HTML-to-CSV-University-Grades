import unicodecsv as csv

from bs4 import BeautifulSoup
import requests
import argparse
import sys

from tools import PasswordPromptAction, query_yes_no
from lxml import html

'''
PARSE ARGUMENTS
'''
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", required=True,
                    help='Your sXXXXX number.')
parser.add_argument("-p", "--password", action=PasswordPromptAction, required=True,
                    help='Your password.')
parser.add_argument("-l", "--language", required=False,
                    help='[optional] Language of the transcript. Under implementation.')
parser.add_argument("-o", "--output", required=False,
                    help='[optional] Provide an output filename')
args = vars(parser.parse_args())

with requests.Session() as session_requests:
    '''
    ====================================
    LOGIN
    ====================================
    '''
    login_url = "https://dziekanat.pjwstk.edu.pl/"
    result = session_requests.get(login_url)
    tree = html.fromstring(result.text)
    VIEWSTATEGENERATOR = list(set(tree.xpath("//input[@name='__VIEWSTATEGENERATOR']/@value")))[0]
    EVENTVALIDATION = list(set(tree.xpath("//input[@name='__EVENTVALIDATION']/@value")))[0]
    VIEWSTATE = list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")))[0]
    # EVENTTARGET = list(set(tree.xpath("//input[@name='__EVENTTARGET']/@value")))[0]
    # EVENTARGUMENT = list(set(tree.xpath("//input[@name='__EVENTARGUMENT']/@value")))[0]
    BUTTON = list(set(tree.xpath("//input[@name='Button1']/@value")))[0]

    login_payload = {
        "txtLogin": args["username"],
        "txtHaslo": args["password"],
        "__VIEWSTATEGENERATOR": VIEWSTATEGENERATOR,
        "__EVENTVALIDATION": EVENTVALIDATION,
        "__VIEWSTATE": VIEWSTATE,
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "Button1": BUTTON,
    }
    login_headers = {
        "referer": login_url
    }
    login_request = session_requests.post(
        login_url,
        data=login_payload,
        headers=login_headers
    )

    print("Logging in...")

    '''
    ====================================
    SWITCH LANGUAGE TO EN/PL
    ====================================
    '''
    # url = 'https://dziekanat.pjwstk.edu.pl/OY.aspx'
    # headers = {
    #     "referer": url
    # }
    # payload = {
    #     "__EVENTTARGET": "ctl00$EnglishLinkButton"
    # }
    # change_language_request = session_requests.post(
    #     url,
    #     data=payload,
    #     headers=headers
    # )
    # print("Language changed status code:  ", change_language_request.status_code)

    '''
    ====================================
    GET GRADES
    ====================================
    '''
    grades_url = 'https://dziekanat.pjwstk.edu.pl/OY.aspx'
    get_grades_headers = {
        "referer": grades_url
    }
    grades_request = session_requests.get(
        grades_url,
        headers=get_grades_headers
    )
    print("Looking for grades...")

    '''
    ====================================
    PRINT TO CSV
    ====================================
    '''
    filename = [args["output"] if args["output"] is not None else str("oceny_" + args["username"] + ".csv")][0]
    outfile = open(filename, "bw")
    writer = csv.writer(outfile)

    soup = BeautifulSoup(grades_request.content, "lxml")
    table = soup.find("table", attrs={"class": "GridView"})

    list_of_rows = []
    try:
        all_elements = table.findAll('tr')
    except Exception as e:
        sys.exit("Could not find any grades. Please, check your credentials and try again.")

    for row in all_elements:
        list_of_cells = []
        for cell in row.findAll(["th", "td"]):
            text = cell.text
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)

    for data in list_of_rows:
        writer.writerow(data)
    print("The grades have been successfully transferred to " + filename)

    if query_yes_no("Print grades to the console, too?"):
        for data in list_of_rows:
            print(' '.join(data))
