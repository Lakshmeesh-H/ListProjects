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

with open('unique.csv', 'w') as my_file3:
    csv_writer = csv.writer(my_file3)
    csv_writer.writerow(['Company Name'])
    for item in new_list: 
        csv_writer.writerow(item.split())

# print(new_list)

# Another method of getting non unique values 

new_set = {}
company50set = set(company50)
company100set = set(company100)
new_set = company100set - company50set
print(new_set)