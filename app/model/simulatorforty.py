import subprocess
import re
import copy
from app.model.militantdata import militantdata
from app.model.dfdata import dfdata
from app.model.main import rounds

blanks = []
i = 0
while i < rounds:
    blanks.append(0)
    i += 1
blanks = copy.deepcopy(blanks)

allstrength1 = []
allnotorietyratio1 = []
alltotalextort1 = []
allcountextort1 = []
allcountbenefit1 = []
allcountpunish1 = []
allcountsupport1 = []
alltotalsupport1 = []
allcountdefend1 = []
allstrength2 = []
allnotorietyratio2 = []
alltotalextort2 = []
allcountextort2 = []
allcountbenefit2 = []
allcountpunish2 = []
allcountsupport2 = []
alltotalsupport2 = []
allcountdefend2 = []
allstrength3 = []
allnotorietyratio3 = []
alltotalextort3 = []
allcountextort3 = []
allcountbenefit3 = []
allcountpunish3 = []
allcountsupport3 = []
alltotalsupport3 = []
allcountdefend3 = []
allstrength4 = []
allnotorietyratio4 = []
alltotalextort4 = []
allcountextort4 = []
allcountbenefit4 = []
allcountpunish4 = []
allcountsupport4 = []
alltotalsupport4 = []
allcountdefend4 = []
allstrength5 = []
allnotorietyratio5 = []
alltotalextort5 = []
allcountextort5 = []
allcountbenefit5 = []
allcountpunish5 = []
allcountsupport5 = []
alltotalsupport5 = []
allcountdefend5 = []
allstrength6 = []
allnotorietyratio6 = []
alltotalextort6 = []
allcountextort6 = []
allcountbenefit6 = []
allcountpunish6 = []
allcountsupport6 = []
alltotalsupport6 = []
allcountdefend6 = []
allstrength7 = []
allnotorietyratio7 = []
alltotalextort7 = []
allcountextort7 = []
allcountbenefit7 = []
allcountpunish7 = []
allcountsupport7 = []
alltotalsupport7 = []
allcountdefend7 = []
allstrength8 = []
allnotorietyratio8 = []
alltotalextort8 = []
allcountextort8 = []
allcountbenefit8 = []
allcountpunish8 = []
allcountsupport8 = []
alltotalsupport8 = []
allcountdefend8 = []
allstrength9 = []
allnotorietyratio9 = []
alltotalextort9 = []
allcountextort9 = []
allcountbenefit9 = []
allcountpunish9 = []
allcountsupport9 = []
alltotalsupport9 = []
allcountdefend9 = []
allstrength10 = []
allnotorietyratio10 = []
alltotalextort10 = []
allcountextort10 = []
allcountbenefit10 = []
allcountpunish10 = []
allcountsupport10 = []
alltotalsupport10 = []
allcountdefend10 = []
allstrength11 = []
allnotorietyratio11 = []
alltotalextort11 = []
allcountextort11 = []
allcountbenefit11 = []
allcountpunish11 = []
allcountsupport11 = []
alltotalsupport11 = []
allcountdefend11 = []
allstrength12 = []
allnotorietyratio12 = []
alltotalextort12 = []
allcountextort12 = []
allcountbenefit12 = []
allcountpunish12 = []
allcountsupport12 = []
alltotalsupport12 = []
allcountdefend12 = []
allstrength13 = []
allnotorietyratio13 = []
alltotalextort13 = []
allcountextort13 = []
allcountbenefit13 = []
allcountpunish13 = []
allcountsupport13 = []
alltotalsupport13 = []
allcountdefend13 = []
allstrength14 = []
allnotorietyratio14 = []
alltotalextort14 = []
allcountextort14 = []
allcountbenefit14 = []
allcountpunish14 = []
allcountsupport14 = []
alltotalsupport14 = []
allcountdefend14 = []
allstrength15 = []
allnotorietyratio15 = []
alltotalextort15 = []
allcountextort15 = []
allcountbenefit15 = []
allcountpunish15 = []
allcountsupport15 = []
alltotalsupport15 = []
allcountdefend15 = []

allcommunity1m1 = []
allcommunity2m1 = []
allcommunity3m1 = []
allcommunity4m1 = []
allcommunity5m1 = []
allcommunity6m1 = []
allcommunity7m1 = []
allcommunity8m1 = []
allcommunity9m1 = []
allcommunity10m1 = []
allcommunity11m1 = []
allcommunity12m1 = []
allcommunity13m1 = []
allcommunity14m1 = []
allcommunity15m1 = []
allcommunity1m2 = []
allcommunity2m2 = []
allcommunity3m2 = []
allcommunity4m2 = []
allcommunity5m2 = []
allcommunity6m2 = []
allcommunity7m2 = []
allcommunity8m2 = []
allcommunity9m2 = []
allcommunity10m2 = []
allcommunity11m2 = []
allcommunity12m2 = []
allcommunity13m2 = []
allcommunity14m2 = []
allcommunity15m2 = []
allcommunity1m3 = []
allcommunity2m3 = []
allcommunity3m3 = []
allcommunity4m3 = []
allcommunity5m3 = []
allcommunity6m3 = []
allcommunity7m3 = []
allcommunity8m3 = []
allcommunity9m3 = []
allcommunity10m3 = []
allcommunity11m3 = []
allcommunity12m3 = []
allcommunity13m3 = []
allcommunity14m3 = []
allcommunity15m3 = []
allcommunity1m4 = []
allcommunity2m4 = []
allcommunity3m4 = []
allcommunity4m4 = []
allcommunity5m4 = []
allcommunity6m4 = []
allcommunity7m4 = []
allcommunity8m4 = []
allcommunity9m4 = []
allcommunity10m4 = []
allcommunity11m4 = []
allcommunity12m4 = []
allcommunity13m4 = []
allcommunity14m4 = []
allcommunity15m4 = []
allcommunity1m5 = []
allcommunity2m5 = []
allcommunity3m5 = []
allcommunity4m5 = []
allcommunity5m5 = []
allcommunity6m5 = []
allcommunity7m5 = []
allcommunity8m5 = []
allcommunity9m5 = []
allcommunity10m5 = []
allcommunity11m5 = []
allcommunity12m5 = []
allcommunity13m5 = []
allcommunity14m5 = []
allcommunity15m5 = []
allcommunity1m6 = []
allcommunity2m6 = []
allcommunity3m6 = []
allcommunity4m6 = []
allcommunity5m6 = []
allcommunity6m6 = []
allcommunity7m6 = []
allcommunity8m6 = []
allcommunity9m6 = []
allcommunity10m6 = []
allcommunity11m6 = []
allcommunity12m6 = []
allcommunity13m6 = []
allcommunity14m6 = []
allcommunity15m6 = []
allcommunity1m7 = []
allcommunity2m7 = []
allcommunity3m7 = []
allcommunity4m7 = []
allcommunity5m7 = []
allcommunity6m7 = []
allcommunity7m7 = []
allcommunity8m7 = []
allcommunity9m7 = []
allcommunity10m7 = []
allcommunity11m7 = []
allcommunity12m7 = []
allcommunity13m7 = []
allcommunity14m7 = []
allcommunity15m7 = []
allcommunity1m8 = []
allcommunity2m8 = []
allcommunity3m8 = []
allcommunity4m8 = []
allcommunity5m8 = []
allcommunity6m8 = []
allcommunity7m8 = []
allcommunity8m8 = []
allcommunity9m8 = []
allcommunity10m8 = []
allcommunity11m8 = []
allcommunity12m8 = []
allcommunity13m8 = []
allcommunity14m8 = []
allcommunity15m8 = []
allcommunity1m9 = []
allcommunity2m9 = []
allcommunity3m9 = []
allcommunity4m9 = []
allcommunity5m9 = []
allcommunity6m9 = []
allcommunity7m9 = []
allcommunity8m9 = []
allcommunity9m9 = []
allcommunity10m9 = []
allcommunity11m9 = []
allcommunity12m9 = []
allcommunity13m9 = []
allcommunity14m9 = []
allcommunity15m9 = []
allcommunity1m10 = []
allcommunity2m10 = []
allcommunity3m10 = []
allcommunity4m10 = []
allcommunity5m10 = []
allcommunity6m10 = []
allcommunity7m10 = []
allcommunity8m10 = []
allcommunity9m10 = []
allcommunity10m10 = []
allcommunity11m10 = []
allcommunity12m10 = []
allcommunity13m10 = []
allcommunity14m10 = []
allcommunity15m10 = []
allcommunity1m11 = []
allcommunity2m11 = []
allcommunity3m11 = []
allcommunity4m11 = []
allcommunity5m11 = []
allcommunity6m11 = []
allcommunity7m11 = []
allcommunity8m11 = []
allcommunity9m11 = []
allcommunity10m11 = []
allcommunity11m11 = []
allcommunity12m11 = []
allcommunity13m11 = []
allcommunity14m11 = []
allcommunity15m11 = []
allcommunity1m12 = []
allcommunity2m12 = []
allcommunity3m12 = []
allcommunity4m12 = []
allcommunity5m12 = []
allcommunity6m12 = []
allcommunity7m12 = []
allcommunity8m12 = []
allcommunity9m12 = []
allcommunity10m12 = []
allcommunity11m12 = []
allcommunity12m12 = []
allcommunity13m12 = []
allcommunity14m12 = []
allcommunity15m12 = []
allcommunity1m13 = []
allcommunity2m13 = []
allcommunity3m13 = []
allcommunity4m13 = []
allcommunity5m13 = []
allcommunity6m13 = []
allcommunity7m13 = []
allcommunity8m13 = []
allcommunity9m13 = []
allcommunity10m13 = []
allcommunity11m13 = []
allcommunity12m13 = []
allcommunity13m13 = []
allcommunity14m13 = []
allcommunity15m13 = []
allcommunity1m14 = []
allcommunity2m14 = []
allcommunity3m14 = []
allcommunity4m14 = []
allcommunity5m14 = []
allcommunity6m14 = []
allcommunity7m14 = []
allcommunity8m14 = []
allcommunity9m14 = []
allcommunity10m14 = []
allcommunity11m14 = []
allcommunity12m14 = []
allcommunity13m14 = []
allcommunity14m14 = []
allcommunity15m14 = []
allcommunity1m15 = []
allcommunity2m15 = []
allcommunity3m15 = []
allcommunity4m15 = []
allcommunity5m15 = []
allcommunity6m15 = []
allcommunity7m15 = []
allcommunity8m15 = []
allcommunity9m15 = []
allcommunity10m15 = []
allcommunity11m15 = []
allcommunity12m15 = []
allcommunity13m15 = []
allcommunity14m15 = []
allcommunity15m15 = []

allcommunity1defend = []
allcommunity2defend = []
allcommunity3defend = []
allcommunity4defend = []
allcommunity5defend = []
allcommunity6defend = []
allcommunity7defend = []
allcommunity8defend = []
allcommunity9defend = []
allcommunity10defend = []
allcommunity11defend = []
allcommunity12defend = []
allcommunity13defend = []
allcommunity14defend = []
allcommunity15defend = []

alloneandtwo = []
alloneandthree = []
alltwoandthree = []
alloneandfour = []
alloneandfive = []
alloneandsix = []
alloneandseven = []
alloneandeight = []
alloneandnine = []
alloneandten = []
alloneandeleven = []
alloneandtwelve = []
alloneandthirteen = []
alloneandfourteen = []
alloneandfifteen = []
alltwoandfour = []
alltwoandfive = []
alltwoandsix = []
alltwoandseven = []
alltwoandeight = []
alltwoandnine = []
alltwoandten = []
alltwoandeleven = []
alltwoandtwelve = []
alltwoandthirteen = []
alltwoandfourteen = []
alltwoandfifteen = []
allthreeandfour = []
allthreeandfive = []
allthreeandsix = []
allthreeandseven = []
allthreeandeight = []
allthreeandnine = []
allthreeandten = []
allthreeandeleven = []
allthreeandtwelve = []
allthreeandthirteen = []
allthreeandfourteen = []
allthreeandfifteen = []
allfourandfive = []
allfourandsix = []
allfourandseven = []
allfourandeight = []
allfourandnine = []
allfourandten = []
allfourandeleven = []
allfourandtwelve = []
allfourandthirteen = []
allfourandfourteen = []
allfourandfifteen = []
allfiveandsix = []
allfiveandseven = []
allfiveandeight = []
allfiveandnine = []
allfiveandten = []
allfiveandeleven = []
allfiveandtwelve = []
allfiveandthirteen = []
allfiveandfourteen = []
allfiveandfifteen = []
allsixandseven = []
allsixandeight = []
allsixandnine = []
allsixandten = []
allsixandeleven = []
allsixandtwelve = []
allsixandthirteen = []
allsixandfourteen = []
allsixandfifteen = []
allsevenandeight = []
allsevenandnine = []
allsevenandten = []
allsevenandeleven = []
allsevenandtwelve = []
allsevenandthirteen = []
allsevenandfourteen = []
allsevenandfifteen = []
alleightandnine = []
alleightandten = []
alleightandeleven = []
alleightandtwelve = []
alleightandthirteen = []
alleightandfourteen = []
alleightandfifteen = []
allnineandten = []
allnineandeleven = []
allnineandtwelve = []
allnineandthirteen = []
allnineandfourteen = []
allnineandfifteen = []
alltenandeleven = []
alltenandtwelve = []
alltenandthirteen = []
alltenandfourteen = []
alltenandfifteen = []
allelevenandtwelve = []
allelevenandthirteen = []
allelevenandfourteen = []
allelevenandfifteen = []
alltwelveandthirteen = []
alltwelveandfourteen = []
alltwelveandfifteen = []
allthirteenandfourteen = []
allthirteenandfifteen = []
allfourteenandfifteen = []

