import pdftables_api
import os


c = pdftables_api.Client('139wczn1gc0x')

file_path = "calendars"

for file in os.listdir(file_path):
    if file.endswith(".pdf"):
        c.xlsx(os.path.join(file_path, file), file + '.xlsx')