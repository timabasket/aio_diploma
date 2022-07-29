import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'creds1.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '18QEQuYP7G9bIFDvq74bGgIPon4wSOICntP3mDIYuQlA'
spreadsheet_id1 = '1HJfs3N6ipC_Z1aTHbDxag0hvIQYMLLRyPPCup1_cB2A'

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

range2 = ["task-list!A4:C16"]
results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheet_id1,
                                                   ranges=range2,
                                                   valueRenderOption='FORMATTED_VALUE',
                                                   dateTimeRenderOption='FORMATTED_STRING').execute()
sheet_values_list = results['valueRanges'][0]['values']

def task_list(mas):
    seq = ""
    for lis in mas:
        seq += '- ' + lis[0] + ' - ' + lis[1] + ': ' + lis[2]
        seq += "\n"
    return seq
print(sheet_values_list)
sheet_values_list = task_list(sheet_values_list)

def test(mas):
    seq = ""
    for lis in mas:
        seq += '- ' + lis[0] + ' ' + lis[1] + ' руб.'
        seq += "\n"
    return seq
print(test(sheet_values_cat1))
sheet_values_cat1 = test(sheet_values_cat1)

def making_a_list(mas):
    main_mas = []
    sentence = ''
    for i in mas:
        main_mas.append(str(i))
        print(main_mas)
    # for item in main_mas:
    #  sentence += item + '\n'