simulations = 40
s = 0
while s < simulations:
    print('simulation',  s+1)
    p = subprocess.Popen(['python', 'results.py'],  stdout=subprocess.PIPE,  stderr=subprocess.PIPE)
    data = p.communicate()
    stringdata = ''.join(map(str,  data))
    parsed = stringdata.rsplit(sep='@')
    militantstrings = parsed[0].rsplit(sep=' * ')
    communitystrings = parsed[1].rsplit(sep=' * ')
    communitystrings2 = parsed[2].rsplit(sep=' * ')
    communitydefendstrings = parsed[3].rsplit(sep=' * ')
    fightstrings = parsed[4].rsplit(sep=' * ')

    community1m1 = []
    community2m1 = []
    community3m1 = []
    community4m1 = []
    community5m1 = []
    community6m1 = []
    community7m1 = []
    community8m1 = []
    community9m1 = []
    community10m1 = []
    community11m1 = []
    community12m1 = []
    community13m1 = []
    community14m1 = []
    community15m1 = []
    community1m2 = []
    community2m2 = []
    community3m2 = []
    community4m2 = []
    community5m2 = []
    community6m2 = []
    community7m2 = []
    community8m2 = []
    community9m2 = []
    community10m2 = []
    community11m2 = []
    community12m2 = []
    community13m2 = []
    community14m2 = []
    community15m2 = []
    community1m3 = []
    community2m3 = []
    community3m3 = []
    community4m3 = []
    community5m3 = []
    community6m3 = []
    community7m3 = []
    community8m3 = []
    community9m3 = []
    community10m3 = []
    community11m3 = []
    community12m3 = []
    community13m3 = []
    community14m3 = []
    community15m3 = []
    community1m4 = []
    community2m4 = []
    community3m4 = []
    community4m4 = []
    community5m4 = []
    community6m4 = []
    community7m4 = []
    community8m4 = []
    community9m4 = []
    community10m4 = []
    community11m4 = []
    community12m4 = []
    community13m4 = []
    community14m4 = []
    community15m4 = []
    community1m5 = []
    community2m5 = []
    community3m5 = []
    community4m5 = []
    community5m5 = []
    community6m5 = []
    community7m5 = []
    community8m5 = []
    community9m5 = []
    community10m5 = []
    community11m5 = []
    community12m5 = []
    community13m5 = []
    community14m5 = []
    community15m5 = []
    community1m6 = []
    community2m6 = []
    community3m6 = []
    community4m6 = []
    community5m6 = []
    community6m6 = []
    community7m6 = []
    community8m6 = []
    community9m6 = []
    community10m6 = []
    community11m6 = []
    community12m6 = []
    community13m6 = []
    community14m6 = []
    community15m6 = []
    community1m7 = []
    community2m7 = []
    community3m7 = []
    community4m7 = []
    community5m7 = []
    community6m7 = []
    community7m7 = []
    community8m7 = []
    community9m7 = []
    community10m7 = []
    community11m7 = []
    community12m7 = []
    community13m7 = []
    community14m7 = []
    community15m7 = []
    community1m8 = []
    community2m8 = []
    community3m8 = []
    community4m8 = []
    community5m8 = []
    community6m8 = []
    community7m8 = []
    community8m8 = []
    community9m8 = []
    community10m8 = []
    community11m8 = []
    community12m8 = []
    community13m8 = []
    community14m8 = []
    community15m8 = []
    community1m9 = []
    community2m9 = []
    community3m9 = []
    community4m9 = []
    community5m9 = []
    community6m9 = []
    community7m9 = []
    community8m9 = []
    community9m9 = []
    community10m9 = []
    community11m9 = []
    community12m9 = []
    community13m9 = []
    community14m9 = []
    community15m9 = []
    community1m10 = []
    community2m10 = []
    community3m10 = []
    community4m10 = []
    community5m10 = []
    community6m10 = []
    community7m10 = []
    community8m10 = []
    community9m10 = []
    community10m10 = []
    community11m10 = []
    community12m10 = []
    community13m10 = []
    community14m10 = []
    community15m10 = []
    community1m11 = []
    community2m11 = []
    community3m11 = []
    community4m11 = []
    community5m11 = []
    community6m11 = []
    community7m11 = []
    community8m11 = []
    community9m11 = []
    community10m11 = []
    community11m11 = []
    community12m11 = []
    community13m11 = []
    community14m11 = []
    community15m11 = []
    community1m12 = []
    community2m12 = []
    community3m12 = []
    community4m12 = []
    community5m12 = []
    community6m12 = []
    community7m12 = []
    community8m12 = []
    community9m12 = []
    community10m12 = []
    community11m12 = []
    community12m12 = []
    community13m12 = []
    community14m12 = []
    community15m12 = []
    community1m13 = []
    community2m13 = []
    community3m13 = []
    community4m13 = []
    community5m13 = []
    community6m13 = []
    community7m13 = []
    community8m13 = []
    community9m13 = []
    community10m13 = []
    community11m13 = []
    community12m13 = []
    community13m13 = []
    community14m13 = []
    community15m13 = []
    community1m14 = []
    community2m14 = []
    community3m14 = []
    community4m14 = []
    community5m14 = []
    community6m14 = []
    community7m14 = []
    community8m14 = []
    community9m14 = []
    community10m14 = []
    community11m14 = []
    community12m14 = []
    community13m14 = []
    community14m14 = []
    community15m14 = []
    community1m15 = []
    community2m15 = []
    community3m15 = []
    community4m15 = []
    community5m15 = []
    community6m15 = []
    community7m15 = []
    community8m15 = []
    community9m15 = []
    community10m15 = []
    community11m15 = []
    community12m15 = []
    community13m15 = []
    community14m15 = []
    community15m15 = []

    # community1m1
    if communitystrings[1] != '[]':
        liststring = communitystrings[1].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community1m1.append(fixed)
            i += 1
    else:
        community1m1 = blanks

    # community2m1
    if communitystrings[2] != '[]':
        liststring = communitystrings[2].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community2m1.append(fixed)
            i += 1
    else:
        community2m1 = blanks

    # community3m1
    if communitystrings[3] != '[]':
        liststring = communitystrings[3].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community3m1.append(fixed)
            i += 1
    else:
        community3m1 = blanks

    # community4m1
    if communitystrings[4] != '[]':
        liststring = communitystrings[4].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community4m1.append(fixed)
            i += 1
    else:
        community4m1 = blanks

    # community5m1
    if communitystrings[5] != '[]':
        liststring = communitystrings[5].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community5m1.append(fixed)
            i += 1
    else:
        community5m1 = blanks

    # community6m1
    if communitystrings[6] != '[]':
        liststring = communitystrings[6].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community6m1.append(fixed)
            i += 1
    else:
        community6m1 = blanks

    # community7m1
    if communitystrings[7] != '[]':
        liststring = communitystrings[7].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community7m1.append(fixed)
            i += 1
    else:
        community7m1 = blanks

    # community8m1
    if communitystrings[8] != '[]':
        liststring = communitystrings[8].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community8m1.append(fixed)
            i += 1
    else:
        community8m1 = blanks

    # community9m1
    if communitystrings[9] != '[]':
        liststring = communitystrings[9].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community9m1.append(fixed)
            i += 1
    else:
        community9m1 = blanks

    # community10m1
    if communitystrings[10] != '[]':
        liststring = communitystrings[10].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community10m1.append(fixed)
            i += 1
    else:
        community10m1 = blanks

    # community11m1
    if communitystrings[11] != '[]':
        liststring = communitystrings[11].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community11m1.append(fixed)
            i += 1
    else:
        community11m1 = blanks

    # community12m1
    if communitystrings[12] != '[]':
        liststring = communitystrings[12].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community12m1.append(fixed)
            i += 1
    else:
        community12m1 = blanks

    # community13m1
    if communitystrings[13] != '[]':
        liststring = communitystrings[13].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community13m1.append(fixed)
            i += 1
    else:
        community13m1 = blanks

    # community14m1
    if communitystrings[14] != '[]':
        liststring = communitystrings[14].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community14m1.append(fixed)
            i += 1
    else:
        community14m1 = blanks

    # community15m1
    if communitystrings[15] != '[]':
        liststring = communitystrings[15].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community15m1.append(fixed)
            i += 1
    else:
        community15m1 = blanks

    # community1m2
    if communitystrings[16] != '[]':
        liststring = communitystrings[16].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community1m2.append(fixed)
            i += 1
    else:
        community1m2 = blanks

    # community2m2
    if communitystrings[17] != '[]':
        liststring = communitystrings[17].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community2m2.append(fixed)
            i += 1
    else:
        community2m2 = blanks

    # community3m2
    if communitystrings[18] != '[]':
        liststring = communitystrings[18].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community3m2.append(fixed)
            i += 1
    else:
        community3m2 = blanks

    # community4m2
    if communitystrings[19] != '[]':
        liststring = communitystrings[19].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community4m2.append(fixed)
            i += 1
    else:
        community4m2 = blanks

    # community5m2
    if communitystrings[20] != '[]':
        liststring = communitystrings[20].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community5m2.append(fixed)
            i += 1
    else:
        community5m2 = blanks

    # community6m2
    if communitystrings[21] != '[]':
        liststring = communitystrings[21].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community6m2.append(fixed)
            i += 1
    else:
        community6m2 = blanks

    # community7m2
    if communitystrings[22] != '[]':
        liststring = communitystrings[22].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community7m2.append(fixed)
            i += 1
    else:
        community7m2 = blanks

    # community8m2
    if communitystrings[23] != '[]':
        liststring = communitystrings[23].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community8m2.append(fixed)
            i += 1
    else:
        community8m2 = blanks

    # community9m2
    if communitystrings[24] != '[]':
        liststring = communitystrings[24].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community9m2.append(fixed)
            i += 1
    else:
        community9m2 = blanks

    # community10m2
    if communitystrings[25] != '[]':
        liststring = communitystrings[25].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community10m2.append(fixed)
            i += 1
    else:
        community10m2 = blanks

    # community11m2
    if communitystrings[26] != '[]':
        liststring = communitystrings[26].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community11m2.append(fixed)
            i += 1
    else:
        community11m2 = blanks

    # community12m2
    if communitystrings[27] != '[]':
        liststring = communitystrings[27].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community12m2.append(fixed)
            i += 1
    else:
        community12m2 = blanks

    # community13m2
    if communitystrings[28] != '[]':
        liststring = communitystrings[28].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community13m2.append(fixed)
            i += 1
    else:
        community13m2 = blanks

    # community14m2
    if communitystrings[29] != '[]':
        liststring = communitystrings[29].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community14m2.append(fixed)
            i += 1
    else:
        community14m2 = blanks

    # community15m2
    if communitystrings[30] != '[]':
        liststring = communitystrings[30].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community15m2.append(fixed)
            i += 1
    else:
        community15m2 = blanks

    # community1m3
    if communitystrings[31] != '[]':
        liststring = communitystrings[31].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community1m3.append(fixed)
            i += 1
    else:
        community1m3 = blanks

    # community2m3
    if communitystrings[32] != '[]':
        liststring = communitystrings[32].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community2m3.append(fixed)
            i += 1
    else:
        community2m3 = blanks

    # community3m3
    if communitystrings[33] != '[]':
        liststring = communitystrings[33].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community3m3.append(fixed)
            i += 1
    else:
        community3m3 = blanks

    # community4m3
    if communitystrings[34] != '[]':
        liststring = communitystrings[34].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community4m3.append(fixed)
            i += 1
    else:
        community4m3 = blanks

    # community5m3
    if communitystrings[35] != '[]':
        liststring = communitystrings[35].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community5m3.append(fixed)
            i += 1
    else:
        community5m3 = blanks

    # community6m3
    if communitystrings[36] != '[]':
        liststring = communitystrings[36].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community6m3.append(fixed)
            i += 1
    else:
        community6m3 = blanks

    # community7m3
    if communitystrings[37] != '[]':
        liststring = communitystrings[37].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community7m3.append(fixed)
            i += 1
    else:
        community7m3 = blanks

    # community8m3
    if communitystrings[38] != '[]':
        liststring = communitystrings[38].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community8m3.append(fixed)
            i += 1
    else:
        community8m3 = blanks

    # community9m3
    if communitystrings[39] != '[]':
        liststring = communitystrings[39].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community9m3.append(fixed)
            i += 1
    else:
        community9m3 = blanks

    # community10m3
    if communitystrings[40] != '[]':
        liststring = communitystrings[40].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community10m3.append(fixed)
            i += 1
    else:
        community10m3 = blanks

    # community11m3
    if communitystrings[41] != '[]':
        liststring = communitystrings[41].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community11m3.append(fixed)
            i += 1
    else:
        community11m3 = blanks

    # community12m3
    if communitystrings[42] != '[]':
        liststring = communitystrings[42].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community12m3.append(fixed)
            i += 1
    else:
        community12m3 = blanks

    # community13m3
    if communitystrings[43] != '[]':
        liststring = communitystrings[43].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community13m3.append(fixed)
            i += 1
    else:
        community13m3 = blanks

    # community14m3
    if communitystrings[44] != '[]':
        liststring = communitystrings[44].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community14m3.append(fixed)
            i += 1
    else:
        community14m3 = blanks

    # community15m3
    if communitystrings[45] != '[]':
        liststring = communitystrings[45].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community15m3.append(fixed)
            i += 1
    else:
        community15m3 = blanks

    # community1m4
    if communitystrings[46] != '[]':
        liststring = communitystrings[46].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community1m4.append(fixed)
            i += 1
    else:
        community1m4 = blanks

    # community2m4
    if communitystrings[47] != '[]':
        liststring = communitystrings[47].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community2m4.append(fixed)
            i += 1
    else:
        community2m4 = blanks

    # community3m4
    if communitystrings[48] != '[]':
        liststring = communitystrings[48].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community3m4.append(fixed)
            i += 1
    else:
        community3m4 = blanks

    # community4m4
    if communitystrings[49] != '[]':
        liststring = communitystrings[49].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community4m4.append(fixed)
            i += 1
    else:
        community4m4 = blanks

    # community5m4
    if communitystrings[50] != '[]':
        liststring = communitystrings[50].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community5m4.append(fixed)
            i += 1
    else:
        community5m4 = blanks

    # community6m4
    if communitystrings[51] != '[]':
        liststring = communitystrings[51].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community6m4.append(fixed)
            i += 1
    else:
        community6m4 = blanks

    # community7m4
    if communitystrings[52] != '[]':
        liststring = communitystrings[52].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community7m4.append(fixed)
            i += 1
    else:
        community7m4 = blanks

    # community8m4
    if communitystrings[53] != '[]':
        liststring = communitystrings[53].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community8m4.append(fixed)
            i += 1
    else:
        community8m4 = blanks

    # community9m4
    if communitystrings[54] != '[]':
        liststring = communitystrings[54].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community9m4.append(fixed)
            i += 1
    else:
        community9m4 = blanks

    # community10m4
    if communitystrings[55] != '[]':
        liststring = communitystrings[55].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community10m4.append(fixed)
            i += 1
    else:
        community10m4 = blanks

    # community11m4
    if communitystrings[56] != '[]':
        liststring = communitystrings[56].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community11m4.append(fixed)
            i += 1
    else:
        community11m4 = blanks

    # community12m4
    if communitystrings[57] != '[]':
        liststring = communitystrings[57].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community12m4.append(fixed)
            i += 1
    else:
        community12m4 = blanks

    # community13m4
    if communitystrings[58] != '[]':
        liststring = communitystrings[58].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community13m4.append(fixed)
            i += 1
    else:
        community13m4 = blanks

    # community14m4
    if communitystrings[59] != '[]':
        liststring = communitystrings[59].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community14m4.append(fixed)
            i += 1
    else:
        community14m4 = blanks

    # community15m4
    if communitystrings[60] != '[]':
        liststring = communitystrings[60].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community15m4.append(fixed)
            i += 1
    else:
        community15m4 = blanks

    # community1m5
    if communitystrings[61] != '[]':
        liststring = communitystrings[61].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community1m5.append(fixed)
            i += 1
    else:
        community1m5 = blanks

    # community2m5
    if communitystrings[62] != '[]':
        liststring = communitystrings[62].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community2m5.append(fixed)
            i += 1
    else:
        community2m5 = blanks

    # community3m5
    if communitystrings[63] != '[]':
        liststring = communitystrings[63].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community3m5.append(fixed)
            i += 1
    else:
        community3m5 = blanks

    # community4m5
    if communitystrings[64] != '[]':
        liststring = communitystrings[64].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community4m5.append(fixed)
            i += 1
    else:
        community4m5 = blanks

    # community5m5
    if communitystrings[65] != '[]':
        liststring = communitystrings[65].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community5m5.append(fixed)
            i += 1
    else:
        community5m5 = blanks

    # community6m5
    if communitystrings[66] != '[]':
        liststring = communitystrings[66].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community6m5.append(fixed)
            i += 1
    else:
        community6m5 = blanks

    # community7m5
    if communitystrings[67] != '[]':
        liststring = communitystrings[67].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community7m5.append(fixed)
            i += 1
    else:
        community7m5 = blanks

    # community8m5
    if communitystrings[68] != '[]':
        liststring = communitystrings[68].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community8m5.append(fixed)
            i += 1
    else:
        community8m5 = blanks

    # community9m5
    if communitystrings[69] != '[]':
        liststring = communitystrings[69].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community9m5.append(fixed)
            i += 1
    else:
        community9m5 = blanks

    # community10m5
    if communitystrings[70] != '[]':
        liststring = communitystrings[70].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community10m5.append(fixed)
            i += 1
    else:
        community10m5 = blanks

    # community11m5
    if communitystrings[71] != '[]':
        liststring = communitystrings[71].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community11m5.append(fixed)
            i += 1
    else:
        community11m5 = blanks

    # community12m5
    if communitystrings[72] != '[]':
        liststring = communitystrings[72].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community12m5.append(fixed)
            i += 1
    else:
        community12m5 = blanks

    # community13m5
    if communitystrings[73] != '[]':
        liststring = communitystrings[73].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community13m5.append(fixed)
            i += 1
    else:
        community13m5 = blanks

    # community14m5
    if communitystrings[74] != '[]':
        liststring = communitystrings[74].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community14m5.append(fixed)
            i += 1
    else:
        community14m5 = blanks

    # community15m5
    if communitystrings[75] != '[]':
        liststring = communitystrings[75].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community15m5.append(fixed)
            i += 1
    else:
        community15m5 = blanks

    # community1m6
    if communitystrings[76] != '[]':
        liststring = communitystrings[76].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community1m6.append(fixed)
            i += 1
    else:
        community1m6 = blanks

    # community2m6
    if communitystrings[77] != '[]':
        liststring = communitystrings[77].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community2m6.append(fixed)
            i += 1
    else:
        community2m6 = blanks

    # community3m6
    if communitystrings[78] != '[]':
        liststring = communitystrings[78].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community3m6.append(fixed)
            i += 1
    else:
        community3m6 = blanks

    # community4m6
    if communitystrings[79] != '[]':
        liststring = communitystrings[79].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community4m6.append(fixed)
            i += 1
    else:
        community4m6 = blanks

    # community5m6
    if communitystrings[80] != '[]':
        liststring = communitystrings[80].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community5m6.append(fixed)
            i += 1
    else:
        community5m6 = blanks

    # community6m6
    if communitystrings[81] != '[]':
        liststring = communitystrings[81].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community6m6.append(fixed)
            i += 1
    else:
        community6m6 = blanks

    # community7m6
    if communitystrings[82] != '[]':
        liststring = communitystrings[82].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community7m6.append(fixed)
            i += 1
    else:
        community7m6 = blanks

    # community8m6
    if communitystrings[83] != '[]':
        liststring = communitystrings[83].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community8m6.append(fixed)
            i += 1
    else:
        community8m6 = blanks

    # community9m6
    if communitystrings[84] != '[]':
        liststring = communitystrings[84].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community9m6.append(fixed)
            i += 1
    else:
        community9m6 = blanks

    # community10m6
    if communitystrings[85] != '[]':
        liststring = communitystrings[85].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community10m6.append(fixed)
            i += 1
    else:
        community10m6 = blanks

    # community11m6
    if communitystrings[86] != '[]':
        liststring = communitystrings[86].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community11m6.append(fixed)
            i += 1
    else:
        community11m6 = blanks

    # community12m6
    if communitystrings[87] != '[]':
        liststring = communitystrings[87].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community12m6.append(fixed)
            i += 1
    else:
        community12m6 = blanks

    # community13m6
    if communitystrings[88] != '[]':
        liststring = communitystrings[88].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community13m6.append(fixed)
            i += 1
    else:
        community13m6 = blanks

    # community14m6
    if communitystrings[89] != '[]':
        liststring = communitystrings[89].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community14m6.append(fixed)
            i += 1
    else:
        community14m6 = blanks

    # community15m6
    if communitystrings[90] != '[]':
        liststring = communitystrings[90].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community15m6.append(fixed)
            i += 1
    else:
        community15m6 = blanks

    # community1m7
    if communitystrings[91] != '[]':
        liststring = communitystrings[91].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community1m7.append(fixed)
            i += 1
    else:
        community1m7 = blanks

    # community2m7
    if communitystrings[92] != '[]':
        liststring = communitystrings[92].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community2m7.append(fixed)
            i += 1
    else:
        community2m7 = blanks

    # community3m7
    if communitystrings[93] != '[]':
        liststring = communitystrings[93].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community3m7.append(fixed)
            i += 1
    else:
        community3m7 = blanks

    # community4m7
    if communitystrings[94] != '[]':
        liststring = communitystrings[94].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community4m7.append(fixed)
            i += 1
    else:
        community4m7 = blanks

    # community5m7
    if communitystrings[95] != '[]':
        liststring = communitystrings[95].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community5m7.append(fixed)
            i += 1
    else:
        community5m7 = blanks

    # community6m7
    if communitystrings[96] != '[]':
        liststring = communitystrings[96].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community6m7.append(fixed)
            i += 1
    else:
        community6m7 = blanks

    # community7m7
    if communitystrings[97] != '[]':
        liststring = communitystrings[97].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community7m7.append(fixed)
            i += 1
    else:
        community7m7 = blanks

    # community8m7
    if communitystrings[98] != '[]':
        liststring = communitystrings[98].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community8m7.append(fixed)
            i += 1
    else:
        community8m7 = blanks

    # community9m7
    if communitystrings[99] != '[]':
        liststring = communitystrings[99].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community9m7.append(fixed)
            i += 1
    else:
        community9m7 = blanks

    # community10m7
    if communitystrings[100] != '[]':
        liststring = communitystrings[100].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community10m7.append(fixed)
            i += 1
    else:
        community10m7 = blanks

    # community11m7
    if communitystrings[101] != '[]':
        liststring = communitystrings[101].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community11m7.append(fixed)
            i += 1
    else:
        community11m7 = blanks

    # community12m7
    if communitystrings[102] != '[]':
        liststring = communitystrings[102].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community12m7.append(fixed)
            i += 1
    else:
        community12m7 = blanks

    # community13m7
    if communitystrings[103] != '[]':
        liststring = communitystrings[103].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community13m7.append(fixed)
            i += 1
    else:
        community13m7 = blanks

    # community14m7
    if communitystrings[104] != '[]':
        liststring = communitystrings[104].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community14m7.append(fixed)
            i += 1
    else:
        community14m7 = blanks

    # community15m7
    if communitystrings[105] != '[]':
        liststring = communitystrings[105].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community15m7.append(fixed)
            i += 1
    else:
        community15m7 = blanks

    # community1m8
    if communitystrings[106] != '[]':
        liststring = communitystrings[106].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community1m8.append(fixed)
            i += 1
    else:
        community1m8 = blanks

    # community2m8
    if communitystrings[107] != '[]':
        liststring = communitystrings[107].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community2m8.append(fixed)
            i += 1
    else:
        community2m8 = blanks

    # community3m8
    if communitystrings[108] != '[]':
        liststring = communitystrings[108].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community3m8.append(fixed)
            i += 1
    else:
        community3m8 = blanks

    # community4m8
    if communitystrings[109] != '[]':
        liststring = communitystrings[109].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community4m8.append(fixed)
            i += 1
    else:
        community4m8 = blanks

    # community5m8
    if communitystrings[110] != '[]':
        liststring = communitystrings[110].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community5m8.append(fixed)
            i += 1
    else:
        community5m8 = blanks

    # community6m8
    if communitystrings[111] != '[]':
        liststring = communitystrings[111].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community6m8.append(fixed)
            i += 1
    else:
        community6m8 = blanks

    # community7m8
    if communitystrings[112] != '[]':
        liststring = communitystrings[112].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community7m8.append(fixed)
            i += 1
    else:
        community7m8 = blanks

    # community8m8
    if communitystrings2[1] != '[]':
        liststring = communitystrings2[1].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community8m8.append(fixed)
            i += 1
    else:
        community8m8 = blanks

    # community9m8
    if communitystrings2[2] != '[]':
        liststring = communitystrings2[2].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community9m8.append(fixed)
            i += 1
    else:
        community9m8 = blanks

    # community10m8
    if communitystrings2[3] != '[]':
        liststring = communitystrings2[3].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community10m8.append(fixed)
            i += 1
    else:
        community10m8 = blanks

    # community11m8
    if communitystrings2[4] != '[]':
        liststring = communitystrings2[4].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community11m8.append(fixed)
            i += 1
    else:
        community11m8 = blanks

    # community12m8
    if communitystrings2[5] != '[]':
        liststring = communitystrings2[5].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community12m8.append(fixed)
            i += 1
    else:
        community12m8 = blanks

    # community13m8
    if communitystrings2[6] != '[]':
        liststring = communitystrings2[6].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community13m8.append(fixed)
            i += 1
    else:
        community13m8 = blanks

    # community14m8
    if communitystrings2[7] != '[]':
        liststring = communitystrings2[7].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community14m8.append(fixed)
            i += 1
    else:
        community14m8 = blanks

    # community15m8
    if communitystrings2[8] != '[]':
        liststring = communitystrings2[8].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community15m8.append(fixed)
            i += 1
    else:
        community15m8 = blanks

    # community1m9
    if communitystrings2[9] != '[]':
        liststring = communitystrings2[9].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community1m9.append(fixed)
            i += 1
    else:
        community1m9 = blanks

    # community2m9
    if communitystrings2[10] != '[]':
        liststring = communitystrings2[10].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community2m9.append(fixed)
            i += 1
    else:
        community2m9 = blanks

    # community3m9
    if communitystrings2[11] != '[]':
        liststring = communitystrings2[11].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community3m9.append(fixed)
            i += 1
    else:
        community3m9 = blanks

    # community4m9
    if communitystrings2[12] != '[]':
        liststring = communitystrings2[12].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community4m9.append(fixed)
            i += 1
    else:
        community4m9 = blanks

    # community5m9
    if communitystrings2[13] != '[]':
        liststring = communitystrings2[13].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community5m9.append(fixed)
            i += 1
    else:
        community5m9 = blanks

    # community6m9
    if communitystrings2[14] != '[]':
        liststring = communitystrings2[14].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community6m9.append(fixed)
            i += 1
    else:
        community6m9 = blanks

    # community7m9
    if communitystrings2[15] != '[]':
        liststring = communitystrings2[15].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community7m9.append(fixed)
            i += 1
    else:
        community7m9 = blanks

    # community8m9
    if communitystrings2[16] != '[]':
        liststring = communitystrings2[16].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community8m9.append(fixed)
            i += 1
    else:
        community8m9 = blanks

    # community9m9
    if communitystrings2[17] != '[]':
        liststring = communitystrings2[17].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community9m9.append(fixed)
            i += 1
    else:
        community9m9 = blanks

    # community10m9
    if communitystrings2[18] != '[]':
        liststring = communitystrings2[18].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community10m9.append(fixed)
            i += 1
    else:
        community10m9 = blanks

    # community11m9
    if communitystrings2[19] != '[]':
        liststring = communitystrings2[19].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community11m9.append(fixed)
            i += 1
    else:
        community11m9 = blanks

    # community12m9
    if communitystrings2[20] != '[]':
        liststring = communitystrings2[20].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community12m9.append(fixed)
            i += 1
    else:
        community12m9 = blanks

    # community13m9
    if communitystrings2[21] != '[]':
        liststring = communitystrings2[21].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community13m9.append(fixed)
            i += 1
    else:
        community13m9 = blanks

    # community14m9
    if communitystrings2[22] != '[]':
        liststring = communitystrings2[22].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community14m9.append(fixed)
            i += 1
    else:
        community14m9 = blanks

    # community15m9
    if communitystrings2[23] != '[]':
        liststring = communitystrings2[23].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community15m9.append(fixed)
            i += 1
    else:
        community15m9 = blanks

    # community1m10
    if communitystrings2[24] != '[]':
        liststring = communitystrings2[24].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community1m10.append(fixed)
            i += 1
    else:
        community1m10 = blanks

    # community2m10
    if communitystrings2[25] != '[]':
        liststring = communitystrings2[25].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community2m10.append(fixed)
            i += 1
    else:
        community2m10 = blanks

    # community3m10
    if communitystrings2[26] != '[]':
        liststring = communitystrings2[26].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community3m10.append(fixed)
            i += 1
    else:
        community3m10 = blanks

    # community4m10
    if communitystrings2[27] != '[]':
        liststring = communitystrings2[27].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community4m10.append(fixed)
            i += 1
    else:
        community4m10 = blanks

    # community5m10
    if communitystrings2[28] != '[]':
        liststring = communitystrings2[28].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community5m10.append(fixed)
            i += 1
    else:
        community5m10 = blanks

    # community6m10
    if communitystrings2[29] != '[]':
        liststring = communitystrings2[29].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community6m10.append(fixed)
            i += 1
    else:
        community6m10 = blanks

    # community7m10
    if communitystrings2[30] != '[]':
        liststring = communitystrings2[30].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community7m10.append(fixed)
            i += 1
    else:
        community7m10 = blanks

    # community8m10
    if communitystrings2[31] != '[]':
        liststring = communitystrings2[31].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community8m10.append(fixed)
            i += 1
    else:
        community8m10 = blanks

    # community9m10
    if communitystrings2[32] != '[]':
        liststring = communitystrings2[32].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community9m10.append(fixed)
            i += 1
    else:
        community9m10 = blanks

    # community10m10
    if communitystrings2[33] != '[]':
        liststring = communitystrings2[33].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community10m10.append(fixed)
            i += 1
    else:
        community10m10 = blanks

    # community11m10
    if communitystrings2[34] != '[]':
        liststring = communitystrings2[34].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community11m10.append(fixed)
            i += 1
    else:
        community11m10 = blanks

    # community12m10
    if communitystrings2[35] != '[]':
        liststring = communitystrings2[35].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community12m10.append(fixed)
            i += 1
    else:
        community12m10 = blanks

    # community13m10
    if communitystrings2[36] != '[]':
        liststring = communitystrings2[36].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community13m10.append(fixed)
            i += 1
    else:
        community13m10 = blanks

    # community14m10
    if communitystrings2[37] != '[]':
        liststring = communitystrings2[37].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community14m10.append(fixed)
            i += 1
    else:
        community14m10 = blanks

    # community15m10
    if communitystrings2[38] != '[]':
        liststring = communitystrings2[38].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community15m10.append(fixed)
            i += 1
    else:
        community15m10 = blanks

    # community1m11
    if communitystrings2[39] != '[]':
        liststring = communitystrings2[39].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community1m11.append(fixed)
            i += 1
    else:
        community1m11 = blanks

    # community2m11
    if communitystrings2[40] != '[]':
        liststring = communitystrings2[40].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community2m11.append(fixed)
            i += 1
    else:
        community2m11 = blanks

    # community3m11
    if communitystrings2[41] != '[]':
        liststring = communitystrings2[41].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community3m11.append(fixed)
            i += 1
    else:
        community3m11 = blanks

    # community4m11
    if communitystrings2[42] != '[]':
        liststring = communitystrings2[42].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community4m11.append(fixed)
            i += 1
    else:
        community4m11 = blanks

    # community5m11
    if communitystrings2[43] != '[]':
        liststring = communitystrings2[43].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community5m11.append(fixed)
            i += 1
    else:
        community5m11 = blanks

    # community6m11
    if communitystrings2[44] != '[]':
        liststring = communitystrings2[44].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community6m11.append(fixed)
            i += 1
    else:
        community6m11 = blanks

    # community7m11
    if communitystrings2[45] != '[]':
        liststring = communitystrings2[45].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community7m11.append(fixed)
            i += 1
    else:
        community7m11 = blanks

    # community8m11
    if communitystrings2[46] != '[]':
        liststring = communitystrings2[46].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community8m11.append(fixed)
            i += 1
    else:
        community8m11 = blanks

    # community9m11
    if communitystrings2[47] != '[]':
        liststring = communitystrings2[47].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community9m11.append(fixed)
            i += 1
    else:
        community9m11 = blanks

    # community10m11
    if communitystrings2[48] != '[]':
        liststring = communitystrings2[48].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community10m11.append(fixed)
            i += 1
    else:
        community10m11 = blanks

    # community11m11
    if communitystrings2[49] != '[]':
        liststring = communitystrings2[49].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community11m11.append(fixed)
            i += 1
    else:
        community11m11 = blanks

    # community12m11
    if communitystrings2[50] != '[]':
        liststring = communitystrings2[50].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community12m11.append(fixed)
            i += 1
    else:
        community12m11 = blanks

    # community13m11
    if communitystrings2[51] != '[]':
        liststring = communitystrings2[51].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community13m11.append(fixed)
            i += 1
    else:
        community13m11 = blanks

    # community14m11
    if communitystrings2[52] != '[]':
        liststring = communitystrings2[52].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community14m11.append(fixed)
            i += 1
    else:
        community14m11 = blanks

    # community15m11
    if communitystrings2[53] != '[]':
        liststring = communitystrings2[53].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community15m11.append(fixed)
            i += 1
    else:
        community15m11 = blanks

    # community1m12
    if communitystrings2[54] != '[]':
        liststring = communitystrings2[54].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community1m12.append(fixed)
            i += 1
    else:
        community1m12 = blanks

    # community2m12
    if communitystrings2[55] != '[]':
        liststring = communitystrings2[55].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community2m12.append(fixed)
            i += 1
    else:
        community2m12 = blanks

    # community3m12
    if communitystrings2[56] != '[]':
        liststring = communitystrings2[56].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community3m12.append(fixed)
            i += 1
    else:
        community3m12 = blanks

    # community4m12
    if communitystrings2[57] != '[]':
        liststring = communitystrings2[57].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community4m12.append(fixed)
            i += 1
    else:
        community4m12 = blanks

    # community5m12
    if communitystrings2[58] != '[]':
        liststring = communitystrings2[58].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community5m12.append(fixed)
            i += 1
    else:
        community5m12 = blanks

    # community6m12
    if communitystrings2[59] != '[]':
        liststring = communitystrings2[59].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community6m12.append(fixed)
            i += 1
    else:
        community6m12 = blanks

    # community7m12
    if communitystrings2[60] != '[]':
        liststring = communitystrings2[60].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community7m12.append(fixed)
            i += 1
    else:
        community7m12 = blanks

    # community8m12
    if communitystrings2[61] != '[]':
        liststring = communitystrings2[61].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community8m12.append(fixed)
            i += 1
    else:
        community8m12 = blanks

    # community9m12
    if communitystrings2[62] != '[]':
        liststring = communitystrings2[62].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community9m12.append(fixed)
            i += 1
    else:
        community9m12 = blanks

    # community10m12
    if communitystrings2[63] != '[]':
        liststring = communitystrings2[63].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community10m12.append(fixed)
            i += 1
    else:
        community10m12 = blanks

    # community11m12
    if communitystrings2[64] != '[]':
        liststring = communitystrings2[64].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community11m12.append(fixed)
            i += 1
    else:
        community11m12 = blanks

    # community12m12
    if communitystrings2[65] != '[]':
        liststring = communitystrings2[65].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community12m12.append(fixed)
            i += 1
    else:
        community12m12 = blanks

    # community13m12
    if communitystrings2[66] != '[]':
        liststring = communitystrings2[66].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community13m12.append(fixed)
            i += 1
    else:
        community13m12 = blanks

    # community14m12
    if communitystrings2[67] != '[]':
        liststring = communitystrings2[67].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community14m12.append(fixed)
            i += 1
    else:
        community14m12 = blanks

    # community15m12
    if communitystrings2[68] != '[]':
        liststring = communitystrings2[68].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community15m12.append(fixed)
            i += 1
    else:
        community15m12 = blanks

    # community1m13
    if communitystrings2[69] != '[]':
        liststring = communitystrings2[69].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community1m13.append(fixed)
            i += 1
    else:
        community1m13 = blanks

    # community2m13
    if communitystrings2[70] != '[]':
        liststring = communitystrings2[70].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community2m13.append(fixed)
            i += 1
    else:
        community2m13 = blanks

    # community3m13
    if communitystrings2[71] != '[]':
        liststring = communitystrings2[71].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community3m13.append(fixed)
            i += 1
    else:
        community3m13 = blanks

    # community4m13
    if communitystrings2[72] != '[]':
        liststring = communitystrings2[72].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community4m13.append(fixed)
            i += 1
    else:
        community4m13 = blanks

    # community5m13
    if communitystrings2[73] != '[]':
        liststring = communitystrings2[73].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community5m13.append(fixed)
            i += 1
    else:
        community5m13 = blanks

    # community6m13
    if communitystrings2[74] != '[]':
        liststring = communitystrings2[74].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community6m13.append(fixed)
            i += 1
    else:
        community6m13 = blanks

    # community7m13
    if communitystrings2[75] != '[]':
        liststring = communitystrings2[75].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community7m13.append(fixed)
            i += 1
    else:
        community7m13 = blanks

    # community8m13
    if communitystrings2[76] != '[]':
        liststring = communitystrings2[76].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community8m13.append(fixed)
            i += 1
    else:
        community8m13 = blanks

    # community9m13
    if communitystrings2[77] != '[]':
        liststring = communitystrings2[77].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community9m13.append(fixed)
            i += 1
    else:
        community9m13 = blanks

    # community10m13
    if communitystrings2[78] != '[]':
        liststring = communitystrings2[78].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community10m13.append(fixed)
            i += 1
    else:
        community10m13 = blanks

    # community11m13
    if communitystrings2[79] != '[]':
        liststring = communitystrings2[79].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community11m13.append(fixed)
            i += 1
    else:
        community11m13 = blanks

    # community12m13
    if communitystrings2[80] != '[]':
        liststring = communitystrings2[80].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community12m13.append(fixed)
            i += 1
    else:
        community12m13 = blanks

    # community13m13
    if communitystrings2[81] != '[]':
        liststring = communitystrings2[81].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community13m13.append(fixed)
            i += 1
    else:
        community13m13 = blanks

    # community14m13
    if communitystrings2[82] != '[]':
        liststring = communitystrings2[82].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community14m13.append(fixed)
            i += 1
    else:
        community14m13 = blanks

    # community15m13
    if communitystrings2[83] != '[]':
        liststring = communitystrings2[83].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community15m13.append(fixed)
            i += 1
    else:
        community15m13 = blanks

    # community1m14
    if communitystrings2[84] != '[]':
        liststring = communitystrings2[84].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community1m14.append(fixed)
            i += 1
    else:
        community1m14 = blanks

    # community2m14
    if communitystrings2[85] != '[]':
        liststring = communitystrings2[85].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community2m14.append(fixed)
            i += 1
    else:
        community2m14 = blanks

    # community3m14
    if communitystrings2[86] != '[]':
        liststring = communitystrings2[86].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community3m14.append(fixed)
            i += 1
    else:
        community3m14 = blanks

    # community4m14
    if communitystrings2[87] != '[]':
        liststring = communitystrings2[87].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community4m14.append(fixed)
            i += 1
    else:
        community4m14 = blanks

    # community5m14
    if communitystrings2[88] != '[]':
        liststring = communitystrings2[88].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community5m14.append(fixed)
            i += 1
    else:
        community5m14 = blanks

    # community6m14
    if communitystrings2[89] != '[]':
        liststring = communitystrings2[89].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community6m14.append(fixed)
            i += 1
    else:
        community6m14 = blanks

    # community7m14
    if communitystrings2[90] != '[]':
        liststring = communitystrings2[90].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community7m14.append(fixed)
            i += 1
    else:
        community7m14 = blanks

    # community8m14
    if communitystrings2[91] != '[]':
        liststring = communitystrings2[91].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community8m14.append(fixed)
            i += 1
    else:
        community8m14 = blanks

    # community9m14
    if communitystrings2[92] != '[]':
        liststring = communitystrings2[92].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community9m14.append(fixed)
            i += 1
    else:
        community9m14 = blanks

    # community10m14
    if communitystrings2[93] != '[]':
        liststring = communitystrings2[93].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community10m14.append(fixed)
            i += 1
    else:
        community10m14 = blanks

    # community11m14
    if communitystrings2[94] != '[]':
        liststring = communitystrings2[94].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community11m14.append(fixed)
            i += 1
    else:
        community11m14 = blanks

    # community12m14
    if communitystrings2[95] != '[]':
        liststring = communitystrings2[95].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community12m14.append(fixed)
            i += 1
    else:
        community12m14 = blanks

    # community13m14
    if communitystrings2[96] != '[]':
        liststring = communitystrings2[96].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community13m14.append(fixed)
            i += 1
    else:
        community13m14 = blanks

    # community14m14
    if communitystrings2[97] != '[]':
        liststring = communitystrings2[97].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community14m14.append(fixed)
            i += 1
    else:
        community14m14 = blanks

    # community15m14
    if communitystrings2[98] != '[]':
        liststring = communitystrings2[98].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community15m14.append(fixed)
            i += 1
    else:
        community15m14 = blanks

    # community1m15
    if communitystrings2[99] != '[]':
        liststring = communitystrings2[99].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community1m15.append(fixed)
            i += 1
    else:
        community1m15 = blanks

    # community2m15
    if communitystrings2[100] != '[]':
        liststring = communitystrings2[100].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community2m15.append(fixed)
            i += 1
    else:
        community2m15 = blanks

    # community3m15
    if communitystrings2[101] != '[]':
        liststring = communitystrings2[101].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]',  '',  liststring[i]))
            community3m15.append(fixed)
            i += 1
    else:
        community3m15 = blanks

    # community4m15
    if communitystrings2[102] != '[]':
        liststring = communitystrings2[102].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community4m15.append(fixed)
            i += 1
    else:
        community4m15 = blanks

    # community5m15
    if communitystrings2[103] != '[]':
        liststring = communitystrings2[103].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community5m15.append(fixed)
            i += 1
    else:
        community5m15 = blanks

    # community6m15
    if communitystrings2[104] != '[]':
        liststring = communitystrings2[104].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community6m15.append(fixed)
            i += 1
    else:
        community6m15 = blanks

    # community7m15
    if communitystrings2[105] != '[]':
        liststring = communitystrings2[105].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community7m15.append(fixed)
            i += 1
    else:
        community7m15 = blanks

    # community8m15
    if communitystrings2[106] != '[]':
        liststring = communitystrings2[106].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community8m15.append(fixed)
            i += 1
    else:
        community8m15 = blanks

    # community9m15
    if communitystrings2[107] != '[]':
        liststring = communitystrings2[107].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community9m15.append(fixed)
            i += 1
    else:
        community9m15 = blanks

    # community10m15
    if communitystrings2[108] != '[]':
        liststring = communitystrings2[108].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community10m15.append(fixed)
            i += 1
    else:
        community10m15 = blanks

    # community11m15
    if communitystrings2[109] != '[]':
        liststring = communitystrings2[109].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community11m15.append(fixed)
            i += 1
    else:
        community11m15 = blanks

    # community12m15
    if communitystrings2[110] != '[]':
        liststring = communitystrings2[110].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community12m15.append(fixed)
            i += 1
    else:
        community12m15 = blanks

    # community13m15
    if communitystrings2[111] != '[]':
        liststring = communitystrings2[111].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community13m15.append(fixed)
            i += 1
    else:
        community13m15 = blanks

    # community14m15
    if communitystrings2[112] != '[]':
        liststring = communitystrings2[112].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community14m15.append(fixed)
            i += 1
    else:
        community14m15 = blanks

    # community15m15
    if communitystrings2[113] != '[]':
        liststring = communitystrings2[113].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community15m15.append(fixed)
            i += 1
    else:
        community15m15 = blanks

    militanttuple = militantdata(militantstrings, blanks)
    dftuple = dfdata(communitydefendstrings, fightstrings, blanks)

    allstrength1.append(militanttuple[0])
    allnotorietyratio1.append(militanttuple[1])
    alltotalextort1.append(militanttuple[2])
    allcountextort1.append(militanttuple[3])
    allcountbenefit1.append(militanttuple[4])
    allcountpunish1.append(militanttuple[5])
    allcountsupport1.append(militanttuple[6])
    alltotalsupport1.append(militanttuple[7])
    allcountdefend1.append(militanttuple[8])

    allstrength2.append(militanttuple[9])
    allnotorietyratio2.append(militanttuple[10])
    alltotalextort2.append(militanttuple[11])
    allcountextort2.append(militanttuple[12])
    allcountbenefit2.append(militanttuple[13])
    allcountpunish2.append(militanttuple[14])
    allcountsupport2.append(militanttuple[15])
    alltotalsupport2.append(militanttuple[16])
    allcountdefend2.append(militanttuple[17])

    allstrength3.append(militanttuple[18])
    allnotorietyratio3.append(militanttuple[19])
    alltotalextort3.append(militanttuple[20])
    allcountextort3.append(militanttuple[21])
    allcountbenefit3.append(militanttuple[22])
    allcountpunish3.append(militanttuple[23])
    allcountsupport3.append(militanttuple[24])
    alltotalsupport3.append(militanttuple[25])
    allcountdefend3.append(militanttuple[26])

    allstrength4.append(militanttuple[27])
    allnotorietyratio4.append(militanttuple[28])
    alltotalextort4.append(militanttuple[29])
    allcountextort4.append(militanttuple[30])
    allcountbenefit4.append(militanttuple[31])
    allcountpunish4.append(militanttuple[32])
    allcountsupport4.append(militanttuple[33])
    alltotalsupport4.append(militanttuple[34])
    allcountdefend4.append(militanttuple[35])

    allstrength5.append(militanttuple[36])
    allnotorietyratio5.append(militanttuple[37])
    alltotalextort5.append(militanttuple[38])
    allcountextort5.append(militanttuple[39])
    allcountbenefit5.append(militanttuple[40])
    allcountpunish5.append(militanttuple[41])
    allcountsupport5.append(militanttuple[42])
    alltotalsupport5.append(militanttuple[43])
    allcountdefend5.append(militanttuple[44])

    allstrength6.append(militanttuple[45])
    allnotorietyratio6.append(militanttuple[46])
    alltotalextort6.append(militanttuple[47])
    allcountextort6.append(militanttuple[48])
    allcountbenefit6.append(militanttuple[49])
    allcountpunish6.append(militanttuple[50])
    allcountsupport6.append(militanttuple[51])
    alltotalsupport6.append(militanttuple[52])
    allcountdefend6.append(militanttuple[53])

    allstrength7.append(militanttuple[54])
    allnotorietyratio7.append(militanttuple[55])
    alltotalextort7.append(militanttuple[56])
    allcountextort7.append(militanttuple[57])
    allcountbenefit7.append(militanttuple[58])
    allcountpunish7.append(militanttuple[59])
    allcountsupport7.append(militanttuple[60])
    alltotalsupport7.append(militanttuple[61])
    allcountdefend7.append(militanttuple[62])

    allstrength8.append(militanttuple[63])
    allnotorietyratio8.append(militanttuple[64])
    alltotalextort8.append(militanttuple[65])
    allcountextort8.append(militanttuple[66])
    allcountbenefit8.append(militanttuple[67])
    allcountpunish8.append(militanttuple[68])
    allcountsupport8.append(militanttuple[69])
    alltotalsupport8.append(militanttuple[70])
    allcountdefend8.append(militanttuple[71])

    allstrength9.append(militanttuple[72])
    allnotorietyratio9.append(militanttuple[73])
    alltotalextort9.append(militanttuple[74])
    allcountextort9.append(militanttuple[75])
    allcountbenefit9.append(militanttuple[76])
    allcountpunish9.append(militanttuple[77])
    allcountsupport9.append(militanttuple[78])
    alltotalsupport9.append(militanttuple[79])
    allcountdefend9.append(militanttuple[80])

    allstrength10.append(militanttuple[81])
    allnotorietyratio10.append(militanttuple[82])
    alltotalextort10.append(militanttuple[83])
    allcountextort10.append(militanttuple[84])
    allcountbenefit10.append(militanttuple[85])
    allcountpunish10.append(militanttuple[86])
    allcountsupport10.append(militanttuple[87])
    alltotalsupport10.append(militanttuple[88])
    allcountdefend10.append(militanttuple[89])

    allstrength11.append(militanttuple[90])
    allnotorietyratio11.append(militanttuple[91])
    alltotalextort11.append(militanttuple[92])
    allcountextort11.append(militanttuple[93])
    allcountbenefit11.append(militanttuple[94])
    allcountpunish11.append(militanttuple[95])
    allcountsupport11.append(militanttuple[96])
    alltotalsupport11.append(militanttuple[97])
    allcountdefend11.append(militanttuple[98])

    allstrength12.append(militanttuple[99])
    allnotorietyratio12.append(militanttuple[100])
    alltotalextort12.append(militanttuple[101])
    allcountextort12.append(militanttuple[102])
    allcountbenefit12.append(militanttuple[103])
    allcountpunish12.append(militanttuple[104])
    allcountsupport12.append(militanttuple[105])
    alltotalsupport12.append(militanttuple[106])
    allcountdefend12.append(militanttuple[107])

    allstrength13.append(militanttuple[108])
    allnotorietyratio13.append(militanttuple[109])
    alltotalextort13.append(militanttuple[110])
    allcountextort13.append(militanttuple[111])
    allcountbenefit13.append(militanttuple[112])
    allcountpunish13.append(militanttuple[113])
    allcountsupport13.append(militanttuple[114])
    alltotalsupport13.append(militanttuple[115])
    allcountdefend13.append(militanttuple[116])

    allstrength14.append(militanttuple[117])
    allnotorietyratio14.append(militanttuple[118])
    alltotalextort14.append(militanttuple[119])
    allcountextort14.append(militanttuple[120])
    allcountbenefit14.append(militanttuple[121])
    allcountpunish14.append(militanttuple[122])
    allcountsupport14.append(militanttuple[123])
    alltotalsupport14.append(militanttuple[124])
    allcountdefend14.append(militanttuple[125])

    allstrength15.append(militanttuple[126])
    allnotorietyratio15.append(militanttuple[127])
    alltotalextort15.append(militanttuple[128])
    allcountextort15.append(militanttuple[129])
    allcountbenefit15.append(militanttuple[130])
    allcountpunish15.append(militanttuple[131])
    allcountsupport15.append(militanttuple[132])
    alltotalsupport15.append(militanttuple[133])
    allcountdefend15.append(militanttuple[134])

    allcommunity1m1.append(community1m1)
    allcommunity2m1.append(community2m1)
    allcommunity3m1.append(community3m1)
    allcommunity4m1.append(community4m1)
    allcommunity5m1.append(community5m1)
    allcommunity6m1.append(community6m1)
    allcommunity7m1.append(community7m1)
    allcommunity8m1.append(community8m1)
    allcommunity9m1.append(community9m1)
    allcommunity10m1.append(community10m1)
    allcommunity11m1.append(community11m1)
    allcommunity12m1.append(community12m1)
    allcommunity13m1.append(community13m1)
    allcommunity14m1.append(community14m1)
    allcommunity15m1.append(community15m1)

    allcommunity1m2.append(community1m2)
    allcommunity2m2.append(community2m2)
    allcommunity3m2.append(community3m2)
    allcommunity4m2.append(community4m2)
    allcommunity5m2.append(community5m2)
    allcommunity6m2.append(community6m2)
    allcommunity7m2.append(community7m2)
    allcommunity8m2.append(community8m2)
    allcommunity9m2.append(community9m2)
    allcommunity10m2.append(community10m2)
    allcommunity11m2.append(community11m2)
    allcommunity12m2.append(community12m2)
    allcommunity13m2.append(community13m2)
    allcommunity14m2.append(community14m2)
    allcommunity15m2.append(community15m2)

    allcommunity1m3.append(community1m3)
    allcommunity2m3.append(community2m3)
    allcommunity3m3.append(community3m3)
    allcommunity4m3.append(community4m3)
    allcommunity5m3.append(community5m3)
    allcommunity6m3.append(community6m3)
    allcommunity7m3.append(community7m3)
    allcommunity8m3.append(community8m3)
    allcommunity9m3.append(community9m3)
    allcommunity10m3.append(community10m3)
    allcommunity11m3.append(community11m3)
    allcommunity12m3.append(community12m3)
    allcommunity13m3.append(community13m3)
    allcommunity14m3.append(community14m3)
    allcommunity15m3.append(community15m3)

    allcommunity1m4.append(community1m4)
    allcommunity2m4.append(community2m4)
    allcommunity3m4.append(community3m4)
    allcommunity4m4.append(community4m4)
    allcommunity5m4.append(community5m4)
    allcommunity6m4.append(community6m4)
    allcommunity7m4.append(community7m4)
    allcommunity8m4.append(community8m4)
    allcommunity9m4.append(community9m4)
    allcommunity10m4.append(community10m4)
    allcommunity11m4.append(community11m4)
    allcommunity12m4.append(community12m4)
    allcommunity13m4.append(community13m4)
    allcommunity14m4.append(community14m4)
    allcommunity15m4.append(community15m4)

    allcommunity1m5.append(community1m5)
    allcommunity2m5.append(community2m5)
    allcommunity3m5.append(community3m5)
    allcommunity4m5.append(community4m5)
    allcommunity5m5.append(community5m5)
    allcommunity6m5.append(community6m5)
    allcommunity7m5.append(community7m5)
    allcommunity8m5.append(community8m5)
    allcommunity9m5.append(community9m5)
    allcommunity10m5.append(community10m5)
    allcommunity11m5.append(community11m5)
    allcommunity12m5.append(community12m5)
    allcommunity13m5.append(community13m5)
    allcommunity14m5.append(community14m5)
    allcommunity15m5.append(community15m5)

    allcommunity1m6.append(community1m6)
    allcommunity2m6.append(community2m6)
    allcommunity3m6.append(community3m6)
    allcommunity4m6.append(community4m6)
    allcommunity5m6.append(community5m6)
    allcommunity6m6.append(community6m6)
    allcommunity7m6.append(community7m6)
    allcommunity8m6.append(community8m6)
    allcommunity9m6.append(community9m6)
    allcommunity10m6.append(community10m6)
    allcommunity11m6.append(community11m6)
    allcommunity12m6.append(community12m6)
    allcommunity13m6.append(community13m6)
    allcommunity14m6.append(community14m6)
    allcommunity15m6.append(community15m6)

    allcommunity1m7.append(community1m7)
    allcommunity2m7.append(community2m7)
    allcommunity3m7.append(community3m7)
    allcommunity4m7.append(community4m7)
    allcommunity5m7.append(community5m7)
    allcommunity6m7.append(community6m7)
    allcommunity7m7.append(community7m7)
    allcommunity8m7.append(community8m7)
    allcommunity9m7.append(community9m7)
    allcommunity10m7.append(community10m7)
    allcommunity11m7.append(community11m7)
    allcommunity12m7.append(community12m7)
    allcommunity13m7.append(community13m7)
    allcommunity14m7.append(community14m7)
    allcommunity15m7.append(community15m7)

    allcommunity1m8.append(community1m8)
    allcommunity2m8.append(community2m8)
    allcommunity3m8.append(community3m8)
    allcommunity4m8.append(community4m8)
    allcommunity5m8.append(community5m8)
    allcommunity6m8.append(community6m8)
    allcommunity7m8.append(community7m8)
    allcommunity8m8.append(community8m8)
    allcommunity9m8.append(community9m8)
    allcommunity10m8.append(community10m8)
    allcommunity11m8.append(community11m8)
    allcommunity12m8.append(community12m8)
    allcommunity13m8.append(community13m8)
    allcommunity14m8.append(community14m8)
    allcommunity15m8.append(community15m8)

    allcommunity1m9.append(community1m9)
    allcommunity2m9.append(community2m9)
    allcommunity3m9.append(community3m9)
    allcommunity4m9.append(community4m9)
    allcommunity5m9.append(community5m9)
    allcommunity6m9.append(community6m9)
    allcommunity7m9.append(community7m9)
    allcommunity8m9.append(community8m9)
    allcommunity9m9.append(community9m9)
    allcommunity10m9.append(community10m9)
    allcommunity11m9.append(community11m9)
    allcommunity12m9.append(community12m9)
    allcommunity13m9.append(community13m9)
    allcommunity14m9.append(community14m9)
    allcommunity15m9.append(community15m9)

    allcommunity1m10.append(community1m10)
    allcommunity2m10.append(community2m10)
    allcommunity3m10.append(community3m10)
    allcommunity4m10.append(community4m10)
    allcommunity5m10.append(community5m10)
    allcommunity6m10.append(community6m10)
    allcommunity7m10.append(community7m10)
    allcommunity8m10.append(community8m10)
    allcommunity9m10.append(community9m10)
    allcommunity10m10.append(community10m10)
    allcommunity11m10.append(community11m10)
    allcommunity12m10.append(community12m10)
    allcommunity13m10.append(community13m10)
    allcommunity14m10.append(community14m10)
    allcommunity15m10.append(community15m10)

    allcommunity1m11.append(community1m11)
    allcommunity2m11.append(community2m11)
    allcommunity3m11.append(community3m11)
    allcommunity4m11.append(community4m11)
    allcommunity5m11.append(community5m11)
    allcommunity6m11.append(community6m11)
    allcommunity7m11.append(community7m11)
    allcommunity8m11.append(community8m11)
    allcommunity9m11.append(community9m11)
    allcommunity10m11.append(community10m11)
    allcommunity11m11.append(community11m11)
    allcommunity12m11.append(community12m11)
    allcommunity13m11.append(community13m11)
    allcommunity14m11.append(community14m11)
    allcommunity15m11.append(community15m11)

    allcommunity1m12.append(community1m12)
    allcommunity2m12.append(community2m12)
    allcommunity3m12.append(community3m12)
    allcommunity4m12.append(community4m12)
    allcommunity5m12.append(community5m12)
    allcommunity6m12.append(community6m12)
    allcommunity7m12.append(community7m12)
    allcommunity8m12.append(community8m12)
    allcommunity9m12.append(community9m12)
    allcommunity10m12.append(community10m12)
    allcommunity11m12.append(community11m12)
    allcommunity12m12.append(community12m12)
    allcommunity13m12.append(community13m12)
    allcommunity14m12.append(community14m12)
    allcommunity15m12.append(community15m12)

    allcommunity1m13.append(community1m13)
    allcommunity2m13.append(community2m13)
    allcommunity3m13.append(community3m13)
    allcommunity4m13.append(community4m13)
    allcommunity5m13.append(community5m13)
    allcommunity6m13.append(community6m13)
    allcommunity7m13.append(community7m13)
    allcommunity8m13.append(community8m13)
    allcommunity9m13.append(community9m13)
    allcommunity10m13.append(community10m13)
    allcommunity11m13.append(community11m13)
    allcommunity12m13.append(community12m13)
    allcommunity13m13.append(community13m13)
    allcommunity14m13.append(community14m13)
    allcommunity15m13.append(community15m13)

    allcommunity1m14.append(community1m14)
    allcommunity2m14.append(community2m14)
    allcommunity3m14.append(community3m14)
    allcommunity4m14.append(community4m14)
    allcommunity5m14.append(community5m14)
    allcommunity6m14.append(community6m14)
    allcommunity7m14.append(community7m14)
    allcommunity8m14.append(community8m14)
    allcommunity9m14.append(community9m14)
    allcommunity10m14.append(community10m14)
    allcommunity11m14.append(community11m14)
    allcommunity12m14.append(community12m14)
    allcommunity13m14.append(community13m14)
    allcommunity14m14.append(community14m14)
    allcommunity15m14.append(community15m14)

    allcommunity1m15.append(community1m15)
    allcommunity2m15.append(community2m15)
    allcommunity3m15.append(community3m15)
    allcommunity4m15.append(community4m15)
    allcommunity5m15.append(community5m15)
    allcommunity6m15.append(community6m15)
    allcommunity7m15.append(community7m15)
    allcommunity8m15.append(community8m15)
    allcommunity9m15.append(community9m15)
    allcommunity10m15.append(community10m15)
    allcommunity11m15.append(community11m15)
    allcommunity12m15.append(community12m15)
    allcommunity13m15.append(community13m15)
    allcommunity14m15.append(community14m15)
    allcommunity15m15.append(community15m15)

    allcommunity1defend.append(dftuple[0])
    allcommunity2defend.append(dftuple[1])
    allcommunity3defend.append(dftuple[2])
    allcommunity4defend.append(dftuple[3])
    allcommunity5defend.append(dftuple[4])
    allcommunity6defend.append(dftuple[5])
    allcommunity7defend.append(dftuple[6])
    allcommunity8defend.append(dftuple[7])
    allcommunity9defend.append(dftuple[8])
    allcommunity10defend.append(dftuple[9])
    allcommunity11defend.append(dftuple[10])
    allcommunity12defend.append(dftuple[11])
    allcommunity13defend.append(dftuple[12])
    allcommunity14defend.append(dftuple[13])
    allcommunity15defend.append(dftuple[14])

    alloneandtwo.append(dftuple[15])
    alloneandthree.append(dftuple[16])
    alloneandfour.append(dftuple[17])
    alloneandfive.append(dftuple[18])
    alloneandsix.append(dftuple[19])
    alloneandseven.append(dftuple[20])
    alloneandeight.append(dftuple[21])
    alloneandnine.append(dftuple[22])
    alloneandten.append(dftuple[23])
    alloneandeleven.append(dftuple[24])
    alloneandtwelve.append(dftuple[25])
    alloneandthirteen.append(dftuple[26])
    alloneandfourteen.append(dftuple[27])
    alloneandfifteen.append(dftuple[28])
    alltwoandthree.append(dftuple[29])
    alltwoandfour.append(dftuple[30])
    alltwoandfive.append(dftuple[31])
    alltwoandsix.append(dftuple[32])
    alltwoandseven.append(dftuple[33])
    alltwoandeight.append(dftuple[34])
    alltwoandnine.append(dftuple[35])
    alltwoandten.append(dftuple[36])
    alltwoandeleven.append(dftuple[37])
    alltwoandtwelve.append(dftuple[38])
    alltwoandthirteen.append(dftuple[39])
    alltwoandfourteen.append(dftuple[40])
    alltwoandfifteen.append(dftuple[41])
    allthreeandfour.append(dftuple[42])
    allthreeandfive.append(dftuple[43])
    allthreeandsix.append(dftuple[44])
    allthreeandseven.append(dftuple[45])
    allthreeandeight.append(dftuple[46])
    allthreeandnine.append(dftuple[47])
    allthreeandten.append(dftuple[48])
    allthreeandeleven.append(dftuple[49])
    allthreeandtwelve.append(dftuple[50])
    allthreeandthirteen.append(dftuple[51])
    allthreeandfourteen.append(dftuple[52])
    allthreeandfifteen.append(dftuple[53])
    allfourandfive.append(dftuple[54])
    allfourandsix.append(dftuple[55])
    allfourandseven.append(dftuple[56])
    allfourandeight.append(dftuple[57])
    allfourandnine.append(dftuple[58])
    allfourandten.append(dftuple[59])
    allfourandeleven.append(dftuple[60])
    allfourandtwelve.append(dftuple[61])
    allfourandthirteen.append(dftuple[62])
    allfourandfourteen.append(dftuple[63])
    allfourandfifteen.append(dftuple[64])
    allfiveandsix.append(dftuple[65])
    allfiveandseven.append(dftuple[66])
    allfiveandeight.append(dftuple[67])
    allfiveandnine.append(dftuple[68])
    allfiveandten.append(dftuple[69])
    allfiveandeleven.append(dftuple[70])
    allfiveandtwelve.append(dftuple[71])
    allfiveandthirteen.append(dftuple[72])
    allfiveandfourteen.append(dftuple[73])
    allfiveandfifteen.append(dftuple[74])
    allsixandseven.append(dftuple[75])
    allsixandeight.append(dftuple[76])
    allsixandnine.append(dftuple[77])
    allsixandten.append(dftuple[78])
    allsixandeleven.append(dftuple[79])
    allsixandtwelve.append(dftuple[80])
    allsixandthirteen.append(dftuple[81])
    allsixandfourteen.append(dftuple[82])
    allsixandfifteen.append(dftuple[83])
    allsevenandeight.append(dftuple[84])
    allsevenandnine.append(dftuple[85])
    allsevenandten.append(dftuple[86])
    allsevenandeleven.append(dftuple[87])
    allsevenandtwelve.append(dftuple[88])
    allsevenandthirteen.append(dftuple[89])
    allsevenandfourteen.append(dftuple[90])
    allsevenandfifteen.append(dftuple[91])
    alleightandnine.append(dftuple[92])
    alleightandten.append(dftuple[93])
    alleightandeleven.append(dftuple[94])
    alleightandtwelve.append(dftuple[95])
    alleightandthirteen.append(dftuple[96])
    alleightandfourteen.append(dftuple[97])
    alleightandfifteen.append(dftuple[98])
    allnineandten.append(dftuple[99])
    allnineandeleven.append(dftuple[100])
    allnineandtwelve.append(dftuple[101])
    allnineandthirteen.append(dftuple[102])
    allnineandfourteen.append(dftuple[103])
    allnineandfifteen.append(dftuple[104])
    alltenandeleven.append(dftuple[105])
    alltenandtwelve.append(dftuple[106])
    alltenandthirteen.append(dftuple[107])
    alltenandfourteen.append(dftuple[108])
    alltenandfifteen.append(dftuple[109])
    allelevenandtwelve.append(dftuple[110])
    allelevenandthirteen.append(dftuple[111])
    allelevenandfourteen.append(dftuple[112])
    allelevenandfifteen.append(dftuple[113])
    alltwelveandthirteen.append(dftuple[114])
    alltwelveandfourteen.append(dftuple[115])
    alltwelveandfifteen.append(dftuple[116])
    allthirteenandfourteen.append(dftuple[117])
    allthirteenandfifteen.append(dftuple[118])
    allfourteenandfifteen.append(dftuple[119])

    s += 1

