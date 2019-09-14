from pandas import DataFrame
from application.model.simulatoronce import avestrength1, avenotorietyratio1, avetotalextort1, avecountextort1, avecountbenefit1, avecountpunish1, avecountsupport1, avetotalsupport1, avecountdefend1, avestrength2 , avenotorietyratio2, avetotalextort2, avecountextort2, avecountbenefit2, avecountpunish2, avecountsupport2, avetotalsupport2, avecountdefend2, avestrength3 , avenotorietyratio3, avetotalextort3, avecountextort3, avecountbenefit3, avecountpunish3, avecountsupport3, avetotalsupport3, avecountdefend3, avestrength4 , avenotorietyratio4, avetotalextort4, avecountextort4, avecountbenefit4, avecountpunish4, avecountsupport4, avetotalsupport4, avecountdefend4, avestrength5 , avenotorietyratio5, avetotalextort5, avecountextort5, avecountbenefit5, avecountpunish5, avecountsupport5, avetotalsupport5, avecountdefend5, avestrength6 , avenotorietyratio6, avetotalextort6, avecountextort6, avecountbenefit6, avecountpunish6, avecountsupport6, avetotalsupport6, avecountdefend6, avestrength7 , avenotorietyratio7, avetotalextort7, avecountextort7, avecountbenefit7, avecountpunish7, avecountsupport7, avetotalsupport7, avecountdefend7, avestrength8 , avenotorietyratio8, avetotalextort8, avecountextort8, avecountbenefit8, avecountpunish8, avecountsupport8, avetotalsupport8, avecountdefend8, avestrength9 , avenotorietyratio9, avetotalextort9, avecountextort9, avecountbenefit9, avecountpunish9, avecountsupport9, avetotalsupport9, avecountdefend9, avestrength10, avenotorietyratio10, avetotalextort10, avecountextort10, avecountbenefit10, avecountpunish10, avecountsupport10, avetotalsupport10, avecountdefend10, avestrength11, avenotorietyratio11, avetotalextort11, avecountextort11, avecountbenefit11, avecountpunish11, avecountsupport11, avetotalsupport11, avecountdefend11, avestrength12, avenotorietyratio12, avetotalextort12, avecountextort12, avecountbenefit12, avecountpunish12, avecountsupport12, avetotalsupport12, avecountdefend12, avestrength13, avenotorietyratio13, avetotalextort13, avecountextort13, avecountbenefit13, avecountpunish13, avecountsupport13, avetotalsupport13, avecountdefend13, avestrength14, avenotorietyratio14, avetotalextort14, avecountextort14, avecountbenefit14, avecountpunish14, avecountsupport14, avetotalsupport14, avecountdefend14, avestrength15, avenotorietyratio15, avetotalextort15, avecountextort15, avecountbenefit15, avecountpunish15, avecountsupport15, avetotalsupport15, avecountdefend15, avecommunity1m1, avecommunity2m1, avecommunity3m1, avecommunity4m1, avecommunity5m1, avecommunity6m1, avecommunity7m1, avecommunity8m1, avecommunity9m1, avecommunity10m1, avecommunity11m1, avecommunity12m1, avecommunity13m1, avecommunity14m1, avecommunity15m1, avecommunity1m2, avecommunity2m2, avecommunity3m2, avecommunity4m2, avecommunity5m2, avecommunity6m2, avecommunity7m2, avecommunity8m2, avecommunity9m2, avecommunity10m2, avecommunity11m2, avecommunity12m2, avecommunity13m2, avecommunity14m2, avecommunity15m2, avecommunity1m3, avecommunity2m3, avecommunity3m3, avecommunity4m3, avecommunity5m3, avecommunity6m3, avecommunity7m3, avecommunity8m3, avecommunity9m3, avecommunity10m3, avecommunity11m3, avecommunity12m3, avecommunity13m3, avecommunity14m3, avecommunity15m3, avecommunity1m4, avecommunity2m4, avecommunity3m4, avecommunity4m4, avecommunity5m4, avecommunity6m4, avecommunity7m4, avecommunity8m4, avecommunity9m4, avecommunity10m4, avecommunity11m4, avecommunity12m4, avecommunity13m4, avecommunity14m4, avecommunity15m4, avecommunity1m5, avecommunity2m5, avecommunity3m5, avecommunity4m5, avecommunity5m5, avecommunity6m5, avecommunity7m5, avecommunity8m5, avecommunity9m5, avecommunity10m5, avecommunity11m5, avecommunity12m5, avecommunity13m5, avecommunity14m5, avecommunity15m5, avecommunity1m6, avecommunity2m6, avecommunity3m6, avecommunity4m6, avecommunity5m6, avecommunity6m6, avecommunity7m6, avecommunity8m6, avecommunity9m6, avecommunity10m6, avecommunity11m6, avecommunity12m6, avecommunity13m6, avecommunity14m6, avecommunity15m6, avecommunity1m7, avecommunity2m7, avecommunity3m7, avecommunity4m7, avecommunity5m7, avecommunity6m7, avecommunity7m7, avecommunity8m7, avecommunity9m7, avecommunity10m7, avecommunity11m7, avecommunity12m7, avecommunity13m7, avecommunity14m7, avecommunity15m7, avecommunity1m8, avecommunity2m8, avecommunity3m8, avecommunity4m8, avecommunity5m8, avecommunity6m8, avecommunity7m8, avecommunity8m8, avecommunity9m8, avecommunity10m8, avecommunity11m8, avecommunity12m8, avecommunity13m8, avecommunity14m8, avecommunity15m8, avecommunity1m9, avecommunity2m9, avecommunity3m9, avecommunity4m9, avecommunity5m9, avecommunity6m9, avecommunity7m9, avecommunity8m9, avecommunity9m9, avecommunity10m9, avecommunity11m9, avecommunity12m9, avecommunity13m9, avecommunity14m9, avecommunity15m9, avecommunity1m10, avecommunity2m10, avecommunity3m10, avecommunity4m10, avecommunity5m10, avecommunity6m10, avecommunity7m10, avecommunity8m10, avecommunity9m10, avecommunity10m10, avecommunity11m10, avecommunity12m10, avecommunity13m10, avecommunity14m10, avecommunity15m10, avecommunity1m11, avecommunity2m11, avecommunity3m11, avecommunity4m11, avecommunity5m11, avecommunity6m11, avecommunity7m11, avecommunity8m11, avecommunity9m11, avecommunity10m11, avecommunity11m11, avecommunity12m11, avecommunity13m11, avecommunity14m11, avecommunity15m11, avecommunity1m12, avecommunity2m12, avecommunity3m12, avecommunity4m12, avecommunity5m12, avecommunity6m12, avecommunity7m12, avecommunity8m12, avecommunity9m12, avecommunity10m12, avecommunity11m12, avecommunity12m12, avecommunity13m12, avecommunity14m12, avecommunity15m12, avecommunity1m13, avecommunity2m13, avecommunity3m13, avecommunity4m13, avecommunity5m13, avecommunity6m13, avecommunity7m13, avecommunity8m13, avecommunity9m13, avecommunity10m13, avecommunity11m13, avecommunity12m13, avecommunity13m13, avecommunity14m13, avecommunity15m13, avecommunity1m14, avecommunity2m14, avecommunity3m14, avecommunity4m14, avecommunity5m14, avecommunity6m14, avecommunity7m14, avecommunity8m14, avecommunity9m14, avecommunity10m14, avecommunity11m14, avecommunity12m14, avecommunity13m14, avecommunity14m14, avecommunity15m14, avecommunity1m15, avecommunity2m15, avecommunity3m15, avecommunity4m15, avecommunity5m15, avecommunity6m15, avecommunity7m15, avecommunity8m15, avecommunity9m15, avecommunity10m15, avecommunity11m15, avecommunity12m15, avecommunity13m15, avecommunity14m15, avecommunity15m15, avecommunity1defend, avecommunity2defend, avecommunity3defend, avecommunity4defend, avecommunity5defend, avecommunity6defend, avecommunity7defend, avecommunity8defend, avecommunity9defend, avecommunity10defend, avecommunity11defend, avecommunity12defend, avecommunity13defend, avecommunity14defend, avecommunity15defend, aveoneandtwo , aveoneandthree, aveoneandfour, aveoneandfive, aveoneandsix , aveoneandseven, aveoneandeight, aveoneandnine, aveoneandten , aveoneandeleven, aveoneandtwelve, aveoneandthirteen, aveoneandfourteen, aveoneandfifteen, avetwoandthree, avetwoandfour, avetwoandfive, avetwoandsix , avetwoandseven, avetwoandeight, avetwoandnine, avetwoandten , avetwoandeleven, avetwoandtwelve, avetwoandthirteen, avetwoandfourteen, avetwoandfifteen, avethreeandfour, avethreeandfive, avethreeandsix, avethreeandseven, avethreeandeight, avethreeandnine, avethreeandten, avethreeandeleven, avethreeandtwelve, avethreeandthirteen, avethreeandfourteen, avethreeandfifteen, avefourandfive, avefourandsix, avefourandseven, avefourandeight, avefourandnine, avefourandten, avefourandeleven, avefourandtwelve, avefourandthirteen, avefourandfourteen, avefourandfifteen, avefiveandsix, avefiveandseven, avefiveandeight, avefiveandnine, avefiveandten, avefiveandeleven, avefiveandtwelve, avefiveandthirteen, avefiveandfourteen, avefiveandfifteen, avesixandseven, avesixandeight, avesixandnine, avesixandten , avesixandeleven, avesixandtwelve, avesixandthirteen, avesixandfourteen, avesixandfifteen, avesevenandeight, avesevenandnine, avesevenandten, avesevenandeleven, avesevenandtwelve, avesevenandthirteen, avesevenandfourteen, avesevenandfifteen, aveeightandnine, aveeightandten, aveeightandeleven, aveeightandtwelve, aveeightandthirteen, aveeightandfourteen, aveeightandfifteen, avenineandten, avenineandeleven, avenineandtwelve, avenineandthirteen, avenineandfourteen, avenineandfifteen, avetenandeleven, avetenandtwelve, avetenandthirteen, avetenandfourteen, avetenandfifteen, aveelevenandtwelve, aveelevenandthirteen, aveelevenandfourteen, aveelevenandfifteen, avetwelveandthirteen, avetwelveandfourteen, avetwelveandfifteen, avethirteenandfourteen, avethirteenandfifteen, avefourteenandfifteen

