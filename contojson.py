from gsheets import Sheets
import json

# Enter your google sheet id
sheet_id = ''
sheet = None


def convert_to_json():
    global sheet, sheet_id
    sheets = Sheets.from_files('./google_api_client_keys/credentials.json')
    sheet = sheets[sheet_id]

    companies = []
    for ws in sheet:
        for row in range(1, ws.nrows):
            companies_sub = {
                "Name": ws.at(row, 1),
                "Location": ws.at(row, 0)
            }
            companies.append(companies_sub)

        unique_keys = []
        for i in range(0, len(companies)):
            if companies[i] not in companies[i+1:]:
                unique_keys.append(companies[i])
        comp = json.dumps(list(unique_keys))

    with open('./static/assets/companies.json', 'w') as fh:
        fh.write(comp)