avestrength1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allstrength1)]
avenotorietyratio1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnotorietyratio1)]
avetotalextort1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalextort1)]
avecountextort1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountextort1)]
avecountbenefit1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountbenefit1)]
avecountpunish1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountpunish1)]
avecountsupport1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountsupport1)]
avetotalsupport1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalsupport1)]
avecountdefend1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountdefend1)]

avestrength2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allstrength2)]
avenotorietyratio2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnotorietyratio2)]
avetotalextort2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalextort2)]
avecountextort2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountextort2)]
avecountbenefit2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountbenefit2)]
avecountpunish2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountpunish2)]
avecountsupport2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountsupport2)]
avetotalsupport2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalsupport2)]
avecountdefend2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountdefend2)]

avestrength3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allstrength3)]
avenotorietyratio3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnotorietyratio3)]
avetotalextort3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalextort3)]
avecountextort3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountextort3)]
avecountbenefit3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountbenefit3)]
avecountpunish3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountpunish3)]
avecountsupport3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountsupport3)]
avetotalsupport3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalsupport3)]
avecountdefend3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountdefend3)]

avestrength4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allstrength4)]
avenotorietyratio4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnotorietyratio4)]
avetotalextort4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalextort4)]
avecountextort4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountextort4)]
avecountbenefit4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountbenefit4)]
avecountpunish4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountpunish4)]
avecountsupport4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountsupport4)]
avetotalsupport4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalsupport4)]
avecountdefend4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountdefend4)]

