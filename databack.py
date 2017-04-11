import os
import sys
import shutil
import datetime


file = "/MedicAid.sqlite3"
today = str(datetime.date.today())
lastmonth = str(datetime.date.today() - datetime.timedelta(days=30)
)
dbdir = os.getcwd()
dbsrc = dbdir + file
dbdest = dbdir + "/databack/"+ file + today

shutil.copy2(dbsrc,dbdest)
try:
    os.remove(dbdir+"databack/"+ file + lastmonth)
except:
    print"nothing removed"
