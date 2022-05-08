import os
import statistics
import matplotlib.pyplot as plt
from earthq01_stat import *

def menu(f):
	print(80*'*')
	print('Ανάλυση Στατιστικών Δεδομένων Αρχείου: ',f)
	print('1. Κυλιόμενος μέσος όρος')
	print('2. Κυλιόμενη διάμεσος')
	print('3. Διακύμανση')
	print('4. Εύρος')
	print('5. Έξοδος')
	choice = 0
	while choice not in [1,2,3,4,5]:
		choice = int(input('Επιλογή = '))
	return choice
	

all_files = os.listdir()
csv_files = []
for f in all_files:
	if '.csv' in f:
		csv_files.append(f)
print(' **** Διαθέσιμα αρχεία ****')
for i in range (len(csv_files)):
	print(f"{i+1:2}", '.',csv_files[i])
print('***************************')
file_index = -1
while file_index not in range(len(csv_files)+1) or file_index < 1:
	file_index = int(input('Επιλογή αρχείου :'))
with open(csv_files[file_index-1],'r') as file_csv:
	raw_data = file_csv.readlines()
data = []
for l in raw_data:
	s = ''
	for ch in l:
		if ch.isdigit():
			s += ch
	s = int(s)
	if l[0] == '-':
		s = -s
	data.append(s)
c = menu(csv_files[file_index-1])
while c != 5:
	if c == 1:
		w = int(input('Παράθυρο δεδομένων (1 όλα τα δεδομένα) = '))
		w_mean(csv_files[file_index-1],data,w)
		c = menu(csv_files[file_index-1])
	if c == 2:
		w = int(input('Παράθυρο δεδομένων (1 όλα τα δεδομένα) = '))
		w_median(csv_files[file_index-1],data,w)
		c = menu(csv_files[file_index-1])
		
		
		
		
		