avestrength5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allstrength5)]
avenotorietyratio5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnotorietyratio5)]
avetotalextort5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalextort5)]
avecountextort5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountextort5)]
avecountbenefit5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountbenefit5)]
avecountpunish5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountpunish5)]
avecountsupport5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountsupport5)]
avetotalsupport5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalsupport5)]
avecountdefend5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountdefend5)]

avestrength6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allstrength6)]
avenotorietyratio6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnotorietyratio6)]
avetotalextort6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalextort6)]
avecountextort6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountextort6)]
avecountbenefit6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountbenefit6)]
avecountpunish6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountpunish6)]
avecountsupport6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountsupport6)]
avetotalsupport6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalsupport6)]
avecountdefend6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountdefend6)]

avestrength7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allstrength7)]
avenotorietyratio7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnotorietyratio7)]
avetotalextort7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalextort7)]
avecountextort7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountextort7)]
avecountbenefit7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountbenefit7)]
avecountpunish7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountpunish7)]
avecountsupport7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountsupport7)]
avetotalsupport7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalsupport7)]
avecountdefend7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountdefend7)]

avestrength8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allstrength8)]
avenotorietyratio8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnotorietyratio8)]
avetotalextort8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalextort8)]
avecountextort8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountextort8)]
avecountbenefit8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountbenefit8)]
avecountpunish8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountpunish8)]
avecountsupport8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountsupport8)]
avetotalsupport8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalsupport8)]
avecountdefend8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountdefend8)]

