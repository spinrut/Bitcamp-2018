import csv
import os

# user = 'MCPS_tweets.csv'
path = 'tweets'  # path to folder

for user in os.listdir('tweets'):
    with open(os.path.join('tweets/', user)) as fin:

        with open('data/outfile_closed(%r)' % user, 'w') as foutClose:
            with open('data/outfile_delay(%r)' % user, 'w') as foutDelay:
                writerC = csv.writer(foutClose, delimiter=' ')
                writerD = csv.writer(foutDelay, delimiter=' ')

                for row in csv.reader(fin, delimiter=','):
                    if 'MCPS' in user:
                        if 'emergency weather conditions' in row[2] and 'closed' in row[2]:
                            writerC.writerow([row[1]])
                        if 'delay' in row[2]:
                            writerD.writerow([row[1]])

                    if 'PGCPS' in user:
                        if 'schools are closed' in row[2] and 'closed' in row[2]:
                            writerC.writerow([row[1]])
                        if 'delay' in row[2]:
                            writerD.writerow([row[1]])

                    if 'Balt' in user:
                        if 'closed' in row[2]:
                            writerC.writerow([row[1]])
                        if 'delay' in row[2]:
                            writerD.writerow([row[1]])

