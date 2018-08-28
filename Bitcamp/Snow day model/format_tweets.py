import numpy as np

file_names_1 = ['closed_', 'delay_']
file_names_2 = ['BaltCoPS', 'MCPS', 'PGCPS']

for f2 in file_names_2:
    for f1 in file_names_1:
        with open('Data_Files/' + f1 + f2 + '_tweets.csv', 'r') as f, open('data/' + f1 + f2 + '.csv', 'w') as out:
            for i in f.readlines():
                if i[0] == '"':
                    out.write(i[1:-2])
                    out.write('\n')
print('Done')
