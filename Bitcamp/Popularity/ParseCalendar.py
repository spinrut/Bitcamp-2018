import csv
import os

# user = 'MCPS_tweets.csv'
path = 'calendars'  # path to folder

for files in os.listdir(path):
    if files.endswith(".csv"):
        with open(os.path.join('calendars/', files)) as fin:
            with open('data/outfile_calendar(%r)' % files, 'w') as foutClose:
                writer = csv.writer(foutClose, delimiter=' ')

                for row in csv.reader(fin, delimiter=','):
                    if 'MCPS' in files:
                        if 'closed' in row[1]:
                            writer.writerow([row[0]])

                    if 'BCPS' in files:
                        if 'Day' in row[0]:
                            writer.writerow([row[1]])
                            writer.writerow([row[3]])

                    if 'BCPS' in files:
                            writer.writerow([row[0]])

