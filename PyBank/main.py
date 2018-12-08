#In this challenge, you are tasked with creating a Python script for 
#analyzing the financial records of your company. You will give a set 
# of financial data called budget_data.csv. The dataset is composed of 
#two columns: Date and Profit/Losses. 
# (Thankfully, your company has rather lax standards for accounting so
#  the records are simple.)

#Your task is to create a Python script that analyzes the records to calculate each of the following:

##1 FIND AND OPEN BUDGET_DAT.CSV 2 COLUMNS DATE AND PROFIT/LOSS
import os
import csv

##Find Data
csvpath = os.path.join('budget_data.csv')

with open(csvpath, 'r') as csvfile:
    ## CSV reader specifies delimiter and variable that holds contents
    ## FIND The total number of months included in the dataset
    ## FIND The total net amount of "Profit/Losses" over the entire period
    ## FIND The average change in "Profit/Losses" between months over the entire period
    ## The greatest increase in profits (date and amount) over the entire period
    ## previous month = 
    ## The greatest decrease in losses (date and amount) over the entire period
    csvreader = csv.reader(csvfile, delimiter=',')
    linenumber = 0
    total = 0
    prev = 0
    maxchange = 0
    maxchangemonth = 0
    minchange = 0
    minchangemonth = 0
    change = 0
    previousmonth = 0
    totalchange = 0
    firstrow = 0
    next(csvreader)
    for row in csvreader:
        linenumber += 1  
        if linenumber ==1:
            firstrow = float(row[1])
        current = float(row[1])
        change = current - prev
        lastrow = float(row[1])
        if change > maxchange:
            maxchange = change
            maxchangemonth = row [0]
        if change < minchange:
            minchange = change
            minchangemonth = row[0]
        total += int(row[1])
        totalchange += int(change)
        prev = current
    avechange = (lastrow - firstrow)/(linenumber-1)
    #print(lastrow)
    #print(firstrow)
    # final script should both print the analysis to the terminal
    #As an example, your analysis should look similar to the one below:
    #Financial Analysis
    #----------------------------
    #Total Months: 86
    #Total: $38382578
    #Average  Change: $-2315.12
    #Greatest Increase in Profits: Feb-2012 ($1926159)
    #Greatest Decrease in Profits: Sep-2013 ($-2196167)
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {linenumber}')
    print(f'Total: ${total}')
    print(f'Average  Change: ${avechange: .2f}')
    print(f'Greatest Increase in Profits: {maxchangemonth} ${maxchange} ')
    print(f'Greatest Decrease in Profits: {minchangemonth} ${minchange}')

output_path = "Results.txt"
    # Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as outfile:

    # Write the first row (column headers)
    outfile.write('Financial Analysis\n')
    outfile.write('----------------------------\n')
    outfile.write(f'Total Months: {linenumber}\n')
    outfile.write(f'Total: ${total}\n')
    outfile.write(f'Average  Change: ${avechange: .2f}\n')
    outfile.write(f'Greatest Increase in Profits: {maxchangemonth} ${maxchange} \n')
    outfile.write(f'Greatest Decrease in Profits: {minchangemonth} ${minchange}\n')
# export a text file with the results