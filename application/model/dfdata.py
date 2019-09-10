import re


def dfdata(communitydefendstrings, fightstrings, blanks):

    # community1defend
    liststring = communitydefendstrings[1].rsplit(sep=',')
    community1defend = []
    if communitydefendstrings[1] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community1defend.append(fixed)
            i += 1
    else:
        community1defend = blanks

    # community2defend
    liststring = communitydefendstrings[2].rsplit(sep=',')
    community2defend = []
    if communitydefendstrings[2] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community2defend.append(fixed)
            i += 1
    else:
        community2defend = blanks

    # community3defend
    liststring = communitydefendstrings[3].rsplit(sep=',')
    community3defend = []
    if communitydefendstrings[3] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community3defend.append(fixed)
            i += 1
    else:
        community3defend = blanks

    # community4defend
    liststring = communitydefendstrings[4].rsplit(sep=',')
    community4defend = []
    if communitydefendstrings[4] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community4defend.append(fixed)
            i += 1
    else:
        community4defend = blanks

    # community5defend
    liststring = communitydefendstrings[5].rsplit(sep=',')
    community5defend = []
    if communitydefendstrings[5] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community5defend.append(fixed)
            i += 1
    else:
        community5defend = blanks

    # community6defend
    liststring = communitydefendstrings[6].rsplit(sep=',')
    community6defend = []
    if communitydefendstrings[6] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community6defend.append(fixed)
            i += 1
    else:
        community6defend = blanks

    # community7defend
    liststring = communitydefendstrings[7].rsplit(sep=',')
    community7defend = []
    if communitydefendstrings[7] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community7defend.append(fixed)
            i += 1
    else:
        community7defend = blanks

    # community8defend
    liststring = communitydefendstrings[8].rsplit(sep=',')
    community8defend = []
    if communitydefendstrings[8] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community8defend.append(fixed)
            i += 1
    else:
        community8defend = blanks

    # community9defend
    liststring = communitydefendstrings[9].rsplit(sep=',')
    community9defend = []
    if communitydefendstrings[9] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community9defend.append(fixed)
            i += 1
    else:
        community9defend = blanks

    # community10defend
    liststring = communitydefendstrings[10].rsplit(sep=',')
    community10defend = []
    if communitydefendstrings[10] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community10defend.append(fixed)
            i += 1
    else:
        community10defend = blanks

    # community11defend
    liststring = communitydefendstrings[11].rsplit(sep=',')
    community11defend = []
    if communitydefendstrings[11] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community11defend.append(fixed)
            i += 1
    else:
        community11defend = blanks

    # community12defend
    liststring = communitydefendstrings[12].rsplit(sep=',')
    community12defend = []
    if communitydefendstrings[12] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community12defend.append(fixed)
            i += 1
    else:
        community12defend = blanks

    # community13defend
    liststring = communitydefendstrings[13].rsplit(sep=',')
    community13defend = []
    if communitydefendstrings[13] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community13defend.append(fixed)
            i += 1
    else:
        community13defend = blanks

    # community14defend
    liststring = communitydefendstrings[14].rsplit(sep=',')
    community14defend = []
    if communitydefendstrings[14] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community14defend.append(fixed)
            i += 1
    else:
        community14defend = blanks

    # community15defend
    liststring = communitydefendstrings[15].rsplit(sep=',')
    community15defend = []
    if communitydefendstrings[15] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            community15defend.append(fixed)
            i += 1
    else:
        community15defend = blanks

# Militant Fighting
    # oneandtwo
    liststring = fightstrings[1].rsplit(sep=',')
    oneandtwo = []
    if fightstrings[1] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            oneandtwo.append(fixed)
            i += 1
    else:
        oneandtwo = blanks

    # oneandthree
    liststring = fightstrings[2].rsplit(sep=',')
    oneandthree = []
    if fightstrings[2] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            oneandthree.append(fixed)
            i += 1
    else:
        oneandthree = blanks

    # oneandfour
    liststring = fightstrings[3].rsplit(sep=',')
    oneandfour = []
    if fightstrings[3] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            oneandfour.append(fixed)
            i += 1
    else:
        oneandfour = blanks

    # oneandfive
    liststring = fightstrings[4].rsplit(sep=',')
    oneandfive = []
    if fightstrings[4] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            oneandfive.append(fixed)
            i += 1
    else:
        oneandfive = blanks

    # oneandsix
    liststring = fightstrings[5].rsplit(sep=',')
    oneandsix = []
    if fightstrings[5] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            oneandsix.append(fixed)
            i += 1
    else:
        oneandsix = blanks

    # oneandseven
    liststring = fightstrings[6].rsplit(sep=',')
    oneandseven = []
    if fightstrings[6] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            oneandseven.append(fixed)
            i += 1
    else:
        oneandseven = blanks

    # oneandeight
    liststring = fightstrings[7].rsplit(sep=',')
    oneandeight = []
    if fightstrings[7] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            oneandeight.append(fixed)
            i += 1
    else:
        oneandeight = blanks

    # oneandnine
    liststring = fightstrings[8].rsplit(sep=',')
    oneandnine = []
    if fightstrings[8] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            oneandnine.append(fixed)
            i += 1
    else:
        oneandnine = blanks

    # oneandten
    liststring = fightstrings[9].rsplit(sep=',')
    oneandten = []
    if fightstrings[9] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            oneandten.append(fixed)
            i += 1
    else:
        oneandten = blanks

    # oneandeleven
    liststring = fightstrings[10].rsplit(sep=',')
    oneandeleven = []
    if fightstrings[10] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            oneandeleven.append(fixed)
            i += 1
    else:
        oneandeleven = blanks

    # oneandtwelve
    liststring = fightstrings[11].rsplit(sep=',')
    oneandtwelve = []
    if fightstrings[11] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            oneandtwelve.append(fixed)
            i += 1
    else:
        oneandtwelve = blanks

    # oneandthirteen
    liststring = fightstrings[12].rsplit(sep=',')
    oneandthirteen = []
    if fightstrings[12] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            oneandthirteen.append(fixed)
            i += 1
    else:
        oneandthirteen = blanks

    # oneandfourteen
    liststring = fightstrings[13].rsplit(sep=',')
    oneandfourteen = []
    if fightstrings[13] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            oneandfourteen.append(fixed)
            i += 1
    else:
        oneandfourteen = blanks

    # oneandfifteen
    liststring = fightstrings[14].rsplit(sep=',')
    oneandfifteen = []
    if fightstrings[14] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            oneandfifteen.append(fixed)
            i += 1
    else:
        oneandfifteen = blanks

    # twoandthree
    liststring = fightstrings[15].rsplit(sep=',')
    twoandthree = []
    if fightstrings[15] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            twoandthree.append(fixed)
            i += 1
    else:
        twoandthree = blanks

    # twoandfour
    liststring = fightstrings[16].rsplit(sep=',')
    twoandfour = []
    if fightstrings[16] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            twoandfour.append(fixed)
            i += 1
    else:
        twoandfour = blanks

    # twoandfive
    liststring = fightstrings[17].rsplit(sep=',')
    twoandfive = []
    if fightstrings[17] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            twoandfive.append(fixed)
            i += 1
    else:
        twoandfive = blanks

    # twoandsix
    liststring = fightstrings[18].rsplit(sep=',')
    twoandsix = []
    if fightstrings[18] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            twoandsix.append(fixed)
            i += 1
    else:
        twoandsix = blanks

    # twoandseven
    liststring = fightstrings[19].rsplit(sep=',')
    twoandseven = []
    if fightstrings[19] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            twoandseven.append(fixed)
            i += 1
    else:
        twoandseven = blanks

    # twoandeight
    liststring = fightstrings[20].rsplit(sep=',')
    twoandeight = []
    if fightstrings[20] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            twoandeight.append(fixed)
            i += 1
    else:
        twoandeight = blanks

    # twoandnine
    liststring = fightstrings[21].rsplit(sep=',')
    twoandnine = []
    if fightstrings[21] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            twoandnine.append(fixed)
            i += 1
    else:
        twoandnine = blanks

    # twoandten
    liststring = fightstrings[22].rsplit(sep=',')
    twoandten = []
    if fightstrings[22] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            twoandten.append(fixed)
            i += 1
    else:
        twoandten = blanks

    # twoandeleven
    liststring = fightstrings[23].rsplit(sep=',')
    twoandeleven = []
    if fightstrings[23] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            twoandeleven.append(fixed)
            i += 1
    else:
        twoandeleven = blanks

    # twoandtwelve
    liststring = fightstrings[24].rsplit(sep=',')
    twoandtwelve = []
    if fightstrings[24] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            twoandtwelve.append(fixed)
            i += 1
    else:
        twoandtwelve = blanks

    # twoandthirteen
    liststring = fightstrings[25].rsplit(sep=',')
    twoandthirteen = []
    if fightstrings[25] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            twoandthirteen.append(fixed)
            i += 1
    else:
        twoandthirteen = blanks

    # twoandfourteen
    liststring = fightstrings[26].rsplit(sep=',')
    twoandfourteen = []
    if fightstrings[26] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            twoandfourteen.append(fixed)
            i += 1
    else:
        twoandfourteen = blanks

    # twoandfifteen
    liststring = fightstrings[27].rsplit(sep=',')
    twoandfifteen = []
    if fightstrings[27] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            twoandfifteen.append(fixed)
            i += 1
    else:
        twoandfifteen = blanks

    # threeandfour
    liststring = fightstrings[28].rsplit(sep=',')
    threeandfour = []
    if fightstrings[28] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            threeandfour.append(fixed)
            i += 1
    else:
        threeandfour = blanks

    # threeandfive
    liststring = fightstrings[29].rsplit(sep=',')
    threeandfive = []
    if fightstrings[29] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            threeandfive.append(fixed)
            i += 1
    else:
        threeandfive = blanks

    # threeandsix
    liststring = fightstrings[30].rsplit(sep=',')
    threeandsix = []
    if fightstrings[30] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            threeandsix.append(fixed)
            i += 1
    else:
        threeandsix = blanks

    # threeandseven
    liststring = fightstrings[31].rsplit(sep=',')
    threeandseven = []
    if fightstrings[31] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            threeandseven.append(fixed)
            i += 1
    else:
        threeandseven = blanks

    # threeandeight
    liststring = fightstrings[32].rsplit(sep=',')
    threeandeight = []
    if fightstrings[32] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            threeandeight.append(fixed)
            i += 1
    else:
        threeandeight = blanks

    # threeandnine
    liststring = fightstrings[33].rsplit(sep=',')
    threeandnine = []
    if fightstrings[33] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            threeandnine.append(fixed)
            i += 1
    else:
        threeandnine = blanks

    # threeandten
    liststring = fightstrings[34].rsplit(sep=',')
    threeandten = []
    if fightstrings[34] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            threeandten.append(fixed)
            i += 1
    else:
        threeandten = blanks

    # threeandeleven
    liststring = fightstrings[35].rsplit(sep=',')
    threeandeleven = []
    if fightstrings[35] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            threeandeleven.append(fixed)
            i += 1
    else:
        threeandeleven = blanks

    # threeandtwelve
    liststring = fightstrings[36].rsplit(sep=',')
    threeandtwelve = []
    if fightstrings[36] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            threeandtwelve.append(fixed)
            i += 1
    else:
        threeandtwelve = blanks

    # threeandthirteen
    liststring = fightstrings[37].rsplit(sep=',')
    threeandthirteen = []
    if fightstrings[37] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            threeandthirteen.append(fixed)
            i += 1
    else:
        threeandthirteen = blanks

    # threeandfourteen
    liststring = fightstrings[38].rsplit(sep=',')
    threeandfourteen = []
    if fightstrings[38] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            threeandfourteen.append(fixed)
            i += 1
    else:
        threeandfourteen = blanks

    # threeandfifteen
    liststring = fightstrings[39].rsplit(sep=',')
    threeandfifteen = []
    if fightstrings[39] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            threeandfifteen.append(fixed)
            i += 1
    else:
        threeandfifteen = blanks

    # fourandfive
    liststring = fightstrings[40].rsplit(sep=',')
    fourandfive = []
    if fightstrings[40] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fourandfive.append(fixed)
            i += 1
    else:
        fourandfive = blanks

    # fourandsix
    liststring = fightstrings[41].rsplit(sep=',')
    fourandsix = []
    if fightstrings[41] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fourandsix.append(fixed)
            i += 1
    else:
        fourandsix = blanks

    # fourandseven
    liststring = fightstrings[42].rsplit(sep=',')
    fourandseven = []
    if fightstrings[42] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fourandseven.append(fixed)
            i += 1
    else:
        fourandseven = blanks

    # fourandeight
    liststring = fightstrings[43].rsplit(sep=',')
    fourandeight = []
    if fightstrings[43] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fourandeight.append(fixed)
            i += 1
    else:
        fourandeight = blanks

    # fourandnine
    liststring = fightstrings[44].rsplit(sep=',')
    fourandnine = []
    if fightstrings[44] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fourandnine.append(fixed)
            i += 1
    else:
        fourandnine = blanks

    # fourandten
    liststring = fightstrings[45].rsplit(sep=',')
    fourandten = []
    if fightstrings[45] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fourandten.append(fixed)
            i += 1
    else:
        fourandten = blanks

    # fourandeleven
    liststring = fightstrings[46].rsplit(sep=',')
    fourandeleven = []
    if fightstrings[46] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fourandeleven.append(fixed)
            i += 1
    else:
        fourandeleven = blanks

    # fourandtwelve
    liststring = fightstrings[47].rsplit(sep=',')
    fourandtwelve = []
    if fightstrings[47] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fourandtwelve.append(fixed)
            i += 1
    else:
        fourandtwelve = blanks

    # fourandthirteen
    liststring = fightstrings[48].rsplit(sep=',')
    fourandthirteen = []
    if fightstrings[48] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fourandthirteen.append(fixed)
            i += 1
    else:
        fourandthirteen = blanks

    # fourandfourteen
    liststring = fightstrings[49].rsplit(sep=',')
    fourandfourteen = []
    if fightstrings[49] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fourandfourteen.append(fixed)
            i += 1
    else:
        fourandfourteen = blanks

    # fourandfifteen
    liststring = fightstrings[50].rsplit(sep=',')
    fourandfifteen = []
    if fightstrings[50] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fourandfifteen.append(fixed)
            i += 1
    else:
        fourandfifteen = blanks

    # fiveandsix
    liststring = fightstrings[51].rsplit(sep=',')
    fiveandsix = []
    if fightstrings[51] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fiveandsix.append(fixed)
            i += 1
    else:
        fiveandsix = blanks

    # fiveandseven
    liststring = fightstrings[52].rsplit(sep=',')
    fiveandseven = []
    if fightstrings[52] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fiveandseven.append(fixed)
            i += 1
    else:
        fiveandseven = blanks

    # fiveandeight
    liststring = fightstrings[53].rsplit(sep=',')
    fiveandeight = []
    if fightstrings[53] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fiveandeight.append(fixed)
            i += 1
    else:
        fiveandeight = blanks

    # fiveandnine
    liststring = fightstrings[54].rsplit(sep=',')
    fiveandnine = []
    if fightstrings[54] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fiveandnine.append(fixed)
            i += 1
    else:
        fiveandnine = blanks

    # fiveandten
    liststring = fightstrings[55].rsplit(sep=',')
    fiveandten = []
    if fightstrings[55] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fiveandten.append(fixed)
            i += 1
    else:
        fiveandten = blanks

    # fiveandeleven
    liststring = fightstrings[56].rsplit(sep=',')
    fiveandeleven = []
    if fightstrings[56] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fiveandeleven.append(fixed)
            i += 1
    else:
        fiveandeleven = blanks

    # fiveandtwelve
    liststring = fightstrings[57].rsplit(sep=',')
    fiveandtwelve = []
    if fightstrings[57] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fiveandtwelve.append(fixed)
            i += 1
    else:
        fiveandtwelve = blanks

    # fiveandthirteen
    liststring = fightstrings[58].rsplit(sep=',')
    fiveandthirteen = []
    if fightstrings[58] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fiveandthirteen.append(fixed)
            i += 1
    else:
        fiveandthirteen = blanks

    # fiveandfourteen
    liststring = fightstrings[59].rsplit(sep=',')
    fiveandfourteen = []
    if fightstrings[59] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fiveandfourteen.append(fixed)
            i += 1
    else:
        fiveandfourteen = blanks

    # fiveandfifteen
    liststring = fightstrings[60].rsplit(sep=',')
    fiveandfifteen = []
    if fightstrings[60] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fiveandfifteen.append(fixed)
            i += 1
    else:
        fiveandfifteen = blanks

    # sixandseven
    liststring = fightstrings[61].rsplit(sep=',')
    sixandseven = []
    if fightstrings[61] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            sixandseven.append(fixed)
            i += 1
    else:
        sixandseven = blanks

    # sixandeight
    liststring = fightstrings[62].rsplit(sep=',')
    sixandeight = []
    if fightstrings[62] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            sixandeight.append(fixed)
            i += 1
    else:
        sixandeight = blanks

    # sixandnine
    liststring = fightstrings[63].rsplit(sep=',')
    sixandnine = []
    if fightstrings[63] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            sixandnine.append(fixed)
            i += 1
    else:
        sixandnine = blanks

    # sixandten
    liststring = fightstrings[64].rsplit(sep=',')
    sixandten = []
    if fightstrings[64] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            sixandten.append(fixed)
            i += 1
    else:
        sixandten = blanks

    # sixandeleven
    liststring = fightstrings[65].rsplit(sep=',')
    sixandeleven = []
    if fightstrings[65] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            sixandeleven.append(fixed)
            i += 1
    else:
        sixandeleven = blanks

    # sixandtwelve
    liststring = fightstrings[66].rsplit(sep=',')
    sixandtwelve = []
    if fightstrings[66] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            sixandtwelve.append(fixed)
            i += 1
    else:
        sixandtwelve = blanks

    # sixandthirteen
    liststring = fightstrings[67].rsplit(sep=',')
    sixandthirteen = []
    if fightstrings[67] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            sixandthirteen.append(fixed)
            i += 1
    else:
        sixandthirteen = blanks

    # sixandfourteen
    liststring = fightstrings[68].rsplit(sep=',')
    sixandfourteen = []
    if fightstrings[68] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            sixandfourteen.append(fixed)
            i += 1
    else:
        sixandfourteen = blanks

    # sixandfifteen
    liststring = fightstrings[69].rsplit(sep=',')
    sixandfifteen = []
    if fightstrings[69] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            sixandfifteen.append(fixed)
            i += 1
    else:
        sixandfifteen = blanks

    # sevenandeight
    liststring = fightstrings[70].rsplit(sep=',')
    sevenandeight = []
    if fightstrings[70] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            sevenandeight.append(fixed)
            i += 1
    else:
        sevenandeight = blanks

    # sevenandnine
    liststring = fightstrings[71].rsplit(sep=',')
    sevenandnine = []
    if fightstrings[71] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            sevenandnine.append(fixed)
            i += 1
    else:
        sevenandnine = blanks

    # sevenandten
    liststring = fightstrings[72].rsplit(sep=',')
    sevenandten = []
    if fightstrings[72] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            sevenandten.append(fixed)
            i += 1
    else:
        sevenandten = blanks

    # sevenandeleven
    liststring = fightstrings[73].rsplit(sep=',')
    sevenandeleven = []
    if fightstrings[73] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            sevenandeleven.append(fixed)
            i += 1
    else:
        sevenandeleven = blanks

    # sevenandtwelve
    liststring = fightstrings[74].rsplit(sep=',')
    sevenandtwelve = []
    if fightstrings[74] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            sevenandtwelve.append(fixed)
            i += 1
    else:
        sevenandtwelve = blanks

    # sevenandthirteen
    liststring = fightstrings[75].rsplit(sep=',')
    sevenandthirteen = []
    if fightstrings[75] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            sevenandthirteen.append(fixed)
            i += 1
    else:
        sevenandthirteen = blanks

    # sevenandfourteen
    liststring = fightstrings[76].rsplit(sep=',')
    sevenandfourteen = []
    if fightstrings[76] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            sevenandfourteen.append(fixed)
            i += 1
    else:
        sevenandfourteen = blanks

    # sevenandfifteen
    liststring = fightstrings[77].rsplit(sep=',')
    sevenandfifteen = []
    if fightstrings[77] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            sevenandfifteen.append(fixed)
            i += 1
    else:
        sevenandfifteen = blanks

    # eightandnine
    liststring = fightstrings[78].rsplit(sep=',')
    eightandnine = []
    if fightstrings[78] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            eightandnine.append(fixed)
            i += 1
    else:
        eightandnine = blanks

    # eightandten
    liststring = fightstrings[79].rsplit(sep=',')
    eightandten = []
    if fightstrings[79] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            eightandten.append(fixed)
            i += 1
    else:
        eightandten = blanks

    # eightandeleven
    liststring = fightstrings[80].rsplit(sep=',')
    eightandeleven = []
    if fightstrings[80] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            eightandeleven.append(fixed)
            i += 1
    else:
        eightandeleven = blanks

    # eightandtwelve
    liststring = fightstrings[81].rsplit(sep=',')
    eightandtwelve = []
    if fightstrings[81] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            eightandtwelve.append(fixed)
            i += 1
    else:
        eightandtwelve = blanks

    # eightandthirteen
    liststring = fightstrings[82].rsplit(sep=',')
    eightandthirteen = []
    if fightstrings[82] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            eightandthirteen.append(fixed)
            i += 1
    else:
        eightandthirteen = blanks

    # eightandfourteen
    liststring = fightstrings[83].rsplit(sep=',')
    eightandfourteen = []
    if fightstrings[83] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            eightandfourteen.append(fixed)
            i += 1
    else:
        eightandfourteen = blanks

    # eightandfifteen
    liststring = fightstrings[84].rsplit(sep=',')
    eightandfifteen = []
    if fightstrings[84] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            eightandfifteen.append(fixed)
            i += 1
    else:
        eightandfifteen = blanks

    # nineandten
    liststring = fightstrings[85].rsplit(sep=',')
    nineandten = []
    if fightstrings[85] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            nineandten.append(fixed)
            i += 1
    else:
        nineandten = blanks

    # nineandeleven
    liststring = fightstrings[86].rsplit(sep=',')
    nineandeleven = []
    if fightstrings[86] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            nineandeleven.append(fixed)
            i += 1
    else:
        nineandeleven = blanks

    # nineandtwelve
    liststring = fightstrings[87].rsplit(sep=',')
    nineandtwelve = []
    if fightstrings[87] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            nineandtwelve.append(fixed)
            i += 1
    else:
        nineandtwelve = blanks

    # nineandthirteen
    liststring = fightstrings[88].rsplit(sep=',')
    nineandthirteen = []
    if fightstrings[88] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            nineandthirteen.append(fixed)
            i += 1
    else:
        nineandthirteen = blanks

    # nineandfourteen
    liststring = fightstrings[89].rsplit(sep=',')
    nineandfourteen = []
    if fightstrings[89] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            nineandfourteen.append(fixed)
            i += 1
    else:
        nineandfourteen = blanks

    # nineandfifteen
    liststring = fightstrings[90].rsplit(sep=',')
    nineandfifteen = []
    if fightstrings[90] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            nineandfifteen.append(fixed)
            i += 1
    else:
        nineandfifteen = blanks

    # tenandeleven
    liststring = fightstrings[91].rsplit(sep=',')
    tenandeleven = []
    if fightstrings[91] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            tenandeleven.append(fixed)
            i += 1
    else:
        tenandeleven = blanks

    # tenandtwelve
    liststring = fightstrings[92].rsplit(sep=',')
    tenandtwelve = []
    if fightstrings[92] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            tenandtwelve.append(fixed)
            i += 1
    else:
        tenandtwelve = blanks

    # tenandthirteen
    liststring = fightstrings[93].rsplit(sep=',')
    tenandthirteen = []
    if fightstrings[93] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            tenandthirteen.append(fixed)
            i += 1
    else:
        tenandthirteen = blanks

    # tenandfourteen
    liststring = fightstrings[94].rsplit(sep=',')
    tenandfourteen = []
    if fightstrings[94] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            tenandfourteen.append(fixed)
            i += 1
    else:
        tenandfourteen = blanks

    # tenandfifteen
    liststring = fightstrings[95].rsplit(sep=',')
    tenandfifteen = []
    if fightstrings[95] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            tenandfifteen.append(fixed)
            i += 1
    else:
        tenandfifteen = blanks

    # elevenandtwelve
    liststring = fightstrings[96].rsplit(sep=',')
    elevenandtwelve = []
    if fightstrings[96] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            elevenandtwelve.append(fixed)
            i += 1
    else:
        elevenandtwelve = blanks

    # elevenandthirteen
    liststring = fightstrings[97].rsplit(sep=',')
    elevenandthirteen = []
    if fightstrings[97] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            elevenandthirteen.append(fixed)
            i += 1
    else:
        elevenandthirteen = blanks

    # elevenandfourteen
    liststring = fightstrings[98].rsplit(sep=',')
    elevenandfourteen = []
    if fightstrings[98] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            elevenandfourteen.append(fixed)
            i += 1
    else:
        elevenandfourteen = blanks

    # elevenandfifteen
    liststring = fightstrings[99].rsplit(sep=',')
    elevenandfifteen = []
    if fightstrings[99] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            elevenandfifteen.append(fixed)
            i += 1
    else:
        elevenandfifteen = blanks

    # twelveandthirteen
    liststring = fightstrings[100].rsplit(sep=',')
    twelveandthirteen = []
    if fightstrings[100] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            twelveandthirteen.append(fixed)
            i += 1
    else:
        twelveandthirteen = blanks

    # twelveandfourteen
    liststring = fightstrings[101].rsplit(sep=',')
    twelveandfourteen = []
    if fightstrings[101] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            twelveandfourteen.append(fixed)
            i += 1
    else:
        twelveandfourteen = blanks

    # twelveandfifteen
    liststring = fightstrings[102].rsplit(sep=',')
    twelveandfifteen = []
    if fightstrings[102] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            twelveandfifteen.append(fixed)
            i += 1
    else:
        twelveandfifteen = blanks

    # thirteenandfourteen
    liststring = fightstrings[103].rsplit(sep=',')
    thirteenandfourteen = []
    if fightstrings[103] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            thirteenandfourteen.append(fixed)
            i += 1
    else:
        thirteenandfourteen = blanks

    # thirteenandfifteen
    liststring = fightstrings[104].rsplit(sep=',')
    thirteenandfifteen = []
    if fightstrings[104] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            thirteenandfifteen.append(fixed)
            i += 1
    else:
        thirteenandfifteen = blanks

    # fourteenandfifteen
    liststring = fightstrings[105].rsplit(sep=',')
    fourteenandfifteen = []
    if fightstrings[105] != '[]':
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            fourteenandfifteen.append(fixed)
            i += 1
    else:
        fourteenandfifteen = blanks

    return(community1defend, community2defend, community3defend, community4defend, community5defend, community6defend,
           community7defend, community8defend, community9defend, community10defend, community11defend, community12defend,
           community13defend, community14defend, community15defend, oneandtwo, oneandthree,  oneandfour, oneandfive,
           oneandsix, oneandseven, oneandeight, oneandnine, oneandten, oneandeleven, oneandtwelve, oneandthirteen,
           oneandfourteen, oneandfifteen, twoandthree, twoandfour, twoandfive, twoandsix, twoandseven, twoandeight,
           twoandnine, twoandten, twoandeleven, twoandtwelve, twoandthirteen, twoandfourteen, twoandfifteen, threeandfour,
           threeandfive, threeandsix, threeandseven, threeandeight, threeandnine, threeandten, threeandeleven, threeandtwelve,
           threeandthirteen, threeandfourteen, threeandfifteen, fourandfive, fourandsix, fourandseven, fourandeight,
           fourandnine, fourandten, fourandeleven, fourandtwelve, fourandthirteen, fourandfourteen, fourandfifteen,
           fiveandsix, fiveandseven, fiveandeight, fiveandnine, fiveandten, fiveandeleven, fiveandtwelve, fiveandthirteen,
           fiveandfourteen, fiveandfifteen, sixandseven, sixandeight, sixandnine, sixandten, sixandeleven, sixandtwelve,
           sixandthirteen, sixandfourteen, sixandfifteen, sevenandeight, sevenandnine, sevenandten, sevenandeleven,
           sevenandtwelve, sevenandthirteen, sevenandfourteen, sevenandfifteen, eightandnine, eightandten, eightandeleven,
           eightandtwelve, eightandthirteen, eightandfourteen, eightandfifteen, nineandten, nineandeleven, nineandtwelve,
           nineandthirteen, nineandfourteen, nineandfifteen, tenandeleven, tenandtwelve, tenandthirteen, tenandfourteen,
           tenandfifteen, elevenandtwelve, elevenandthirteen, elevenandfourteen, elevenandfifteen, twelveandthirteen,
           twelveandfourteen, twelveandfifteen, thirteenandfourteen, thirteenandfifteen, fourteenandfifteen)
