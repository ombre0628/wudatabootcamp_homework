

import os 
import csv
import numpy as np

csvpath=os.path.join('/Users/ombre0628/Desktop/python-challenge/PyBank/budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    csvheader=next(csvreader)
    #print(f"Header: {csvheader}")


    month=[]
    totalProfit=0
    Revenue=[]
    for row in csvreader:
        month.append(row[0])
        totalProfit=totalProfit+int(row[1])
        Revenue.append(int(row[1]))
    
    totalMonth= len(month) 

    previousMon=np.array(Revenue[0:40])
    nextMon=np.array(Revenue[1:41])
    change=nextMon-previousMon
    averageChange=np.sum(change)/40


    greatestInAmount= change.max()
    greatestInDate=month[int(list(change).index(greatestInAmount))+1]


    greatestDeAmount=change.min()
    greatestDeDate=month[int(list(change).index(greatestDeAmount))+1]


print('Financial Analysis\n' 
'-------------------------\n'
'Total Months: {0}\n'
'Total:$ {1}\n'
'Average  Change: ${2}\n'
'Greatest Increase in Profits:{3}(${4})\n'
'Greatest Decrease in Profits:{5}(${6})\n'
.format(totalMonth, 
        totalProfit, 
        averageChange,
        greatestInDate,
        greatestInAmount,
        greatestDeDate,
        greatestDeAmount,
        )

)  

output_path = os.path.join('/Users/ombre0628/Desktop/python-challenge/PyBank/', 'output_of_funtion.txt')
txtfile=open(output_path,'w')
txtfile.write(
'Financial Analysis\n' 
'-------------------------\n'
'Total Months: {0}\n'   
'Total:$ {1}\n'
'Average  Change: ${2}\n'
'Greatest Increase in Profits:{3}(${4})\n'
'Greatest Decrease in Profits:{5}(${6})\n'
.format(totalMonth, 
        totalProfit, 
        averageChange,
        greatestInDate,
        greatestInAmount,
        greatestDeDate,
        greatestDeAmount,
        )
        )
txtfile.close()

    
    



    

    
    


