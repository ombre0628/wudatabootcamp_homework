
### Heroes Of Pymoli Data Analysis
# Summary

* Male player is largest portion who make up 83.59% of the entire players. However, from Average Purchase Price and Average Purchase Total per Person", they spend less than other two groups.

* From Age Demographics, we can see age 20-24 is major group in this game. They make most value, but the players whose  age 35-39 spend more. 

* "Sticky Factor" shows audience loyalty to application. It's an important factor to evaluate how successful this games is. It comes from "Monthly Active Users (MAU)" and "Daily Active Users (DAU)". However, this data doesn't show those. It olny shows 35% of total players who shop more than once. 

* In the top 10 of "Most Popular Item" list, we can see 8 items's price are higher than average price($3.05), which means players are willing to buy high value items.   Also, from the data of Most Profitable Items, high priced item creates more profit than low priced items. 


-----

### Note
* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# Dependencies and Setup
import pandas as pd
import numpy as np



# Raw data file
file_to_load = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()

## Player Count

* Display the total number of players



total_player=len(purchase_data["SN"].unique())
            
play_count_df=pd.DataFrame({"Total Players":[total_player]})
                 
play_count_df
                 

## Purchasing Analysis (Total)

* Run basic calculations to obtain number of unique items, average price, etc.


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame



unique_item=purchase_data["Item ID"].nunique()


NumberofPurchases=len(purchase_data["Purchase ID"])

Average_Price1=purchase_data["Price"].mean()
Average_Price="${:.2f}".format(Average_Price1)


Total_Revenue1=purchase_data["Price"].sum()
Total_Revenue="${:.2f}".format(Total_Revenue1)


purchase_data_df=pd.DataFrame({"Number of Unique Items":[unique_item],'Average Price':[Average_Price], 'Number of Purchases':[NumberofPurchases],'Total Revenue':[Total_Revenue]})
purchase_data_df=purchase_data_df[['Number of Unique Items','Average Price','Number of Purchases','Total Revenue']]
purchase_data_df

## Repeat Purchasing Rate

Repeat_Purchasing =(NumberofPurchases-total_player)/total_player*100
Repeat_Purchasing_rate="{:.2f}%".format(Repeat_Purchasing)
Repeat_Purchasing_rate

## Gender Demographics

* Percentage and Count of Male Players


* Percentage and Count of Female Players


* Percentage and Count of Other / Non-Disclosed




playersGender=purchase_data["Gender"].unique()

Count_PlayersGender=purchase_data["Gender"].value_counts()

Count_PlayersGenderPercentage=Count_PlayersGender/NumberofPurchases*100
Count_PlayersGenderPercentage=Count_PlayersGenderPercentage.map('{:.2f}%'.format)

purchase_data_df=pd.DataFrame({"Percentage of Players":Count_PlayersGenderPercentage,"Total Count":Count_PlayersGender})
purchase_data_df



## Purchasing Analysis (Gender)

* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender




* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame

Total_Purchase_Value=purchase_data.groupby(["Gender"])["Price"].sum()
Total_Purchase_Value=Total_Purchase_Value.map('${:.2f}'.format)


AveragePurchase_Value=purchase_data.groupby(["Gender"])["Price"].mean()
AveragePurchase_Value=AveragePurchase_Value.map('${:.2f}'.format)

per_person=purchase_data.groupby(["Gender","SN"])["Price"].mean()
AveragePurchase_Value_per_person=per_person.groupby(["Gender"]).mean()
AveragePurchase_Value_per_person=AveragePurchase_Value_per_person.map('${:.2f}'.format)

Genderpurchase_data_df=pd.DataFrame({"Purchase Count":Count_PlayersGender,"Average Purchase Price":AveragePurchase_Value,"Total Purchase Value":Total_Purchase_Value,"Avg Purchase Total per Person":AveragePurchase_Value_per_person})
Genderpurchase_data_df=Genderpurchase_data_df[['Purchase Count','Average Purchase Price','Total Purchase Value','Avg Purchase Total per Person']]

Genderpurchase_data_df.head()

## Age Demographics

* Establish bins for ages


* Categorize the existing players using the age bins. Hint: use pd.cut()


* Calculate the numbers and percentages by age group


* Create a summary data frame to hold the results


* Optional: round the percentage column to two decimal points


* Display Age Demographics Table


# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
purchase_data['Age_range'] = pd.cut(purchase_data["Age"], age_bins, labels=group_names)

