import csv
import json

# Reading a CSV file:
#
with open("res/Cs205Final.csv") as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]

stocksDict = {}
for row in data:
    if row["Symbol"] == "GSPC":
        indexrow = row
for row in data:
    symbol = row["Symbol"]
    industry = row["Industry"]
    DPS = row["DPS"]
    DY = row["DY"]
    r1 = float(row["1"])
    r2 = float(row["2"])
    r3 = float(row["3"])
    r4 = float(row["4"])
    r5 = float(row["5"])
    r6 = float(row["6"])
    r7 = float(row["7"])
    r8 = float(row["8"])
    r9 = float(row["9"])
    r10 = float(row["10"])
    r11 = float(row["11"])
    r12 = float(row["12"])
    r13 = float(row["13"])
    r14 = float(row["14"])
    r15 = float(row["15"])
    r16 = float(row["16"])
    r17 = float(row["17"])
    r18 = float(row["18"])
    r19 = float(row["19"])
    r20 = float(row["20"])
    r21 = float(row["21"])
    r22 = float(row["22"])
    r23 = float(row["23"])
    r24 = float(row["24"])
    average1 = (r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12)/12
    average2 = (r13+r14+r15+r16+r17+r18+r19+r20+r21+r22+r23+r24)/12
    row["average1"] = average1
    row["average2"] = average2
    if symbol not in stocksDict:
        stocksDict[symbol] = {
        "totalreturn1" : 0,
        "totalreturn2" : 0
        }
    stocksDict[symbol]["industry"] = industry
    stocksDict[symbol]["DPS"] = DPS
    stocksDict[symbol]["DY"] = DY
    stocksDict[symbol]["totalreturn1"] = (r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12)
    stocksDict[symbol]["avgreturn1"] = stocksDict[symbol]["totalreturn1"]/12
    stocksDict[symbol]["annualreturn1"] = stocksDict[symbol]["avgreturn1"]*12
    stocksDict[symbol]["totalreturn2"] = (r13+r14+r15+r16+r17+r18+r19+r20+r21+r22+r23+r24)
    stocksDict[symbol]["avgreturn2"] = stocksDict[symbol]["totalreturn2"]/12
    stocksDict[symbol]["annualreturn2"] = stocksDict[symbol]["avgreturn2"]*12

    stocksDict[symbol]["sqdiff1"] = (r1-average1)**2+(r2-average1)**2+(r3-average1)**2+(r4-average1)**2+(r5-average1)**2+(r6-average1)**2+\
    (r7-average1)**2+(r8-average1)**2+(r9-average1)**2+(r10-average1)**2+(r11-average1)**2+(r12-average1)**2
    stocksDict[symbol]["sqdiff2"] = (r13-average2)**2+(r14-average2)**2+(r15-average2)**2+(r16-average2)**2+(r17-average2)**2+(r18-average2)**2+\
    (r19-average2)**2+(r20-average2)**2+(r21-average2)**2+(r22-average2)**2+(r23-average2)**2+(r24-average2)**2
    stocksDict[symbol]["stdreturn1"] = (stocksDict[symbol]["sqdiff1"]/11)**.5
    stocksDict[symbol]["stdreturn2"] = (stocksDict[symbol]["sqdiff2"]/11)**.5
    i1 = float(indexrow["1"])
    i2 = float(indexrow["2"])
    i3 = float(indexrow["3"])
    i4 = float(indexrow["4"])
    i5 = float(indexrow["5"])
    i6 = float(indexrow["6"])
    i7 = float(indexrow["7"])
    i8 = float(indexrow["8"])
    i9 = float(indexrow["9"])
    i10 = float(indexrow["10"])
    i11 = float(indexrow["11"])
    i12 = float(indexrow["12"])
    i13 = float(indexrow["13"])
    i14 = float(indexrow["14"])
    i15 = float(indexrow["15"])
    i16 = float(indexrow["16"])
    i17 = float(indexrow["17"])
    i18 = float(indexrow["18"])
    i19 = float(indexrow["19"])
    i20 = float(indexrow["20"])
    i21 = float(indexrow["21"])
    i22 = float(indexrow["22"])
    i23 = float(indexrow["23"])
    i24 = float(indexrow["24"])
    stocksDict[symbol]["sumxy1"] =  (r1*i1+r2*i2+r3*i3+r4*i4+r5*i5+r6*i6+r7*i7+\
    r8*i8+r9*i9+r10*i10+r11*i11+r12*i12)
    stocksDict[symbol]["sumxy2"] = (r13*i13+r14*i14+r15*i15+\
    r16*i16+r17*i17+r18*i18+r19*i19+r20*i20+r21*i21+r22*i22+r23*i23+r24*i24)
    stocksDict[symbol]["(xbar*ybar*n)1"] = stocksDict["GSPC"]["avgreturn1"] * stocksDict[symbol]["avgreturn1"] * 12
    stocksDict[symbol]["(xbar*ybar*n)2"] = stocksDict["GSPC"]["avgreturn2"] * stocksDict[symbol]["avgreturn2"] * 12
    stocksDict[symbol]["covariance1"] = (stocksDict[symbol]["sumxy1"] - stocksDict[symbol]["(xbar*ybar*n)1"])/11
    stocksDict[symbol]["covariance2"] = (stocksDict[symbol]["sumxy2"] - stocksDict[symbol]["(xbar*ybar*n)2"])/11
    stocksDict[symbol]["r1"] = stocksDict[symbol]["covariance1"]/(stocksDict["GSPC"]["stdreturn1"]*stocksDict[symbol]["stdreturn1"])
    stocksDict[symbol]["r2"] = stocksDict[symbol]["covariance2"]/(stocksDict["GSPC"]["stdreturn2"]*stocksDict[symbol]["stdreturn2"])
    stocksDict[symbol]["beta1"] = stocksDict[symbol]["r1"] * stocksDict["GSPC"]["stdreturn1"] / stocksDict[symbol]["stdreturn1"]
    stocksDict[symbol]["beta2"] = stocksDict[symbol]["r2"] * stocksDict["GSPC"]["stdreturn2"] / stocksDict[symbol]["stdreturn2"]

stocksList = []

for symbol in stocksDict:
    annualreturn1 = stocksDict[symbol]["annualreturn1"]
    annualreturn2 = stocksDict[symbol]["annualreturn2"]
    avgreturn1 = stocksDict[symbol]["avgreturn1"]
    avgreturn2 = stocksDict[symbol]["avgreturn2"]
    stdreturn1 = stocksDict[symbol]["stdreturn1"]
    stdreturn2 = stocksDict[symbol]["stdreturn2"]
    beta1 = stocksDict[symbol]["beta1"]
    beta2 = stocksDict[symbol]["beta2"]
    industry = stocksDict[symbol]["industry"]
    DPS = stocksDict[symbol]["DPS"]
    DY = stocksDict[symbol]["DY"]
    stocksList.append({"symbol":symbol,"annualreturn1":annualreturn1,"annualreturn2":annualreturn2,"avg1":avgreturn1,\
    "avg2":avgreturn2,"stdev1":stdreturn1,"stdev2":stdreturn2,"beta1":beta1,"beta2":beta2,"industry":industry,\
    "DPS":DPS,"DY":DY})

# Writing to a JSON file:
#
with open("res/stocks2.json", "w") as f:
    outdata = json.dumps(stocksList, indent=2)
    f.write(outdata)
