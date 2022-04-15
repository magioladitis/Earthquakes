import os

all_files = os.listdir()
csv_files = []
for f in all_files:
	if '.csv' in f:
		csv_files.append(f)
for f_c in csv_files:
	with open(f_c,'r') as file_csv:
		raw_data = file_csv.readlines()
	data = []
	for l in raw_data:
		s = ''
		for ch in l:
			if ch.isdigit():
				s += ch
		data.append(int(s))
	print('File = ',f,'mean value = ',sum(data)/len(data))
