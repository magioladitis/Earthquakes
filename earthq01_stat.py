import statistics
import matplotlib.pyplot as plt

def w_mean(f,d,w):
	print('Κυλιόμενος μέσος όρος αρχείου : ',f,' παράθυρο δεδομένων = ',w)
	m = []
	for i in range(len(d)-w):
		m.append(sum(d[i:i+w])/w)
	plt.plot(m)
	plt.title('Κυλιόμενος μέσος όρος - παράθυρο δεδομένων = '+str(w))
	plt.show()
	
def w_median(f,d,w):
	print('Κυλιόμενη διάμεσος αρχείου : ',f,' παράθυρο δεδομένων = ',w)
	m = []
	for i in range(len(d)-w):
		m.append(statistics.median(d[i:i+w]))
	plt.plot(m)
	plt.title('Κυλιόμενη διάμεσος - παράθυρο δεδομένων = '+str(w))
	plt.show()