ageTotal_Count=purchase_data.groupby(['Age_range'])['Age'].count()


Percentage_of_Players=ageTotal_Count/NumberofPurchases*100
Percentage_of_Players=Percentage_of_Players.map('{:.2f}%'.format)

Age_Demographics_df=pd.DataFrame({'Percentage of Players':Percentage_of_Players,'Total Count':ageTotal_Count})
Age_Demographics_df.head(10)


## Purchasing Analysis (Age)

* Bin the purchase_data data frame by age


* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame

AgeTotal_Purchase_Value=purchase_data.groupby(['Age_range'])['Price'].sum()
AgeTotal_Purchase_Value=AgeTotal_Purchase_Value.map('${:.2f}'.format)
AgeAverage_Purchase_Price=purchase_data.groupby(['Age_range'])['Price'].mean()
AgeAverage_Purchase_Price=AgeAverage_Purchase_Price.map('${:.2f}'.format)

AgeAveragePurchaseTotalperPerson=purchase_data.groupby(['Age_range','SN'])['Price'].mean()

AgeAveragePurchaseTotalperPersonR=AgeAveragePurchaseTotalperPerson.groupby(['Age_range']).mean()
AgeAveragePurchaseTotalperPersonR=AgeAveragePurchaseTotalperPersonR.map('${:.2f}'.format)

Age_Purchasing_Analysis_df=pd.DataFrame({'Purchase Count':ageTotal_Count,'Average Purchase Price':AgeAverage_Purchase_Price,
                                         'Total Purchase Value':AgeTotal_Purchase_Value,
                                         'Average Purchase Total per Person':AgeAveragePurchaseTotalperPersonR})
Age_Purchasing_Analysis_df=Age_Purchasing_Analysis_df[['Purchase Count','Average Purchase Price','Total Purchase Value','Average Purchase Total per Person']]
Age_Purchasing_Analysis_df.head(10)

## Top Spenders

* Run basic calculations to obtain the results in the table below


* Create a summary data frame to hold the results


* Sort the total purchase value column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame



Top_Spenders_sum =purchase_data.groupby(['SN','Age'])['Price'].sum()



Top_Spenders_count =purchase_data.groupby(['SN','Age'])['Purchase ID'].count()



Top_Spenders_avg = purchase_data.groupby(['SN','Age'])['Price'].mean()
Top_Spenders_avg = Top_Spenders_avg.map('${:.2f}'.format)


Top_Spenders_df=pd.DataFrame({'Purchase Count':Top_Spenders_count,
                              'Average Purchase Price':Top_Spenders_avg,
                              'Total Purchase Value':Top_Spenders_sum})

Top_Spenders_df=Top_Spenders_df[['Purchase Count','Average Purchase Price','Total Purchase Value']]
Top_Spenders_df=Top_Spenders_df.sort_values(by=["Total Purchase Value"],ascending=False)


Top_Spenders_df.head(20)





## Most Popular Items

* Retrieve the Item ID, Item Name, and Item Price columns


* Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value


* Create a summary data frame to hold the results


* Sort the purchase count column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame



PopularItems_count =purchase_data.groupby(['Item ID', 'Item Name'])['Purchase ID'].count()

PopularItems_avg = purchase_data.groupby(['Item ID', 'Item Name'])['Price'].mean()
PopularItems_avg1 = PopularItems_avg.map('${:.2f}'.format)

PopularItems_sum = purchase_data.groupby(['Item ID', 'Item Name'])['Price'].sum()
PopularItems_sum1 = PopularItems_sum.map('${:.2f}'.format)





PopularItems_df1 = pd.DataFrame({'Purchase Count':PopularItems_count,
                              'Item Price':PopularItems_avg1,
                              'Total Purchase Value':PopularItems_sum1})

PopularItems_df1 = PopularItems_df1[['Purchase Count','Item Price','Total Purchase Value']]


PopularItems_df1 = PopularItems_df1.sort_values(by=['Purchase Count'],ascending=False)

PopularItems_df1.head(10)

## Most Profitable Items

* Sort the above table by total purchase value in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the data frame



PopularItems_df = pd.DataFrame({'Purchase Count':PopularItems_count,
                              'Item Price':PopularItems_avg,
                              'Total Purchase Value':PopularItems_sum})
PopularItems_df = PopularItems_df[['Purchase Count','Item Price','Total Purchase Value']]
Profitable_Items = PopularItems_df.sort_values(by=['Total Purchase Value'], ascending = False)


Profitable_Items .head(20)






    