def simulator2():
    strength1 = []
    for i in avestrength1:
        strength1.append(float(str(i[0])[:4]))
    strength2 = []
    for i in avestrength2:
        strength2.append(float(str(i[0])[:4]))
    strength3 = []
    for i in avestrength3:
        strength3.append(float(str(i[0])[:4]))
    strength4 = []
    for i in avestrength4:
        strength4.append(float(str(i[0])[:4]))
    strength5 = []
    for i in avestrength5:
        strength5.append(float(str(i[0])[:4]))
    strength6 = []
    for i in avestrength6:
        strength6.append(float(str(i[0])[:4]))
    strength7 = []
    for i in avestrength7:
        strength7.append(float(str(i[0])[:4]))
    strength8 = []
    for i in avestrength8:
        strength8.append(float(str(i[0])[:4]))
    strength9 = []
    for i in avestrength9:
        strength9.append(float(str(i[0])[:4]))
    strength10 = []
    for i in avestrength10:
        strength10.append(float(str(i[0])[:4]))
    strength11 = []
    for i in avestrength11:
        strength11.append(float(str(i[0])[:4]))
    strength12 = []
    for i in avestrength12:
        strength12.append(float(str(i[0])[:4]))
    strength13 = []
    for i in avestrength13:
        strength13.append(float(str(i[0])[:4]))
    strength14 = []
    for i in avestrength14:
        strength14.append(float(str(i[0])[:4]))
    strength15 = []
    for i in avestrength15:
        strength15.append(float(str(i[0])[:4]))

    community1defend = []
    for i in avecommunity1defend:
        community1defend.append(float(str(i[0])[:4]))
    community2defend = []
    for i in avecommunity2defend:
        community2defend.append(float(str(i[0])[:4]))
    community3defend = []
    for i in avecommunity3defend:
        community3defend.append(float(str(i[0])[:4]))
    community4defend = []
    for i in avecommunity4defend:
        community4defend.append(float(str(i[0])[:4]))
    community5defend = []
    for i in avecommunity5defend:
        community5defend.append(float(str(i[0])[:4]))
    community6defend = []
    for i in avecommunity6defend:
        community6defend.append(float(str(i[0])[:4]))
    community7defend = []
    for i in avecommunity7defend:
        community7defend.append(float(str(i[0])[:4]))
    community8defend = []
    for i in avecommunity8defend:
        community8defend.append(float(str(i[0])[:4]))
    community9defend = []
    for i in avecommunity9defend:
        community9defend.append(float(str(i[0])[:4]))
    community10defend = []
    for i in avecommunity10defend:
        community10defend.append(float(str(i[0])[:4]))
    community11defend = []
    for i in avecommunity11defend:
        community11defend.append(float(str(i[0])[:4]))
    community12defend = []
    for i in avecommunity12defend:
        community12defend.append(float(str(i[0])[:4]))
    community13defend = []
    for i in avecommunity13defend:
        community13defend.append(float(str(i[0])[:4]))
    community14defend = []
    for i in avecommunity14defend:
        community14defend.append(float(str(i[0])[:4]))
    community15defend = []
    for i in avecommunity15defend:
        community15defend.append(float(str(i[0])[:4]))

    oneandtwo = []
    for i in aveoneandtwo:
        oneandtwo.append(float(str(i[0])[:4]))
    oneandthree = []
    for i in aveoneandthree:
        oneandthree.append(float(str(i[0])[:4]))
    oneandfour = []
    for i in aveoneandfour:
        oneandfour.append(float(str(i[0])[:4]))
    oneandfive = []
    for i in aveoneandfive:
        oneandfive.append(float(str(i[0])[:4]))
    oneandsix = []
    for i in aveoneandsix:
        oneandsix.append(float(str(i[0])[:4]))
    oneandseven = []
    for i in aveoneandseven:
        oneandseven.append(float(str(i[0])[:4]))
    oneandeight = []
    for i in aveoneandeight:
        oneandeight.append(float(str(i[0])[:4]))
    oneandnine = []
    for i in aveoneandnine:
        oneandnine.append(float(str(i[0])[:4]))
    oneandten = []
    for i in aveoneandten:
        oneandten.append(float(str(i[0])[:4]))
    oneandeleven = []
    for i in aveoneandeleven:
        oneandeleven.append(float(str(i[0])[:4]))
    oneandtwelve = []
    for i in aveoneandtwelve:
        oneandtwelve.append(float(str(i[0])[:4]))
    oneandthirteen = []
    for i in aveoneandthirteen:
        oneandthirteen.append(float(str(i[0])[:4]))
    oneandfourteen = []
    for i in aveoneandfourteen:
        oneandfourteen.append(float(str(i[0])[:4]))
    oneandfifteen = []
    for i in aveoneandfifteen:
        oneandfifteen.append(float(str(i[0])[:4]))
    twoandthree = []
    for i in avetwoandthree:
        twoandthree.append(float(str(i[0])[:4]))
    twoandfour = []
    for i in avetwoandfour:
        twoandfour.append(float(str(i[0])[:4]))
    twoandfive = []
    for i in avetwoandfive:
        twoandfive.append(float(str(i[0])[:4]))
    twoandsix = []
    for i in avetwoandsix:
        twoandsix.append(float(str(i[0])[:4]))
    twoandseven = []
    for i in avetwoandseven:
        twoandseven.append(float(str(i[0])[:4]))
    twoandeight = []
    for i in avetwoandeight:
        twoandeight.append(float(str(i[0])[:4]))
    twoandnine = []
    for i in avetwoandnine:
        twoandnine.append(float(str(i[0])[:4]))
    twoandten = []
    for i in avetwoandten:
        twoandten.append(float(str(i[0])[:4]))
    twoandeleven = []
    for i in avetwoandeleven:
        twoandeleven.append(float(str(i[0])[:4]))
    twoandtwelve = []
    for i in avetwoandtwelve:
        twoandtwelve.append(float(str(i[0])[:4]))
    twoandthirteen = []
    for i in avetwoandthirteen:
        twoandthirteen.append(float(str(i[0])[:4]))
    twoandfourteen = []
    for i in avetwoandfourteen:
        twoandfourteen.append(float(str(i[0])[:4]))
    twoandfifteen = []
    for i in avetwoandfifteen:
        twoandfifteen.append(float(str(i[0])[:4]))
    threeandfour = []
    for i in avethreeandfour:
        threeandfour.append(float(str(i[0])[:4]))
    threeandfive = []
    for i in avethreeandfive:
        threeandfive.append(float(str(i[0])[:4]))
    threeandsix = []
    for i in avethreeandsix:
        threeandsix.append(float(str(i[0])[:4]))
    threeandseven = []
    for i in avethreeandseven:
        threeandseven.append(float(str(i[0])[:4]))
    threeandeight = []
    for i in avethreeandeight:
        threeandeight.append(float(str(i[0])[:4]))
    threeandnine = []
    for i in avethreeandnine:
        threeandnine.append(float(str(i[0])[:4]))
    threeandten = []
    for i in avethreeandten:
        threeandten.append(float(str(i[0])[:4]))
    threeandeleven = []
    for i in avethreeandeleven:
        threeandeleven.append(float(str(i[0])[:4]))
    threeandtwelve = []
    for i in avethreeandtwelve:
        threeandtwelve.append(float(str(i[0])[:4]))
    threeandthirteen = []
    for i in avethreeandthirteen:
        threeandthirteen.append(float(str(i[0])[:4]))
    threeandfourteen = []
    for i in avethreeandfourteen:
        threeandfourteen.append(float(str(i[0])[:4]))
    threeandfifteen = []
    for i in avethreeandfifteen:
        threeandfifteen.append(float(str(i[0])[:4]))
    fourandfive = []
    for i in avefourandfive:
        fourandfive.append(float(str(i[0])[:4]))
    fourandsix = []
    for i in avefourandsix:
        fourandsix.append(float(str(i[0])[:4]))
    fourandseven = []
    for i in avefourandseven:
        fourandseven.append(float(str(i[0])[:4]))
    fourandeight = []
    for i in avefourandeight:
        fourandeight.append(float(str(i[0])[:4]))
    fourandnine = []
    for i in avefourandnine:
        fourandnine.append(float(str(i[0])[:4]))
    fourandten = []
    for i in avefourandten:
        fourandten.append(float(str(i[0])[:4]))
    fourandeleven = []
    for i in avefourandeleven:
        fourandeleven.append(float(str(i[0])[:4]))
    fourandtwelve = []
    for i in avefourandtwelve:
        fourandtwelve.append(float(str(i[0])[:4]))
    fourandthirteen = []
    for i in avefourandthirteen:
        fourandthirteen.append(float(str(i[0])[:4]))
    fourandfourteen = []
    for i in avefourandfourteen:
        fourandfourteen.append(float(str(i[0])[:4]))
    fourandfifteen = []
    for i in avefourandfifteen:
        fourandfifteen.append(float(str(i[0])[:4]))
    fiveandsix = []
    for i in avefiveandsix:
        fiveandsix.append(float(str(i[0])[:4]))
    fiveandseven = []
    for i in avefiveandseven:
        fiveandseven.append(float(str(i[0])[:4]))
    fiveandeight = []
    for i in avefiveandeight:
        fiveandeight.append(float(str(i[0])[:4]))
    fiveandnine = []
    for i in avefiveandnine:
        fiveandnine.append(float(str(i[0])[:4]))
    fiveandten = []
    for i in avefiveandten:
        fiveandten.append(float(str(i[0])[:4]))
    fiveandeleven = []
    for i in avefiveandeleven:
        fiveandeleven.append(float(str(i[0])[:4]))
    fiveandtwelve = []
    for i in avefiveandtwelve:
        fiveandtwelve.append(float(str(i[0])[:4]))
    fiveandthirteen = []
    for i in avefiveandthirteen:
        fiveandthirteen.append(float(str(i[0])[:4]))
    fiveandfourteen = []
    for i in avefiveandfourteen:
        fiveandfourteen.append(float(str(i[0])[:4]))
    fiveandfifteen = []
    for i in avefiveandfifteen:
        fiveandfifteen.append(float(str(i[0])[:4]))
    sixandseven = []
    for i in avesixandseven:
        sixandseven.append(float(str(i[0])[:4]))
    sixandeight = []
    for i in avesixandeight:
        sixandeight.append(float(str(i[0])[:4]))
    sixandnine = []
    for i in avesixandnine:
        sixandnine.append(float(str(i[0])[:4]))
    sixandten = []
    for i in avesixandten:
        sixandten.append(float(str(i[0])[:4]))
    sixandeleven = []
    for i in avesixandeleven:
        sixandeleven.append(float(str(i[0])[:4]))
    sixandtwelve = []
    for i in avesixandtwelve:
        sixandtwelve.append(float(str(i[0])[:4]))
    sixandthirteen = []
    for i in avesixandthirteen:
        sixandthirteen.append(float(str(i[0])[:4]))
    sixandfourteen = []
    for i in avesixandfourteen:
        sixandfourteen.append(float(str(i[0])[:4]))
    sixandfifteen = []
    for i in avesixandfifteen:
        sixandfifteen.append(float(str(i[0])[:4]))
    sevenandeight = []
    for i in avesevenandeight:
        sevenandeight.append(float(str(i[0])[:4]))
    sevenandnine = []
    for i in avesevenandnine:
        sevenandnine.append(float(str(i[0])[:4]))
    sevenandten = []
    for i in avesevenandten:
        sevenandten.append(float(str(i[0])[:4]))
    sevenandeleven = []
    for i in avesevenandeleven:
        sevenandeleven.append(float(str(i[0])[:4]))
    sevenandtwelve = []
    for i in avesevenandtwelve:
        sevenandtwelve.append(float(str(i[0])[:4]))
    sevenandthirteen = []
    for i in avesevenandthirteen:
        sevenandthirteen.append(float(str(i[0])[:4]))
    sevenandfourteen = []
    for i in avesevenandfourteen:
        sevenandfourteen.append(float(str(i[0])[:4]))
    sevenandfifteen = []
    for i in avesevenandfifteen:
        sevenandfifteen.append(float(str(i[0])[:4]))
    eightandnine = []
    for i in aveeightandnine:
        eightandnine.append(float(str(i[0])[:4]))
    eightandten = []
    for i in aveeightandten:
        eightandten.append(float(str(i[0])[:4]))
    eightandeleven = []
    for i in aveeightandeleven:
        eightandeleven.append(float(str(i[0])[:4]))
    eightandtwelve = []
    for i in aveeightandtwelve:
        eightandtwelve.append(float(str(i[0])[:4]))
    eightandthirteen = []
    for i in aveeightandthirteen:
        eightandthirteen.append(float(str(i[0])[:4]))
    eightandfourteen = []
    for i in aveeightandfourteen:
        eightandfourteen.append(float(str(i[0])[:4]))
    eightandfifteen = []
    for i in aveeightandfifteen:
        eightandfifteen.append(float(str(i[0])[:4]))
    nineandten = []
    for i in avenineandten:
        nineandten.append(float(str(i[0])[:4]))
    nineandeleven = []
    for i in avenineandeleven:
        nineandeleven.append(float(str(i[0])[:4]))
    nineandtwelve = []
    for i in avenineandtwelve:
        nineandtwelve.append(float(str(i[0])[:4]))
    nineandthirteen = []
    for i in avenineandthirteen:
        nineandthirteen.append(float(str(i[0])[:4]))
    nineandfourteen = []
    for i in avenineandfourteen:
        nineandfourteen.append(float(str(i[0])[:4]))
    nineandfifteen = []
    for i in avenineandfifteen:
        nineandfifteen.append(float(str(i[0])[:4]))
    tenandeleven = []
    for i in avetenandeleven:
        tenandeleven.append(float(str(i[0])[:4]))
    tenandtwelve = []
    for i in avetenandtwelve:
        tenandtwelve.append(float(str(i[0])[:4]))
    tenandthirteen = []
    for i in avetenandthirteen:
        tenandthirteen.append(float(str(i[0])[:4]))
    tenandfourteen = []
    for i in avetenandfourteen:
        tenandfourteen.append(float(str(i[0])[:4]))
    tenandfifteen = []
    for i in avetenandfifteen:
        tenandfifteen.append(float(str(i[0])[:4]))
    elevenandtwelve = []
    for i in aveelevenandtwelve:
        elevenandtwelve.append(float(str(i[0])[:4]))
    elevenandthirteen = []
    for i in aveelevenandthirteen:
        elevenandthirteen.append(float(str(i[0])[:4]))
    elevenandfourteen = []
    for i in aveelevenandfourteen:
        elevenandfourteen.append(float(str(i[0])[:4]))
    elevenandfifteen = []
    for i in aveelevenandfifteen:
        elevenandfifteen.append(float(str(i[0])[:4]))
    twelveandthirteen = []
    for i in avetwelveandthirteen:
        twelveandthirteen.append(float(str(i[0])[:4]))
    twelveandfourteen = []
    for i in avetwelveandfourteen:
        twelveandfourteen.append(float(str(i[0])[:4]))
    twelveandfifteen = []
    for i in avetwelveandfifteen:
        twelveandfifteen.append(float(str(i[0])[:4]))
    thirteenandfourteen = []
    for i in avethirteenandfourteen:
        thirteenandfourteen.append(float(str(i[0])[:4]))
    thirteenandfifteen = []
    for i in avethirteenandfifteen:
        thirteenandfifteen.append(float(str(i[0])[:4]))
    fourteenandfifteen = []
    for i in avefourteenandfifteen:
        fourteenandfifteen.append(float(str(i[0])[:4]))

    rounds = []
    i = 1
    while i <= len(avestrength1):
        rounds.append(i)
        i += 1
    df = DataFrame({'rounds': rounds, 'strength1': strength1, 'notorietyratio1': avenotorietyratio1, 'totalextort1': avetotalextort1, 'countextort1': avecountextort1, 'countbenefit1': avecountbenefit1, 'countpunish1': avecountpunish1, 'countsupport1': avecountsupport1, 'totalsupport1': avetotalsupport1, 'countdefend1': avecountdefend1, 'strength2': strength2, 'notorietyratio2': avenotorietyratio2, 'totalextort2': avetotalextort2, 'countextort2': avecountextort2, 'countbenefit2': avecountbenefit2, 'countpunish2': avecountpunish2, 'countsupport2': avecountsupport2, 'totalsupport2': avetotalsupport2, 'countdefend2': avecountdefend2, 'strength3': strength3, 'notorietyratio3': avenotorietyratio3, 'totalextort3': avetotalextort3, 'countextort3': avecountextort3, 'countbenefit3': avecountbenefit3, 'countpunish3': avecountpunish3, 'countsupport3': avecountsupport3, 'totalsupport3': avetotalsupport3, 'countdefend3': avecountdefend3, 'strength4': strength4, 'notorietyratio4': avenotorietyratio4, 'totalextort4': avetotalextort4, 'countextort4': avecountextort4, 'countbenefit4': avecountbenefit4, 'countpunish4': avecountpunish4, 'countsupport4': avecountsupport4, 'totalsupport4': avetotalsupport4, 'countdefend4': avecountdefend4, 'strength5': strength5, 'notorietyratio5': avenotorietyratio5, 'totalextort5': avetotalextort5, 'countextort5': avecountextort5, 'countbenefit5': avecountbenefit5, 'countpunish5': avecountpunish5, 'countsupport5': avecountsupport5, 'totalsupport5': avetotalsupport5, 'countdefend5': avecountdefend5, 'strength6': strength6, 'notorietyratio6': avenotorietyratio6, 'totalextort6': avetotalextort6, 'countextort6': avecountextort6, 'countbenefit6': avecountbenefit6, 'countpunish6': avecountpunish6, 'countsupport6': avecountsupport6, 'totalsupport6': avetotalsupport6, 'countdefend6': avecountdefend6, 'strength7': strength7, 'notorietyratio7': avenotorietyratio7, 'totalextort7': avetotalextort7, 'countextort7': avecountextort7, 'countbenefit7': avecountbenefit7, 'countpunish7': avecountpunish7, 'countsupport7': avecountsupport7, 'totalsupport7': avetotalsupport7, 'countdefend7': avecountdefend7, 'strength8': strength8, 'notorietyratio8': avenotorietyratio8, 'totalextort8': avetotalextort8, 'countextort8': avecountextort8, 'countbenefit8': avecountbenefit8, 'countpunish8': avecountpunish8, 'countsupport8': avecountsupport8, 'totalsupport8': avetotalsupport8, 'countdefend8': avecountdefend8, 'strength9': strength9, 'notorietyratio9': avenotorietyratio9, 'totalextort9': avetotalextort9, 'countextort9': avecountextort9, 'countbenefit9': avecountbenefit9, 'countpunish9': avecountpunish9, 'countsupport9': avecountsupport9, 'totalsupport9': avetotalsupport9, 'countdefend9': avecountdefend9, 'strength10': strength10, 'notorietyratio10': avenotorietyratio10, 'totalextort10': avetotalextort10, 'countextort10': avecountextort10, 'countbenefit10': avecountbenefit10, 'countpunish10': avecountpunish10, 'countsupport10': avecountsupport10, 'totalsupport10': avetotalsupport10, 'countdefend10': avecountdefend10, 'strength11': strength11, 'notorietyratio11': avenotorietyratio11, 'totalextort11': avetotalextort11, 'countextort11': avecountextort11, 'countbenefit11': avecountbenefit11, 'countpunish11': avecountpunish11, 'countsupport11': avecountsupport11, 'totalsupport11': avetotalsupport11, 'countdefend11': avecountdefend11, 'strength12': strength12, 'notorietyratio12': avenotorietyratio12, 'totalextort12': avetotalextort12, 'countextort12': avecountextort12, 'countbenefit12': avecountbenefit12, 'countpunish12': avecountpunish12, 'countsupport12': avecountsupport12, 'totalsupport12': avetotalsupport12, 'countdefend12': avecountdefend12, 'strength13': strength13, 'notorietyratio13': avenotorietyratio13, 'totalextort13': avetotalextort13, 'countextort13': avecountextort13, 'countbenefit13': avecountbenefit13, 'countpunish13': avecountpunish13, 'countsupport13': avecountsupport13, 'totalsupport13': avetotalsupport13, 'countdefend13': avecountdefend13, 'strength14': strength14, 'notorietyratio14': avenotorietyratio14, 'totalextort14': avetotalextort14, 'countextort14': avecountextort14, 'countbenefit14': avecountbenefit14, 'countpunish14': avecountpunish14, 'countsupport14': avecountsupport14, 'totalsupport14': avetotalsupport14, 'countdefend14': avecountdefend14, 'strength15': strength15, 'notorietyratio15': avenotorietyratio15, 'totalextort15': avetotalextort15, 'countextort15': avecountextort15, 'countbenefit15': avecountbenefit15, 'countpunish15': avecountpunish15, 'countsupport15': avecountsupport15, 'totalsupport15': avetotalsupport15, 'countdefend15': avecountdefend15, 'community1m1': avecommunity1m1, 'community2m1': avecommunity2m1, 'community3m1': avecommunity3m1, 'community4m1': avecommunity4m1, 'community5m1': avecommunity5m1, 'community6m1': avecommunity6m1, 'community7m1': avecommunity7m1, 'community8m1': avecommunity8m1, 'community9m1': avecommunity9m1, 'community10m1': avecommunity10m1, 'community11m1': avecommunity11m1, 'community12m1': avecommunity12m1, 'community13m1': avecommunity13m1, 'community14m1': avecommunity14m1, 'community15m1': avecommunity15m1, 'community1m2': avecommunity1m2, 'community2m2': avecommunity2m2, 'community3m2': avecommunity3m2, 'community4m2': avecommunity4m2, 'community5m2': avecommunity5m2, 'community6m2': avecommunity6m2, 'community7m2': avecommunity7m2, 'community8m2': avecommunity8m2, 'community9m2': avecommunity9m2, 'community10m2': avecommunity10m2, 'community11m2': avecommunity11m2, 'community12m2': avecommunity12m2, 'community13m2': avecommunity13m2, 'community14m2': avecommunity14m2, 'community15m2': avecommunity15m2, 'community1m3': avecommunity1m3, 'community2m3': avecommunity2m3, 'community3m3': avecommunity3m3, 'community4m3': avecommunity4m3, 'community5m3': avecommunity5m3, 'community6m3': avecommunity6m3, 'community7m3': avecommunity7m3, 'community8m3': avecommunity8m3, 'community9m3': avecommunity9m3, 'community10m3': avecommunity10m3, 'community11m3': avecommunity11m3, 'community12m3': avecommunity12m3, 'community13m3': avecommunity13m3, 'community14m3': avecommunity14m3, 'community15m3': avecommunity15m3, 'community1m4': avecommunity1m4, 'community2m4': avecommunity2m4, 'community3m4': avecommunity3m4, 'community4m4': avecommunity4m4, 'community5m4': avecommunity5m4, 'community6m4': avecommunity6m4, 'community7m4': avecommunity7m4, 'community8m4': avecommunity8m4, 'community9m4': avecommunity9m4, 'community10m4': avecommunity10m4, 'community11m4': avecommunity11m4, 'community12m4': avecommunity12m4, 'community13m4': avecommunity13m4, 'community14m4': avecommunity14m4, 'community15m4': avecommunity15m4, 'community1m5': avecommunity1m5, 'community2m5': avecommunity2m5, 'community3m5': avecommunity3m5, 'community4m5': avecommunity4m5, 'community5m5': avecommunity5m5, 'community6m5': avecommunity6m5, 'community7m5': avecommunity7m5, 'community8m5': avecommunity8m5, 'community9m5': avecommunity9m5, 'community10m5': avecommunity10m5, 'community11m5': avecommunity11m5, 'community12m5': avecommunity12m5, 'community13m5': avecommunity13m5, 'community14m5': avecommunity14m5, 'community15m5': avecommunity15m5, 'community1m6': avecommunity1m6, 'community2m6': avecommunity2m6, 'community3m6': avecommunity3m6, 'community4m6': avecommunity4m6, 'community5m6': avecommunity5m6, 'community6m6': avecommunity6m6, 'community7m6': avecommunity7m6, 'community8m6': avecommunity8m6, 'community9m6': avecommunity9m6, 'community10m6': avecommunity10m6, 'community11m6': avecommunity11m6, 'community12m6': avecommunity12m6, 'community13m6': avecommunity13m6, 'community14m6': avecommunity14m6, 'community15m6': avecommunity15m6, 'community1m7': avecommunity1m7, 'community2m7': avecommunity2m7, 'community3m7': avecommunity3m7, 'community4m7': avecommunity4m7, 'community5m7': avecommunity5m7, 'community6m7': avecommunity6m7, 'community7m7': avecommunity7m7, 'community8m7': avecommunity8m7, 'community9m7': avecommunity9m7, 'community10m7': avecommunity10m7, 'community11m7': avecommunity11m7, 'community12m7': avecommunity12m7, 'community13m7': avecommunity13m7, 'community14m7': avecommunity14m7, 'community15m7': avecommunity15m7, 'community1m8': avecommunity1m8, 'community2m8': avecommunity2m8, 'community3m8': avecommunity3m8, 'community4m8': avecommunity4m8, 'community5m8': avecommunity5m8, 'community6m8': avecommunity6m8, 'community7m8': avecommunity7m8, 'community8m8': avecommunity8m8, 'community9m8': avecommunity9m8, 'community10m8': avecommunity10m8, 'community11m8': avecommunity11m8, 'community12m8': avecommunity12m8, 'community13m8': avecommunity13m8, 'community14m8': avecommunity14m8, 'community15m8': avecommunity15m8, 'community1m9': avecommunity1m9, 'community2m9': avecommunity2m9, 'community3m9': avecommunity3m9, 'community4m9': avecommunity4m9, 'community5m9': avecommunity5m9, 'community6m9': avecommunity6m9, 'community7m9': avecommunity7m9, 'community8m9': avecommunity8m9, 'community9m9': avecommunity9m9, 'community10m9': avecommunity10m9, 'community11m9': avecommunity11m9, 'community12m9': avecommunity12m9, 'community13m9': avecommunity13m9, 'community14m9': avecommunity14m9, 'community15m9': avecommunity15m9, 'community1m10': avecommunity1m10, 'community2m10': avecommunity2m10, 'community3m10': avecommunity3m10, 'community4m10': avecommunity4m10, 'community5m10': avecommunity5m10, 'community6m10': avecommunity6m10, 'community7m10': avecommunity7m10, 'community8m10': avecommunity8m10, 'community9m10': avecommunity9m10, 'community10m10': avecommunity10m10, 'community11m10': avecommunity11m10, 'community12m10': avecommunity12m10, 'community13m10': avecommunity13m10, 'community14m10': avecommunity14m10, 'community15m10': avecommunity15m10, 'community1m11': avecommunity1m11, 'community2m11': avecommunity2m11, 'community3m11': avecommunity3m11, 'community4m11': avecommunity4m11, 'community5m11': avecommunity5m11, 'community6m11': avecommunity6m11, 'community7m11': avecommunity7m11, 'community8m11': avecommunity8m11, 'community9m11': avecommunity9m11, 'community10m11': avecommunity10m11, 'community11m11': avecommunity11m11, 'community12m11': avecommunity12m11, 'community13m11': avecommunity13m11, 'community14m11': avecommunity14m11, 'community15m11': avecommunity15m11, 'community1m12': avecommunity1m12, 'community2m12': avecommunity2m12, 'community3m12': avecommunity3m12, 'community4m12': avecommunity4m12, 'community5m12': avecommunity5m12, 'community6m12': avecommunity6m12, 'community7m12': avecommunity7m12, 'community8m12': avecommunity8m12, 'community9m12': avecommunity9m12, 'community10m12': avecommunity10m12, 'community11m12': avecommunity11m12, 'community12m12': avecommunity12m12, 'community13m12': avecommunity13m12, 'community14m12': avecommunity14m12, 'community15m12': avecommunity15m12, 'community1m13': avecommunity1m13, 'community2m13': avecommunity2m13, 'community3m13': avecommunity3m13, 'community4m13': avecommunity4m13, 'community5m13': avecommunity5m13, 'community6m13': avecommunity6m13, 'community7m13': avecommunity7m13, 'community8m13': avecommunity8m13, 'community9m13': avecommunity9m13, 'community10m13': avecommunity10m13, 'community11m13': avecommunity11m13, 'community12m13': avecommunity12m13, 'community13m13': avecommunity13m13, 'community14m13': avecommunity14m13, 'community15m13': avecommunity15m13, 'community1m14': avecommunity1m14, 'community2m14': avecommunity2m14, 'community3m14': avecommunity3m14, 'community4m14': avecommunity4m14, 'community5m14': avecommunity5m14, 'community6m14': avecommunity6m14, 'community7m14': avecommunity7m14, 'community8m14': avecommunity8m14, 'community9m14': avecommunity9m14, 'community10m14': avecommunity10m14, 'community11m14': avecommunity11m14, 'community12m14': avecommunity12m14, 'community13m14': avecommunity13m14, 'community14m14': avecommunity14m14, 'community15m14': avecommunity15m14, 'community1m15': avecommunity1m15, 'community2m15': avecommunity2m15, 'community3m15': avecommunity3m15, 'community4m15': avecommunity4m15, 'community5m15': avecommunity5m15, 'community6m15': avecommunity6m15, 'community7m15': avecommunity7m15, 'community8m15': avecommunity8m15, 'community9m15': avecommunity9m15, 'community10m15': avecommunity10m15, 'community11m15': avecommunity11m15, 'community12m15': avecommunity12m15, 'community13m15': avecommunity13m15, 'community14m15': avecommunity14m15, 'community15m15': avecommunity15m15, 'community1defend': community1defend, 'community2defend': community2defend, 'community3defend': community3defend, 'community4defend': community4defend, 'community5defend': community5defend, 'community6defend': community6defend, 'community7defend': community7defend, 'community8defend': community8defend, 'community9defend': community9defend, 'community10defend': community10defend, 'community11defend': community11defend, 'community12defend': community12defend, 'community13defend': community13defend, 'community14defend': community14defend, 'community15defend': community15defend, 'oneandtwo': oneandtwo, 'oneandthree': oneandthree, 'twoandthree': twoandthree, 'oneandfour': oneandfour, 'oneandfive': oneandfive, 'oneandsix': oneandsix, 'oneandseven': oneandseven, 'oneandeight': oneandeight, 'oneandnine': oneandnine, 'oneandten': oneandten, 'oneandeleven': oneandeleven, 'oneandtwelve': oneandtwelve, 'oneandthirteen': oneandthirteen, 'oneandfourteen': oneandfourteen, 'oneandfifteen': oneandfifteen, 'twoandfour': twoandfour, 'twoandfive': twoandfive, 'twoandsix': twoandsix, 'twoandseven': twoandseven, 'twoandeight': twoandeight, 'twoandnine': twoandnine, 'twoandten': twoandten, 'twoandeleven': twoandeleven, 'twoandtwelve': twoandtwelve, 'twoandthirteen': twoandthirteen, 'twoandfourteen': twoandfourteen, 'twoandfifteen': twoandfifteen, 'threeandfour': threeandfour, 'threeandfive': threeandfive, 'threeandsix': threeandsix, 'threeandseven': threeandseven, 'threeandeight': threeandeight, 'threeandnine': threeandnine, 'threeandten': threeandten, 'threeandeleven': threeandeleven, 'threeandtwelve': threeandtwelve, 'threeandthirteen': threeandthirteen, 'threeandfourteen': threeandfourteen, 'threeandfifteen': threeandfifteen, 'fourandfive': fourandfive, 'fourandsix': fourandsix, 'fourandseven': fourandseven, 'fourandeight': fourandeight, 'fourandnine': fourandnine, 'fourandten': fourandten, 'fourandeleven': fourandeleven, 'fourandtwelve': fourandtwelve, 'fourandthirteen': fourandthirteen, 'fourandfourteen': fourandfourteen, 'fourandfifteen': fourandfifteen, 'fiveandsix': fiveandsix, 'fiveandseven': fiveandseven, 'fiveandeight': fiveandeight, 'fiveandnine': fiveandnine, 'fiveandten': fiveandten, 'fiveandeleven': fiveandeleven, 'fiveandtwelve': fiveandtwelve, 'fiveandthirteen': fiveandthirteen, 'fiveandfourteen': fiveandfourteen, 'fiveandfifteen': fiveandfifteen, 'sixandseven': sixandseven, 'sixandeight': sixandeight, 'sixandnine': sixandnine, 'sixandten': sixandten, 'sixandeleven': sixandeleven, 'sixandtwelve': sixandtwelve, 'sixandthirteen': sixandthirteen, 'sixandfourteen': sixandfourteen, 'sixandfifteen': sixandfifteen, 'sevenandeight': sevenandeight, 'sevenandnine': sevenandnine, 'sevenandten': sevenandten, 'sevenandeleven': sevenandeleven, 'sevenandtwelve': sevenandtwelve, 'sevenandthirteen': sevenandthirteen, 'sevenandfourteen': sevenandfourteen, 'sevenandfifteen': sevenandfifteen, 'eightandnine': eightandnine, 'eightandten': eightandten, 'eightandeleven': eightandeleven, 'eightandtwelve': eightandtwelve, 'eightandthirteen': eightandthirteen, 'eightandfourteen': eightandfourteen, 'eightandfifteen': eightandfifteen, 'nineandten': nineandten, 'nineandeleven': nineandeleven, 'nineandtwelve': nineandtwelve, 'nineandthirteen': nineandthirteen, 'nineandfourteen': nineandfourteen, 'nineandfifteen': nineandfifteen, 'tenandeleven': tenandeleven, 'tenandtwelve': tenandtwelve, 'tenandthirteen': tenandthirteen, 'tenandfourteen': tenandfourteen, 'tenandfifteen': tenandfifteen, 'elevenandtwelve': elevenandtwelve, 'elevenandthirteen': elevenandthirteen, 'elevenandfourteen': elevenandfourteen, 'elevenandfifteen': elevenandfifteen, 'twelveandthirteen': twelveandthirteen, 'twelveandfourteen': twelveandfourteen, 'twelveandfifteen': twelveandfifteen, 'thirteenandfourteen': thirteenandfourteen, 'thirteenandfifteen': thirteenandfifteen, 'fourteenandfifteen': fourteenandfifteen})
    df = df[['rounds', 'strength1', 'notorietyratio1', 'totalextort1', 'countextort1', 'countbenefit1', 'countpunish1', 'countsupport1', 'totalsupport1', 'countdefend1', 'strength2', 'notorietyratio2', 'totalextort2', 'countextort2', 'countbenefit2', 'countpunish2', 'countsupport2', 'totalsupport2', 'countdefend2', 'strength3', 'notorietyratio3', 'totalextort3', 'countextort3', 'countbenefit3', 'countpunish3', 'countsupport3', 'totalsupport3', 'countdefend3', 'strength4', 'notorietyratio4', 'totalextort4', 'countextort4', 'countbenefit4', 'countpunish4', 'countsupport4', 'totalsupport4', 'countdefend4', 'strength5', 'notorietyratio5', 'totalextort5', 'countextort5', 'countbenefit5', 'countpunish5', 'countsupport5', 'totalsupport5', 'countdefend5', 'strength6', 'notorietyratio6', 'totalextort6', 'countextort6', 'countbenefit6', 'countpunish6', 'countsupport6', 'totalsupport6', 'countdefend6', 'strength7', 'notorietyratio7', 'totalextort7', 'countextort7', 'countbenefit7', 'countpunish7', 'countsupport7', 'totalsupport7', 'countdefend7', 'strength8', 'notorietyratio8', 'totalextort8', 'countextort8', 'countbenefit8', 'countpunish8', 'countsupport8', 'totalsupport8', 'countdefend8', 'strength9', 'notorietyratio9', 'totalextort9', 'countextort9', 'countbenefit9', 'countpunish9', 'countsupport9', 'totalsupport9', 'countdefend9', 'strength10', 'notorietyratio10', 'totalextort10', 'countextort10', 'countbenefit10', 'countpunish10', 'countsupport10', 'totalsupport10', 'countdefend10', 'strength11', 'notorietyratio11', 'totalextort11', 'countextort11', 'countbenefit11', 'countpunish11', 'countsupport11', 'totalsupport11', 'countdefend11', 'strength12', 'notorietyratio12', 'totalextort12', 'countextort12', 'countbenefit12', 'countpunish12', 'countsupport12', 'totalsupport12', 'countdefend12', 'strength13', 'notorietyratio13', 'totalextort13', 'countextort13', 'countbenefit13', 'countpunish13', 'countsupport13', 'totalsupport13', 'countdefend13', 'strength14', 'notorietyratio14', 'totalextort14', 'countextort14', 'countbenefit14', 'countpunish14', 'countsupport14', 'totalsupport14', 'countdefend14', 'strength15', 'notorietyratio15', 'totalextort15', 'countextort15', 'countbenefit15', 'countpunish15', 'countsupport15', 'totalsupport15', 'countdefend15', 'community1m1', 'community2m1', 'community3m1', 'community4m1', 'community5m1', 'community6m1', 'community7m1', 'community8m1', 'community9m1', 'community10m1', 'community11m1', 'community12m1', 'community13m1', 'community14m1', 'community15m1', 'community1m2', 'community2m2', 'community3m2', 'community4m2', 'community5m2', 'community6m2', 'community7m2', 'community8m2', 'community9m2', 'community10m2', 'community11m2', 'community12m2', 'community13m2', 'community14m2', 'community15m2', 'community1m3', 'community2m3', 'community3m3', 'community4m3', 'community5m3', 'community6m3', 'community7m3', 'community8m3', 'community9m3', 'community10m3', 'community11m3', 'community12m3', 'community13m3', 'community14m3', 'community15m3', 'community1m4', 'community2m4', 'community3m4', 'community4m4', 'community5m4', 'community6m4', 'community7m4', 'community8m4', 'community9m4', 'community10m4', 'community11m4', 'community12m4', 'community13m4', 'community14m4', 'community15m4', 'community1m5', 'community2m5', 'community3m5', 'community4m5', 'community5m5', 'community6m5', 'community7m5', 'community8m5', 'community9m5', 'community10m5', 'community11m5', 'community12m5', 'community13m5', 'community14m5', 'community15m5', 'community1m6', 'community2m6', 'community3m6', 'community4m6', 'community5m6', 'community6m6', 'community7m6', 'community8m6', 'community9m6', 'community10m6', 'community11m6', 'community12m6', 'community13m6', 'community14m6', 'community15m6', 'community1m7', 'community2m7', 'community3m7', 'community4m7', 'community5m7', 'community6m7', 'community7m7', 'community8m7', 'community9m7', 'community10m7', 'community11m7', 'community12m7', 'community13m7', 'community14m7', 'community15m7', 'community1m8', 'community2m8', 'community3m8', 'community4m8', 'community5m8', 'community6m8', 'community7m8', 'community8m8', 'community9m8', 'community10m8', 'community11m8', 'community12m8', 'community13m8', 'community14m8', 'community15m8', 'community1m9', 'community2m9', 'community3m9', 'community4m9', 'community5m9', 'community6m9', 'community7m9', 'community8m9', 'community9m9', 'community10m9', 'community11m9', 'community12m9', 'community13m9', 'community14m9', 'community15m9', 'community1m10', 'community2m10', 'community3m10', 'community4m10', 'community5m10', 'community6m10', 'community7m10', 'community8m10', 'community9m10', 'community10m10', 'community11m10', 'community12m10', 'community13m10', 'community14m10', 'community15m10', 'community1m11', 'community2m11', 'community3m11', 'community4m11', 'community5m11', 'community6m11', 'community7m11', 'community8m11', 'community9m11', 'community10m11', 'community11m11', 'community12m11', 'community13m11', 'community14m11', 'community15m11', 'community1m12', 'community2m12', 'community3m12', 'community4m12', 'community5m12', 'community6m12', 'community7m12', 'community8m12', 'community9m12', 'community10m12', 'community11m12', 'community12m12', 'community13m12', 'community14m12', 'community15m12', 'community1m13', 'community2m13', 'community3m13', 'community4m13', 'community5m13', 'community6m13', 'community7m13', 'community8m13', 'community9m13', 'community10m13', 'community11m13', 'community12m13', 'community13m13', 'community14m13', 'community15m13', 'community1m14', 'community2m14', 'community3m14', 'community4m14', 'community5m14', 'community6m14', 'community7m14', 'community8m14', 'community9m14', 'community10m14', 'community11m14', 'community12m14', 'community13m14', 'community14m14', 'community15m14', 'community1m15', 'community2m15', 'community3m15', 'community4m15', 'community5m15', 'community6m15', 'community7m15', 'community8m15', 'community9m15', 'community10m15', 'community11m15', 'community12m15', 'community13m15', 'community14m15', 'community15m15', 'community1defend', 'community2defend', 'community3defend', 'community4defend', 'community5defend', 'community6defend', 'community7defend', 'community8defend', 'community9defend', 'community10defend', 'community11defend', 'community12defend', 'community13defend', 'community14defend', 'community15defend', 'oneandtwo', 'oneandthree', 'oneandfour', 'oneandfive', 'oneandsix', 'oneandseven', 'oneandeight', 'oneandnine', 'oneandten', 'oneandeleven', 'oneandtwelve', 'oneandthirteen', 'oneandfourteen', 'oneandfifteen', 'twoandthree', 'twoandfour', 'twoandfive', 'twoandsix', 'twoandseven', 'twoandeight', 'twoandnine', 'twoandten', 'twoandeleven', 'twoandtwelve', 'twoandthirteen', 'twoandfourteen', 'twoandfifteen', 'threeandfour', 'threeandfive', 'threeandsix', 'threeandseven', 'threeandeight', 'threeandnine', 'threeandten', 'threeandeleven', 'threeandtwelve', 'threeandthirteen', 'threeandfourteen', 'threeandfifteen', 'fourandfive', 'fourandsix', 'fourandseven', 'fourandeight', 'fourandnine', 'fourandten', 'fourandeleven', 'fourandtwelve', 'fourandthirteen', 'fourandfourteen', 'fourandfifteen', 'fiveandsix', 'fiveandseven', 'fiveandeight', 'fiveandnine', 'fiveandten', 'fiveandeleven', 'fiveandtwelve', 'fiveandthirteen', 'fiveandfourteen', 'fiveandfifteen', 'sixandseven', 'sixandeight', 'sixandnine', 'sixandten', 'sixandeleven', 'sixandtwelve', 'sixandthirteen', 'sixandfourteen', 'sixandfifteen', 'sevenandeight', 'sevenandnine', 'sevenandten', 'sevenandeleven', 'sevenandtwelve', 'sevenandthirteen', 'sevenandfourteen', 'sevenandfifteen', 'eightandnine', 'eightandten', 'eightandeleven', 'eightandtwelve', 'eightandthirteen', 'eightandfourteen', 'eightandfifteen', 'nineandten', 'nineandeleven', 'nineandtwelve', 'nineandthirteen', 'nineandfourteen', 'nineandfifteen', 'tenandeleven', 'tenandtwelve', 'tenandthirteen', 'tenandfourteen', 'tenandfifteen', 'elevenandtwelve', 'elevenandthirteen', 'elevenandfourteen', 'elevenandfifteen', 'twelveandthirteen', 'twelveandfourteen', 'twelveandfifteen', 'thirteenandfourteen', 'thirteenandfifteen', 'fourteenandfifteen']]
    print('Data Saved')
    return df

data = simulator2()
print(data['strength1'])