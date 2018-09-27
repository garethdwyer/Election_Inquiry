import os
import csv
import collections

class Election():
    def __init__(self, data, number):
        self.data = data
        self.number = number
    def analysis(self):
        election_csv = os.path.join(self.data)
        candidates = collections.Counter()
        total_votes = 0
        with open(election_csv, 'r') as count_file:
            csv_reader = csv.reader(count_file, delimiter=",")
            next(csv_reader)
            for row in csv_reader:
                candidates[row[2]] += 1
        total_votes = sum(candidates.values())
        print("Election Results #" + str(self.number))
        print("-"*50)
        print('Total Votes : {}'.format(total_votes))
        print("-"*50)
        for candidate in candidates.keys():
            print('{}:  {:.1f}% ({})'.format(candidate,  float(candidates[candidate]) * 100.0 / total_votes, candidates[candidate]))
        print("-"*50)
        print("Winner: {}".format(candidates.most_common(1)[0][0]))
        print("*"*50)

#########################################################################################

e1 = Election("election_data_1.csv", 1)
e2 = Election("election_data_2.csv", 2)

e1.analysis()
e2.analysis()

















