import csv
import random
import pandas as pd
import numpy as np
from numpy.random import choice

df = pd.read_csv('Cleansed_data.csv')
groupedcount = df.urban_or_rural_area.value_counts()
# ageDriver = df.age_of_driver
# groupedcount=ageDriver[(ageDriver>=0)& (ageDriver<=30)].count()
#df.groupby(df.sex_of_driver).count()
print(groupedcount)





def add_postal_codes_by_weight(values):
    df = pd.read_csv('Cleansed_data.csv')
    saved_column = df.longitude
    csvfile = 'Cleansed_data.csv'
    statelist = ["AB", "AL", "B", "BA", "BB", "BD", "BH", "BL", "BN", "BR", "BS", "BT", "CA", "CB", "CF", "CH", "CM", "CO",
                 "CR", "CT", "CV", "CW", "DA", "DD", "DE", "DG", "DH", "DL", "DN", "DT", "DY", "E", "EC", "EH", "EN", "EX",
                 "FK", "FY", "G", "GL", "GU", "HA", "HD", "HG", "HP", "HR", "HS", "HU", "HX", "IG", "IP", "IV", "KA", "KT",
                 "KW", "KY", "L", "LA", "LD", "LE", "LL", "LN", "LS", "LU", "M", "ME", "MK", "ML", "N", "NE", "NG", "NN",
                 "NP", "NR", "NW", "OL", "OX", "PA", "PE", "PH", "PL", "PO", "PR", "RG", "RH", "RM", "S", "SA", "SE", "SG",
                 "SK", "SL", "SM", "SN", "SO", "SP", "SR", "SS", "ST", "SW", "SY", "TA", "TD", "TF", "TN", "TQ", "TR", "TS",
                 "TW", "UB", "W", "WA", "WC", "WD", "WF", "WN", "WR", "WS", "WV", "YO"]

    weight = [random.random() for _ in range(0, 120)]
    s = sum(weight)
    weight = [ i/s for i in weight ]
    with open(csvfile, 'r') as fin, open('new_' + csvfile, 'w') as fout:
        reader = csv.reader(fin)
        writer = csv.writer(fout, lineterminator='\n')
        for row in reader:
            if row[7] == "longitude":
                writer.writerow(row + ["PostalCode"])
            #row.append(random.choice(statelist))
            row.append(choice(statelist,1, p=weight))
            writer.writerow(row)