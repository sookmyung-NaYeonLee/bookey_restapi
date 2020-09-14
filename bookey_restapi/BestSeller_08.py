import csv
import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookey_restapi.settings")
django.setup()

from api_book.models import *

CSV_PATH = './kyobo_08best.csv'

with open(CSV_PATH, newline='') as csvfile:  # 4. newline =''
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        BestSeller.objects.create(  # 5. class명.objects.create
            rank=row['RANK'],
            bid=Book.objects.get(bid=int(row['ISBN'])),
        )
