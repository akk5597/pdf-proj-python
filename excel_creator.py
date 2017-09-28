import openpyxl as opx
import json

def ccc(col,row):
	return chr(col+64)+str(row)

wb = opx.load_workbook('data_file.xlsx')
sheet = wb.create_sheet('Attempt1',0)

data = json.loads(open('my_file_clg.json','r').read())

sheet[ccc(1,1)] = 'College Codes'

columns = [
	'First Class with Distinction',
	'First Class',
	'Quality Result',
	'Higher Second Class',
	'Second Class',
	'Pass Numbers',
	'Others',
	'Total'
]

ccol = 'A'
for i,col in enumerate(columns):
	sheet[ccc(i+2,1)] = col

grade_list=[
	'FIRST CLASS WITH DISTINCTION\n\n', 
	'FIRST CLASS\n\n',
	'HIGHER SECOND CLASS\n\n',
	'   SECOND CLASS\n\n',
	'PASS NUMBERS\n\n',
	'FAIL A.T.K.T.\n\n',
	'FOR UNFAIRMEANS\n\n',
	'FOR ELIGIBILITY\n\n',
	'RESULT RESERVE FOR  BACKLOG\n\n',
	'RESULT RESERVE FOR OTHER REASON\n\n'
]

data_xl = {}

for clg in data:
	data_xl[clg] = []
	data_xl[clg].append(len(data.get(clg).get(grade_list[0].strip(),[]))) # First class with distinction
	data_xl[clg].append(len(data.get(clg).get(grade_list[1].strip(),[]))) # First class
	data_xl[clg].append(len(data.get(clg).get(grade_list[2].strip(),[]))) # Higher Second Class
	data_xl[clg].append(len(data.get(clg).get(grade_list[3].strip(),[]))) # Second Class
	data_xl[clg].append(len(data.get(clg).get(grade_list[4].strip(),[]))) # Pass Numbers
	data_xl[clg].append(
		len(data.get(clg).get(grade_list[5].strip(),[])) + 
		len(data.get(clg).get(grade_list[6].strip(),[])) + 
		len(data.get(clg).get(grade_list[7].strip(),[])) + 
		len(data.get(clg).get(grade_list[8].strip(),[])) + 
		len(data.get(clg).get(grade_list[9].strip(),[]))
	) # Others

crow = 2

for clg in data_xl:
	sheet[ccc(1,crow)] = clg
	sheet[ccc(2,crow)] = data_xl[clg][0] # First Class with Distinction
	sheet[ccc(3,crow)] = data_xl[clg][1] # First Class
	sheet[ccc(4,crow)] = data_xl[clg][0] + data_xl[clg][1] # Quality Result
	sheet[ccc(5,crow)] = data_xl[clg][2] # Higher Second Class
	sheet[ccc(6,crow)] = data_xl[clg][3] # Second Class
	sheet[ccc(7,crow)] = data_xl[clg][4] # Pass Numbers
	sheet[ccc(8,crow)] = data_xl[clg][5] # Others
	sheet[ccc(9,crow)] = sum(data_xl[clg])
	crow += 1

wb.save('data_file.xlsx')