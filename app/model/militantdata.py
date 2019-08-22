import re


def militantdata(militantstrings, blanks):

    strength1 = []
    notorietyratio1 = []
    totalextort1 = []
    countextort1 = []
    countbenefit1 = []
    countpunish1 = []
    countsupport1 = []
    totalsupport1 = []
    countdefend1 = []
    strength2 = []
    notorietyratio2 = []
    totalextort2 = []
    countextort2 = []
    countbenefit2 = []
    countpunish2 = []
    countsupport2 = []
    totalsupport2 = []
    countdefend2 = []
    strength3 = []
    notorietyratio3 = []
    totalextort3 = []
    countextort3 = []
    countbenefit3 = []
    countpunish3 = []
    countsupport3 = []
    totalsupport3 = []
    countdefend3 = []
    strength4 = []
    notorietyratio4 = []
    totalextort4 = []
    countextort4 = []
    countbenefit4 = []
    countpunish4 = []
    countsupport4 = []
    totalsupport4 = []
    countdefend4 = []
    strength5 = []
    notorietyratio5 = []
    totalextort5 = []
    countextort5 = []
    countbenefit5 = []
    countpunish5 = []
    countsupport5 = []
    totalsupport5 = []
    countdefend5 = []
    strength6 = []
    notorietyratio6 = []
    totalextort6 = []
    countextort6 = []
    countbenefit6 = []
    countpunish6 = []
    countsupport6 = []
    totalsupport6 = []
    countdefend6 = []
    strength7 = []
    notorietyratio7 = []
    totalextort7 = []
    countextort7 = []
    countbenefit7 = []
    countpunish7 = []
    countsupport7 = []
    totalsupport7 = []
    countdefend7 = []
    strength8 = []
    notorietyratio8 = []
    totalextort8 = []
    countextort8 = []
    countbenefit8 = []
    countpunish8 = []
    countsupport8 = []
    totalsupport8 = []
    countdefend8 = []
    strength9 = []
    notorietyratio9 = []
    totalextort9 = []
    countextort9 = []
    countbenefit9 = []
    countpunish9 = []
    countsupport9 = []
    totalsupport9 = []
    countdefend9 = []
    strength10 = []
    notorietyratio10 = []
    totalextort10 = []
    countextort10 = []
    countbenefit10 = []
    countpunish10 = []
    countsupport10 = []
    totalsupport10 = []
    countdefend10 = []
    strength11 = []
    notorietyratio11 = []
    totalextort11 = []
    countextort11 = []
    countbenefit11 = []
    countpunish11 = []
    countsupport11 = []
    totalsupport11 = []
    countdefend11 = []
    strength12 = []
    notorietyratio12 = []
    totalextort12 = []
    countextort12 = []
    countbenefit12 = []
    countpunish12 = []
    countsupport12 = []
    totalsupport12 = []
    countdefend12 = []
    strength13 = []
    notorietyratio13 = []
    totalextort13 = []
    countextort13 = []
    countbenefit13 = []
    countpunish13 = []
    countsupport13 = []
    totalsupport13 = []
    countdefend13 = []
    strength14 = []
    notorietyratio14 = []
    totalextort14 = []
    countextort14 = []
    countbenefit14 = []
    countpunish14 = []
    countsupport14 = []
    totalsupport14 = []
    countdefend14 = []
    strength15 = []
    notorietyratio15 = []
    totalextort15 = []
    countextort15 = []
    countbenefit15 = []
    countpunish15 = []
    countsupport15 = []
    totalsupport15 = []
    countdefend15 = []

    # strength m1
    liststring = militantstrings[1].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        strength1.append(fixed)
        i += 1

    # notorietyratio m1
    liststring = militantstrings[2].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        notorietyratio1.append(fixed)
        i += 1

    # totalextort m1
    liststring = militantstrings[3].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        totalextort1.append(fixed)
        i += 1

    # countextort m1
    liststring = militantstrings[4].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        countextort1.append(fixed)
        i += 1

    # countbenefit m1
    liststring = militantstrings[5].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        countbenefit1.append(fixed)
        i += 1

    # countpunish m1
    liststring = militantstrings[6].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        countpunish1.append(fixed)
        i += 1

    # countsupport m1
    liststring = militantstrings[7].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        countsupport1.append(fixed)
        i += 1

    # totalsupport m1
    liststring = militantstrings[8].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        totalsupport1.append(fixed)
        i += 1

    # countdefend m1
    liststring = militantstrings[9].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        countdefend1.append(fixed)
        i += 1

    # strength m2
    liststring = militantstrings[11].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        strength2.append(fixed)
        i += 1

    # notorietyratio m2
    liststring = militantstrings[12].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        notorietyratio2.append(fixed)
        i += 1

    # totalextort m2
    liststring = militantstrings[13].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        totalextort2.append(fixed)
        i += 1

    # countextort m2
    liststring = militantstrings[14].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        countextort2.append(fixed)
        i += 1

    # countbenefit m2
    liststring = militantstrings[15].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        countbenefit2.append(fixed)
        i += 1

    # countpunish m2
    liststring = militantstrings[16].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        countpunish2.append(fixed)
        i += 1

    # countsupport m2
    liststring = militantstrings[17].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        countsupport2.append(fixed)
        i += 1

    # totalsupport m2
    liststring = militantstrings[18].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        totalsupport2.append(fixed)
        i += 1

    # countdefend m2
    liststring = militantstrings[19].rsplit(sep=',')
    i = 0
    while i < len(liststring):
        fixed = float(re.sub('[\[\]]', '', liststring[i]))
        countdefend2.append(fixed)
        i += 1

    if len(militantstrings) > 21:
        # strength m3
        liststring = militantstrings[21].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            strength3.append(fixed)
            i += 1

        # notorietyratio m3
        liststring = militantstrings[22].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            notorietyratio3.append(fixed)
            i += 1

        # totalextort m3
        liststring = militantstrings[23].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalextort3.append(fixed)
            i += 1

        # countextort m3
        liststring = militantstrings[24].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countextort3.append(fixed)
            i += 1

        # countbenefit m3
        liststring = militantstrings[25].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countbenefit3.append(fixed)
            i += 1

        # countpunish m3
        liststring = militantstrings[26].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countpunish3.append(fixed)
            i += 1

        # countsupport m3
        liststring = militantstrings[27].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countsupport3.append(fixed)
            i += 1

        # totalsupport m3
        liststring = militantstrings[28].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalsupport3.append(fixed)
            i += 1

        # countdefend m3
        liststring = militantstrings[29].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countdefend3.append(fixed)
            i += 1
    else:
        strength3 = blanks
        notorietyratio3 = blanks
        totalextort3 = blanks
        countextort3 = blanks
        countbenefit3 = blanks
        countpunish3 = blanks
        countsupport3 = blanks
        totalsupport3 = blanks
        countdefend3 = blanks

    if len(militantstrings) > 31:
        # strength m4
        liststring = militantstrings[31].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            strength4.append(fixed)
            i += 1

        # notorietyratio m4
        liststring = militantstrings[32].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            notorietyratio4.append(fixed)
            i += 1

        # totalextort m4
        liststring = militantstrings[33].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalextort4.append(fixed)
            i += 1

        # countextort m4
        liststring = militantstrings[34].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countextort4.append(fixed)
            i += 1

        # countbenefit m4
        liststring = militantstrings[35].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countbenefit4.append(fixed)
            i += 1

        # countpunish m4
        liststring = militantstrings[36].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countpunish4.append(fixed)
            i += 1

        # countsupport m4
        liststring = militantstrings[37].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countsupport4.append(fixed)
            i += 1

        # totalsupport m4
        liststring = militantstrings[38].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalsupport4.append(fixed)
            i += 1

        # countdefend m4
        liststring = militantstrings[39].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countdefend4.append(fixed)
            i += 1
    else:
        strength4 = blanks
        notorietyratio4 = blanks
        totalextort4 = blanks
        countextort4 = blanks
        countbenefit4 = blanks
        countpunish4 = blanks
        countsupport4 = blanks
        totalsupport4 = blanks
        countdefend4 = blanks

    if len(militantstrings) > 41:
        # strength m5
        liststring = militantstrings[41].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            strength5.append(fixed)
            i += 1

        # notorietyratio m5
        liststring = militantstrings[42].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            notorietyratio5.append(fixed)
            i += 1

        # totalextort m5
        liststring = militantstrings[43].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalextort5.append(fixed)
            i += 1

        # countextort m5
        liststring = militantstrings[44].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countextort5.append(fixed)
            i += 1

        # countbenefit m5
        liststring = militantstrings[45].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countbenefit5.append(fixed)
            i += 1

        # countpunish m5
        liststring = militantstrings[46].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countpunish5.append(fixed)
            i += 1

        # countsupport m5
        liststring = militantstrings[47].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countsupport5.append(fixed)
            i += 1

        # totalsupport m5
        liststring = militantstrings[48].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalsupport5.append(fixed)
            i += 1

        # countdefend m5
        liststring = militantstrings[49].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countdefend5.append(fixed)
            i += 1
    else:
        strength5 = blanks
        notorietyratio5 = blanks
        totalextort5 = blanks
        countextort5 = blanks
        countbenefit5 = blanks
        countpunish5 = blanks
        countsupport5 = blanks
        totalsupport5 = blanks
        countdefend5 = blanks

    if len(militantstrings) > 51:
        # strength m6
        liststring = militantstrings[51].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            strength6.append(fixed)
            i += 1

        # notorietyratio m6
        liststring = militantstrings[52].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            notorietyratio6.append(fixed)
            i += 1

        # totalextort m6
        liststring = militantstrings[53].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalextort6.append(fixed)
            i += 1

        # countextort m6
        liststring = militantstrings[54].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countextort6.append(fixed)
            i += 1

        # countbenefit m6
        liststring = militantstrings[55].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countbenefit6.append(fixed)
            i += 1

        # countpunish m6
        liststring = militantstrings[56].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countpunish6.append(fixed)
            i += 1

        # countsupport m6
        liststring = militantstrings[57].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countsupport6.append(fixed)
            i += 1

        # totalsupport m6
        liststring = militantstrings[58].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalsupport6.append(fixed)
            i += 1

        # countdefend m6
        liststring = militantstrings[59].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countdefend6.append(fixed)
            i += 1
    else:
        strength6 = blanks
        notorietyratio6 = blanks
        totalextort6 = blanks
        countextort6 = blanks
        countbenefit6 = blanks
        countpunish6 = blanks
        countsupport6 = blanks
        totalsupport6 = blanks
        countdefend6 = blanks

    if len(militantstrings) > 61:
        # strength m7
        liststring = militantstrings[61].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            strength7.append(fixed)
            i += 1

        # notorietyratio m7
        liststring = militantstrings[62].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            notorietyratio7.append(fixed)
            i += 1

        # totalextort m7
        liststring = militantstrings[63].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalextort7.append(fixed)
            i += 1

        # countextort m7
        liststring = militantstrings[64].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countextort7.append(fixed)
            i += 1

        # countbenefit m7
        liststring = militantstrings[65].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countbenefit7.append(fixed)
            i += 1

        # countpunish m7
        liststring = militantstrings[66].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countpunish7.append(fixed)
            i += 1

        # countsupport m7
        liststring = militantstrings[67].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countsupport7.append(fixed)
            i += 1

        # totalsupport m7
        liststring = militantstrings[68].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalsupport7.append(fixed)
            i += 1

        # countdefend m7
        liststring = militantstrings[69].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countdefend7.append(fixed)
            i += 1
    else:
        strength7 = blanks
        notorietyratio7 = blanks
        totalextort7 = blanks
        countextort7 = blanks
        countbenefit7 = blanks
        countpunish7 = blanks
        countsupport7 = blanks
        totalsupport7 = blanks
        countdefend7 = blanks

    if len(militantstrings) > 71:
        # strength m8
        liststring = militantstrings[71].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            strength8.append(fixed)
            i += 1

        # notorietyratio m8
        liststring = militantstrings[72].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            notorietyratio8.append(fixed)
            i += 1

        # totalextort m8
        liststring = militantstrings[73].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalextort8.append(fixed)
            i += 1

        # countextort m8
        liststring = militantstrings[74].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countextort8.append(fixed)
            i += 1

        # countbenefit m8
        liststring = militantstrings[75].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countbenefit8.append(fixed)
            i += 1

        # countpunish m8
        liststring = militantstrings[76].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countpunish8.append(fixed)
            i += 1

        # countsupport m8
        liststring = militantstrings[77].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countsupport8.append(fixed)
            i += 1

        # totalsupport m8
        liststring = militantstrings[78].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalsupport8.append(fixed)
            i += 1

        # countdefend m8
        liststring = militantstrings[79].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countdefend8.append(fixed)
            i += 1
    else:
        strength8 = blanks
        notorietyratio8 = blanks
        totalextort8 = blanks
        countextort8 = blanks
        countbenefit8 = blanks
        countpunish8 = blanks
        countsupport8 = blanks
        totalsupport8 = blanks
        countdefend8 = blanks

    if len(militantstrings) > 81:
        # strength m9
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            strength9.append(fixed)
            i += 1

        # notorietyratio m9
        liststring = militantstrings[82].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            notorietyratio9.append(fixed)
            i += 1

        # totalextort m9
        liststring = militantstrings[83].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalextort9.append(fixed)
            i += 1

        # countextort m9
        liststring = militantstrings[84].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countextort9.append(fixed)
            i += 1

        # countbenefit m9
        liststring = militantstrings[85].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countbenefit9.append(fixed)
            i += 1

        # countpunish m9
        liststring = militantstrings[86].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countpunish9.append(fixed)
            i += 1

        # countsupport m9
        liststring = militantstrings[87].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countsupport9.append(fixed)
            i += 1

        # totalsupport m9
        liststring = militantstrings[88].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalsupport9.append(fixed)
            i += 1

        # countdefend m9
        liststring = militantstrings[89].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countdefend9.append(fixed)
            i += 1
    else:
        strength9 = blanks
        notorietyratio9 = blanks
        totalextort9 = blanks
        countextort9 = blanks
        countbenefit9 = blanks
        countpunish9 = blanks
        countsupport9 = blanks
        totalsupport9 = blanks
        countdefend9 = blanks

    if len(militantstrings) > 91:
        # strength m10
        liststring = militantstrings[91].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            strength10.append(fixed)
            i += 1

        # notorietyratio m10
        liststring = militantstrings[92].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            notorietyratio10.append(fixed)
            i += 1

        # totalextort m10
        liststring = militantstrings[93].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalextort10.append(fixed)
            i += 1

        # countextort m10
        liststring = militantstrings[94].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countextort10.append(fixed)
            i += 1

        # countbenefit m10
        liststring = militantstrings[95].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countbenefit10.append(fixed)
            i += 1

        # countpunish m10
        liststring = militantstrings[96].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countpunish10.append(fixed)
            i += 1

        # countsupport m10
        liststring = militantstrings[97].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countsupport10.append(fixed)
            i += 1

        # totalsupport m10
        liststring = militantstrings[98].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalsupport10.append(fixed)
            i += 1

        # countdefend m10
        liststring = militantstrings[99].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countdefend10.append(fixed)
            i += 1
    else:
        strength10 = blanks
        notorietyratio10 = blanks
        totalextort10 = blanks
        countextort10 = blanks
        countbenefit10 = blanks
        countpunish10 = blanks
        countsupport10 = blanks
        totalsupport10 = blanks
        countdefend10 = blanks

    if len(militantstrings) > 101:
        # strength m11
        liststring = militantstrings[101].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            strength11.append(fixed)
            i += 1

        # notorietyratio m11
        liststring = militantstrings[102].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            notorietyratio11.append(fixed)
            i += 1

        # totalextort m11
        liststring = militantstrings[103].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalextort11.append(fixed)
            i += 1

        # countextort m11
        liststring = militantstrings[104].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countextort11.append(fixed)
            i += 1

        # countbenefit m11
        liststring = militantstrings[105].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countbenefit11.append(fixed)
            i += 1

        # countpunish m11
        liststring = militantstrings[106].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countpunish11.append(fixed)
            i += 1

        # countsupport m11
        liststring = militantstrings[107].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countsupport11.append(fixed)
            i += 1

        # totalsupport m11
        liststring = militantstrings[108].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalsupport11.append(fixed)
            i += 1

        # countdefend m11
        liststring = militantstrings[109].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countdefend11.append(fixed)
            i += 1
    else:
        strength11 = blanks
        notorietyratio11 = blanks
        totalextort11 = blanks
        countextort11 = blanks
        countbenefit11 = blanks
        countpunish11 = blanks
        countsupport11 = blanks
        totalsupport11 = blanks
        countdefend11 = blanks

    if len(militantstrings) > 111:
        # strength m12
        liststring = militantstrings[111].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            strength12.append(fixed)
            i += 1

        # notorietyratio m12
        liststring = militantstrings[112].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            notorietyratio12.append(fixed)
            i += 1

        # totalextort m12
        liststring = militantstrings[113].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalextort12.append(fixed)
            i += 1

        # countextort m12
        liststring = militantstrings[114].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countextort12.append(fixed)
            i += 1

        # countbenefit m12
        liststring = militantstrings[115].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countbenefit12.append(fixed)
            i += 1

        # countpunish m12
        liststring = militantstrings[116].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countpunish12.append(fixed)
            i += 1

        # countsupport m12
        liststring = militantstrings[117].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countsupport12.append(fixed)
            i += 1

        # totalsupport m12
        liststring = militantstrings[118].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalsupport12.append(fixed)
            i += 1

        # countdefend m12
        liststring = militantstrings[119].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countdefend12.append(fixed)
            i += 1
    else:
        strength12 = blanks
        notorietyratio12 = blanks
        totalextort12 = blanks
        countextort12 = blanks
        countbenefit12 = blanks
        countpunish12 = blanks
        countsupport12 = blanks
        totalsupport12 = blanks
        countdefend12 = blanks

    if len(militantstrings) > 121:
        # strength m13
        liststring = militantstrings[121].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            strength13.append(fixed)
            i += 1

        # notorietyratio m13
        liststring = militantstrings[122].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            notorietyratio13.append(fixed)
            i += 1

        # totalextort m13
        liststring = militantstrings[123].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalextort13.append(fixed)
            i += 1

        # countextort m13
        liststring = militantstrings[124].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countextort13.append(fixed)
            i += 1

        # countbenefit m13
        liststring = militantstrings[125].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countbenefit13.append(fixed)
            i += 1

        # countpunish m13
        liststring = militantstrings[126].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countpunish13.append(fixed)
            i += 1

        # countsupport m13
        liststring = militantstrings[127].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countsupport13.append(fixed)
            i += 1

        # totalsupport m13
        liststring = militantstrings[128].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalsupport13.append(fixed)
            i += 1

        # countdefend m13
        liststring = militantstrings[129].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countdefend13.append(fixed)
            i += 1
    else:
        strength13 = blanks
        notorietyratio13 = blanks
        totalextort13 = blanks
        countextort13 = blanks
        countbenefit13 = blanks
        countpunish13 = blanks
        countsupport13 = blanks
        totalsupport13 = blanks
        countdefend13 = blanks

    if len(militantstrings) > 131:
        # strength m14
        liststring = militantstrings[131].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            strength14.append(fixed)
            i += 1

        # notorietyratio m14
        liststring = militantstrings[132].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            notorietyratio14.append(fixed)
            i += 1

        # totalextort m14
        liststring = militantstrings[133].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalextort14.append(fixed)
            i += 1

        # countextort m14
        liststring = militantstrings[134].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countextort14.append(fixed)
            i += 1

        # countbenefit m14
        liststring = militantstrings[135].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countbenefit14.append(fixed)
            i += 1

        # countpunish m14
        liststring = militantstrings[136].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countpunish14.append(fixed)
            i += 1

        # countsupport m14
        liststring = militantstrings[137].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countsupport14.append(fixed)
            i += 1

        # totalsupport m14
        liststring = militantstrings[138].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalsupport14.append(fixed)
            i += 1

        # countdefend m14
        liststring = militantstrings[139].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countdefend14.append(fixed)
            i += 1
    else:
        strength14 = blanks
        notorietyratio14 = blanks
        totalextort14 = blanks
        countextort14 = blanks
        countbenefit14 = blanks
        countpunish14 = blanks
        countsupport14 = blanks
        totalsupport14 = blanks
        countdefend14 = blanks

    if len(militantstrings) > 141:
        # strength m15
        liststring = militantstrings[141].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            strength15.append(fixed)
            i += 1

        # notorietyratio m15
        liststring = militantstrings[142].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            notorietyratio15.append(fixed)
            i += 1

        # totalextort m15
        liststring = militantstrings[143].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalextort15.append(fixed)
            i += 1

        # countextort m15
        liststring = militantstrings[144].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countextort15.append(fixed)
            i += 1

        # countbenefit m15
        liststring = militantstrings[145].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countbenefit15.append(fixed)
            i += 1

        # countpunish m15
        liststring = militantstrings[146].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countpunish15.append(fixed)
            i += 1

        # countsupport m15
        liststring = militantstrings[147].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countsupport15.append(fixed)
            i += 1

        # totalsupport m15
        liststring = militantstrings[148].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            totalsupport15.append(fixed)
            i += 1

        # countdefend m15
        liststring = militantstrings[149].rsplit(sep=',')
        i = 0
        while i < len(liststring):
            fixed = float(re.sub('[\[\]]', '', liststring[i]))
            countdefend15.append(fixed)
            i += 1
    else:
        strength15 = blanks
        notorietyratio15 = blanks
        totalextort15 = blanks
        countextort15 = blanks
        countbenefit15 = blanks
        countpunish15 = blanks
        countsupport15 = blanks
        totalsupport15 = blanks
        countdefend15 = blanks

    return(strength1, notorietyratio1, totalextort1, countextort1, countbenefit1, countpunish1, countsupport1,
           totalsupport1, countdefend1, strength2, notorietyratio2, totalextort2, countextort2, countbenefit2,
           countpunish2, countsupport2, totalsupport2, countdefend2, strength3, notorietyratio3, totalextort3,
           countextort3, countbenefit3, countpunish3, countsupport3, totalsupport3, countdefend3, strength4,
           notorietyratio4, totalextort4, countextort4, countbenefit4, countpunish4, countsupport4, totalsupport4,
           countdefend4, strength5, notorietyratio5, totalextort5, countextort5, countbenefit5, countpunish5,
           countsupport5, totalsupport5, countdefend5, strength6, notorietyratio6, totalextort6, countextort6,
           countbenefit6, countpunish6, countsupport6, totalsupport6, countdefend6, strength7, notorietyratio7,
           totalextort7, countextort7, countbenefit7, countpunish7, countsupport7, totalsupport7, countdefend7,
           strength8, notorietyratio8, totalextort8, countextort8, countbenefit8, countpunish8, countsupport8,
           totalsupport8, countdefend8, strength9, notorietyratio9, totalextort9, countextort9, countbenefit9,
           countpunish9, countsupport9, totalsupport9, countdefend9, strength10, notorietyratio10, totalextort10,
           countextort10, countbenefit10, countpunish10, countsupport10, totalsupport10, countdefend10,
           strength11, notorietyratio11, totalextort11, countextort11, countbenefit11, countpunish11, countsupport11,
           totalsupport11, countdefend11, strength12, notorietyratio12, totalextort12, countextort12, countbenefit12,
           countpunish12, countsupport12, totalsupport12, countdefend12, strength13, notorietyratio13,
           totalextort13, countextort13, countbenefit13, countpunish13, countsupport13, totalsupport13,
           countdefend13, strength14, notorietyratio14, totalextort14, countextort14, countbenefit14,
           countpunish14, countsupport14, totalsupport14, countdefend14, strength15, notorietyratio15,
           totalextort15, countextort15, countbenefit15, countpunish15, countsupport15, totalsupport15,
           countdefend15)
