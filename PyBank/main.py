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
            
            # Extract profit/loss value
            profit_loss = int(row[1])
            
            # Calculate net total amount
            net_profit_loss += profit_loss
            
            # Calculate change in profit/loss
            if total_months > 1:
                change = profit_loss - previous_profit_loss
                total_change += change


# Print summary results in to screen
print('Financial Analysis')

print('-------------------------')

# Print total number of months
print(f'Total Months: {total_months}')