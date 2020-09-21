import csv
import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookey_restapi.settings")
django.setup()

from api_result.models import *
from api_book.models import *

CSV_PATH = './result_best2.csv' #Result 파일 수정하

with open(CSV_PATH, newline='') as csvfile:  # 4. newline =''
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        Result.objects.create(  # 5. class명.objects.create
            good=row['good'],
            bid=Book.objects.get(bid=int(float(row['ISBN']))),
        )
