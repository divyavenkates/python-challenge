# import os and csv
import os
import csv
# create path for budget_data.csv file 
filepath=os.path.join("Resources","budget_data.csv")
# open and read budget_data.csv file 
with open(filepath,'r') as file: 
    csvreader=csv.reader(file, delimiter=",")
    #set the first line in budget_data.csv file as header 
    header=next(csvreader)

    #set months and totalprice equal to 0
    months=0
    totalprice=0
    #create empty list for each column in list 
    profits=[]
    date=[]
    #create empty list for profit changes between each row 
    changes=[]

    #for each row in budget_data.csv file
    for row in csvreader:
        #add one to value of months 
        months+=1
         #add the integer value from Profit/Losses column to value of totalprice
        totalprice += int(row[1])
        #append the string value from first column to date list 
        date.append(row[0]) 
        #append the integer value from Profit/Losses column to date list 
        profits.append(int(row[1])) 

    #for every value in profits list
    for i in range (len(profits)-1):
        #append the subtraction of that value from the next value to changes list
        changes.append(profits[i+1] - profits[i])

    #to calculate the average change add all the values from changes list and divide by the number of numbers 
    average = sum(changes)/len(changes) 
 
    #get index of the maximum and miunimum value of changes list 
    maxindex = changes.index(max(changes))
    minindex = changes.index(min(changes))

    #print these statements
    print("Financial Analysis")
    print("---------------------------- ")  
    print(f"Total Months: {months}")
    print(f"Total: ${totalprice}")
    print(f"Average Change: $ {round(average,2)}")
    print(f"Greatest Increase in Profits: {date[maxindex+1]} (${changes[maxindex]})")
    print(f"Greatest Decrease in Profits: {date[minindex+1]} (${changes[minindex]})")

#create a path for a file that will print the analysis for the data 
outputpath=os.path.join("Analysis", "pybank.txt")
# open and write the following statements 
with open(outputpath,'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------------- \n")  
    file.write(f"Total Months: {months}\n")
    file.write(f"Total: ${totalprice} \n") 
    file.write(f"Average Change: $ {round(average,2)}\n")
    file.write(f"Greatest Increase in Profits: {date[maxindex+1]} (${changes[maxindex]})\n")
    file.write(f"Greatest Decrease in Profits: {date[minindex+1]} (${changes[minindex]})\n")