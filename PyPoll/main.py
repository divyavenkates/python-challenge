# import os and csv
import os
import csv
# create path for election_data.csv file 
filepath=os.path.join("Resources","election_data.csv")

# open and read election_data.csv file 
with open(filepath,'r') as file: 
    csvreader=csv.reader(file, delimiter=",")
    #set the first line in election_data.csv file as header 
    header=next(csvreader)

     #set total votes and each candidates votes equal to 0
    votes=0
    charlesvotes=0
    dianavotes=0
    raymonvotes=0
     #create empty list for each candidate
    candidates=[]

    #for each row in election_data.csv file
    for row in csvreader:
        #add one to value of votes
        votes+=1
        #if a name from candidate column from file is not in candidates list, add it 
        if row[2] not in candidates:
            candidates.append(row[2])   

        #if the name from candidate column from file is the first name in candidates list, add one to value of charlesvotes
        if row[2] == candidates[0]:
            charlesvotes+=1
        #if the name from candidate column from file is the second name in candidates list, add one to value of dianavotes
        elif row[2]== candidates[1]:
            dianavotes+=1
        #if the name from candidate column from file is the third name in candidates list, add one to value of raymon
        elif row[2]== candidates[2]:
            raymonvotes+=1
 
    #calculate percent of each candidates votes by dividing their votes by total votes and multiplying by 100
    charlespercent = (charlesvotes/votes)*100
    dianapercent = (dianavotes/votes)*100
    raymonpercent = (raymonvotes/votes)*100

    # if charlesvotes is greater than dianavotes and raymonvotes, winner is charles
    if (charlesvotes>dianavotes) & (charlesvotes>raymonvotes):
        winner="Charles Casper Stockham"
    # if dianavotes is greater than charlesvotes and raymonvotes, winner is diana
    elif (dianavotes>charlesvotes) & (dianavotes>raymonvotes):
        winner="Diana DeGette"
    # if raymonvotes is greater than charlesvotes and dianavotes, winner is raymon
    elif (raymonvotes>charlesvotes) & (raymonvotes>dianavotes):
        winner="Raymon Anthony Doane"

     #print these statements
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

#create a path for a file that will print the analysis for the data 
outputpath=os.path.join("Analysis", "pypoll.txt")
# open and write the following statements 
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