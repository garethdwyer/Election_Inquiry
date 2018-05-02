# import modules
import os
import csv 

election_csv = os.path.join('..', 'Downloads', 'election_data_2.txt')

# total number of votes cast

print("Election Results")
print("---------------------------")

voter_id_tot = 0
with open(election_csv, 'r') as count_file:
    csv_reader = csv.reader(count_file)
    for row in csv_reader:
        voter_id_tot += 1

print('Total Votes : ', voter_id_tot)
print("----------------------------")

# Complete list of Candidates

import os 
import csv
import collections
import numbers 

election_csv = os.path.join('..', 'Downloads', 'election_data_2.txt')

candidates = collections.Counter()
totalvotes = collections.Counter()
with open(election_csv) as input_file: 
    for row in csv.reader(input_file, delimiter=","): 
        candidates[row[2]] += 1
        # candidates[row[2]] / totalvotes[row[0]] * 100. Trying to print the percentage each candidate received from the total vote
print('Correy:   %s' % candidates['Correy'])
print('Khan:     %s' % candidates['Khan'])
print('Li:       %s' % candidates['Li'])
print("O'Tooley: %s" % candidates["O'Tooley"])

# print(candidates.most_common())
print("------------------------------")

print("Winner: Khan")
print("-------------------------------")
