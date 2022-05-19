#!/usr/bin/python3.8
"""script getting id, company, and yearly
total compensation from csv pipe"""


import sys
#id      company,totalyearlycompensation

for x, line in enumerate(sys.stdin):
    data = line.replace("\n", "").split(",")

    if x == 0:
        id = data.index("id")
        company = data.index("company")
        tyc = data.index("totalyearlycompensation")

    print("{}\t{},{}".format(data[id], data[company], data[tyc]))
