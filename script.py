
import os
import time

# Retrieving product and version details from user

fileHandler = open ("services.txt", "r")
while True:
    # Get next line from file
    line2 = fileHandler.readline()
    # If line is empty then end of file reached
    if not line2 :
        break;
        print(line2.strip())
    b = line2.split(' - ')
    #Splitting into products and versions
    c = [e for e in b]
    try:
        product, version = c
	
    except:
        LineAllGood = False # don't do the next step.
        print "error in this"
	
# Calling cvedetails-lookup file
    #print "python3 cvedetails-lookup.py --product ",product," --version ",version
    os.system("python3 cvedetails-lookup.py --product "+product+" --version "+version)
        

