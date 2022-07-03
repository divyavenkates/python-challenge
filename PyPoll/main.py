import os
filepath=os.path.join("Resources","election_data.csv")
import csv
with open(filepath,'r') as file: 
    csvreader=csv.reader(file, delimiter=",")
    header=next(csvreader)

    votes=0
    charlesvotes=0
    dianavotes=0
    raymonvotes=0
    candidates=[]
    for row in csvreader:
        votes+=1
        if row[2] not in candidates:
            candidates.append(row[2])   
                 
        if row[2] == candidates[0]:
            charlesvotes+=1
        elif row[2]== candidates[1]:
            dianavotes+=1
        elif row[2]== candidates[2]:
            raymonvotes+=1
 
    charlespercent = (charlesvotes/votes)*100
    dianapercent = (dianavotes/votes)*100
    raymonpercent = (raymonvotes/votes)*100

    if (charlesvotes>dianavotes) & (charlesvotes>raymonvotes):
        winner="Charles Casper Stockham"
    elif (dianavotes>charlesvotes) & (dianavotes>raymonvotes):
        winner="Diana DeGette"
    elif (raymonvotes>charlesvotes) & (raymonvotes>dianavotes):
        winner="Raymon Anthony Doane"


    print("Election Results")
    print("---------------------------- ")  
    print(f"Total Votes: {votes}")
    print("---------------------------- ") 
    print(f"{candidates[0]}: {round(charlespercent,3)}% ({charlesvotes})")
    print(f"{candidates[1]}: {round(dianapercent,3)}% ({dianavotes})")
    print(f"{candidates[2]}: {round(raymonpercent,3)}% ({raymonvotes})")
    print("---------------------------- ") 
    print(f"Winner: {winner}") 
    print("---------------------------- ") 

outputpath=os.path.join("Analysis", "pypoll.txt")
with open(outputpath,'w') as file:
    file.write("Election Results\n")
    file.write("---------------------------- \n")  
    file.write(f"Total Votes: {votes}\n")
    file.write("---------------------------- \n") 
    file.write(f"{candidates[0]}: {round(charlespercent,3)}% ({charlesvotes})\n")
    file.write(f"{candidates[1]}: {round(dianapercent,3)}% ({dianavotes})\n")
    file.write(f"{candidates[2]}: {round(raymonpercent,3)}% ({raymonvotes})\n")
    file.write("----------------------------\n ") 
    file.write(f"Winner: {winner}\n") 
    file.write ("---------------------------- \n") 