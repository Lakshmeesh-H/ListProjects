import csv

# Finding matching and not matching columns between 2 different csv files 

company50 = []
with open('nifty50.csv', mode='r') as my_file:
    csv_reader = csv.reader(my_file, delimiter=',')
    for companies in csv_reader:
        company50.append(companies[0])
# print(company50)

company100 = []
with open('nifty100.csv', mode='r') as my_file2:
    csv_reader2 = csv.reader(my_file2, delimiter=',')
    for companies in csv_reader2:
        company100.append(companies[0])
# print(company100)

new_list = []
for company in company100:
    if  company not in company50:
        new_list.append(company)

print(new_list)