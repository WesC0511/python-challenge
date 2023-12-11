#Import
import os
import csv

#Define 
months = []
pl_changes = []

count_months = 0
net_pl = 0
prior_pl = 0
current_pl = 0
pl_change = 0

#Change directory
os.chdir(os.path.dirname(__file__))

#Path
budget_data_csv_path = os.path.join("budget_data.csv")

#Open and Read csv
with open(budget_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csv_reader:
        count_months += 1


        current_pl = int(row[1])
        net_pl += current_pl

        if (count_months == 1):
            prior_pl = current_pl
            continue

        else:
            pl_change = current_pl - prior_pl

            months.append(row[0])

            pl_changes.append(pl_change)

            prior_pl = current_pl
#Find and Calculate data
    sum_profit_loss = sum(pl_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    highest_change = max(pl_changes)
    lowest_change = min(pl_changes)

    highest_month_index = pl_changes.index(highest_change)
    lowest_month_index = pl_changes.index(lowest_change)

    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

#Print
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_pl}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")

#Export File
budget_file = os.path.join("budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count_months}\n")
    outfile.write(f"Total:  ${net_pl}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")