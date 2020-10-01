import os
import csv

#creating path to collect data from the my PyBank Folder
budget_data = os.path.join('budget_file.csv')

#delcare variables that will be used throughout program
total_months = 0 #int value to hold number of months
total_profit = 0 #int value to hold value of profit
value = 0 #int variable that will hold the value for each row
change = 0 #int variable that will store the change in value from each row
profit = [] #list variable that will store the list of a row
months = [] #same instance but for the months in the row


#Reading in the csv file that we are working with
with open(budget_data) as csvfile:

    #splittin gth edata with a comma delimiter
    reader = csv.reader(csvfile, delimiter=",")

    #Telling the program to skep the heaader values
    header = next(reader)

    #Setting a variable first_value = to the first row with will a value
    first_value = next(reader)

    #Setting the a variable total_profit = the long value in the data set
    total_profit += int(first_value[1])

    #Same instance for value
    value += int(first_value[1])

    #initiating for loop to read through the values of the csv file
    for row in reader:

        #Appending the values in the 1st column to my variable months
        months.append(row[0])

        #Running a calculation within the for loop that will keep track of the
        #change in value throughout the data set
        #it is subtracting the first value from the upcoming second value within the loop
        change = int(row[1]) - value
        profit.append(change)
        value = int(row[1])

        #counter int variable that is storing the total value of months within the data set
        total_months += 1

        #Grabbing the total sum of the data set
        total_profit = total_profit + int(row[1])

        #exit the for loop by indentation

    #Finding the max profit within the data set
    #Python is locating the max value change and storing the value in the large_increase variable
    large_increase = max(profit)

    #Creating an index for the location of which this max profit takes place
    large_index = profit.index(large_increase)

    #Using the index created to find the date for which this occurs within the data set
    large_date = months[large_index]

    #Same instance for the largest decrease in profits
    large_decrease = min(profit)
    decrease_index = profit.index(large_decrease)
    decrease_date = months[decrease_index]

    #finding the average of the change with the new values that were found from tracking the total
    #change of values
    #storing this value in variable average_change
    #we are using the sum and length function to perform this calculation
    average_change = sum(profit)/len(profit)

    #Printing the Analysis for the user
    #using a round function to round the average change to the nearest 2 decimal places
    print(f"Financial Analysis")
    print(f"-----------------------")
    print(f"Total Months: {(total_months)}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${str(round(average_change,2))}")
    print(f"Greatest Increase in Profits: {large_date} (${large_increase})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${large_decrease})")

#opening the output file with the newly summarized and formatted data
output_data = os.path.join("Analyzed_Data.csv")

with open(output_data, "w") as writer:

    #writing out to the data to the csv file
    writer.write(f"Financial Analysis")
    writer.write(f"\n----------------------------------")
    writer.write(f"\n")
    writer.write(f"Total Months: {total_months}")
    writer.write(f"\n\n")
    writer.write(f"Total: ${total_profit}")
    writer.write(f"\n\n")
    writer.write(f"Average Change: ${str(round(average_change,2))}")
    writer.write(f"\n\n")
    writer.write(f"Greatest Increase in Profits: {large_date} (${large_increase})")
    writer.write(f"\n\n")
    writer.write(f"Greatest Decrease in Profits: {decrease_date} (${large_decrease})")









