import re

# Regular Expression to find Roll Numbers
roll_re = re.compile('S\d{9}')

# List of text that needs to be searched
dept_list=[
	'FOR Branch  S.E.(2014 PAT.)(CIVIL)',
	'FOR Branch  S.E.(2014 PAT.)(MECHANICAL)',
	'FOR Branch  S.E.(2014 PAT.)(ELECTRICAL)',
	'FOR Branch  S.E.(2014 PAT.)(ELECTRONICS &TELECOM)',
	'FOR Branch  S.E.(2014 PAT.)(INSTRUMENTATION & Control)',
	'FOR Branch  S.E.(2014 PAT.)(COMPUTER)',
	'FOR Branch  S.E.(2014 PAT.)(CHEMICAL)',
	'FOR Branch  S.E.(2014 PAT.)(MECHANICAL SANDWICH)',
	'FOR Branch  S.E.(2014 PAT.)(INFORMATIOM TECHNOLOGY)',
	'FOR Branch  S.E.(2014 PAT.)(AUTOMOBILE)'
]

# List of names of departments
depts = [
	'CIVIL',
	'MECHANICAL',
	'ELECTRICAL',
	'ELECTRONICS &TELECOM',
	'INSTRUMENTATION & Control',
	'COMPUTER',
	'CHEMICAL',
	'MECHANICAL SANDWICH',
	'INFORMATIOM TECHNOLOGY',
	'AUTOMOBILE'
]

# List of grades
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

# Opening file
file_text = open('pdf.txt','r')

# Converting file to single string variable
text = []
for line in file_text:
	text.append(line)

text = ''.join(text)

# Indices of the department in the text, basically separation points for the data according to departments
indices_dept = []
for dept in dept_list:
	indices_dept.append(text.find(dept))

# Dictionary to save all data
# Data will be saved in following manner
# data -> dept -> grade -> list of roll numbers
data = {}

# Main loop to start data mining
for i,dept in enumerate(depts):
	# Empty dictionary
	data[dept] = {}
	if i<9:
		currtext = text[indices_dept[i]:indices_dept[i+1]]
	else:
		currtext = text[indices_dept[9]:]
	
	# Indices of the grades separation
	grade_indices = []
	for grade in grade_list:
		grade_indices.append(currtext.find(grade))

	# Loop to go through the appropriate text to find roll numbers
	for j,grade in enumerate(grade_indices):
		if j<9:
			searchtext = currtext[grade_indices[j]:grade_indices[j+1]]
		else:
			searchtext = currtext[grade_indices[9]:]

		rolls = roll_re.findall(searchtext)

		# Storing values to final list
		data[dept][grade_list[j]] = rolls

clg_data = {}
for dept in data:
	for grade in data[dept]:
		for rolls in data[dept][grade]:
			num = rolls[3:6]
			clg_data.setdefault(num,{})
			clg_data[num].setdefault(grade.strip(),[])
			clg_data[num][grade.strip()].append(rolls)

import json
# save to file:
with open('my_file.json', 'w') as f:
    json.dump(data, f, indent = 4)

with open('my_file_clg.json', 'w') as f:
    json.dump(clg_data, f, indent = 4)