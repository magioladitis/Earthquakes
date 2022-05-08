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
	
def w_variance(f,d,w):
	print('Κυλιόμενη διάμεσος αρχείου : ',f,' παράθυρο δεδομένων = ',w)
	m = []
	for i in range(len(d)-w):
		m.append(statistics.pvariance(d[i:i+w]))
	plt.plot(m)
	plt.title('Κυλιόμενη διακύμανση - παράθυρο δεδομένων = '+str(w))
	plt.show()
	
def w_min_max(f,d,w):
	print('Κυλιόμενο εύρος αρχείου : ',f,' παράθυρο δεδομένων = ',w)
	mi = []
	ma = []
	e = []
	for i in range(len(d)-w):
		mi.append(min(d[i:i+w]))
		ma.append(max(d[i:i+w]))
		e.append(ma[-1] - mi[-1])
	plt.plot(mi,'b',label='minimum')
	plt.plot(ma,'r',label='maximum')
	plt.legend()
	plt.title('Κυλιόμενα min max - παράθυρο δεδομένων = '+str(w))
	plt.show()
	plt.plot(e)
	plt.title('Κυλιόμενο εύρος - παράθυρο δεδομένων = '+str(w))
	plt.show()