avestrength9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allstrength9)]
avenotorietyratio9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnotorietyratio9)]
avetotalextort9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalextort9)]
avecountextort9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountextort9)]
avecountbenefit9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountbenefit9)]
avecountpunish9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountpunish9)]
avecountsupport9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountsupport9)]
avetotalsupport9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalsupport9)]
avecountdefend9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountdefend9)]

avestrength10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allstrength10)]
avenotorietyratio10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnotorietyratio10)]
avetotalextort10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalextort10)]
avecountextort10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountextort10)]
avecountbenefit10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountbenefit10)]
avecountpunish10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountpunish10)]
avecountsupport10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountsupport10)]
avetotalsupport10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalsupport10)]
avecountdefend10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountdefend10)]

avestrength11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allstrength11)]
avenotorietyratio11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnotorietyratio11)]
avetotalextort11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalextort11)]
avecountextort11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountextort11)]
avecountbenefit11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountbenefit11)]
avecountpunish11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountpunish11)]
avecountsupport11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountsupport11)]
avetotalsupport11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalsupport11)]
avecountdefend11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountdefend11)]

avestrength12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allstrength12)]
avenotorietyratio12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnotorietyratio12)]
avetotalextort12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalextort12)]
avecountextort12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountextort12)]
avecountbenefit12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountbenefit12)]
avecountpunish12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountpunish12)]
avecountsupport12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountsupport12)]
avetotalsupport12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalsupport12)]
avecountdefend12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountdefend12)]

