import random
import subprocess
import sys

import json

import time

allDivinations = []

i = 0
while i < int(sys.argv[1]):
    p = subprocess.Popen(['th sample.lua productNames/lm_lstm_epoch50.00_1.3150.t7 -seed ' + str(random.randint(100,1000)) + ' > names_tmp.txt'], shell=True)
    status = p.wait()
    print(status)
    
    p = subprocess.Popen(['th sample.lua prices/lm_lstm_epoch50.00_1.2193.t7 -seed ' + str(random.randint(100,1000)) + ' > prices_tmp.txt'], shell=True)
    status = p.wait()
    print(status)

    subprocess.Popen(['th sample.lua reviews/lm_lstm_epoch2.28_1.1002.t7 -seed ' + str(random.randint(1,1000)) +  ' > reviews_tmp.txt'], shell=True)
    status = p.wait()
    print(status)
    time.sleep(10)
    chosenImage = (random.randint(0,41), random.randint(0,9), random.randint(0,9))

    chosenNames = []
    chosenPrices = []
    chosenReviews = []

    


    with open('names_tmp.txt', 'r') as names:
        for count, line in enumerate(names):
            chosenNames.append(line)

    with open('prices_tmp.txt', 'r') as prices:
        for count, line in enumerate(prices):
            if count > 5:
                chosenPrices.append(line)

    with open('reviews_tmp.txt', 'r') as reviews:
        lastLine = 'bb'
        startedReview = False
        currentReview = ''
        for line in reviews:
            if line == '\n' and startedReview:
                currentReview += line
                chosenReviews.append(currentReview)
                currentReview = ''
                startedReview = False
            if lastLine == '\n':
                startedReview = True
                currentReview += '<h2>' + line + '</h2><br />'
                lastLine = line
            elif startedReview:
                if 'By' in line:
                    currentReview += '<br /><b>' + line + '</b><br />'
                    lastLine = line
                else:
                    currentReview += line
                    lastLine = line
            else:
                lastLine = line
    if len(chosenReviews) == 0:
        print("no review! skipping!")
        continue
    finalName = chosenNames[random.randint(0,len(chosenNames)-1)].strip()
    finalPrice = chosenPrices[random.randint(0,len(chosenPrices)-1)]
    if len(chosenReviews) < 2:
    	finalReview = chosenReviews[0]
    else:
    	finalReview = chosenReviews[random.randint(0,len(chosenReviews)-1)]
    finalImage = ("/images/spirits/%i_%i_%i.jpg" % chosenImage)

    divination = {'productName': finalName, 'price': finalPrice,
                  'finalReview': finalReview, 'finalImage': finalImage}
    allDivinations.append(divination)
    i += 1

with open('divinations.json', 'w') as final:
    json.dump(allDivinations, final)
