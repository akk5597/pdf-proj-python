import json
import openpyxl as opx

data = json.loads(open('my_file_clg.json').read())
wb = opx.load_workbook('data_file.xlsx')

sheet = opx.create_sheet('Attempt1',0)

header = [
	'FIRST CLASS WITH DISTINCTION',
	'FIRST CLASS',
	'HIGHER SECOND CLASS',
	'SECOND CLASS',
	'PASS NUMBERS',
	'FAIL A.T.K.T.',
	'FOR UNFAIRMEANS',
	'FOR ELIGIBILITY',
	'RESULT RESERVE FOR  BACKLOG',
	'RESULT RESERVE FOR OTHER REASON'
]

for clg in data:
