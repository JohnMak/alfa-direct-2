import os
import test
import data

comingDataDir = 'coming data/'
proccesedDataDir = 'processed data/'
outputImagesDir = 'output images/'

files = os.listdir(comingDataDir)

for file in files:
    fileInName = comingDataDir + file
    print fileInName
    data.init(fileInName)

    #timeStart='20111003_103000'
    #timeEnd='20111202_183000'

    timeStart='20111003_103000'
    timeEnd='20120224_183000'


    max_dif=-1000
    fileToSave = proccesedDataDir + file[:-4] + '.csv'
    fo = open(fileToSave, 'w+')

    for i in range(1,201):
        for j in range(i+1,201):
            value = test.strat_reverse_calc(i, j, timeStart, timeEnd)
            fo.write(str(i)+','+str(j)+','+str(value)+'\n')
            max_dif=max(max_dif,value)
        print str(i)+','+str(j)+' = '+str(max_dif)
    fo.close()