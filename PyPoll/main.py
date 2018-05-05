# SECOND ELECTION!!!
# import modules
import os
import csv
import collections
# read data into counter to create candidate field
# set path for file
election_csv = os.path.join('..', 'Downloads', 'election_data_2.txt')
print("Election Results # 2: ")
print("-"*50)
candidates = collections.Counter()
voter_id_tot = 0
# open the cvs and loop through the votes
with open(election_csv, 'r') as count_file:
    csv_reader = csv.reader(count_file, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        candidates[row[2]] += 1
# total number of votes cast
voter_id_tot = sum(candidates.values())
print('Total Votes : {}'.format(voter_id_tot))
print("-"*50)
# the percentage each candidate received over the total number of votes cast
for candidate in candidates.keys():
    print('{}:  {:.1f}% ({})'.format(candidate,  float(candidates[candidate]) * 100.0 / voter_id_tot, candidates[candidate]))
# print(candidates.most_common())
print("-"*50)
print("Winner: {}".format(candidates.most_common(1)[0][0]))
print("-"*50)




# FIRST ELECTION!!! 
import os
import csv
import collections
# read data into counter to create candidate field
# set path for file
election_csv = os.path.join('..', 'Downloads', 'election_data_1 (1).txt')
print("Election Results # 1")
print("-"*50)
candidates = collections.Counter()
voter_id_tot = 0
# open the cvs and loop through the votes
with open(election_csv, 'r') as count_file:
    csv_reader = csv.reader(count_file, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        candidates[row[2]] += 1
# total number of votes cast
voter_id_tot = sum(candidates.values())
print('Total Votes : {}'.format(voter_id_tot))
print("-"*50)
# the percentage each candidate received over the total number of votes cast
for candidate in candidates.keys():
    print('{}:  {:.1f}% ({})'.format(candidate,  float(candidates[candidate]) * 100.0 / voter_id_tot, candidates[candidate]))
# print(candidates.most_common())
print("-"*50)
print("Winner: {}".format(candidates.most_common(1)[0][0]))
print("-"*50)