avestrength13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allstrength13)]
avenotorietyratio13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnotorietyratio13)]
avetotalextort13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalextort13)]
avecountextort13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountextort13)]
avecountbenefit13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountbenefit13)]
avecountpunish13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountpunish13)]
avecountsupport13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountsupport13)]
avetotalsupport13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalsupport13)]
avecountdefend13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountdefend13)]

avestrength14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allstrength14)]
avenotorietyratio14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnotorietyratio14)]
avetotalextort14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalextort14)]
avecountextort14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountextort14)]
avecountbenefit14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountbenefit14)]
avecountpunish14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountpunish14)]
avecountsupport14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountsupport14)]
avetotalsupport14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalsupport14)]
avecountdefend14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountdefend14)]

avestrength15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allstrength15)]
avenotorietyratio15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnotorietyratio15)]
avetotalextort15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalextort15)]
avecountextort15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountextort15)]
avecountbenefit15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountbenefit15)]
avecountpunish15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountpunish15)]
avecountsupport15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountsupport15)]
avetotalsupport15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltotalsupport15)]
avecountdefend15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcountdefend15)]

avecommunity1m1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity1m1)]
avecommunity2m1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity2m1)]
avecommunity3m1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity3m1)]
avecommunity4m1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity4m1)]
avecommunity5m1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity5m1)]
avecommunity6m1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity6m1)]
avecommunity7m1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity7m1)]
avecommunity8m1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity8m1)]
avecommunity9m1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity9m1)]
avecommunity10m1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity10m1)]
avecommunity11m1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity11m1)]
avecommunity12m1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity12m1)]
avecommunity13m1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity13m1)]
avecommunity14m1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity14m1)]
avecommunity15m1 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity15m1)]

