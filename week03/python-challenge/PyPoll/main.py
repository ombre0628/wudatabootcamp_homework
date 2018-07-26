import numpy as np
import os 
import csv

csvpath=os.path.join('/Users/ombre0628/Desktop/python-challenge/PyPoll/Resources/election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    csvheader=next(csvreader)
    # print(f"Header: {csvheader}")

    votecast=[]
    candidateslist=[]

    for row in csvreader:
        votecast.append(row[0])
        candidateslist.append(row[2])


totalvote = len(votecast)

candidatesName=set(candidateslist)
candidate_list=list(candidatesName)

    
result = {}
for name in candidate_list:

    count = candidateslist.count(name)
    percentage = count/totalvote
    result[name] = [count, percentage]

key_max = max(result.keys(), key=(lambda k: result[k]))


#print(key_max)
#print(result)

print('Election Results\n' 
'-------------------------\n'
'Total Votes: {0}\n'
'-------------------------\n'
'{1}: {2:.3f}%({3})\n'
'{4}: {5:.3f}%({6})\n'
'{7}: {8:.3f}%({9})\n'
'{10}: {11:.3f}%({12})\n'
'-------------------------\n'
'Winner: {13}\n'
'-------------------------\n'
.format(totalvote, 
        candidate_list[0], 
        result[candidate_list[0]][1]*100,
        result[candidate_list[0]][0],
        candidate_list[1], 
        result[candidate_list[1]][1]*100,
        result[candidate_list[1]][0],
        candidate_list[2], 
        result[candidate_list[2]][1]*100,
        result[candidate_list[2]][0],
        candidate_list[3], 
        result[candidate_list[3]][1]*100,
        result[candidate_list[3]][0],
        key_max,

        )

)  

output_path = os.path.join('/Users/ombre0628/Desktop/python-challenge/PyPoll/', 'output_of_funtion.txt')
txtfile=open(output_path,'w')
txtfile.write(
'Election Results\n' 
'-------------------------\n'
'Total Votes: {0}\n'
'-------------------------\n'
'{1}: {2:.3f}%({3})\n'
'{4}: {5:.3f}%({6})\n'
'{7}: {8:.3f}%({9})\n'
'{10}: {11:.3f}%({12})\n'
'-------------------------\n'
'Winner: {13}\n'
'-------------------------\n'
.format(totalvote, 
        candidate_list[0], 
        result[candidate_list[0]][1]*100,
        result[candidate_list[0]][0],
        candidate_list[1], 
        result[candidate_list[1]][1]*100,
        result[candidate_list[1]][0],
        candidate_list[2], 
        result[candidate_list[2]][1]*100,
        result[candidate_list[2]][0],
        candidate_list[3], 
        result[candidate_list[3]][1]*100,
        result[candidate_list[3]][0],
        key_max,

        ) 
)
txtfile.close()
    
   
       



