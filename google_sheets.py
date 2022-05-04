import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'creds1.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '#'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

range1 = ["List1!A2:C6"]  #

results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheet_id,
                                                   ranges=range1,
                                                   valueRenderOption='FORMATTED_VALUE',
                                                   dateTimeRenderOption='FORMATTED_STRING').execute()
sheet_values_cat1 = results['valueRanges'][0]['values']

print(sheet_values_cat1)


def test(mas):
    seq = ""
    for lis in mas:
        for text in lis:
            seq += text
        seq += "\\n"
    return seq


def making_a_list(mas):
    main_mas = []
    sentence = ''
    for i in mas:
        main_mas.append(str(i))
        print(main_mas)
    # for item in main_mas:
    #  sentence += item + '\n'


sheet_values_cat1 = test(sheet_values_cat1)
print(test(sheet_values_cat1))
