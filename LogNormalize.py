import pandas as pd
import numpy as np
import argparse
import gp
def GCTDataFrame(pathToGCF):
    df = pd.read_csv(pathToGCF, sep='\t',skiprows=2)
    for index, row in df.iterrows():
        for i in range (len(row)):
            if type(row[i]) == float:
                if row[i] >= 0:
                    row[i] = round(np.log(row[i]),3)
                else:
                    row[i] = 0
        df.iloc[index] = row
    return df
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str,
                    help="input file path")
parser.add_argument("-o", "--output",
                    help="output file path")
args = parser.parse_args()
pathtoGCF = args.input
outfile = args.output
f = open(pathtoGCF, 'r')
lines = f.readlines()
header = lines[0:2]
normalizedDF = GCTDataFrame(pathtoGCF)
normalizedDF.to_csv(outfile, sep = '\t', index = False)
out = open(outfile, 'r')
info = out.read()
out.close()
out = open(outfile, 'w')
out.write(header[0])
out.write(header[1])
out.write(info)
out.close()