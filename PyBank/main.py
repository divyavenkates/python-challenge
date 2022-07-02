import os
filepath=os.path.join("Resources","budget_data.csv")
import csv
with open(filepath,'r') as file: 
    csvreader=csv.reader(file, delimiter=",")
    header=next(csvreader)

    months=0
    totalprice=0
    profit_losses=[]
    date=[]
    changes=[]
    for row in csvreader:
        months+=1
        totalprice += int(row[1])
        date.append(row[0]) 
        profit_losses.append(int(row[1])) 

    for i in range (len(profit_losses)-1):
        changes.append(profit_losses[i+1] - profit_losses[i])

    average = sum(changes)/len(changes) 
 
    maxindex = changes.index(max(changes))
    minindex = changes.index(min(changes))

    print("Financial Analysis")
    print("---------------------------- ")  
    print(f"Total Months: {months}")
    print(f"Total: ${totalprice}")
    print(f"Average Change: $ {round(average,2)}")
    print(f"Greatest Increase in Profits: {date[maxindex+1]} (${max(changes)})")
    print(f"Greatest Decrease in Profits: {date[minindex+1]} (${min(changes)})")