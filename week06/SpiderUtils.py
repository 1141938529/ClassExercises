import csv


def printList(mlist):
    for item in mlist:
        print(item)

def writeCsvFile(filePath,iternator):
    with open(filePath,mode="w",newline="") as file:
        writer = csv.writer(file)
        for item in iternator:
            writer.writerow(item)
    pass