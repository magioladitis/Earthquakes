from statistics import mean

def Average(l): 
    avg = mean(l) 
    return avg
  
my_list = [2,4,6,8,10] 
average = Average(my_list) 
  
print "Average of my_list is", average