avecommunity1m2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity1m2)]
avecommunity2m2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity2m2)]
avecommunity3m2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity3m2)]
avecommunity4m2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity4m2)]
avecommunity5m2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity5m2)]
avecommunity6m2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity6m2)]
avecommunity7m2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity7m2)]
avecommunity8m2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity8m2)]
avecommunity9m2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity9m2)]
avecommunity10m2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity10m2)]
avecommunity11m2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity11m2)]
avecommunity12m2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity12m2)]
avecommunity13m2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity13m2)]
avecommunity14m2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity14m2)]
avecommunity15m2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity15m2)]

avecommunity1m3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity1m3)]
avecommunity2m3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity2m3)]
avecommunity3m3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity3m3)]
avecommunity4m3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity4m3)]
avecommunity5m3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity5m3)]
avecommunity6m3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity6m3)]
avecommunity7m3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity7m3)]
avecommunity8m3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity8m3)]
avecommunity9m3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity9m3)]
avecommunity10m3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity10m3)]
avecommunity11m3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity11m3)]
avecommunity12m3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity12m3)]
avecommunity13m3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity13m3)]
avecommunity14m3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity14m3)]
avecommunity15m3 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity15m3)]

avecommunity1m4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity1m4)]
avecommunity2m4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity2m4)]
avecommunity3m4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity3m4)]
avecommunity4m4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity4m4)]
avecommunity5m4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity5m4)]
avecommunity6m4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity6m4)]
avecommunity7m4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity7m4)]
avecommunity8m4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity8m4)]
avecommunity9m4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity9m4)]
avecommunity10m4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity10m4)]
avecommunity11m4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity11m4)]
avecommunity12m4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity12m4)]
avecommunity13m4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity13m4)]
avecommunity14m4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity14m4)]
avecommunity15m4 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity15m4)]

