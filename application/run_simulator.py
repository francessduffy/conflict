from redis import Redis
from pandas import DataFrame
import rq


def simulator():
    sims = 5
    print('Initiating Simulations...')
    subqueue = rq.Queue('simulator', connection=Redis.from_url('redis://ec2-54-146-142-160.compute-1.amazonaws.com:6379'), default_timeout=400)
    job = subqueue.enqueue('application.tasks.simulator_instance')
    finished = False
    while finished == False:
        finished = job.is_finished
    modelresults = job.result

    i = 1
    print(int((i / sims) * 100), '% complete')

    strength1 = modelresults[0][0]
    notorietyratio1 = modelresults[0][1]
    totalextort1 = modelresults[0][2]
    countextort1 = modelresults[0][3]
    countbenefit1 = modelresults[0][4]
    countpunish1 = modelresults[0][5]
    countsupport1 = modelresults[0][6]
    totalsupport1 = modelresults[0][7]
    countdefend1 = modelresults[0][8]
    strength2 = modelresults[1][0]
    notorietyratio2 = modelresults[1][1]
    totalextort2 = modelresults[1][2]
    countextort2 = modelresults[1][3]
    countbenefit2 = modelresults[1][4]
    countpunish2 = modelresults[1][5]
    countsupport2 = modelresults[1][6]
    totalsupport2 = modelresults[1][7]
    countdefend2 = modelresults[1][8]
    strength3 = modelresults[2][0]
    notorietyratio3 = modelresults[2][1]
    totalextort3 = modelresults[2][2]
    countextort3 = modelresults[2][3]
    countbenefit3 = modelresults[2][4]
    countpunish3 = modelresults[2][5]
    countsupport3 = modelresults[2][6]
    totalsupport3 = modelresults[2][7]
    countdefend3 = modelresults[2][8]
    strength4 = modelresults[3][0]
    notorietyratio4 = modelresults[3][1]
    totalextort4 = modelresults[3][2]
    countextort4 = modelresults[3][3]
    countbenefit4 = modelresults[3][4]
    countpunish4 = modelresults[3][5]
    countsupport4 = modelresults[3][6]
    totalsupport4 = modelresults[3][7]
    countdefend4 = modelresults[3][8]
    strength5 = modelresults[4][0]
    notorietyratio5 = modelresults[4][1]
    totalextort5 = modelresults[4][2]
    countextort5 = modelresults[4][3]
    countbenefit5 = modelresults[4][4]
    countpunish5 = modelresults[4][5]
    countsupport5 = modelresults[4][6]
    totalsupport5 = modelresults[4][7]
    countdefend5 = modelresults[4][8]
    strength6 = modelresults[5][0]
    notorietyratio6 = modelresults[5][1]
    totalextort6 = modelresults[5][2]
    countextort6 = modelresults[5][3]
    countbenefit6 = modelresults[5][4]
    countpunish6 = modelresults[5][5]
    countsupport6 = modelresults[5][6]
    totalsupport6 = modelresults[5][7]
    countdefend6 = modelresults[5][8]
    strength7 = modelresults[6][0]
    notorietyratio7 = modelresults[6][1]
    totalextort7 = modelresults[6][2]
    countextort7 = modelresults[6][3]
    countbenefit7 = modelresults[6][4]
    countpunish7 = modelresults[6][5]
    countsupport7 = modelresults[6][6]
    totalsupport7 = modelresults[6][7]
    countdefend7 = modelresults[6][8]
    strength8 = modelresults[7][0]
    notorietyratio8 = modelresults[7][1]
    totalextort8 = modelresults[7][2]
    countextort8 = modelresults[7][3]
    countbenefit8 = modelresults[7][4]
    countpunish8 = modelresults[7][5]
    countsupport8 = modelresults[7][6]
    totalsupport8 = modelresults[7][7]
    countdefend8 = modelresults[7][8]
    strength9 = modelresults[8][0]
    notorietyratio9 = modelresults[8][1]
    totalextort9 = modelresults[8][2]
    countextort9 = modelresults[8][3]
    countbenefit9 = modelresults[8][4]
    countpunish9 = modelresults[8][5]
    countsupport9 = modelresults[8][6]
    totalsupport9 = modelresults[8][7]
    countdefend9 = modelresults[8][8]
    strength10 = modelresults[9][0]
    notorietyratio10 = modelresults[9][1]
    totalextort10 = modelresults[9][2]
    countextort10 = modelresults[9][3]
    countbenefit10 = modelresults[9][4]
    countpunish10 = modelresults[9][5]
    countsupport10 = modelresults[9][6]
    totalsupport10 = modelresults[9][7]
    countdefend10 = modelresults[9][8]
    strength11 = modelresults[10][0]
    notorietyratio11 = modelresults[10][1]
    totalextort11 = modelresults[10][2]
    countextort11 = modelresults[10][3]
    countbenefit11 = modelresults[10][4]
    countpunish11 = modelresults[10][5]
    countsupport11 = modelresults[10][6]
    totalsupport11 = modelresults[10][7]
    countdefend11 = modelresults[10][8]
    strength12 = modelresults[11][0]
    notorietyratio12 = modelresults[11][1]
    totalextort12 = modelresults[11][2]
    countextort12 = modelresults[11][3]
    countbenefit12 = modelresults[11][4]
    countpunish12 = modelresults[11][5]
    countsupport12 = modelresults[11][6]
    totalsupport12 = modelresults[11][7]
    countdefend12 = modelresults[11][8]
    strength13 = modelresults[12][0]
    notorietyratio13 = modelresults[12][1]
    totalextort13 = modelresults[12][2]
    countextort13 = modelresults[12][3]
    countbenefit13 = modelresults[12][4]
    countpunish13 = modelresults[12][5]
    countsupport13 = modelresults[12][6]
    totalsupport13 = modelresults[12][7]
    countdefend13 = modelresults[12][8]
    strength14 = modelresults[13][0]
    notorietyratio14 = modelresults[13][1]
    totalextort14 = modelresults[13][2]
    countextort14 = modelresults[13][3]
    countbenefit14 = modelresults[13][4]
    countpunish14 = modelresults[13][5]
    countsupport14 = modelresults[13][6]
    totalsupport14 = modelresults[13][7]
    countdefend14 = modelresults[13][8]
    strength15 = modelresults[14][0]
    notorietyratio15 = modelresults[14][1]
    totalextort15 = modelresults[14][2]
    countextort15 = modelresults[14][3]
    countbenefit15 = modelresults[14][4]
    countpunish15 = modelresults[14][5]
    countsupport15 = modelresults[14][6]
    totalsupport15 = modelresults[14][7]
    countdefend15 = modelresults[14][8]
    community1m1 = modelresults[15][0]
    community2m1 = modelresults[15][1]
    community3m1 = modelresults[15][2]
    community4m1 = modelresults[15][3]
    community5m1 = modelresults[15][4]
    community6m1 = modelresults[15][5]
    community7m1 = modelresults[15][6]
    community8m1 = modelresults[15][7]
    community9m1 = modelresults[15][8]
    community10m1 = modelresults[15][9]
    community11m1 = modelresults[15][10]
    community12m1 = modelresults[15][11]
    community13m1 = modelresults[15][12]
    community14m1 = modelresults[15][13]
    community15m1 = modelresults[15][14]
    community1m2 = modelresults[16][0]
    community2m2 = modelresults[16][1]
    community3m2 = modelresults[16][2]
    community4m2 = modelresults[16][3]
    community5m2 = modelresults[16][4]
    community6m2 = modelresults[16][5]
    community7m2 = modelresults[16][6]
    community8m2 = modelresults[16][7]
    community9m2 = modelresults[16][8]
    community10m2 = modelresults[16][9]
    community11m2 = modelresults[16][10]
    community12m2 = modelresults[16][11]
    community13m2 = modelresults[16][12]
    community14m2 = modelresults[16][13]
    community15m2 = modelresults[16][14]
    community1m3 = modelresults[17][0]
    community2m3 = modelresults[17][1]
    community3m3 = modelresults[17][2]
    community4m3 = modelresults[17][3]
    community5m3 = modelresults[17][4]
    community6m3 = modelresults[17][5]
    community7m3 = modelresults[17][6]
    community8m3 = modelresults[17][7]
    community9m3 = modelresults[17][8]
    community10m3 = modelresults[17][9]
    community11m3 = modelresults[17][10]
    community12m3 = modelresults[17][11]
    community13m3 = modelresults[17][12]
    community14m3 = modelresults[17][13]
    community15m3 = modelresults[17][14]
    community1m4 = modelresults[18][0]
    community2m4 = modelresults[18][1]
    community3m4 = modelresults[18][2]
    community4m4 = modelresults[18][3]
    community5m4 = modelresults[18][4]
    community6m4 = modelresults[18][5]
    community7m4 = modelresults[18][6]
    community8m4 = modelresults[18][7]
    community9m4 = modelresults[18][8]
    community10m4 = modelresults[18][9]
    community11m4 = modelresults[18][10]
    community12m4 = modelresults[18][11]
    community13m4 = modelresults[18][12]
    community14m4 = modelresults[18][13]
    community15m4 = modelresults[18][14]
    community1m5 = modelresults[19][0]
    community2m5 = modelresults[19][1]
    community3m5 = modelresults[19][2]
    community4m5 = modelresults[19][3]
    community5m5 = modelresults[19][4]
    community6m5 = modelresults[19][5]
    community7m5 = modelresults[19][6]
    community8m5 = modelresults[19][7]
    community9m5 = modelresults[19][8]
    community10m5 = modelresults[19][9]
    community11m5 = modelresults[19][10]
    community12m5 = modelresults[19][11]
    community13m5 = modelresults[19][12]
    community14m5 = modelresults[19][13]
    community15m5 = modelresults[19][14]
    community1m6 = modelresults[20][0]
    community2m6 = modelresults[20][1]
    community3m6 = modelresults[20][2]
    community4m6 = modelresults[20][3]
    community5m6 = modelresults[20][4]
    community6m6 = modelresults[20][5]
    community7m6 = modelresults[20][6]
    community8m6 = modelresults[20][7]
    community9m6 = modelresults[20][8]
    community10m6 = modelresults[20][9]
    community11m6 = modelresults[20][10]
    community12m6 = modelresults[20][11]
    community13m6 = modelresults[20][12]
    community14m6 = modelresults[20][13]
    community15m6 = modelresults[20][14]
    community1m7 = modelresults[21][0]
    community2m7 = modelresults[21][1]
    community3m7 = modelresults[21][2]
    community4m7 = modelresults[21][3]
    community5m7 = modelresults[21][4]
    community6m7 = modelresults[21][5]
    community7m7 = modelresults[21][6]
    community8m7 = modelresults[21][7]
    community9m7 = modelresults[21][8]
    community10m7 = modelresults[21][9]
    community11m7 = modelresults[21][10]
    community12m7 = modelresults[21][11]
    community13m7 = modelresults[21][12]
    community14m7 = modelresults[21][13]
    community15m7 = modelresults[21][14]
    community1m8 = modelresults[22][0]
    community2m8 = modelresults[22][1]
    community3m8 = modelresults[22][2]
    community4m8 = modelresults[22][3]
    community5m8 = modelresults[22][4]
    community6m8 = modelresults[22][5]
    community7m8 = modelresults[22][6]
    community8m8 = modelresults[22][7]
    community9m8 = modelresults[22][8]
    community10m8 = modelresults[22][9]
    community11m8 = modelresults[22][10]
    community12m8 = modelresults[22][11]
    community13m8 = modelresults[22][12]
    community14m8 = modelresults[22][13]
    community15m8 = modelresults[22][14]
    community1m9 = modelresults[23][0]
    community2m9 = modelresults[23][1]
    community3m9 = modelresults[23][2]
    community4m9 = modelresults[23][3]
    community5m9 = modelresults[23][4]
    community6m9 = modelresults[23][5]
    community7m9 = modelresults[23][6]
    community8m9 = modelresults[23][7]
    community9m9 = modelresults[23][8]
    community10m9 = modelresults[23][9]
    community11m9 = modelresults[23][10]
    community12m9 = modelresults[23][11]
    community13m9 = modelresults[23][12]
    community14m9 = modelresults[23][13]
    community15m9 = modelresults[23][14]
    community1m10 = modelresults[24][0]
    community2m10 = modelresults[24][1]
    community3m10 = modelresults[24][2]
    community4m10 = modelresults[24][3]
    community5m10 = modelresults[24][4]
    community6m10 = modelresults[24][5]
    community7m10 = modelresults[24][6]
    community8m10 = modelresults[24][7]
    community9m10 = modelresults[24][8]
    community10m10 = modelresults[24][9]
    community11m10 = modelresults[24][10]
    community12m10 = modelresults[24][11]
    community13m10 = modelresults[24][12]
    community14m10 = modelresults[24][13]
    community15m10 = modelresults[24][14]
    community1m11 = modelresults[25][0]
    community2m11 = modelresults[25][1]
    community3m11 = modelresults[25][2]
    community4m11 = modelresults[25][3]
    community5m11 = modelresults[25][4]
    community6m11 = modelresults[25][5]
    community7m11 = modelresults[25][6]
    community8m11 = modelresults[25][7]
    community9m11 = modelresults[25][8]
    community10m11 = modelresults[25][9]
    community11m11 = modelresults[25][10]
    community12m11 = modelresults[25][11]
    community13m11 = modelresults[25][12]
    community14m11 = modelresults[25][13]
    community15m11 = modelresults[25][14]
    community1m12 = modelresults[26][0]
    community2m12 = modelresults[26][1]
    community3m12 = modelresults[26][2]
    community4m12 = modelresults[26][3]
    community5m12 = modelresults[26][4]
    community6m12 = modelresults[26][5]
    community7m12 = modelresults[26][6]
    community8m12 = modelresults[26][7]
    community9m12 = modelresults[26][8]
    community10m12 = modelresults[26][9]
    community11m12 = modelresults[26][10]
    community12m12 = modelresults[26][11]
    community13m12 = modelresults[26][12]
    community14m12 = modelresults[26][13]
    community15m12 = modelresults[26][14]
    community1m13 = modelresults[27][0]
    community2m13 = modelresults[27][1]
    community3m13 = modelresults[27][2]
    community4m13 = modelresults[27][3]
    community5m13 = modelresults[27][4]
    community6m13 = modelresults[27][5]
    community7m13 = modelresults[27][6]
    community8m13 = modelresults[27][7]
    community9m13 = modelresults[27][8]
    community10m13 = modelresults[27][9]
    community11m13 = modelresults[27][10]
    community12m13 = modelresults[27][11]
    community13m13 = modelresults[27][12]
    community14m13 = modelresults[27][13]
    community15m13 = modelresults[27][14]
    community1m14 = modelresults[28][0]
    community2m14 = modelresults[28][1]
    community3m14 = modelresults[28][2]
    community4m14 = modelresults[28][3]
    community5m14 = modelresults[28][4]
    community6m14 = modelresults[28][5]
    community7m14 = modelresults[28][6]
    community8m14 = modelresults[28][7]
    community9m14 = modelresults[28][8]
    community10m14 = modelresults[28][9]
    community11m14 = modelresults[28][10]
    community12m14 = modelresults[28][11]
    community13m14 = modelresults[28][12]
    community14m14 = modelresults[28][13]
    community15m14 = modelresults[28][14]
    community1m15 = modelresults[29][0]
    community2m15 = modelresults[29][1]
    community3m15 = modelresults[29][2]
    community4m15 = modelresults[29][3]
    community5m15 = modelresults[29][4]
    community6m15 = modelresults[29][5]
    community7m15 = modelresults[29][6]
    community8m15 = modelresults[29][7]
    community9m15 = modelresults[29][8]
    community10m15 = modelresults[29][9]
    community11m15 = modelresults[29][10]
    community12m15 = modelresults[29][11]
    community13m15 = modelresults[29][12]
    community14m15 = modelresults[29][13]
    community15m15 = modelresults[29][14]
    community1defend = modelresults[30][0]
    community2defend = modelresults[30][1]
    community3defend = modelresults[30][2]
    community4defend = modelresults[30][3]
    community5defend = modelresults[30][4]
    community6defend = modelresults[30][5]
    community7defend = modelresults[30][6]
    community8defend = modelresults[30][7]
    community9defend = modelresults[30][8]
    community10defend = modelresults[30][9]
    community11defend = modelresults[30][10]
    community12defend = modelresults[30][11]
    community13defend = modelresults[30][12]
    community14defend = modelresults[30][13]
    community15defend = modelresults[30][14]
    oneandtwo = modelresults[31][0]
    oneandthree = modelresults[31][1]
    oneandfour = modelresults[31][2]
    oneandfive = modelresults[31][3]
    oneandsix = modelresults[31][4]
    oneandseven = modelresults[31][5]
    oneandeight = modelresults[31][6]
    oneandnine = modelresults[31][7]
    oneandten = modelresults[31][8]
    oneandeleven = modelresults[31][9]
    oneandtwelve = modelresults[31][10]
    oneandthirteen = modelresults[31][11]
    oneandfourteen = modelresults[31][12]
    oneandfifteen = modelresults[31][13]
    twoandthree = modelresults[31][14]
    twoandfour = modelresults[31][15]
    twoandfive = modelresults[31][16]
    twoandsix = modelresults[31][17]
    twoandseven = modelresults[31][18]
    twoandeight = modelresults[31][19]
    twoandnine = modelresults[31][20]
    twoandten = modelresults[31][21]
    twoandeleven = modelresults[31][22]
    twoandtwelve = modelresults[31][23]
    twoandthirteen = modelresults[31][24]
    twoandfourteen = modelresults[31][25]
    twoandfifteen = modelresults[31][26]
    threeandfour = modelresults[31][27]
    threeandfive = modelresults[31][28]
    threeandsix = modelresults[31][29]
    threeandseven = modelresults[31][30]
    threeandeight = modelresults[31][31]
    threeandnine = modelresults[31][32]
    threeandten = modelresults[31][33]
    threeandeleven = modelresults[31][34]
    threeandtwelve = modelresults[31][35]
    threeandthirteen = modelresults[31][36]
    threeandfourteen = modelresults[31][37]
    threeandfifteen = modelresults[31][38]
    fourandfive = modelresults[31][39]
    fourandsix = modelresults[31][40]
    fourandseven = modelresults[31][41]
    fourandeight = modelresults[31][42]
    fourandnine = modelresults[31][43]
    fourandten = modelresults[31][44]
    fourandeleven = modelresults[31][45]
    fourandtwelve = modelresults[31][46]
    fourandthirteen = modelresults[31][47]
    fourandfourteen = modelresults[31][48]
    fourandfifteen = modelresults[31][49]
    fiveandsix = modelresults[31][50]
    fiveandseven = modelresults[31][51]
    fiveandeight = modelresults[31][52]
    fiveandnine = modelresults[31][53]
    fiveandten = modelresults[31][54]
    fiveandeleven = modelresults[31][55]
    fiveandtwelve = modelresults[31][56]
    fiveandthirteen = modelresults[31][57]
    fiveandfourteen = modelresults[31][58]
    fiveandfifteen = modelresults[31][59]
    sixandseven = modelresults[31][60]
    sixandeight = modelresults[31][61]
    sixandnine = modelresults[31][62]
    sixandten = modelresults[31][63]
    sixandeleven = modelresults[31][64]
    sixandtwelve = modelresults[31][65]
    sixandthirteen = modelresults[31][66]
    sixandfourteen = modelresults[31][67]
    sixandfifteen = modelresults[31][68]
    sevenandeight = modelresults[31][69]
    sevenandnine = modelresults[31][70]
    sevenandten = modelresults[31][71]
    sevenandeleven = modelresults[31][72]
    sevenandtwelve = modelresults[31][73]
    sevenandthirteen = modelresults[31][74]
    sevenandfourteen = modelresults[31][75]
    sevenandfifteen = modelresults[31][76]
    eightandnine = modelresults[31][77]
    eightandten = modelresults[31][78]
    eightandeleven = modelresults[31][79]
    eightandtwelve = modelresults[31][80]
    eightandthirteen = modelresults[31][81]
    eightandfourteen = modelresults[31][82]
    eightandfifteen = modelresults[31][83]
    nineandten = modelresults[31][84]
    nineandeleven = modelresults[31][85]
    nineandtwelve = modelresults[31][86]
    nineandthirteen = modelresults[31][87]
    nineandfourteen = modelresults[31][88]
    nineandfifteen = modelresults[31][89]
    tenandeleven = modelresults[31][90]
    tenandtwelve = modelresults[31][91]
    tenandthirteen = modelresults[31][92]
    tenandfourteen = modelresults[31][93]
    tenandfifteen = modelresults[31][94]
    elevenandtwelve = modelresults[31][95]
    elevenandthirteen = modelresults[31][96]
    elevenandfourteen = modelresults[31][97]
    elevenandfifteen = modelresults[31][98]
    twelveandthirteen = modelresults[31][99]
    twelveandfourteen = modelresults[31][100]
    twelveandfifteen = modelresults[31][101]
    thirteenandfourteen = modelresults[31][102]
    thirteenandfifteen = modelresults[31][103]
    fourteenandfifteen = modelresults[31][104]

    # print('strength1 # 1:', modelresults[0][0][0])

    i += 1
    while i < sims+1:
        job = subqueue.enqueue('application.tasks.simulator_instance')
        finished = False
        while finished == False:
            finished = job.is_finished
        modelresults = job.result
        print(int((i / sims) * 100), '% complete')
        # fulljob.meta['progress'] = int((i / sims) * 100)
        # fulljob.save_meta()
        # print('strength1 #', i + 1, ':', modelresults[0][0][0])
        strength1 = [x + y for x, y in zip(strength1, modelresults[0][0])]
        notorietyratio1 = [x + y for x, y in zip(notorietyratio1, modelresults[0][1])]
        totalextort1 = [x + y for x, y in zip(totalextort1, modelresults[0][2])]
        countextort1 = [x + y for x, y in zip(countextort1, modelresults[0][3])]
        countbenefit1 = [x + y for x, y in zip(countbenefit1, modelresults[0][4])]
        countpunish1 = [x + y for x, y in zip(countpunish1, modelresults[0][5])]
        countsupport1 = [x + y for x, y in zip(countsupport1, modelresults[0][6])]
        totalsupport1 = [x + y for x, y in zip(totalsupport1, modelresults[0][7])]
        countdefend1 = [x + y for x, y in zip(countdefend1, modelresults[0][8])]
        strength2 = [x + y for x, y in zip(strength2, modelresults[1][0])]
        notorietyratio2 = [x + y for x, y in zip(notorietyratio2, modelresults[1][1])]
        totalextort2 = [x + y for x, y in zip(totalextort2, modelresults[1][2])]
        countextort2 = [x + y for x, y in zip(countextort2, modelresults[1][3])]
        countbenefit2 = [x + y for x, y in zip(countbenefit2, modelresults[1][4])]
        countpunish2 = [x + y for x, y in zip(countpunish2, modelresults[1][5])]
        countsupport2 = [x + y for x, y in zip(countsupport2, modelresults[1][6])]
        totalsupport2 = [x + y for x, y in zip(totalsupport2, modelresults[1][7])]
        countdefend2 = [x + y for x, y in zip(countdefend2, modelresults[1][8])]
        strength3 = [x + y for x, y in zip(strength3, modelresults[2][0])]
        notorietyratio3 = [x + y for x, y in zip(notorietyratio3, modelresults[2][1])]
        totalextort3 = [x + y for x, y in zip(totalextort3, modelresults[2][2])]
        countextort3 = [x + y for x, y in zip(countextort3, modelresults[2][3])]
        countbenefit3 = [x + y for x, y in zip(countbenefit3, modelresults[2][4])]
        countpunish3 = [x + y for x, y in zip(countpunish3, modelresults[2][5])]
        countsupport3 = [x + y for x, y in zip(countsupport3, modelresults[2][6])]
        totalsupport3 = [x + y for x, y in zip(totalsupport3, modelresults[2][7])]
        countdefend3 = [x + y for x, y in zip(countdefend3, modelresults[2][8])]
        strength4 = [x + y for x, y in zip(strength4, modelresults[3][0])]
        notorietyratio4 = [x + y for x, y in zip(notorietyratio4, modelresults[3][1])]
        totalextort4 = [x + y for x, y in zip(totalextort4, modelresults[3][2])]
        countextort4 = [x + y for x, y in zip(countextort4, modelresults[3][3])]
        countbenefit4 = [x + y for x, y in zip(countbenefit4, modelresults[3][4])]
        countpunish4 = [x + y for x, y in zip(countpunish4, modelresults[3][5])]
        countsupport4 = [x + y for x, y in zip(countsupport4, modelresults[3][6])]
        totalsupport4 = [x + y for x, y in zip(totalsupport4, modelresults[3][7])]
        countdefend4 = [x + y for x, y in zip(countdefend4, modelresults[3][8])]
        strength5 = [x + y for x, y in zip(strength5, modelresults[4][0])]
        notorietyratio5 = [x + y for x, y in zip(notorietyratio5, modelresults[4][1])]
        totalextort5 = [x + y for x, y in zip(totalextort5, modelresults[4][2])]
        countextort5 = [x + y for x, y in zip(countextort5, modelresults[4][3])]
        countbenefit5 = [x + y for x, y in zip(countbenefit5, modelresults[4][4])]
        countpunish5 = [x + y for x, y in zip(countpunish5, modelresults[4][5])]
        countsupport5 = [x + y for x, y in zip(countsupport5, modelresults[4][6])]
        totalsupport5 = [x + y for x, y in zip(totalsupport5, modelresults[4][7])]
        countdefend5 = [x + y for x, y in zip(countdefend5, modelresults[4][8])]
        strength6 = [x + y for x, y in zip(strength6, modelresults[5][0])]
        notorietyratio6 = [x + y for x, y in zip(notorietyratio6, modelresults[5][1])]
        totalextort6 = [x + y for x, y in zip(totalextort6, modelresults[5][2])]
        countextort6 = [x + y for x, y in zip(countextort6, modelresults[5][3])]
        countbenefit6 = [x + y for x, y in zip(countbenefit6, modelresults[5][4])]
        countpunish6 = [x + y for x, y in zip(countpunish6, modelresults[5][5])]
        countsupport6 = [x + y for x, y in zip(countsupport6, modelresults[5][6])]
        totalsupport6 = [x + y for x, y in zip(totalsupport6, modelresults[5][7])]
        countdefend6 = [x + y for x, y in zip(countdefend6, modelresults[5][8])]
        strength7 = [x + y for x, y in zip(strength7, modelresults[6][0])]
        notorietyratio7 = [x + y for x, y in zip(notorietyratio7, modelresults[6][1])]
        totalextort7 = [x + y for x, y in zip(totalextort7, modelresults[6][2])]
        countextort7 = [x + y for x, y in zip(countextort7, modelresults[6][3])]
        countbenefit7 = [x + y for x, y in zip(countbenefit7, modelresults[6][4])]
        countpunish7 = [x + y for x, y in zip(countpunish7, modelresults[6][5])]
        countsupport7 = [x + y for x, y in zip(countsupport7, modelresults[6][6])]
        totalsupport7 = [x + y for x, y in zip(totalsupport7, modelresults[6][7])]
        countdefend7 = [x + y for x, y in zip(countdefend7, modelresults[6][8])]
        strength8 = [x + y for x, y in zip(strength8, modelresults[7][0])]
        notorietyratio8 = [x + y for x, y in zip(notorietyratio8, modelresults[7][1])]
        totalextort8 = [x + y for x, y in zip(totalextort8, modelresults[7][2])]
        countextort8 = [x + y for x, y in zip(countextort8, modelresults[7][3])]
        countbenefit8 = [x + y for x, y in zip(countbenefit8, modelresults[7][4])]
        countpunish8 = [x + y for x, y in zip(countpunish8, modelresults[7][5])]
        countsupport8 = [x + y for x, y in zip(countsupport8, modelresults[7][6])]
        totalsupport8 = [x + y for x, y in zip(totalsupport8, modelresults[7][7])]
        countdefend8 = [x + y for x, y in zip(countdefend8, modelresults[7][8])]
        strength9 = [x + y for x, y in zip(strength9, modelresults[8][0])]
        notorietyratio9 = [x + y for x, y in zip(notorietyratio9, modelresults[8][1])]
        totalextort9 = [x + y for x, y in zip(totalextort9, modelresults[8][2])]
        countextort9 = [x + y for x, y in zip(countextort9, modelresults[8][3])]
        countbenefit9 = [x + y for x, y in zip(countbenefit9, modelresults[8][4])]
        countpunish9 = [x + y for x, y in zip(countpunish9, modelresults[8][5])]
        countsupport9 = [x + y for x, y in zip(countsupport9, modelresults[8][6])]
        totalsupport9 = [x + y for x, y in zip(totalsupport9, modelresults[8][7])]
        countdefend9 = [x + y for x, y in zip(countdefend9, modelresults[8][8])]
        strength10 = [x + y for x, y in zip(strength10, modelresults[9][0])]
        notorietyratio10 = [x + y for x, y in zip(notorietyratio10, modelresults[9][1])]
        totalextort10 = [x + y for x, y in zip(totalextort10, modelresults[9][2])]
        countextort10 = [x + y for x, y in zip(countextort10, modelresults[9][3])]
        countbenefit10 = [x + y for x, y in zip(countbenefit10, modelresults[9][4])]
        countpunish10 = [x + y for x, y in zip(countpunish10, modelresults[9][5])]
        countsupport10 = [x + y for x, y in zip(countsupport10, modelresults[9][6])]
        totalsupport10 = [x + y for x, y in zip(totalsupport10, modelresults[9][7])]
        countdefend10 = [x + y for x, y in zip(countdefend10, modelresults[9][8])]
        strength11 = [x + y for x, y in zip(strength11, modelresults[10][0])]
        notorietyratio11 = [x + y for x, y in zip(notorietyratio11, modelresults[10][1])]
        totalextort11 = [x + y for x, y in zip(totalextort11, modelresults[10][2])]
        countextort11 = [x + y for x, y in zip(countextort11, modelresults[10][3])]
        countbenefit11 = [x + y for x, y in zip(countbenefit11, modelresults[10][4])]
        countpunish11 = [x + y for x, y in zip(countpunish11, modelresults[10][5])]
        countsupport11 = [x + y for x, y in zip(countsupport11, modelresults[10][6])]
        totalsupport11 = [x + y for x, y in zip(totalsupport11, modelresults[10][7])]
        countdefend11 = [x + y for x, y in zip(countdefend11, modelresults[10][8])]
        strength12 = [x + y for x, y in zip(strength12, modelresults[11][0])]
        notorietyratio12 = [x + y for x, y in zip(notorietyratio12, modelresults[11][1])]
        totalextort12 = [x + y for x, y in zip(totalextort12, modelresults[11][2])]
        countextort12 = [x + y for x, y in zip(countextort12, modelresults[11][3])]
        countbenefit12 = [x + y for x, y in zip(countbenefit12, modelresults[11][4])]
        countpunish12 = [x + y for x, y in zip(countpunish12, modelresults[11][5])]
        countsupport12 = [x + y for x, y in zip(countsupport12, modelresults[11][6])]
        totalsupport12 = [x + y for x, y in zip(totalsupport12, modelresults[11][7])]
        countdefend12 = [x + y for x, y in zip(countdefend12, modelresults[11][8])]
        strength13 = [x + y for x, y in zip(strength13, modelresults[12][0])]
        notorietyratio13 = [x + y for x, y in zip(notorietyratio13, modelresults[12][1])]
        totalextort13 = [x + y for x, y in zip(totalextort13, modelresults[12][2])]
        countextort13 = [x + y for x, y in zip(countextort13, modelresults[12][3])]
        countbenefit13 = [x + y for x, y in zip(countbenefit13, modelresults[12][4])]
        countpunish13 = [x + y for x, y in zip(countpunish13, modelresults[12][5])]
        countsupport13 = [x + y for x, y in zip(countsupport13, modelresults[12][6])]
        totalsupport13 = [x + y for x, y in zip(totalsupport13, modelresults[12][7])]
        countdefend13 = [x + y for x, y in zip(countdefend13, modelresults[12][8])]
        strength14 = [x + y for x, y in zip(strength14, modelresults[13][0])]
        notorietyratio14 = [x + y for x, y in zip(notorietyratio14, modelresults[13][1])]
        totalextort14 = [x + y for x, y in zip(totalextort14, modelresults[13][2])]
        countextort14 = [x + y for x, y in zip(countextort14, modelresults[13][3])]
        countbenefit14 = [x + y for x, y in zip(countbenefit14, modelresults[13][4])]
        countpunish14 = [x + y for x, y in zip(countpunish14, modelresults[13][5])]
        countsupport14 = [x + y for x, y in zip(countsupport14, modelresults[13][6])]
        totalsupport14 = [x + y for x, y in zip(totalsupport14, modelresults[13][7])]
        countdefend14 = [x + y for x, y in zip(countdefend14, modelresults[13][8])]
        strength15 = [x + y for x, y in zip(strength15, modelresults[14][0])]
        notorietyratio15 = [x + y for x, y in zip(notorietyratio15, modelresults[14][1])]
        totalextort15 = [x + y for x, y in zip(totalextort15, modelresults[14][2])]
        countextort15 = [x + y for x, y in zip(countextort15, modelresults[14][3])]
        countbenefit15 = [x + y for x, y in zip(countbenefit15, modelresults[14][4])]
        countpunish15 = [x + y for x, y in zip(countpunish15, modelresults[14][5])]
        countsupport15 = [x + y for x, y in zip(countsupport15, modelresults[14][6])]
        totalsupport15 = [x + y for x, y in zip(totalsupport15, modelresults[14][7])]
        countdefend15 = [x + y for x, y in zip(countdefend15, modelresults[14][8])]
        community1m1 = [x + y for x, y in zip(community1m1, modelresults[15][0])]
        community2m1 = [x + y for x, y in zip(community2m1, modelresults[15][1])]
        community3m1 = [x + y for x, y in zip(community3m1, modelresults[15][2])]
        community4m1 = [x + y for x, y in zip(community4m1, modelresults[15][3])]
        community5m1 = [x + y for x, y in zip(community5m1, modelresults[15][4])]
        community6m1 = [x + y for x, y in zip(community6m1, modelresults[15][5])]
        community7m1 = [x + y for x, y in zip(community7m1, modelresults[15][6])]
        community8m1 = [x + y for x, y in zip(community8m1, modelresults[15][7])]
        community9m1 = [x + y for x, y in zip(community9m1, modelresults[15][8])]
        community10m1 = [x + y for x, y in zip(community10m1, modelresults[15][9])]
        community11m1 = [x + y for x, y in zip(community11m1, modelresults[15][10])]
        community12m1 = [x + y for x, y in zip(community12m1, modelresults[15][11])]
        community13m1 = [x + y for x, y in zip(community13m1, modelresults[15][12])]
        community14m1 = [x + y for x, y in zip(community14m1, modelresults[15][13])]
        community15m1 = [x + y for x, y in zip(community15m1, modelresults[15][14])]
        community1m2 = [x + y for x, y in zip(community1m2, modelresults[16][0])]
        community2m2 = [x + y for x, y in zip(community2m2, modelresults[16][1])]
        community3m2 = [x + y for x, y in zip(community3m2, modelresults[16][2])]
        community4m2 = [x + y for x, y in zip(community4m2, modelresults[16][3])]
        community5m2 = [x + y for x, y in zip(community5m2, modelresults[16][4])]
        community6m2 = [x + y for x, y in zip(community6m2, modelresults[16][5])]
        community7m2 = [x + y for x, y in zip(community7m2, modelresults[16][6])]
        community8m2 = [x + y for x, y in zip(community8m2, modelresults[16][7])]
        community9m2 = [x + y for x, y in zip(community9m2, modelresults[16][8])]
        community10m2 = [x + y for x, y in zip(community10m2, modelresults[16][9])]
        community11m2 = [x + y for x, y in zip(community11m2, modelresults[16][10])]
        community12m2 = [x + y for x, y in zip(community12m2, modelresults[16][11])]
        community13m2 = [x + y for x, y in zip(community13m2, modelresults[16][12])]
        community14m2 = [x + y for x, y in zip(community14m2, modelresults[16][13])]
        community15m2 = [x + y for x, y in zip(community15m2, modelresults[16][14])]
        community1m3 = [x + y for x, y in zip(community1m3, modelresults[17][0])]
        community2m3 = [x + y for x, y in zip(community2m3, modelresults[17][1])]
        community3m3 = [x + y for x, y in zip(community3m3, modelresults[17][2])]
        community4m3 = [x + y for x, y in zip(community4m3, modelresults[17][3])]
        community5m3 = [x + y for x, y in zip(community5m3, modelresults[17][4])]
        community6m3 = [x + y for x, y in zip(community6m3, modelresults[17][5])]
        community7m3 = [x + y for x, y in zip(community7m3, modelresults[17][6])]
        community8m3 = [x + y for x, y in zip(community8m3, modelresults[17][7])]
        community9m3 = [x + y for x, y in zip(community9m3, modelresults[17][8])]
        community10m3 = [x + y for x, y in zip(community10m3, modelresults[17][9])]
        community11m3 = [x + y for x, y in zip(community11m3, modelresults[17][10])]
        community12m3 = [x + y for x, y in zip(community12m3, modelresults[17][11])]
        community13m3 = [x + y for x, y in zip(community13m3, modelresults[17][12])]
        community14m3 = [x + y for x, y in zip(community14m3, modelresults[17][13])]
        community15m3 = [x + y for x, y in zip(community15m3, modelresults[17][14])]
        community1m4 = [x + y for x, y in zip(community1m4, modelresults[18][0])]
        community2m4 = [x + y for x, y in zip(community2m4, modelresults[18][1])]
        community3m4 = [x + y for x, y in zip(community3m4, modelresults[18][2])]
        community4m4 = [x + y for x, y in zip(community4m4, modelresults[18][3])]
        community5m4 = [x + y for x, y in zip(community5m4, modelresults[18][4])]
        community6m4 = [x + y for x, y in zip(community6m4, modelresults[18][5])]
        community7m4 = [x + y for x, y in zip(community7m4, modelresults[18][6])]
        community8m4 = [x + y for x, y in zip(community8m4, modelresults[18][7])]
        community9m4 = [x + y for x, y in zip(community9m4, modelresults[18][8])]
        community10m4 = [x + y for x, y in zip(community10m4, modelresults[18][9])]
        community11m4 = [x + y for x, y in zip(community11m4, modelresults[18][10])]
        community12m4 = [x + y for x, y in zip(community12m4, modelresults[18][11])]
        community13m4 = [x + y for x, y in zip(community13m4, modelresults[18][12])]
        community14m4 = [x + y for x, y in zip(community14m4, modelresults[18][13])]
        community15m4 = [x + y for x, y in zip(community15m4, modelresults[18][14])]
        community1m5 = [x + y for x, y in zip(community1m5, modelresults[19][0])]
        community2m5 = [x + y for x, y in zip(community2m5, modelresults[19][1])]
        community3m5 = [x + y for x, y in zip(community3m5, modelresults[19][2])]
        community4m5 = [x + y for x, y in zip(community4m5, modelresults[19][3])]
        community5m5 = [x + y for x, y in zip(community5m5, modelresults[19][4])]
        community6m5 = [x + y for x, y in zip(community6m5, modelresults[19][5])]
        community7m5 = [x + y for x, y in zip(community7m5, modelresults[19][6])]
        community8m5 = [x + y for x, y in zip(community8m5, modelresults[19][7])]
        community9m5 = [x + y for x, y in zip(community9m5, modelresults[19][8])]
        community10m5 = [x + y for x, y in zip(community10m5, modelresults[19][9])]
        community11m5 = [x + y for x, y in zip(community11m5, modelresults[19][10])]
        community12m5 = [x + y for x, y in zip(community12m5, modelresults[19][11])]
        community13m5 = [x + y for x, y in zip(community13m5, modelresults[19][12])]
        community14m5 = [x + y for x, y in zip(community14m5, modelresults[19][13])]
        community15m5 = [x + y for x, y in zip(community15m5, modelresults[19][14])]
        community1m6 = [x + y for x, y in zip(community1m6, modelresults[20][0])]
        community2m6 = [x + y for x, y in zip(community2m6, modelresults[20][1])]
        community3m6 = [x + y for x, y in zip(community3m6, modelresults[20][2])]
        community4m6 = [x + y for x, y in zip(community4m6, modelresults[20][3])]
        community5m6 = [x + y for x, y in zip(community5m6, modelresults[20][4])]
        community6m6 = [x + y for x, y in zip(community6m6, modelresults[20][5])]
        community7m6 = [x + y for x, y in zip(community7m6, modelresults[20][6])]
        community8m6 = [x + y for x, y in zip(community8m6, modelresults[20][7])]
        community9m6 = [x + y for x, y in zip(community9m6, modelresults[20][8])]
        community10m6 = [x + y for x, y in zip(community10m6, modelresults[20][9])]
        community11m6 = [x + y for x, y in zip(community11m6, modelresults[20][10])]
        community12m6 = [x + y for x, y in zip(community12m6, modelresults[20][11])]
        community13m6 = [x + y for x, y in zip(community13m6, modelresults[20][12])]
        community14m6 = [x + y for x, y in zip(community14m6, modelresults[20][13])]
        community15m6 = [x + y for x, y in zip(community15m6, modelresults[20][14])]
        community1m7 = [x + y for x, y in zip(community1m7, modelresults[21][0])]
        community2m7 = [x + y for x, y in zip(community2m7, modelresults[21][1])]
        community3m7 = [x + y for x, y in zip(community3m7, modelresults[21][2])]
        community4m7 = [x + y for x, y in zip(community4m7, modelresults[21][3])]
        community5m7 = [x + y for x, y in zip(community5m7, modelresults[21][4])]
        community6m7 = [x + y for x, y in zip(community6m7, modelresults[21][5])]
        community7m7 = [x + y for x, y in zip(community7m7, modelresults[21][6])]
        community8m7 = [x + y for x, y in zip(community8m7, modelresults[21][7])]
        community9m7 = [x + y for x, y in zip(community9m7, modelresults[21][8])]
        community10m7 = [x + y for x, y in zip(community10m7, modelresults[21][9])]
        community11m7 = [x + y for x, y in zip(community11m7, modelresults[21][10])]
        community12m7 = [x + y for x, y in zip(community12m7, modelresults[21][11])]
        community13m7 = [x + y for x, y in zip(community13m7, modelresults[21][12])]
        community14m7 = [x + y for x, y in zip(community14m7, modelresults[21][13])]
        community15m7 = [x + y for x, y in zip(community15m7, modelresults[21][14])]
        community1m8 = [x + y for x, y in zip(community1m8, modelresults[22][0])]
        community2m8 = [x + y for x, y in zip(community2m8, modelresults[22][1])]
        community3m8 = [x + y for x, y in zip(community3m8, modelresults[22][2])]
        community4m8 = [x + y for x, y in zip(community4m8, modelresults[22][3])]
        community5m8 = [x + y for x, y in zip(community5m8, modelresults[22][4])]
        community6m8 = [x + y for x, y in zip(community6m8, modelresults[22][5])]
        community7m8 = [x + y for x, y in zip(community7m8, modelresults[22][6])]
        community8m8 = [x + y for x, y in zip(community8m8, modelresults[22][7])]
        community9m8 = [x + y for x, y in zip(community9m8, modelresults[22][8])]
        community10m8 = [x + y for x, y in zip(community10m8, modelresults[22][9])]
        community11m8 = [x + y for x, y in zip(community11m8, modelresults[22][10])]
        community12m8 = [x + y for x, y in zip(community12m8, modelresults[22][11])]
        community13m8 = [x + y for x, y in zip(community13m8, modelresults[22][12])]
        community14m8 = [x + y for x, y in zip(community14m8, modelresults[22][13])]
        community15m8 = [x + y for x, y in zip(community15m8, modelresults[22][14])]
        community1m9 = [x + y for x, y in zip(community1m9, modelresults[23][0])]
        community2m9 = [x + y for x, y in zip(community2m9, modelresults[23][1])]
        community3m9 = [x + y for x, y in zip(community3m9, modelresults[23][2])]
        community4m9 = [x + y for x, y in zip(community4m9, modelresults[23][3])]
        community5m9 = [x + y for x, y in zip(community5m9, modelresults[23][4])]
        community6m9 = [x + y for x, y in zip(community6m9, modelresults[23][5])]
        community7m9 = [x + y for x, y in zip(community7m9, modelresults[23][6])]
        community8m9 = [x + y for x, y in zip(community8m9, modelresults[23][7])]
        community9m9 = [x + y for x, y in zip(community9m9, modelresults[23][8])]
        community10m9 = [x + y for x, y in zip(community10m9, modelresults[23][9])]
        community11m9 = [x + y for x, y in zip(community11m9, modelresults[23][10])]
        community12m9 = [x + y for x, y in zip(community12m9, modelresults[23][11])]
        community13m9 = [x + y for x, y in zip(community13m9, modelresults[23][12])]
        community14m9 = [x + y for x, y in zip(community14m9, modelresults[23][13])]
        community15m9 = [x + y for x, y in zip(community15m9, modelresults[23][14])]
        community1m10 = [x + y for x, y in zip(community1m10, modelresults[24][0])]
        community2m10 = [x + y for x, y in zip(community2m10, modelresults[24][1])]
        community3m10 = [x + y for x, y in zip(community3m10, modelresults[24][2])]
        community4m10 = [x + y for x, y in zip(community4m10, modelresults[24][3])]
        community5m10 = [x + y for x, y in zip(community5m10, modelresults[24][4])]
        community6m10 = [x + y for x, y in zip(community6m10, modelresults[24][5])]
        community7m10 = [x + y for x, y in zip(community7m10, modelresults[24][6])]
        community8m10 = [x + y for x, y in zip(community8m10, modelresults[24][7])]
        community9m10 = [x + y for x, y in zip(community9m10, modelresults[24][8])]
        community10m10 = [x + y for x, y in zip(community10m10, modelresults[24][9])]
        community11m10 = [x + y for x, y in zip(community11m10, modelresults[24][10])]
        community12m10 = [x + y for x, y in zip(community12m10, modelresults[24][11])]
        community13m10 = [x + y for x, y in zip(community13m10, modelresults[24][12])]
        community14m10 = [x + y for x, y in zip(community14m10, modelresults[24][13])]
        community15m10 = [x + y for x, y in zip(community15m10, modelresults[24][14])]
        community1m11 = [x + y for x, y in zip(community1m11, modelresults[25][0])]
        community2m11 = [x + y for x, y in zip(community2m11, modelresults[25][1])]
        community3m11 = [x + y for x, y in zip(community3m11, modelresults[25][2])]
        community4m11 = [x + y for x, y in zip(community4m11, modelresults[25][3])]
        community5m11 = [x + y for x, y in zip(community5m11, modelresults[25][4])]
        community6m11 = [x + y for x, y in zip(community6m11, modelresults[25][5])]
        community7m11 = [x + y for x, y in zip(community7m11, modelresults[25][6])]
        community8m11 = [x + y for x, y in zip(community8m11, modelresults[25][7])]
        community9m11 = [x + y for x, y in zip(community9m11, modelresults[25][8])]
        community10m11 = [x + y for x, y in zip(community10m11, modelresults[25][9])]
        community11m11 = [x + y for x, y in zip(community11m11, modelresults[25][10])]
        community12m11 = [x + y for x, y in zip(community12m11, modelresults[25][11])]
        community13m11 = [x + y for x, y in zip(community13m11, modelresults[25][12])]
        community14m11 = [x + y for x, y in zip(community14m11, modelresults[25][13])]
        community15m11 = [x + y for x, y in zip(community15m11, modelresults[25][14])]
        community1m12 = [x + y for x, y in zip(community1m12, modelresults[26][0])]
        community2m12 = [x + y for x, y in zip(community2m12, modelresults[26][1])]
        community3m12 = [x + y for x, y in zip(community3m12, modelresults[26][2])]
        community4m12 = [x + y for x, y in zip(community4m12, modelresults[26][3])]
        community5m12 = [x + y for x, y in zip(community5m12, modelresults[26][4])]
        community6m12 = [x + y for x, y in zip(community6m12, modelresults[26][5])]
        community7m12 = [x + y for x, y in zip(community7m12, modelresults[26][6])]
        community8m12 = [x + y for x, y in zip(community8m12, modelresults[26][7])]
        community9m12 = [x + y for x, y in zip(community9m12, modelresults[26][8])]
        community10m12 = [x + y for x, y in zip(community10m12, modelresults[26][9])]
        community11m12 = [x + y for x, y in zip(community11m12, modelresults[26][10])]
        community12m12 = [x + y for x, y in zip(community12m12, modelresults[26][11])]
        community13m12 = [x + y for x, y in zip(community13m12, modelresults[26][12])]
        community14m12 = [x + y for x, y in zip(community14m12, modelresults[26][13])]
        community15m12 = [x + y for x, y in zip(community15m12, modelresults[26][14])]
        community1m13 = [x + y for x, y in zip(community1m13, modelresults[27][0])]
        community2m13 = [x + y for x, y in zip(community2m13, modelresults[27][1])]
        community3m13 = [x + y for x, y in zip(community3m13, modelresults[27][2])]
        community4m13 = [x + y for x, y in zip(community4m13, modelresults[27][3])]
        community5m13 = [x + y for x, y in zip(community5m13, modelresults[27][4])]
        community6m13 = [x + y for x, y in zip(community6m13, modelresults[27][5])]
        community7m13 = [x + y for x, y in zip(community7m13, modelresults[27][6])]
        community8m13 = [x + y for x, y in zip(community8m13, modelresults[27][7])]
        community9m13 = [x + y for x, y in zip(community9m13, modelresults[27][8])]
        community10m13 = [x + y for x, y in zip(community10m13, modelresults[27][9])]
        community11m13 = [x + y for x, y in zip(community11m13, modelresults[27][10])]
        community12m13 = [x + y for x, y in zip(community12m13, modelresults[27][11])]
        community13m13 = [x + y for x, y in zip(community13m13, modelresults[27][12])]
        community14m13 = [x + y for x, y in zip(community14m13, modelresults[27][13])]
        community15m13 = [x + y for x, y in zip(community15m13, modelresults[27][14])]
        community1m14 = [x + y for x, y in zip(community1m14, modelresults[28][0])]
        community2m14 = [x + y for x, y in zip(community2m14, modelresults[28][1])]
        community3m14 = [x + y for x, y in zip(community3m14, modelresults[28][2])]
        community4m14 = [x + y for x, y in zip(community4m14, modelresults[28][3])]
        community5m14 = [x + y for x, y in zip(community5m14, modelresults[28][4])]
        community6m14 = [x + y for x, y in zip(community6m14, modelresults[28][5])]
        community7m14 = [x + y for x, y in zip(community7m14, modelresults[28][6])]
        community8m14 = [x + y for x, y in zip(community8m14, modelresults[28][7])]
        community9m14 = [x + y for x, y in zip(community9m14, modelresults[28][8])]
        community10m14 = [x + y for x, y in zip(community10m14, modelresults[28][9])]
        community11m14 = [x + y for x, y in zip(community11m14, modelresults[28][10])]
        community12m14 = [x + y for x, y in zip(community12m14, modelresults[28][11])]
        community13m14 = [x + y for x, y in zip(community13m14, modelresults[28][12])]
        community14m14 = [x + y for x, y in zip(community14m14, modelresults[28][13])]
        community15m14 = [x + y for x, y in zip(community15m14, modelresults[28][14])]
        community1m15 = [x + y for x, y in zip(community1m15, modelresults[29][0])]
        community2m15 = [x + y for x, y in zip(community2m15, modelresults[29][1])]
        community3m15 = [x + y for x, y in zip(community3m15, modelresults[29][2])]
        community4m15 = [x + y for x, y in zip(community4m15, modelresults[29][3])]
        community5m15 = [x + y for x, y in zip(community5m15, modelresults[29][4])]
        community6m15 = [x + y for x, y in zip(community6m15, modelresults[29][5])]
        community7m15 = [x + y for x, y in zip(community7m15, modelresults[29][6])]
        community8m15 = [x + y for x, y in zip(community8m15, modelresults[29][7])]
        community9m15 = [x + y for x, y in zip(community9m15, modelresults[29][8])]
        community10m15 = [x + y for x, y in zip(community10m15, modelresults[29][9])]
        community11m15 = [x + y for x, y in zip(community11m15, modelresults[29][10])]
        community12m15 = [x + y for x, y in zip(community12m15, modelresults[29][11])]
        community13m15 = [x + y for x, y in zip(community13m15, modelresults[29][12])]
        community14m15 = [x + y for x, y in zip(community14m15, modelresults[29][13])]
        community15m15 = [x + y for x, y in zip(community15m15, modelresults[29][14])]
        community1defend = [x + y for x, y in zip(community1defend, modelresults[30][0])]
        community2defend = [x + y for x, y in zip(community2defend, modelresults[30][1])]
        community3defend = [x + y for x, y in zip(community3defend, modelresults[30][2])]
        community4defend = [x + y for x, y in zip(community4defend, modelresults[30][3])]
        community5defend = [x + y for x, y in zip(community5defend, modelresults[30][4])]
        community6defend = [x + y for x, y in zip(community6defend, modelresults[30][5])]
        community7defend = [x + y for x, y in zip(community7defend, modelresults[30][6])]
        community8defend = [x + y for x, y in zip(community8defend, modelresults[30][7])]
        community9defend = [x + y for x, y in zip(community9defend, modelresults[30][8])]
        community10defend = [x + y for x, y in zip(community10defend, modelresults[30][9])]
        community11defend = [x + y for x, y in zip(community11defend, modelresults[30][10])]
        community12defend = [x + y for x, y in zip(community12defend, modelresults[30][11])]
        community13defend = [x + y for x, y in zip(community13defend, modelresults[30][12])]
        community14defend = [x + y for x, y in zip(community14defend, modelresults[30][13])]
        community15defend = [x + y for x, y in zip(community15defend, modelresults[30][14])]
        oneandtwo = [x + y for x, y in zip(oneandtwo, modelresults[31][0])]
        oneandthree = [x + y for x, y in zip(oneandthree, modelresults[31][1])]
        oneandfour = [x + y for x, y in zip(oneandfour, modelresults[31][2])]
        oneandfive = [x + y for x, y in zip(oneandfive, modelresults[31][3])]
        oneandsix = [x + y for x, y in zip(oneandsix, modelresults[31][4])]
        oneandseven = [x + y for x, y in zip(oneandseven, modelresults[31][5])]
        oneandeight = [x + y for x, y in zip(oneandeight, modelresults[31][6])]
        oneandnine = [x + y for x, y in zip(oneandnine, modelresults[31][7])]
        oneandten = [x + y for x, y in zip(oneandten, modelresults[31][8])]
        oneandeleven = [x + y for x, y in zip(oneandeleven, modelresults[31][9])]
        oneandtwelve = [x + y for x, y in zip(oneandtwelve, modelresults[31][10])]
        oneandthirteen = [x + y for x, y in zip(oneandthirteen, modelresults[31][11])]
        oneandfourteen = [x + y for x, y in zip(oneandfourteen, modelresults[31][12])]
        oneandfifteen = [x + y for x, y in zip(oneandfifteen, modelresults[31][13])]
        twoandthree = [x + y for x, y in zip(twoandthree, modelresults[31][14])]
        twoandfour = [x + y for x, y in zip(twoandfour, modelresults[31][15])]
        twoandfive = [x + y for x, y in zip(twoandfive, modelresults[31][16])]
        twoandsix = [x + y for x, y in zip(twoandsix, modelresults[31][17])]
        twoandseven = [x + y for x, y in zip(twoandseven, modelresults[31][18])]
        twoandeight = [x + y for x, y in zip(twoandeight, modelresults[31][19])]
        twoandnine = [x + y for x, y in zip(twoandnine, modelresults[31][20])]
        twoandten = [x + y for x, y in zip(twoandten, modelresults[31][21])]
        twoandeleven = [x + y for x, y in zip(twoandeleven, modelresults[31][22])]
        twoandtwelve = [x + y for x, y in zip(twoandtwelve, modelresults[31][23])]
        twoandthirteen = [x + y for x, y in zip(twoandthirteen, modelresults[31][24])]
        twoandfourteen = [x + y for x, y in zip(twoandfourteen, modelresults[31][25])]
        twoandfifteen = [x + y for x, y in zip(twoandfifteen, modelresults[31][26])]
        threeandfour = [x + y for x, y in zip(threeandfour, modelresults[31][27])]
        threeandfive = [x + y for x, y in zip(threeandfive, modelresults[31][28])]
        threeandsix = [x + y for x, y in zip(threeandsix, modelresults[31][29])]
        threeandseven = [x + y for x, y in zip(threeandseven, modelresults[31][30])]
        threeandeight = [x + y for x, y in zip(threeandeight, modelresults[31][31])]
        threeandnine = [x + y for x, y in zip(threeandnine, modelresults[31][32])]
        threeandten = [x + y for x, y in zip(threeandten, modelresults[31][33])]
        threeandeleven = [x + y for x, y in zip(threeandeleven, modelresults[31][34])]
        threeandtwelve = [x + y for x, y in zip(threeandtwelve, modelresults[31][35])]
        threeandthirteen = [x + y for x, y in zip(threeandthirteen, modelresults[31][36])]
        threeandfourteen = [x + y for x, y in zip(threeandfourteen, modelresults[31][37])]
        threeandfifteen = [x + y for x, y in zip(threeandfifteen, modelresults[31][38])]
        fourandfive = [x + y for x, y in zip(fourandfive, modelresults[31][39])]
        fourandsix = [x + y for x, y in zip(fourandsix, modelresults[31][40])]
        fourandseven = [x + y for x, y in zip(fourandseven, modelresults[31][41])]
        fourandeight = [x + y for x, y in zip(fourandeight, modelresults[31][42])]
        fourandnine = [x + y for x, y in zip(fourandnine, modelresults[31][43])]
        fourandten = [x + y for x, y in zip(fourandten, modelresults[31][44])]
        fourandeleven = [x + y for x, y in zip(fourandeleven, modelresults[31][45])]
        fourandtwelve = [x + y for x, y in zip(fourandtwelve, modelresults[31][46])]
        fourandthirteen = [x + y for x, y in zip(fourandthirteen, modelresults[31][47])]
        fourandfourteen = [x + y for x, y in zip(fourandfourteen, modelresults[31][48])]
        fourandfifteen = [x + y for x, y in zip(fourandfifteen, modelresults[31][49])]
        fiveandsix = [x + y for x, y in zip(fiveandsix, modelresults[31][50])]
        fiveandseven = [x + y for x, y in zip(fiveandseven, modelresults[31][51])]
        fiveandeight = [x + y for x, y in zip(fiveandeight, modelresults[31][52])]
        fiveandnine = [x + y for x, y in zip(fiveandnine, modelresults[31][53])]
        fiveandten = [x + y for x, y in zip(fiveandten, modelresults[31][54])]
        fiveandeleven = [x + y for x, y in zip(fiveandeleven, modelresults[31][55])]
        fiveandtwelve = [x + y for x, y in zip(fiveandtwelve, modelresults[31][56])]
        fiveandthirteen = [x + y for x, y in zip(fiveandthirteen, modelresults[31][57])]
        fiveandfourteen = [x + y for x, y in zip(fiveandfourteen, modelresults[31][58])]
        fiveandfifteen = [x + y for x, y in zip(fiveandfifteen, modelresults[31][59])]
        sixandseven = [x + y for x, y in zip(sixandseven, modelresults[31][60])]
        sixandeight = [x + y for x, y in zip(sixandeight, modelresults[31][61])]
        sixandnine = [x + y for x, y in zip(sixandnine, modelresults[31][62])]
        sixandten = [x + y for x, y in zip(sixandten, modelresults[31][63])]
        sixandeleven = [x + y for x, y in zip(sixandeleven, modelresults[31][64])]
        sixandtwelve = [x + y for x, y in zip(sixandtwelve, modelresults[31][65])]
        sixandthirteen = [x + y for x, y in zip(sixandthirteen, modelresults[31][66])]
        sixandfourteen = [x + y for x, y in zip(sixandfourteen, modelresults[31][67])]
        sixandfifteen = [x + y for x, y in zip(sixandfifteen, modelresults[31][68])]
        sevenandeight = [x + y for x, y in zip(sevenandeight, modelresults[31][69])]
        sevenandnine = [x + y for x, y in zip(sevenandnine, modelresults[31][70])]
        sevenandten = [x + y for x, y in zip(sevenandten, modelresults[31][71])]
        sevenandeleven = [x + y for x, y in zip(sevenandeleven, modelresults[31][72])]
        sevenandtwelve = [x + y for x, y in zip(sevenandtwelve, modelresults[31][73])]
        sevenandthirteen = [x + y for x, y in zip(sevenandthirteen, modelresults[31][74])]
        sevenandfourteen = [x + y for x, y in zip(sevenandfourteen, modelresults[31][75])]
        sevenandfifteen = [x + y for x, y in zip(sevenandfifteen, modelresults[31][76])]
        eightandnine = [x + y for x, y in zip(eightandnine, modelresults[31][77])]
        eightandten = [x + y for x, y in zip(eightandten, modelresults[31][78])]
        eightandeleven = [x + y for x, y in zip(eightandeleven, modelresults[31][79])]
        eightandtwelve = [x + y for x, y in zip(eightandtwelve, modelresults[31][80])]
        eightandthirteen = [x + y for x, y in zip(eightandthirteen, modelresults[31][81])]
        eightandfourteen = [x + y for x, y in zip(eightandfourteen, modelresults[31][82])]
        eightandfifteen = [x + y for x, y in zip(eightandfifteen, modelresults[31][83])]
        nineandten = [x + y for x, y in zip(nineandten, modelresults[31][84])]
        nineandeleven = [x + y for x, y in zip(nineandeleven, modelresults[31][85])]
        nineandtwelve = [x + y for x, y in zip(nineandtwelve, modelresults[31][86])]
        nineandthirteen = [x + y for x, y in zip(nineandthirteen, modelresults[31][87])]
        nineandfourteen = [x + y for x, y in zip(nineandfourteen, modelresults[31][88])]
        nineandfifteen = [x + y for x, y in zip(nineandfifteen, modelresults[31][89])]
        tenandeleven = [x + y for x, y in zip(tenandeleven, modelresults[31][90])]
        tenandtwelve = [x + y for x, y in zip(tenandtwelve, modelresults[31][91])]
        tenandthirteen = [x + y for x, y in zip(tenandthirteen, modelresults[31][92])]
        tenandfourteen = [x + y for x, y in zip(tenandfourteen, modelresults[31][93])]
        tenandfifteen = [x + y for x, y in zip(tenandfifteen, modelresults[31][94])]
        elevenandtwelve = [x + y for x, y in zip(elevenandtwelve, modelresults[31][95])]
        elevenandthirteen = [x + y for x, y in zip(elevenandthirteen, modelresults[31][96])]
        elevenandfourteen = [x + y for x, y in zip(elevenandfourteen, modelresults[31][97])]
        elevenandfifteen = [x + y for x, y in zip(elevenandfifteen, modelresults[31][98])]
        twelveandthirteen = [x + y for x, y in zip(twelveandthirteen, modelresults[31][99])]
        twelveandfourteen = [x + y for x, y in zip(twelveandfourteen, modelresults[31][100])]
        twelveandfifteen = [x + y for x, y in zip(twelveandfifteen, modelresults[31][101])]
        thirteenandfourteen = [x + y for x, y in zip(thirteenandfourteen, modelresults[31][102])]
        thirteenandfifteen = [x + y for x, y in zip(thirteenandfifteen, modelresults[31][103])]
        fourteenandfifteen = [x + y for x, y in zip(fourteenandfifteen, modelresults[31][104])]
        i += 1

    for i in range(len(strength1)):
        strength1[i] /= sims
    for i in range(len(notorietyratio1)):
        notorietyratio1[i] /= sims
    for i in range(len(totalextort1)):
        totalextort1[i] /= sims
    for i in range(len(countextort1)):
        countextort1[i] /= sims
    for i in range(len(countbenefit1)):
        countbenefit1[i] /= sims
    for i in range(len(countpunish1)):
        countpunish1[i] /= sims
    for i in range(len(countsupport1)):
        countsupport1[i] /= sims
    for i in range(len(totalsupport1)):
        totalsupport1[i] /= sims
    for i in range(len(countdefend1)):
        countdefend1[i] /= sims
    for i in range(len(strength2)):
        strength2[i] /= sims
    for i in range(len(notorietyratio2)):
        notorietyratio2[i] /= sims
    for i in range(len(totalextort2)):
        totalextort2[i] /= sims
    for i in range(len(countextort2)):
        countextort2[i] /= sims
    for i in range(len(countbenefit2)):
        countbenefit2[i] /= sims
    for i in range(len(countpunish2)):
        countpunish2[i] /= sims
    for i in range(len(countsupport2)):
        countsupport2[i] /= sims
    for i in range(len(totalsupport2)):
        totalsupport2[i] /= sims
    for i in range(len(countdefend2)):
        countdefend2[i] /= sims
    for i in range(len(strength3)):
        strength3[i] /= sims
    for i in range(len(notorietyratio3)):
        notorietyratio3[i] /= sims
    for i in range(len(totalextort3)):
        totalextort3[i] /= sims
    for i in range(len(countextort3)):
        countextort3[i] /= sims
    for i in range(len(countbenefit3)):
        countbenefit3[i] /= sims
    for i in range(len(countpunish3)):
        countpunish3[i] /= sims
    for i in range(len(countsupport3)):
        countsupport3[i] /= sims
    for i in range(len(totalsupport3)):
        totalsupport3[i] /= sims
    for i in range(len(countdefend3)):
        countdefend3[i] /= sims
    for i in range(len(strength4)):
        strength4[i] /= sims
    for i in range(len(notorietyratio4)):
        notorietyratio4[i] /= sims
    for i in range(len(totalextort4)):
        totalextort4[i] /= sims
    for i in range(len(countextort4)):
        countextort4[i] /= sims
    for i in range(len(countbenefit4)):
        countbenefit4[i] /= sims
    for i in range(len(countpunish4)):
        countpunish4[i] /= sims
    for i in range(len(countsupport4)):
        countsupport4[i] /= sims
    for i in range(len(totalsupport4)):
        totalsupport4[i] /= sims
    for i in range(len(countdefend4)):
        countdefend4[i] /= sims
    for i in range(len(strength5)):
        strength5[i] /= sims
    for i in range(len(notorietyratio5)):
        notorietyratio5[i] /= sims
    for i in range(len(totalextort5)):
        totalextort5[i] /= sims
    for i in range(len(countextort5)):
        countextort5[i] /= sims
    for i in range(len(countbenefit5)):
        countbenefit5[i] /= sims
    for i in range(len(countpunish5)):
        countpunish5[i] /= sims
    for i in range(len(countsupport5)):
        countsupport5[i] /= sims
    for i in range(len(totalsupport5)):
        totalsupport5[i] /= sims
    for i in range(len(countdefend5)):
        countdefend5[i] /= sims
    for i in range(len(strength6)):
        strength6[i] /= sims
    for i in range(len(notorietyratio6)):
        notorietyratio6[i] /= sims
    for i in range(len(totalextort6)):
        totalextort6[i] /= sims
    for i in range(len(countextort6)):
        countextort6[i] /= sims
    for i in range(len(countbenefit6)):
        countbenefit6[i] /= sims
    for i in range(len(countpunish6)):
        countpunish6[i] /= sims
    for i in range(len(countsupport6)):
        countsupport6[i] /= sims
    for i in range(len(totalsupport6)):
        totalsupport6[i] /= sims
    for i in range(len(countdefend6)):
        countdefend6[i] /= sims
    for i in range(len(strength7)):
        strength7[i] /= sims
    for i in range(len(notorietyratio7)):
        notorietyratio7[i] /= sims
    for i in range(len(totalextort7)):
        totalextort7[i] /= sims
    for i in range(len(countextort7)):
        countextort7[i] /= sims
    for i in range(len(countbenefit7)):
        countbenefit7[i] /= sims
    for i in range(len(countpunish7)):
        countpunish7[i] /= sims
    for i in range(len(countsupport7)):
        countsupport7[i] /= sims
    for i in range(len(totalsupport7)):
        totalsupport7[i] /= sims
    for i in range(len(countdefend7)):
        countdefend7[i] /= sims
    for i in range(len(strength8)):
        strength8[i] /= sims
    for i in range(len(notorietyratio8)):
        notorietyratio8[i] /= sims
    for i in range(len(totalextort8)):
        totalextort8[i] /= sims
    for i in range(len(countextort8)):
        countextort8[i] /= sims
    for i in range(len(countbenefit8)):
        countbenefit8[i] /= sims
    for i in range(len(countpunish8)):
        countpunish8[i] /= sims
    for i in range(len(countsupport8)):
        countsupport8[i] /= sims
    for i in range(len(totalsupport8)):
        totalsupport8[i] /= sims
    for i in range(len(countdefend8)):
        countdefend8[i] /= sims
    for i in range(len(strength9)):
        strength9[i] /= sims
    for i in range(len(notorietyratio9)):
        notorietyratio9[i] /= sims
    for i in range(len(totalextort9)):
        totalextort9[i] /= sims
    for i in range(len(countextort9)):
        countextort9[i] /= sims
    for i in range(len(countbenefit9)):
        countbenefit9[i] /= sims
    for i in range(len(countpunish9)):
        countpunish9[i] /= sims
    for i in range(len(countsupport9)):
        countsupport9[i] /= sims
    for i in range(len(totalsupport9)):
        totalsupport9[i] /= sims
    for i in range(len(countdefend9)):
        countdefend9[i] /= sims
    for i in range(len(strength10)):
        strength10[i] /= sims
    for i in range(len(notorietyratio10)):
        notorietyratio10[i] /= sims
    for i in range(len(totalextort10)):
        totalextort10[i] /= sims
    for i in range(len(countextort10)):
        countextort10[i] /= sims
    for i in range(len(countbenefit10)):
        countbenefit10[i] /= sims
    for i in range(len(countpunish10)):
        countpunish10[i] /= sims
    for i in range(len(countsupport10)):
        countsupport10[i] /= sims
    for i in range(len(totalsupport10)):
        totalsupport10[i] /= sims
    for i in range(len(countdefend10)):
        countdefend10[i] /= sims
    for i in range(len(strength11)):
        strength11[i] /= sims
    for i in range(len(notorietyratio11)):
        notorietyratio11[i] /= sims
    for i in range(len(totalextort11)):
        totalextort11[i] /= sims
    for i in range(len(countextort11)):
        countextort11[i] /= sims
    for i in range(len(countbenefit11)):
        countbenefit11[i] /= sims
    for i in range(len(countpunish11)):
        countpunish11[i] /= sims
    for i in range(len(countsupport11)):
        countsupport11[i] /= sims
    for i in range(len(totalsupport11)):
        totalsupport11[i] /= sims
    for i in range(len(countdefend11)):
        countdefend11[i] /= sims
    for i in range(len(strength12)):
        strength12[i] /= sims
    for i in range(len(notorietyratio12)):
        notorietyratio12[i] /= sims
    for i in range(len(totalextort12)):
        totalextort12[i] /= sims
    for i in range(len(countextort12)):
        countextort12[i] /= sims
    for i in range(len(countbenefit12)):
        countbenefit12[i] /= sims
    for i in range(len(countpunish12)):
        countpunish12[i] /= sims
    for i in range(len(countsupport12)):
        countsupport12[i] /= sims
    for i in range(len(totalsupport12)):
        totalsupport12[i] /= sims
    for i in range(len(countdefend12)):
        countdefend12[i] /= sims
    for i in range(len(strength13)):
        strength13[i] /= sims
    for i in range(len(notorietyratio13)):
        notorietyratio13[i] /= sims
    for i in range(len(totalextort13)):
        totalextort13[i] /= sims
    for i in range(len(countextort13)):
        countextort13[i] /= sims
    for i in range(len(countbenefit13)):
        countbenefit13[i] /= sims
    for i in range(len(countpunish13)):
        countpunish13[i] /= sims
    for i in range(len(countsupport13)):
        countsupport13[i] /= sims
    for i in range(len(totalsupport13)):
        totalsupport13[i] /= sims
    for i in range(len(countdefend13)):
        countdefend13[i] /= sims
    for i in range(len(strength14)):
        strength14[i] /= sims
    for i in range(len(notorietyratio14)):
        notorietyratio14[i] /= sims
    for i in range(len(totalextort14)):
        totalextort14[i] /= sims
    for i in range(len(countextort14)):
        countextort14[i] /= sims
    for i in range(len(countbenefit14)):
        countbenefit14[i] /= sims
    for i in range(len(countpunish14)):
        countpunish14[i] /= sims
    for i in range(len(countsupport14)):
        countsupport14[i] /= sims
    for i in range(len(totalsupport14)):
        totalsupport14[i] /= sims
    for i in range(len(countdefend14)):
        countdefend14[i] /= sims
    for i in range(len(strength15)):
        strength15[i] /= sims
    for i in range(len(notorietyratio15)):
        notorietyratio15[i] /= sims
    for i in range(len(totalextort15)):
        totalextort15[i] /= sims
    for i in range(len(countextort15)):
        countextort15[i] /= sims
    for i in range(len(countbenefit15)):
        countbenefit15[i] /= sims
    for i in range(len(countpunish15)):
        countpunish15[i] /= sims
    for i in range(len(countsupport15)):
        countsupport15[i] /= sims
    for i in range(len(totalsupport15)):
        totalsupport15[i] /= sims
    for i in range(len(countdefend15)):
        countdefend15[i] /= sims
    for i in range(len(community1m1)):
        community1m1[i] /= sims
    for i in range(len(community2m1)):
        community2m1[i] /= sims
    for i in range(len(community3m1)):
        community3m1[i] /= sims
    for i in range(len(community4m1)):
        community4m1[i] /= sims
    for i in range(len(community5m1)):
        community5m1[i] /= sims
    for i in range(len(community6m1)):
        community6m1[i] /= sims
    for i in range(len(community7m1)):
        community7m1[i] /= sims
    for i in range(len(community8m1)):
        community8m1[i] /= sims
    for i in range(len(community9m1)):
        community9m1[i] /= sims
    for i in range(len(community10m1)):
        community10m1[i] /= sims
    for i in range(len(community11m1)):
        community11m1[i] /= sims
    for i in range(len(community12m1)):
        community12m1[i] /= sims
    for i in range(len(community13m1)):
        community13m1[i] /= sims
    for i in range(len(community14m1)):
        community14m1[i] /= sims
    for i in range(len(community15m1)):
        community15m1[i] /= sims
    for i in range(len(community1m2)):
        community1m2[i] /= sims
    for i in range(len(community2m2)):
        community2m2[i] /= sims
    for i in range(len(community3m2)):
        community3m2[i] /= sims
    for i in range(len(community4m2)):
        community4m2[i] /= sims
    for i in range(len(community5m2)):
        community5m2[i] /= sims
    for i in range(len(community6m2)):
        community6m2[i] /= sims
    for i in range(len(community7m2)):
        community7m2[i] /= sims
    for i in range(len(community8m2)):
        community8m2[i] /= sims
    for i in range(len(community9m2)):
        community9m2[i] /= sims
    for i in range(len(community10m2)):
        community10m2[i] /= sims
    for i in range(len(community11m2)):
        community11m2[i] /= sims
    for i in range(len(community12m2)):
        community12m2[i] /= sims
    for i in range(len(community13m2)):
        community13m2[i] /= sims
    for i in range(len(community14m2)):
        community14m2[i] /= sims
    for i in range(len(community15m2)):
        community15m2[i] /= sims
    for i in range(len(community1m3)):
        community1m3[i] /= sims
    for i in range(len(community2m3)):
        community2m3[i] /= sims
    for i in range(len(community3m3)):
        community3m3[i] /= sims
    for i in range(len(community4m3)):
        community4m3[i] /= sims
    for i in range(len(community5m3)):
        community5m3[i] /= sims
    for i in range(len(community6m3)):
        community6m3[i] /= sims
    for i in range(len(community7m3)):
        community7m3[i] /= sims
    for i in range(len(community8m3)):
        community8m3[i] /= sims
    for i in range(len(community9m3)):
        community9m3[i] /= sims
    for i in range(len(community10m3)):
        community10m3[i] /= sims
    for i in range(len(community11m3)):
        community11m3[i] /= sims
    for i in range(len(community12m3)):
        community12m3[i] /= sims
    for i in range(len(community13m3)):
        community13m3[i] /= sims
    for i in range(len(community14m3)):
        community14m3[i] /= sims
    for i in range(len(community15m3)):
        community15m3[i] /= sims
    for i in range(len(community1m4)):
        community1m4[i] /= sims
    for i in range(len(community2m4)):
        community2m4[i] /= sims
    for i in range(len(community3m4)):
        community3m4[i] /= sims
    for i in range(len(community4m4)):
        community4m4[i] /= sims
    for i in range(len(community5m4)):
        community5m4[i] /= sims
    for i in range(len(community6m4)):
        community6m4[i] /= sims
    for i in range(len(community7m4)):
        community7m4[i] /= sims
    for i in range(len(community8m4)):
        community8m4[i] /= sims
    for i in range(len(community9m4)):
        community9m4[i] /= sims
    for i in range(len(community10m4)):
        community10m4[i] /= sims
    for i in range(len(community11m4)):
        community11m4[i] /= sims
    for i in range(len(community12m4)):
        community12m4[i] /= sims
    for i in range(len(community13m4)):
        community13m4[i] /= sims
    for i in range(len(community14m4)):
        community14m4[i] /= sims
    for i in range(len(community15m4)):
        community15m4[i] /= sims
    for i in range(len(community1m5)):
        community1m5[i] /= sims
    for i in range(len(community2m5)):
        community2m5[i] /= sims
    for i in range(len(community3m5)):
        community3m5[i] /= sims
    for i in range(len(community4m5)):
        community4m5[i] /= sims
    for i in range(len(community5m5)):
        community5m5[i] /= sims
    for i in range(len(community6m5)):
        community6m5[i] /= sims
    for i in range(len(community7m5)):
        community7m5[i] /= sims
    for i in range(len(community8m5)):
        community8m5[i] /= sims
    for i in range(len(community9m5)):
        community9m5[i] /= sims
    for i in range(len(community10m5)):
        community10m5[i] /= sims
    for i in range(len(community11m5)):
        community11m5[i] /= sims
    for i in range(len(community12m5)):
        community12m5[i] /= sims
    for i in range(len(community13m5)):
        community13m5[i] /= sims
    for i in range(len(community14m5)):
        community14m5[i] /= sims
    for i in range(len(community15m5)):
        community15m5[i] /= sims
    for i in range(len(community1m6)):
        community1m6[i] /= sims
    for i in range(len(community2m6)):
        community2m6[i] /= sims
    for i in range(len(community3m6)):
        community3m6[i] /= sims
    for i in range(len(community4m6)):
        community4m6[i] /= sims
    for i in range(len(community5m6)):
        community5m6[i] /= sims
    for i in range(len(community6m6)):
        community6m6[i] /= sims
    for i in range(len(community7m6)):
        community7m6[i] /= sims
    for i in range(len(community8m6)):
        community8m6[i] /= sims
    for i in range(len(community9m6)):
        community9m6[i] /= sims
    for i in range(len(community10m6)):
        community10m6[i] /= sims
    for i in range(len(community11m6)):
        community11m6[i] /= sims
    for i in range(len(community12m6)):
        community12m6[i] /= sims
    for i in range(len(community13m6)):
        community13m6[i] /= sims
    for i in range(len(community14m6)):
        community14m6[i] /= sims
    for i in range(len(community15m6)):
        community15m6[i] /= sims
    for i in range(len(community1m7)):
        community1m7[i] /= sims
    for i in range(len(community2m7)):
        community2m7[i] /= sims
    for i in range(len(community3m7)):
        community3m7[i] /= sims
    for i in range(len(community4m7)):
        community4m7[i] /= sims
    for i in range(len(community5m7)):
        community5m7[i] /= sims
    for i in range(len(community6m7)):
        community6m7[i] /= sims
    for i in range(len(community7m7)):
        community7m7[i] /= sims
    for i in range(len(community8m7)):
        community8m7[i] /= sims
    for i in range(len(community9m7)):
        community9m7[i] /= sims
    for i in range(len(community10m7)):
        community10m7[i] /= sims
    for i in range(len(community11m7)):
        community11m7[i] /= sims
    for i in range(len(community12m7)):
        community12m7[i] /= sims
    for i in range(len(community13m7)):
        community13m7[i] /= sims
    for i in range(len(community14m7)):
        community14m7[i] /= sims
    for i in range(len(community15m7)):
        community15m7[i] /= sims
    for i in range(len(community1m8)):
        community1m8[i] /= sims
    for i in range(len(community2m8)):
        community2m8[i] /= sims
    for i in range(len(community3m8)):
        community3m8[i] /= sims
    for i in range(len(community4m8)):
        community4m8[i] /= sims
    for i in range(len(community5m8)):
        community5m8[i] /= sims
    for i in range(len(community6m8)):
        community6m8[i] /= sims
    for i in range(len(community7m8)):
        community7m8[i] /= sims
    for i in range(len(community8m8)):
        community8m8[i] /= sims
    for i in range(len(community9m8)):
        community9m8[i] /= sims
    for i in range(len(community10m8)):
        community10m8[i] /= sims
    for i in range(len(community11m8)):
        community11m8[i] /= sims
    for i in range(len(community12m8)):
        community12m8[i] /= sims
    for i in range(len(community13m8)):
        community13m8[i] /= sims
    for i in range(len(community14m8)):
        community14m8[i] /= sims
    for i in range(len(community15m8)):
        community15m8[i] /= sims
    for i in range(len(community1m9)):
        community1m9[i] /= sims
    for i in range(len(community2m9)):
        community2m9[i] /= sims
    for i in range(len(community3m9)):
        community3m9[i] /= sims
    for i in range(len(community4m9)):
        community4m9[i] /= sims
    for i in range(len(community5m9)):
        community5m9[i] /= sims
    for i in range(len(community6m9)):
        community6m9[i] /= sims
    for i in range(len(community7m9)):
        community7m9[i] /= sims
    for i in range(len(community8m9)):
        community8m9[i] /= sims
    for i in range(len(community9m9)):
        community9m9[i] /= sims
    for i in range(len(community10m9)):
        community10m9[i] /= sims
    for i in range(len(community11m9)):
        community11m9[i] /= sims
    for i in range(len(community12m9)):
        community12m9[i] /= sims
    for i in range(len(community13m9)):
        community13m9[i] /= sims
    for i in range(len(community14m9)):
        community14m9[i] /= sims
    for i in range(len(community15m9)):
        community15m9[i] /= sims
    for i in range(len(community1m10)):
        community1m10[i] /= sims
    for i in range(len(community2m10)):
        community2m10[i] /= sims
    for i in range(len(community3m10)):
        community3m10[i] /= sims
    for i in range(len(community4m10)):
        community4m10[i] /= sims
    for i in range(len(community5m10)):
        community5m10[i] /= sims
    for i in range(len(community6m10)):
        community6m10[i] /= sims
    for i in range(len(community7m10)):
        community7m10[i] /= sims
    for i in range(len(community8m10)):
        community8m10[i] /= sims
    for i in range(len(community9m10)):
        community9m10[i] /= sims
    for i in range(len(community10m10)):
        community10m10[i] /= sims
    for i in range(len(community11m10)):
        community11m10[i] /= sims
    for i in range(len(community12m10)):
        community12m10[i] /= sims
    for i in range(len(community13m10)):
        community13m10[i] /= sims
    for i in range(len(community14m10)):
        community14m10[i] /= sims
    for i in range(len(community15m10)):
        community15m10[i] /= sims
    for i in range(len(community1m11)):
        community1m11[i] /= sims
    for i in range(len(community2m11)):
        community2m11[i] /= sims
    for i in range(len(community3m11)):
        community3m11[i] /= sims
    for i in range(len(community4m11)):
        community4m11[i] /= sims
    for i in range(len(community5m11)):
        community5m11[i] /= sims
    for i in range(len(community6m11)):
        community6m11[i] /= sims
    for i in range(len(community7m11)):
        community7m11[i] /= sims
    for i in range(len(community8m11)):
        community8m11[i] /= sims
    for i in range(len(community9m11)):
        community9m11[i] /= sims
    for i in range(len(community10m11)):
        community10m11[i] /= sims
    for i in range(len(community11m11)):
        community11m11[i] /= sims
    for i in range(len(community12m11)):
        community12m11[i] /= sims
    for i in range(len(community13m11)):
        community13m11[i] /= sims
    for i in range(len(community14m11)):
        community14m11[i] /= sims
    for i in range(len(community15m11)):
        community15m11[i] /= sims
    for i in range(len(community1m12)):
        community1m12[i] /= sims
    for i in range(len(community2m12)):
        community2m12[i] /= sims
    for i in range(len(community3m12)):
        community3m12[i] /= sims
    for i in range(len(community4m12)):
        community4m12[i] /= sims
    for i in range(len(community5m12)):
        community5m12[i] /= sims
    for i in range(len(community6m12)):
        community6m12[i] /= sims
    for i in range(len(community7m12)):
        community7m12[i] /= sims
    for i in range(len(community8m12)):
        community8m12[i] /= sims
    for i in range(len(community9m12)):
        community9m12[i] /= sims
    for i in range(len(community10m12)):
        community10m12[i] /= sims
    for i in range(len(community11m12)):
        community11m12[i] /= sims
    for i in range(len(community12m12)):
        community12m12[i] /= sims
    for i in range(len(community13m12)):
        community13m12[i] /= sims
    for i in range(len(community14m12)):
        community14m12[i] /= sims
    for i in range(len(community15m12)):
        community15m12[i] /= sims
    for i in range(len(community1m13)):
        community1m13[i] /= sims
    for i in range(len(community2m13)):
        community2m13[i] /= sims
    for i in range(len(community3m13)):
        community3m13[i] /= sims
    for i in range(len(community4m13)):
        community4m13[i] /= sims
    for i in range(len(community5m13)):
        community5m13[i] /= sims
    for i in range(len(community6m13)):
        community6m13[i] /= sims
    for i in range(len(community7m13)):
        community7m13[i] /= sims
    for i in range(len(community8m13)):
        community8m13[i] /= sims
    for i in range(len(community9m13)):
        community9m13[i] /= sims
    for i in range(len(community10m13)):
        community10m13[i] /= sims
    for i in range(len(community11m13)):
        community11m13[i] /= sims
    for i in range(len(community12m13)):
        community12m13[i] /= sims
    for i in range(len(community13m13)):
        community13m13[i] /= sims
    for i in range(len(community14m13)):
        community14m13[i] /= sims
    for i in range(len(community15m13)):
        community15m13[i] /= sims
    for i in range(len(community1m14)):
        community1m14[i] /= sims
    for i in range(len(community2m14)):
        community2m14[i] /= sims
    for i in range(len(community3m14)):
        community3m14[i] /= sims
    for i in range(len(community4m14)):
        community4m14[i] /= sims
    for i in range(len(community5m14)):
        community5m14[i] /= sims
    for i in range(len(community6m14)):
        community6m14[i] /= sims
    for i in range(len(community7m14)):
        community7m14[i] /= sims
    for i in range(len(community8m14)):
        community8m14[i] /= sims
    for i in range(len(community9m14)):
        community9m14[i] /= sims
    for i in range(len(community10m14)):
        community10m14[i] /= sims
    for i in range(len(community11m14)):
        community11m14[i] /= sims
    for i in range(len(community12m14)):
        community12m14[i] /= sims
    for i in range(len(community13m14)):
        community13m14[i] /= sims
    for i in range(len(community14m14)):
        community14m14[i] /= sims
    for i in range(len(community15m14)):
        community15m14[i] /= sims
    for i in range(len(community1m15)):
        community1m15[i] /= sims
    for i in range(len(community2m15)):
        community2m15[i] /= sims
    for i in range(len(community3m15)):
        community3m15[i] /= sims
    for i in range(len(community4m15)):
        community4m15[i] /= sims
    for i in range(len(community5m15)):
        community5m15[i] /= sims
    for i in range(len(community6m15)):
        community6m15[i] /= sims
    for i in range(len(community7m15)):
        community7m15[i] /= sims
    for i in range(len(community8m15)):
        community8m15[i] /= sims
    for i in range(len(community9m15)):
        community9m15[i] /= sims
    for i in range(len(community10m15)):
        community10m15[i] /= sims
    for i in range(len(community11m15)):
        community11m15[i] /= sims
    for i in range(len(community12m15)):
        community12m15[i] /= sims
    for i in range(len(community13m15)):
        community13m15[i] /= sims
    for i in range(len(community14m15)):
        community14m15[i] /= sims
    for i in range(len(community15m15)):
        community15m15[i] /= sims
    for i in range(len(community1defend)):
        community1defend[i] /= sims
    for i in range(len(community2defend)):
        community2defend[i] /= sims
    for i in range(len(community3defend)):
        community3defend[i] /= sims
    for i in range(len(community4defend)):
        community4defend[i] /= sims
    for i in range(len(community5defend)):
        community5defend[i] /= sims
    for i in range(len(community6defend)):
        community6defend[i] /= sims
    for i in range(len(community7defend)):
        community7defend[i] /= sims
    for i in range(len(community8defend)):
        community8defend[i] /= sims
    for i in range(len(community9defend)):
        community9defend[i] /= sims
    for i in range(len(community10defend)):
        community10defend[i] /= sims
    for i in range(len(community11defend)):
        community11defend[i] /= sims
    for i in range(len(community12defend)):
        community12defend[i] /= sims
    for i in range(len(community13defend)):
        community13defend[i] /= sims
    for i in range(len(community14defend)):
        community14defend[i] /= sims
    for i in range(len(community15defend)):
        community15defend[i] /= sims
    for i in range(len(oneandtwo)):
        oneandtwo[i] /= sims
    for i in range(len(oneandthree)):
        oneandthree[i] /= sims
    for i in range(len(oneandfour)):
        oneandfour[i] /= sims
    for i in range(len(oneandfive)):
        oneandfive[i] /= sims
    for i in range(len(oneandsix)):
        oneandsix[i] /= sims
    for i in range(len(oneandseven)):
        oneandseven[i] /= sims
    for i in range(len(oneandeight)):
        oneandeight[i] /= sims
    for i in range(len(oneandnine)):
        oneandnine[i] /= sims
    for i in range(len(oneandten)):
        oneandten[i] /= sims
    for i in range(len(oneandeleven)):
        oneandeleven[i] /= sims
    for i in range(len(oneandtwelve)):
        oneandtwelve[i] /= sims
    for i in range(len(oneandthirteen)):
        oneandthirteen[i] /= sims
    for i in range(len(oneandfourteen)):
        oneandfourteen[i] /= sims
    for i in range(len(oneandfifteen)):
        oneandfifteen[i] /= sims
    for i in range(len(twoandthree)):
        twoandthree[i] /= sims
    for i in range(len(twoandfour)):
        twoandfour[i] /= sims
    for i in range(len(twoandfive)):
        twoandfive[i] /= sims
    for i in range(len(twoandsix)):
        twoandsix[i] /= sims
    for i in range(len(twoandseven)):
        twoandseven[i] /= sims
    for i in range(len(twoandeight)):
        twoandeight[i] /= sims
    for i in range(len(twoandnine)):
        twoandnine[i] /= sims
    for i in range(len(twoandten)):
        twoandten[i] /= sims
    for i in range(len(twoandeleven)):
        twoandeleven[i] /= sims
    for i in range(len(twoandtwelve)):
        twoandtwelve[i] /= sims
    for i in range(len(twoandthirteen)):
        twoandthirteen[i] /= sims
    for i in range(len(twoandfourteen)):
        twoandfourteen[i] /= sims
    for i in range(len(twoandfifteen)):
        twoandfifteen[i] /= sims
    for i in range(len(threeandfour)):
        threeandfour[i] /= sims
    for i in range(len(threeandfive)):
        threeandfive[i] /= sims
    for i in range(len(threeandsix)):
        threeandsix[i] /= sims
    for i in range(len(threeandseven)):
        threeandseven[i] /= sims
    for i in range(len(threeandeight)):
        threeandeight[i] /= sims
    for i in range(len(threeandnine)):
        threeandnine[i] /= sims
    for i in range(len(threeandten)):
        threeandten[i] /= sims
    for i in range(len(threeandeleven)):
        threeandeleven[i] /= sims
    for i in range(len(threeandtwelve)):
        threeandtwelve[i] /= sims
    for i in range(len(threeandthirteen)):
        threeandthirteen[i] /= sims
    for i in range(len(threeandfourteen)):
        threeandfourteen[i] /= sims
    for i in range(len(threeandfifteen)):
        threeandfifteen[i] /= sims
    for i in range(len(fourandfive)):
        fourandfive[i] /= sims
    for i in range(len(fourandsix)):
        fourandsix[i] /= sims
    for i in range(len(fourandseven)):
        fourandseven[i] /= sims
    for i in range(len(fourandeight)):
        fourandeight[i] /= sims
    for i in range(len(fourandnine)):
        fourandnine[i] /= sims
    for i in range(len(fourandten)):
        fourandten[i] /= sims
    for i in range(len(fourandeleven)):
        fourandeleven[i] /= sims
    for i in range(len(fourandtwelve)):
        fourandtwelve[i] /= sims
    for i in range(len(fourandthirteen)):
        fourandthirteen[i] /= sims
    for i in range(len(fourandfourteen)):
        fourandfourteen[i] /= sims
    for i in range(len(fourandfifteen)):
        fourandfifteen[i] /= sims
    for i in range(len(fiveandsix)):
        fiveandsix[i] /= sims
    for i in range(len(fiveandseven)):
        fiveandseven[i] /= sims
    for i in range(len(fiveandeight)):
        fiveandeight[i] /= sims
    for i in range(len(fiveandnine)):
        fiveandnine[i] /= sims
    for i in range(len(fiveandten)):
        fiveandten[i] /= sims
    for i in range(len(fiveandeleven)):
        fiveandeleven[i] /= sims
    for i in range(len(fiveandtwelve)):
        fiveandtwelve[i] /= sims
    for i in range(len(fiveandthirteen)):
        fiveandthirteen[i] /= sims
    for i in range(len(fiveandfourteen)):
        fiveandfourteen[i] /= sims
    for i in range(len(fiveandfifteen)):
        fiveandfifteen[i] /= sims
    for i in range(len(sixandseven)):
        sixandseven[i] /= sims
    for i in range(len(sixandeight)):
        sixandeight[i] /= sims
    for i in range(len(sixandnine)):
        sixandnine[i] /= sims
    for i in range(len(sixandten)):
        sixandten[i] /= sims
    for i in range(len(sixandeleven)):
        sixandeleven[i] /= sims
    for i in range(len(sixandtwelve)):
        sixandtwelve[i] /= sims
    for i in range(len(sixandthirteen)):
        sixandthirteen[i] /= sims
    for i in range(len(sixandfourteen)):
        sixandfourteen[i] /= sims
    for i in range(len(sixandfifteen)):
        sixandfifteen[i] /= sims
    for i in range(len(sevenandeight)):
        sevenandeight[i] /= sims
    for i in range(len(sevenandnine)):
        sevenandnine[i] /= sims
    for i in range(len(sevenandten)):
        sevenandten[i] /= sims
    for i in range(len(sevenandeleven)):
        sevenandeleven[i] /= sims
    for i in range(len(sevenandtwelve)):
        sevenandtwelve[i] /= sims
    for i in range(len(sevenandthirteen)):
        sevenandthirteen[i] /= sims
    for i in range(len(sevenandfourteen)):
        sevenandfourteen[i] /= sims
    for i in range(len(sevenandfifteen)):
        sevenandfifteen[i] /= sims
    for i in range(len(eightandnine)):
        eightandnine[i] /= sims
    for i in range(len(eightandten)):
        eightandten[i] /= sims
    for i in range(len(eightandeleven)):
        eightandeleven[i] /= sims
    for i in range(len(eightandtwelve)):
        eightandtwelve[i] /= sims
    for i in range(len(eightandthirteen)):
        eightandthirteen[i] /= sims
    for i in range(len(eightandfourteen)):
        eightandfourteen[i] /= sims
    for i in range(len(eightandfifteen)):
        eightandfifteen[i] /= sims
    for i in range(len(nineandten)):
        nineandten[i] /= sims
    for i in range(len(nineandeleven)):
        nineandeleven[i] /= sims
    for i in range(len(nineandtwelve)):
        nineandtwelve[i] /= sims
    for i in range(len(nineandthirteen)):
        nineandthirteen[i] /= sims
    for i in range(len(nineandfourteen)):
        nineandfourteen[i] /= sims
    for i in range(len(nineandfifteen)):
        nineandfifteen[i] /= sims
    for i in range(len(tenandeleven)):
        tenandeleven[i] /= sims
    for i in range(len(tenandtwelve)):
        tenandtwelve[i] /= sims
    for i in range(len(tenandthirteen)):
        tenandthirteen[i] /= sims
    for i in range(len(tenandfourteen)):
        tenandfourteen[i] /= sims
    for i in range(len(tenandfifteen)):
        tenandfifteen[i] /= sims
    for i in range(len(elevenandtwelve)):
        elevenandtwelve[i] /= sims
    for i in range(len(elevenandthirteen)):
        elevenandthirteen[i] /= sims
    for i in range(len(elevenandfourteen)):
        elevenandfourteen[i] /= sims
    for i in range(len(elevenandfifteen)):
        elevenandfifteen[i] /= sims
    for i in range(len(twelveandthirteen)):
        twelveandthirteen[i] /= sims
    for i in range(len(twelveandfourteen)):
        twelveandfourteen[i] /= sims
    for i in range(len(twelveandfifteen)):
        twelveandfifteen[i] /= sims
    for i in range(len(thirteenandfourteen)):
        thirteenandfourteen[i] /= sims
    for i in range(len(thirteenandfifteen)):
        thirteenandfifteen[i] /= sims
    for i in range(len(fourteenandfifteen)):
        fourteenandfifteen[i] /= sims

    print('Simulations Completed')
    print('Average strength1:', strength1[0])

    rounds = []
    i = 1
    while i <= len(strength1):
        rounds.append(i)
        i += 1
    df = DataFrame({'rounds': rounds, 'strength1': strength1, 'notorietyratio1': notorietyratio1, 'totalextort1': totalextort1, 'countextort1': countextort1, 'countbenefit1': countbenefit1, 'countpunish1': countpunish1, 'countsupport1': countsupport1, 'totalsupport1': totalsupport1, 'countdefend1': countdefend1, 'strength2': strength2, 'notorietyratio2': notorietyratio2, 'totalextort2': totalextort2, 'countextort2': countextort2, 'countbenefit2': countbenefit2, 'countpunish2': countpunish2, 'countsupport2': countsupport2, 'totalsupport2': totalsupport2, 'countdefend2': countdefend2, 'strength3': strength3, 'notorietyratio3': notorietyratio3, 'totalextort3': totalextort3, 'countextort3': countextort3, 'countbenefit3': countbenefit3, 'countpunish3': countpunish3, 'countsupport3': countsupport3, 'totalsupport3': totalsupport3, 'countdefend3': countdefend3, 'strength4': strength4, 'notorietyratio4': notorietyratio4, 'totalextort4': totalextort4, 'countextort4': countextort4, 'countbenefit4': countbenefit4, 'countpunish4': countpunish4, 'countsupport4': countsupport4, 'totalsupport4': totalsupport4, 'countdefend4': countdefend4, 'strength5': strength5, 'notorietyratio5': notorietyratio5, 'totalextort5': totalextort5, 'countextort5': countextort5, 'countbenefit5': countbenefit5, 'countpunish5': countpunish5, 'countsupport5': countsupport5, 'totalsupport5': totalsupport5, 'countdefend5': countdefend5, 'strength6': strength6, 'notorietyratio6': notorietyratio6, 'totalextort6': totalextort6, 'countextort6': countextort6, 'countbenefit6': countbenefit6, 'countpunish6': countpunish6, 'countsupport6': countsupport6, 'totalsupport6': totalsupport6, 'countdefend6': countdefend6, 'strength7': strength7, 'notorietyratio7': notorietyratio7, 'totalextort7': totalextort7, 'countextort7': countextort7, 'countbenefit7': countbenefit7, 'countpunish7': countpunish7, 'countsupport7': countsupport7, 'totalsupport7': totalsupport7, 'countdefend7': countdefend7, 'strength8': strength8, 'notorietyratio8': notorietyratio8, 'totalextort8': totalextort8, 'countextort8': countextort8, 'countbenefit8': countbenefit8, 'countpunish8': countpunish8, 'countsupport8': countsupport8, 'totalsupport8': totalsupport8, 'countdefend8': countdefend8, 'strength9': strength9, 'notorietyratio9': notorietyratio9, 'totalextort9': totalextort9, 'countextort9': countextort9, 'countbenefit9': countbenefit9, 'countpunish9': countpunish9, 'countsupport9': countsupport9, 'totalsupport9': totalsupport9, 'countdefend9': countdefend9, 'strength10': strength10, 'notorietyratio10': notorietyratio10, 'totalextort10': totalextort10, 'countextort10': countextort10, 'countbenefit10': countbenefit10, 'countpunish10': countpunish10, 'countsupport10': countsupport10, 'totalsupport10': totalsupport10, 'countdefend10': countdefend10, 'strength11': strength11, 'notorietyratio11': notorietyratio11, 'totalextort11': totalextort11, 'countextort11': countextort11, 'countbenefit11': countbenefit11, 'countpunish11': countpunish11, 'countsupport11': countsupport11, 'totalsupport11': totalsupport11, 'countdefend11': countdefend11, 'strength12': strength12, 'notorietyratio12': notorietyratio12, 'totalextort12': totalextort12, 'countextort12': countextort12, 'countbenefit12': countbenefit12, 'countpunish12': countpunish12, 'countsupport12': countsupport12, 'totalsupport12': totalsupport12, 'countdefend12': countdefend12, 'strength13': strength13, 'notorietyratio13': notorietyratio13, 'totalextort13': totalextort13, 'countextort13': countextort13, 'countbenefit13': countbenefit13, 'countpunish13': countpunish13, 'countsupport13': countsupport13, 'totalsupport13': totalsupport13, 'countdefend13': countdefend13, 'strength14': strength14, 'notorietyratio14': notorietyratio14, 'totalextort14': totalextort14, 'countextort14': countextort14, 'countbenefit14': countbenefit14, 'countpunish14': countpunish14, 'countsupport14': countsupport14, 'totalsupport14': totalsupport14, 'countdefend14': countdefend14, 'strength15': strength15, 'notorietyratio15': notorietyratio15, 'totalextort15': totalextort15, 'countextort15': countextort15, 'countbenefit15': countbenefit15, 'countpunish15': countpunish15, 'countsupport15': countsupport15, 'totalsupport15': totalsupport15, 'countdefend15': countdefend15, 'community1m1': community1m1, 'community2m1': community2m1, 'community3m1': community3m1, 'community4m1': community4m1, 'community5m1': community5m1, 'community6m1': community6m1, 'community7m1': community7m1, 'community8m1': community8m1, 'community9m1': community9m1, 'community10m1': community10m1, 'community11m1': community11m1, 'community12m1': community12m1, 'community13m1': community13m1, 'community14m1': community14m1, 'community15m1': community15m1, 'community1m2': community1m2, 'community2m2': community2m2, 'community3m2': community3m2, 'community4m2': community4m2, 'community5m2': community5m2, 'community6m2': community6m2, 'community7m2': community7m2, 'community8m2': community8m2, 'community9m2': community9m2, 'community10m2': community10m2, 'community11m2': community11m2, 'community12m2': community12m2, 'community13m2': community13m2, 'community14m2': community14m2, 'community15m2': community15m2, 'community1m3': community1m3, 'community2m3': community2m3, 'community3m3': community3m3, 'community4m3': community4m3, 'community5m3': community5m3, 'community6m3': community6m3, 'community7m3': community7m3, 'community8m3': community8m3, 'community9m3': community9m3, 'community10m3': community10m3, 'community11m3': community11m3, 'community12m3': community12m3, 'community13m3': community13m3, 'community14m3': community14m3, 'community15m3': community15m3, 'community1m4': community1m4, 'community2m4': community2m4, 'community3m4': community3m4, 'community4m4': community4m4, 'community5m4': community5m4, 'community6m4': community6m4, 'community7m4': community7m4, 'community8m4': community8m4, 'community9m4': community9m4, 'community10m4': community10m4, 'community11m4': community11m4, 'community12m4': community12m4, 'community13m4': community13m4, 'community14m4': community14m4, 'community15m4': community15m4, 'community1m5': community1m5, 'community2m5': community2m5, 'community3m5': community3m5, 'community4m5': community4m5, 'community5m5': community5m5, 'community6m5': community6m5, 'community7m5': community7m5, 'community8m5': community8m5, 'community9m5': community9m5, 'community10m5': community10m5, 'community11m5': community11m5, 'community12m5': community12m5, 'community13m5': community13m5, 'community14m5': community14m5, 'community15m5': community15m5, 'community1m6': community1m6, 'community2m6': community2m6, 'community3m6': community3m6, 'community4m6': community4m6, 'community5m6': community5m6, 'community6m6': community6m6, 'community7m6': community7m6, 'community8m6': community8m6, 'community9m6': community9m6, 'community10m6': community10m6, 'community11m6': community11m6, 'community12m6': community12m6, 'community13m6': community13m6, 'community14m6': community14m6, 'community15m6': community15m6, 'community1m7': community1m7, 'community2m7': community2m7, 'community3m7': community3m7, 'community4m7': community4m7, 'community5m7': community5m7, 'community6m7': community6m7, 'community7m7': community7m7, 'community8m7': community8m7, 'community9m7': community9m7, 'community10m7': community10m7, 'community11m7': community11m7, 'community12m7': community12m7, 'community13m7': community13m7, 'community14m7': community14m7, 'community15m7': community15m7, 'community1m8': community1m8, 'community2m8': community2m8, 'community3m8': community3m8, 'community4m8': community4m8, 'community5m8': community5m8, 'community6m8': community6m8, 'community7m8': community7m8, 'community8m8': community8m8, 'community9m8': community9m8, 'community10m8': community10m8, 'community11m8': community11m8, 'community12m8': community12m8, 'community13m8': community13m8, 'community14m8': community14m8, 'community15m8': community15m8, 'community1m9': community1m9, 'community2m9': community2m9, 'community3m9': community3m9, 'community4m9': community4m9, 'community5m9': community5m9, 'community6m9': community6m9, 'community7m9': community7m9, 'community8m9': community8m9, 'community9m9': community9m9, 'community10m9': community10m9, 'community11m9': community11m9, 'community12m9': community12m9, 'community13m9': community13m9, 'community14m9': community14m9, 'community15m9': community15m9, 'community1m10': community1m10, 'community2m10': community2m10, 'community3m10': community3m10, 'community4m10': community4m10, 'community5m10': community5m10, 'community6m10': community6m10, 'community7m10': community7m10, 'community8m10': community8m10, 'community9m10': community9m10, 'community10m10': community10m10, 'community11m10': community11m10, 'community12m10': community12m10, 'community13m10': community13m10, 'community14m10': community14m10, 'community15m10': community15m10, 'community1m11': community1m11, 'community2m11': community2m11, 'community3m11': community3m11, 'community4m11': community4m11, 'community5m11': community5m11, 'community6m11': community6m11, 'community7m11': community7m11, 'community8m11': community8m11, 'community9m11': community9m11, 'community10m11': community10m11, 'community11m11': community11m11, 'community12m11': community12m11, 'community13m11': community13m11, 'community14m11': community14m11, 'community15m11': community15m11, 'community1m12': community1m12, 'community2m12': community2m12, 'community3m12': community3m12, 'community4m12': community4m12, 'community5m12': community5m12, 'community6m12': community6m12, 'community7m12': community7m12, 'community8m12': community8m12, 'community9m12': community9m12, 'community10m12': community10m12, 'community11m12': community11m12, 'community12m12': community12m12, 'community13m12': community13m12, 'community14m12': community14m12, 'community15m12': community15m12, 'community1m13': community1m13, 'community2m13': community2m13, 'community3m13': community3m13, 'community4m13': community4m13, 'community5m13': community5m13, 'community6m13': community6m13, 'community7m13': community7m13, 'community8m13': community8m13, 'community9m13': community9m13, 'community10m13': community10m13, 'community11m13': community11m13, 'community12m13': community12m13, 'community13m13': community13m13, 'community14m13': community14m13, 'community15m13': community15m13, 'community1m14': community1m14, 'community2m14': community2m14, 'community3m14': community3m14, 'community4m14': community4m14, 'community5m14': community5m14, 'community6m14': community6m14, 'community7m14': community7m14, 'community8m14': community8m14, 'community9m14': community9m14, 'community10m14': community10m14, 'community11m14': community11m14, 'community12m14': community12m14, 'community13m14': community13m14, 'community14m14': community14m14, 'community15m14': community15m14, 'community1m15': community1m15, 'community2m15': community2m15, 'community3m15': community3m15, 'community4m15': community4m15, 'community5m15': community5m15, 'community6m15': community6m15, 'community7m15': community7m15, 'community8m15': community8m15, 'community9m15': community9m15, 'community10m15': community10m15, 'community11m15': community11m15, 'community12m15': community12m15, 'community13m15': community13m15, 'community14m15': community14m15, 'community15m15': community15m15, 'community1defend': community1defend, 'community2defend': community2defend, 'community3defend': community3defend, 'community4defend': community4defend, 'community5defend': community5defend, 'community6defend': community6defend, 'community7defend': community7defend, 'community8defend': community8defend, 'community9defend': community9defend, 'community10defend': community10defend, 'community11defend': community11defend, 'community12defend': community12defend, 'community13defend': community13defend, 'community14defend': community14defend, 'community15defend': community15defend, 'oneandtwo': oneandtwo, 'oneandthree': oneandthree, 'twoandthree': twoandthree, 'oneandfour': oneandfour, 'oneandfive': oneandfive, 'oneandsix': oneandsix, 'oneandseven': oneandseven, 'oneandeight': oneandeight, 'oneandnine': oneandnine, 'oneandten': oneandten, 'oneandeleven': oneandeleven, 'oneandtwelve': oneandtwelve, 'oneandthirteen': oneandthirteen, 'oneandfourteen': oneandfourteen, 'oneandfifteen': oneandfifteen, 'twoandfour': twoandfour, 'twoandfive': twoandfive, 'twoandsix': twoandsix, 'twoandseven': twoandseven, 'twoandeight': twoandeight, 'twoandnine': twoandnine, 'twoandten': twoandten, 'twoandeleven': twoandeleven, 'twoandtwelve': twoandtwelve, 'twoandthirteen': twoandthirteen, 'twoandfourteen': twoandfourteen, 'twoandfifteen': twoandfifteen, 'threeandfour': threeandfour, 'threeandfive': threeandfive, 'threeandsix': threeandsix, 'threeandseven': threeandseven, 'threeandeight': threeandeight, 'threeandnine': threeandnine, 'threeandten': threeandten, 'threeandeleven': threeandeleven, 'threeandtwelve': threeandtwelve, 'threeandthirteen': threeandthirteen, 'threeandfourteen': threeandfourteen, 'threeandfifteen': threeandfifteen, 'fourandfive': fourandfive, 'fourandsix': fourandsix, 'fourandseven': fourandseven, 'fourandeight': fourandeight, 'fourandnine': fourandnine, 'fourandten': fourandten, 'fourandeleven': fourandeleven, 'fourandtwelve': fourandtwelve, 'fourandthirteen': fourandthirteen, 'fourandfourteen': fourandfourteen, 'fourandfifteen': fourandfifteen, 'fiveandsix': fiveandsix, 'fiveandseven': fiveandseven, 'fiveandeight': fiveandeight, 'fiveandnine': fiveandnine, 'fiveandten': fiveandten, 'fiveandeleven': fiveandeleven, 'fiveandtwelve': fiveandtwelve, 'fiveandthirteen': fiveandthirteen, 'fiveandfourteen': fiveandfourteen, 'fiveandfifteen': fiveandfifteen, 'sixandseven': sixandseven, 'sixandeight': sixandeight, 'sixandnine': sixandnine, 'sixandten': sixandten, 'sixandeleven': sixandeleven, 'sixandtwelve': sixandtwelve, 'sixandthirteen': sixandthirteen, 'sixandfourteen': sixandfourteen, 'sixandfifteen': sixandfifteen, 'sevenandeight': sevenandeight, 'sevenandnine': sevenandnine, 'sevenandten': sevenandten, 'sevenandeleven': sevenandeleven, 'sevenandtwelve': sevenandtwelve, 'sevenandthirteen': sevenandthirteen, 'sevenandfourteen': sevenandfourteen, 'sevenandfifteen': sevenandfifteen, 'eightandnine': eightandnine, 'eightandten': eightandten, 'eightandeleven': eightandeleven, 'eightandtwelve': eightandtwelve, 'eightandthirteen': eightandthirteen, 'eightandfourteen': eightandfourteen, 'eightandfifteen': eightandfifteen, 'nineandten': nineandten, 'nineandeleven': nineandeleven, 'nineandtwelve': nineandtwelve, 'nineandthirteen': nineandthirteen, 'nineandfourteen': nineandfourteen, 'nineandfifteen': nineandfifteen, 'tenandeleven': tenandeleven, 'tenandtwelve': tenandtwelve, 'tenandthirteen': tenandthirteen, 'tenandfourteen': tenandfourteen, 'tenandfifteen': tenandfifteen, 'elevenandtwelve': elevenandtwelve, 'elevenandthirteen': elevenandthirteen, 'elevenandfourteen': elevenandfourteen, 'elevenandfifteen': elevenandfifteen, 'twelveandthirteen': twelveandthirteen, 'twelveandfourteen': twelveandfourteen, 'twelveandfifteen': twelveandfifteen, 'thirteenandfourteen': thirteenandfourteen, 'thirteenandfifteen': thirteenandfifteen, 'fourteenandfifteen': fourteenandfifteen})
    df = df[['rounds', 'strength1', 'notorietyratio1', 'totalextort1', 'countextort1', 'countbenefit1', 'countpunish1', 'countsupport1', 'totalsupport1', 'countdefend1', 'strength2', 'notorietyratio2', 'totalextort2', 'countextort2', 'countbenefit2', 'countpunish2', 'countsupport2', 'totalsupport2', 'countdefend2', 'strength3', 'notorietyratio3', 'totalextort3', 'countextort3', 'countbenefit3', 'countpunish3', 'countsupport3', 'totalsupport3', 'countdefend3', 'strength4', 'notorietyratio4', 'totalextort4', 'countextort4', 'countbenefit4', 'countpunish4', 'countsupport4', 'totalsupport4', 'countdefend4', 'strength5', 'notorietyratio5', 'totalextort5', 'countextort5', 'countbenefit5', 'countpunish5', 'countsupport5', 'totalsupport5', 'countdefend5', 'strength6', 'notorietyratio6', 'totalextort6', 'countextort6', 'countbenefit6', 'countpunish6', 'countsupport6', 'totalsupport6', 'countdefend6', 'strength7', 'notorietyratio7', 'totalextort7', 'countextort7', 'countbenefit7', 'countpunish7', 'countsupport7', 'totalsupport7', 'countdefend7', 'strength8', 'notorietyratio8', 'totalextort8', 'countextort8', 'countbenefit8', 'countpunish8', 'countsupport8', 'totalsupport8', 'countdefend8', 'strength9', 'notorietyratio9', 'totalextort9', 'countextort9', 'countbenefit9', 'countpunish9', 'countsupport9', 'totalsupport9', 'countdefend9', 'strength10', 'notorietyratio10', 'totalextort10', 'countextort10', 'countbenefit10', 'countpunish10', 'countsupport10', 'totalsupport10', 'countdefend10', 'strength11', 'notorietyratio11', 'totalextort11', 'countextort11', 'countbenefit11', 'countpunish11', 'countsupport11', 'totalsupport11', 'countdefend11', 'strength12', 'notorietyratio12', 'totalextort12', 'countextort12', 'countbenefit12', 'countpunish12', 'countsupport12', 'totalsupport12', 'countdefend12', 'strength13', 'notorietyratio13', 'totalextort13', 'countextort13', 'countbenefit13', 'countpunish13', 'countsupport13', 'totalsupport13', 'countdefend13', 'strength14', 'notorietyratio14', 'totalextort14', 'countextort14', 'countbenefit14', 'countpunish14', 'countsupport14', 'totalsupport14', 'countdefend14', 'strength15', 'notorietyratio15', 'totalextort15', 'countextort15', 'countbenefit15', 'countpunish15', 'countsupport15', 'totalsupport15', 'countdefend15', 'community1m1', 'community2m1', 'community3m1', 'community4m1', 'community5m1', 'community6m1', 'community7m1', 'community8m1', 'community9m1', 'community10m1', 'community11m1', 'community12m1', 'community13m1', 'community14m1', 'community15m1', 'community1m2', 'community2m2', 'community3m2', 'community4m2', 'community5m2', 'community6m2', 'community7m2', 'community8m2', 'community9m2', 'community10m2', 'community11m2', 'community12m2', 'community13m2', 'community14m2', 'community15m2', 'community1m3', 'community2m3', 'community3m3', 'community4m3', 'community5m3', 'community6m3', 'community7m3', 'community8m3', 'community9m3', 'community10m3', 'community11m3', 'community12m3', 'community13m3', 'community14m3', 'community15m3', 'community1m4', 'community2m4', 'community3m4', 'community4m4', 'community5m4', 'community6m4', 'community7m4', 'community8m4', 'community9m4', 'community10m4', 'community11m4', 'community12m4', 'community13m4', 'community14m4', 'community15m4', 'community1m5', 'community2m5', 'community3m5', 'community4m5', 'community5m5', 'community6m5', 'community7m5', 'community8m5', 'community9m5', 'community10m5', 'community11m5', 'community12m5', 'community13m5', 'community14m5', 'community15m5', 'community1m6', 'community2m6', 'community3m6', 'community4m6', 'community5m6', 'community6m6', 'community7m6', 'community8m6', 'community9m6', 'community10m6', 'community11m6', 'community12m6', 'community13m6', 'community14m6', 'community15m6', 'community1m7', 'community2m7', 'community3m7', 'community4m7', 'community5m7', 'community6m7', 'community7m7', 'community8m7', 'community9m7', 'community10m7', 'community11m7', 'community12m7', 'community13m7', 'community14m7', 'community15m7', 'community1m8', 'community2m8', 'community3m8', 'community4m8', 'community5m8', 'community6m8', 'community7m8', 'community8m8', 'community9m8', 'community10m8', 'community11m8', 'community12m8', 'community13m8', 'community14m8', 'community15m8', 'community1m9', 'community2m9', 'community3m9', 'community4m9', 'community5m9', 'community6m9', 'community7m9', 'community8m9', 'community9m9', 'community10m9', 'community11m9', 'community12m9', 'community13m9', 'community14m9', 'community15m9', 'community1m10', 'community2m10', 'community3m10', 'community4m10', 'community5m10', 'community6m10', 'community7m10', 'community8m10', 'community9m10', 'community10m10', 'community11m10', 'community12m10', 'community13m10', 'community14m10', 'community15m10', 'community1m11', 'community2m11', 'community3m11', 'community4m11', 'community5m11', 'community6m11', 'community7m11', 'community8m11', 'community9m11', 'community10m11', 'community11m11', 'community12m11', 'community13m11', 'community14m11', 'community15m11', 'community1m12', 'community2m12', 'community3m12', 'community4m12', 'community5m12', 'community6m12', 'community7m12', 'community8m12', 'community9m12', 'community10m12', 'community11m12', 'community12m12', 'community13m12', 'community14m12', 'community15m12', 'community1m13', 'community2m13', 'community3m13', 'community4m13', 'community5m13', 'community6m13', 'community7m13', 'community8m13', 'community9m13', 'community10m13', 'community11m13', 'community12m13', 'community13m13', 'community14m13', 'community15m13', 'community1m14', 'community2m14', 'community3m14', 'community4m14', 'community5m14', 'community6m14', 'community7m14', 'community8m14', 'community9m14', 'community10m14', 'community11m14', 'community12m14', 'community13m14', 'community14m14', 'community15m14', 'community1m15', 'community2m15', 'community3m15', 'community4m15', 'community5m15', 'community6m15', 'community7m15', 'community8m15', 'community9m15', 'community10m15', 'community11m15', 'community12m15', 'community13m15', 'community14m15', 'community15m15', 'community1defend', 'community2defend', 'community3defend', 'community4defend', 'community5defend', 'community6defend', 'community7defend', 'community8defend', 'community9defend', 'community10defend', 'community11defend', 'community12defend', 'community13defend', 'community14defend', 'community15defend', 'oneandtwo', 'oneandthree', 'oneandfour', 'oneandfive', 'oneandsix', 'oneandseven', 'oneandeight', 'oneandnine', 'oneandten', 'oneandeleven', 'oneandtwelve', 'oneandthirteen', 'oneandfourteen', 'oneandfifteen', 'twoandthree', 'twoandfour', 'twoandfive', 'twoandsix', 'twoandseven', 'twoandeight', 'twoandnine', 'twoandten', 'twoandeleven', 'twoandtwelve', 'twoandthirteen', 'twoandfourteen', 'twoandfifteen', 'threeandfour', 'threeandfive', 'threeandsix', 'threeandseven', 'threeandeight', 'threeandnine', 'threeandten', 'threeandeleven', 'threeandtwelve', 'threeandthirteen', 'threeandfourteen', 'threeandfifteen', 'fourandfive', 'fourandsix', 'fourandseven', 'fourandeight', 'fourandnine', 'fourandten', 'fourandeleven', 'fourandtwelve', 'fourandthirteen', 'fourandfourteen', 'fourandfifteen', 'fiveandsix', 'fiveandseven', 'fiveandeight', 'fiveandnine', 'fiveandten', 'fiveandeleven', 'fiveandtwelve', 'fiveandthirteen', 'fiveandfourteen', 'fiveandfifteen', 'sixandseven', 'sixandeight', 'sixandnine', 'sixandten', 'sixandeleven', 'sixandtwelve', 'sixandthirteen', 'sixandfourteen', 'sixandfifteen', 'sevenandeight', 'sevenandnine', 'sevenandten', 'sevenandeleven', 'sevenandtwelve', 'sevenandthirteen', 'sevenandfourteen', 'sevenandfifteen', 'eightandnine', 'eightandten', 'eightandeleven', 'eightandtwelve', 'eightandthirteen', 'eightandfourteen', 'eightandfifteen', 'nineandten', 'nineandeleven', 'nineandtwelve', 'nineandthirteen', 'nineandfourteen', 'nineandfifteen', 'tenandeleven', 'tenandtwelve', 'tenandthirteen', 'tenandfourteen', 'tenandfifteen', 'elevenandtwelve', 'elevenandthirteen', 'elevenandfourteen', 'elevenandfifteen', 'twelveandthirteen', 'twelveandfourteen', 'twelveandfifteen', 'thirteenandfourteen', 'thirteenandfifteen', 'fourteenandfifteen']]
    print('Data Saved')
    return df
