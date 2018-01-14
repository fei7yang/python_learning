import csv,sys,codecs
with open( './broadcast2.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        #row_encoded =  row.unicode(row,"utf-8")
        row_strr = "".join(row)
        #row_unicode = row_strr.decode('utf-8')
        #row_gb = row_strr.encode('gb2312')
        #print type(row)
        #print type("".join(row))
        print'-'*20
        print row
f.close()
