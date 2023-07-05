import csv
import os

# Path to collect data from the Resources folder
py_bank_data_csv = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
net_profit_loss = 0
previous_profit_loss = 0
total_change = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 9999999999999999999
greatest_decrease_date = ""
total_profit_loss = 0

# Read in the CSV file
with open(py_bank_data_csv, 'r') as csvfile:
        
        # Split the data on commas
        csv_reader = csv.reader(csvfile, delimiter=',')

        # Read the header row first (skip this step if there is no header)
        csv_header = next(csv_reader)

        # Iterate through the remaining rows
        for row in csv_reader:

            # Increment total number of months
            total_months += 1
            # Obtain profit/loss value
            profit_loss = int(row[1])

            # Calculate net total amount
            net_profit_loss += profit_loss

            # Calculate change in profit/loss
            if total_months > 1:
                change = profit_loss - previous_profit_loss
                total_profit_loss += change

                # Check for greatest increase with date
                if change > greatest_increase:
                    greatest_increase = change
                    greatest_increase_date = row[0]

                # Check for greatest decrease with date
                if change < greatest_decrease:
                    greatest_decrease = change
                    greatest_decrease_date = row[0]

            # Update previous profit/loss
            previous_profit_loss = profit_loss

# Calculate average change
average_change = total_profit_loss / (total_months - 1)

# Print results
print('Financial Analysis')
print('-------------------------')
print(f'Total Months: {total_months}')
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${round(average_change,2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Write results to a text file
output_file = "financial_analysis.txt"
with open(output_file, 'w') as file:
    
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_profit_loss}\n")
    file.write(f"Average Change: ${round(average_change,2)}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print("Results exported to financial_analysis.txt.")