avecommunity1m5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity1m5)]
avecommunity2m5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity2m5)]
avecommunity3m5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity3m5)]
avecommunity4m5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity4m5)]
avecommunity5m5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity5m5)]
avecommunity6m5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity6m5)]
avecommunity7m5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity7m5)]
avecommunity8m5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity8m5)]
avecommunity9m5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity9m5)]
avecommunity10m5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity10m5)]
avecommunity11m5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity11m5)]
avecommunity12m5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity12m5)]
avecommunity13m5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity13m5)]
avecommunity14m5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity14m5)]
avecommunity15m5 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity15m5)]

avecommunity1m6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity1m6)]
avecommunity2m6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity2m6)]
avecommunity3m6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity3m6)]
avecommunity4m6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity4m6)]
avecommunity5m6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity5m6)]
avecommunity6m6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity6m6)]
avecommunity7m6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity7m6)]
avecommunity8m6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity8m6)]
avecommunity9m6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity9m6)]
avecommunity10m6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity10m6)]
avecommunity11m6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity11m6)]
avecommunity12m6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity12m6)]
avecommunity13m6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity13m6)]
avecommunity14m6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity14m6)]
avecommunity15m6 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity15m6)]

avecommunity1m7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity1m7)]
avecommunity2m7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity2m7)]
avecommunity3m7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity3m7)]
avecommunity4m7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity4m7)]
avecommunity5m7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity5m7)]
avecommunity6m7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity6m7)]
avecommunity7m7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity7m7)]
avecommunity8m7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity8m7)]
avecommunity9m7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity9m7)]
avecommunity10m7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity10m7)]
avecommunity11m7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity11m7)]
avecommunity12m7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity12m7)]
avecommunity13m7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity13m7)]
avecommunity14m7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity14m7)]
avecommunity15m7 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity15m7)]

avecommunity1m8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity1m8)]
avecommunity2m8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity2m8)]
avecommunity3m8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity3m8)]
avecommunity4m8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity4m8)]
avecommunity5m8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity5m8)]
avecommunity6m8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity6m8)]
avecommunity7m8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity7m8)]
avecommunity8m8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity8m8)]
avecommunity9m8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity9m8)]
avecommunity10m8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity10m8)]
avecommunity11m8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity11m8)]
avecommunity12m8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity12m8)]
avecommunity13m8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity13m8)]
avecommunity14m8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity14m8)]
avecommunity15m8 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity15m8)]

avecommunity1m9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity1m9)]
avecommunity2m9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity2m9)]
avecommunity3m9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity3m9)]
avecommunity4m9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity4m9)]
avecommunity5m9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity5m9)]
avecommunity6m9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity6m9)]
avecommunity7m9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity7m9)]
avecommunity8m9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity8m9)]
avecommunity9m9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity9m9)]
avecommunity10m9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity10m9)]
avecommunity11m9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity11m9)]
avecommunity12m9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity12m9)]
avecommunity13m9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity13m9)]
avecommunity14m9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity14m9)]
avecommunity15m9 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity15m9)]

avecommunity1m10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity1m10)]
avecommunity2m10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity2m10)]
avecommunity3m10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity3m10)]
avecommunity4m10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity4m10)]
avecommunity5m10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity5m10)]
avecommunity6m10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity6m10)]
avecommunity7m10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity7m10)]
avecommunity8m10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity8m10)]
avecommunity9m10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity9m10)]
avecommunity10m10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity10m10)]
avecommunity11m10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity11m10)]
avecommunity12m10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity12m10)]
avecommunity13m10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity13m10)]
avecommunity14m10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity14m10)]
avecommunity15m10 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity15m10)]

avecommunity1m11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity1m11)]
avecommunity2m11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity2m11)]
avecommunity3m11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity3m11)]
avecommunity4m11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity4m11)]
avecommunity5m11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity5m11)]
avecommunity6m11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity6m11)]
avecommunity7m11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity7m11)]
avecommunity8m11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity8m11)]
avecommunity9m11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity9m11)]
avecommunity10m11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity10m11)]
avecommunity11m11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity11m11)]
avecommunity12m11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity12m11)]
avecommunity13m11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity13m11)]
avecommunity14m11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity14m11)]
avecommunity15m11 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity15m11)]

avecommunity1m12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity1m12)]
avecommunity2m12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity2m12)]
avecommunity3m12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity3m12)]
avecommunity4m12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity4m12)]
avecommunity5m12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity5m12)]
avecommunity6m12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity6m12)]
avecommunity7m12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity7m12)]
avecommunity8m12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity8m12)]
avecommunity9m12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity9m12)]
avecommunity10m12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity10m12)]
avecommunity11m12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity11m12)]
avecommunity12m12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity12m12)]
avecommunity13m12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity13m12)]
avecommunity14m12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity14m12)]
avecommunity15m12 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity15m12)]

avecommunity1m13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity1m13)]
avecommunity2m13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity2m13)]
avecommunity3m13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity3m13)]
avecommunity4m13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity4m13)]
avecommunity5m13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity5m13)]
avecommunity6m13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity6m13)]
avecommunity7m13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity7m13)]
avecommunity8m13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity8m13)]
avecommunity9m13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity9m13)]
avecommunity10m13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity10m13)]
avecommunity11m13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity11m13)]
avecommunity12m13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity12m13)]
avecommunity13m13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity13m13)]
avecommunity14m13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity14m13)]
avecommunity15m13 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity15m13)]

avecommunity1m14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity1m14)]
avecommunity2m14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity2m14)]
avecommunity3m14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity3m14)]
avecommunity4m14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity4m14)]
avecommunity5m14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity5m14)]
avecommunity6m14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity6m14)]
avecommunity7m14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity7m14)]
avecommunity8m14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity8m14)]
avecommunity9m14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity9m14)]
avecommunity10m14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity10m14)]
avecommunity11m14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity11m14)]
avecommunity12m14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity12m14)]
avecommunity13m14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity13m14)]
avecommunity14m14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity14m14)]
avecommunity15m14 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity15m14)]

avecommunity1m15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity1m15)]
avecommunity2m15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity2m15)]
avecommunity3m15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity3m15)]
avecommunity4m15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity4m15)]
avecommunity5m15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity5m15)]
avecommunity6m15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity6m15)]
avecommunity7m15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity7m15)]
avecommunity8m15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity8m15)]
avecommunity9m15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity9m15)]
avecommunity10m15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity10m15)]
avecommunity11m15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity11m15)]
avecommunity12m15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity12m15)]
avecommunity13m15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity13m15)]
avecommunity14m15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity14m15)]
avecommunity15m15 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity15m15)]

avecommunity1defend = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity1defend)]
avecommunity2defend = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity2defend)]
avecommunity3defend = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity3defend)]
avecommunity4defend = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity4defend)]
avecommunity5defend = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity5defend)]
avecommunity6defend = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity6defend)]
avecommunity7defend = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity7defend)]
avecommunity8defend = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity8defend)]
avecommunity9defend = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity9defend)]
avecommunity10defend = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity10defend)]
avecommunity11defend = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity11defend)]
avecommunity12defend = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity12defend)]
avecommunity13defend = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity13defend)]
avecommunity14defend = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity14defend)]
avecommunity15defend = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allcommunity15defend)]

aveoneandtwo = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alloneandtwo)]
aveoneandthree = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alloneandthree)]
avetwoandthree = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltwoandthree)]

aveoneandtwo = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alloneandtwo)]
aveoneandthree = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alloneandthree)]
aveoneandfour = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alloneandfour)]
aveoneandfive = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alloneandfive)]
aveoneandsix = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alloneandsix)]
aveoneandseven = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alloneandseven)]
aveoneandeight = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alloneandeight)]
aveoneandnine = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alloneandnine)]
aveoneandten = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alloneandten)]
aveoneandeleven = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alloneandeleven)]
aveoneandtwelve = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alloneandtwelve)]
aveoneandthirteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alloneandthirteen)]
aveoneandfourteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alloneandfourteen)]
aveoneandfifteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alloneandfifteen)]

avetwoandthree = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltwoandthree)]
avetwoandfour = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltwoandfour)]
avetwoandfive = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltwoandfive)]
avetwoandsix = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltwoandsix)]
avetwoandseven = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltwoandseven)]
avetwoandeight = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltwoandeight)]
avetwoandnine = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltwoandnine)]
avetwoandten = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltwoandten)]
avetwoandeleven = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltwoandeleven)]
avetwoandtwelve = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltwoandtwelve)]
avetwoandthirteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltwoandthirteen)]
avetwoandfourteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltwoandfourteen)]
avetwoandfifteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltwoandfifteen)]

avethreeandfour = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allthreeandfour)]
avethreeandfive = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allthreeandfive)]
avethreeandsix = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allthreeandsix)]
avethreeandseven = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allthreeandseven)]
avethreeandeight = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allthreeandeight)]
avethreeandnine = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allthreeandnine)]
avethreeandten = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allthreeandten)]
avethreeandeleven = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allthreeandeleven)]
avethreeandtwelve = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allthreeandtwelve)]
avethreeandthirteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allthreeandthirteen)]
avethreeandfourteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allthreeandfourteen)]
avethreeandfifteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allthreeandfifteen)]

avefourandfive = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfourandfive)]
avefourandsix = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfourandsix)]
avefourandseven = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfourandseven)]
avefourandeight = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfourandeight)]
avefourandnine = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfourandnine)]
avefourandten = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfourandten)]
avefourandeleven = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfourandeleven)]
avefourandtwelve = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfourandtwelve)]
avefourandthirteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfourandthirteen)]
avefourandfourteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfourandfourteen)]
avefourandfifteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfourandfifteen)]

avefiveandsix = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfiveandsix)]
avefiveandseven = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfiveandseven)]
avefiveandeight = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfiveandeight)]
avefiveandnine = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfiveandnine)]
avefiveandten = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfiveandten)]
avefiveandeleven = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfiveandeleven)]
avefiveandtwelve = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfiveandtwelve)]
avefiveandthirteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfiveandthirteen)]
avefiveandfourteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfiveandfourteen)]
avefiveandfifteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfiveandfifteen)]

avesixandseven = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allsixandseven)]
avesixandeight = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allsixandeight)]
avesixandnine = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allsixandnine)]
avesixandten = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allsixandten)]
avesixandeleven = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allsixandeleven)]
avesixandtwelve = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allsixandtwelve)]
avesixandthirteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allsixandthirteen)]
avesixandfourteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allsixandfourteen)]
avesixandfifteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allsixandfifteen)]

avesevenandeight = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allsevenandeight)]
avesevenandnine = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allsevenandnine)]
avesevenandten = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allsevenandten)]
avesevenandeleven = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allsevenandeleven)]
avesevenandtwelve = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allsevenandtwelve)]
avesevenandthirteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allsevenandthirteen)]
avesevenandfourteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allsevenandfourteen)]
avesevenandfifteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allsevenandfifteen)]

aveeightandnine = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alleightandnine)]
aveeightandten = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alleightandten)]
aveeightandeleven = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alleightandeleven)]
aveeightandtwelve = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alleightandtwelve)]
aveeightandthirteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alleightandthirteen)]
aveeightandfourteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alleightandfourteen)]
aveeightandfifteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alleightandfifteen)]

avenineandten = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnineandten)]
avenineandeleven = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnineandeleven)]
avenineandtwelve = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnineandtwelve)]
avenineandthirteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnineandthirteen)]
avenineandfourteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnineandfourteen)]
avenineandfifteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allnineandfifteen)]

avetenandeleven = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltenandeleven)]
avetenandtwelve = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltenandtwelve)]
avetenandthirteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltenandthirteen)]
avetenandfourteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltenandfourteen)]
avetenandfifteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltenandfifteen)]

aveelevenandtwelve = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allelevenandtwelve)]
aveelevenandthirteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allelevenandthirteen)]
aveelevenandfourteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allelevenandfourteen)]
aveelevenandfifteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allelevenandfifteen)]

avetwelveandthirteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltwelveandthirteen)]
avetwelveandfourteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltwelveandfourteen)]
avetwelveandfifteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*alltwelveandfifteen)]

avethirteenandfourteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allthirteenandfourteen)]
avethirteenandfifteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allthirteenandfifteen)]
avefourteenandfifteen = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+sr+tt)/40 for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, sr, tt in zip(*allfourteenandfifteen)]
