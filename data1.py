import csv 
import math

with open('data.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data = file_data[0]
print(file_data)

def mean(data):
    total = 0
    for i in data:
        total += float(i)
    
    mean = total/len(data)
    return mean

print(mean(file_data))
squared_list = []
for number in file_data:
    a = float(number)-mean(file_data)
    a = a**2
    squared_list.append(a)

summation = 0
for i in squared_list:
    summation = summation + i

result = summation/(len(file_data)-1)
standard_deviation = math.sqrt(result)
print(standard_deviation)