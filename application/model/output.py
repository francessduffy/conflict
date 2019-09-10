import matplotlib.pyplot as plt
from pandas import DataFrame
# from app.model.simulator import avestrength1, avenotorietyratio1, avetotalextort1, avecountextort1, avecountbenefit1, avecountpunish1, avecountsupport1, avetotalsupport1, avecountdefend1, avestrength2 , avenotorietyratio2, avetotalextort2, avecountextort2, avecountbenefit2, avecountpunish2, avecountsupport2, avetotalsupport2, avecountdefend2, avestrength3 , avenotorietyratio3, avetotalextort3, avecountextort3, avecountbenefit3, avecountpunish3, avecountsupport3, avetotalsupport3, avecountdefend3, avestrength4 , avenotorietyratio4, avetotalextort4, avecountextort4, avecountbenefit4, avecountpunish4, avecountsupport4, avetotalsupport4, avecountdefend4, avestrength5 , avenotorietyratio5, avetotalextort5, avecountextort5, avecountbenefit5, avecountpunish5, avecountsupport5, avetotalsupport5, avecountdefend5, avestrength6 , avenotorietyratio6, avetotalextort6, avecountextort6, avecountbenefit6, avecountpunish6, avecountsupport6, avetotalsupport6, avecountdefend6, avestrength7 , avenotorietyratio7, avetotalextort7, avecountextort7, avecountbenefit7, avecountpunish7, avecountsupport7, avetotalsupport7, avecountdefend7, avestrength8 , avenotorietyratio8, avetotalextort8, avecountextort8, avecountbenefit8, avecountpunish8, avecountsupport8, avetotalsupport8, avecountdefend8, avestrength9 , avenotorietyratio9, avetotalextort9, avecountextort9, avecountbenefit9, avecountpunish9, avecountsupport9, avetotalsupport9, avecountdefend9, avestrength10, avenotorietyratio10, avetotalextort10, avecountextort10, avecountbenefit10, avecountpunish10, avecountsupport10, avetotalsupport10, avecountdefend10, avestrength11, avenotorietyratio11, avetotalextort11, avecountextort11, avecountbenefit11, avecountpunish11, avecountsupport11, avetotalsupport11, avecountdefend11, avestrength12, avenotorietyratio12, avetotalextort12, avecountextort12, avecountbenefit12, avecountpunish12, avecountsupport12, avetotalsupport12, avecountdefend12, avestrength13, avenotorietyratio13, avetotalextort13, avecountextort13, avecountbenefit13, avecountpunish13, avecountsupport13, avetotalsupport13, avecountdefend13, avestrength14, avenotorietyratio14, avetotalextort14, avecountextort14, avecountbenefit14, avecountpunish14, avecountsupport14, avetotalsupport14, avecountdefend14, avestrength15, avenotorietyratio15, avetotalextort15, avecountextort15, avecountbenefit15, avecountpunish15, avecountsupport15, avetotalsupport15, avecountdefend15, avecommunity1m1, avecommunity2m1, avecommunity3m1, avecommunity4m1, avecommunity5m1, avecommunity6m1, avecommunity7m1, avecommunity8m1, avecommunity9m1, avecommunity10m1, avecommunity11m1, avecommunity12m1, avecommunity13m1, avecommunity14m1, avecommunity15m1, avecommunity1m2, avecommunity2m2, avecommunity3m2, avecommunity4m2, avecommunity5m2, avecommunity6m2, avecommunity7m2, avecommunity8m2, avecommunity9m2, avecommunity10m2, avecommunity11m2, avecommunity12m2, avecommunity13m2, avecommunity14m2, avecommunity15m2, avecommunity1m3, avecommunity2m3, avecommunity3m3, avecommunity4m3, avecommunity5m3, avecommunity6m3, avecommunity7m3, avecommunity8m3, avecommunity9m3, avecommunity10m3, avecommunity11m3, avecommunity12m3, avecommunity13m3, avecommunity14m3, avecommunity15m3, avecommunity1m4, avecommunity2m4, avecommunity3m4, avecommunity4m4, avecommunity5m4, avecommunity6m4, avecommunity7m4, avecommunity8m4, avecommunity9m4, avecommunity10m4, avecommunity11m4, avecommunity12m4, avecommunity13m4, avecommunity14m4, avecommunity15m4, avecommunity1m5, avecommunity2m5, avecommunity3m5, avecommunity4m5, avecommunity5m5, avecommunity6m5, avecommunity7m5, avecommunity8m5, avecommunity9m5, avecommunity10m5, avecommunity11m5, avecommunity12m5, avecommunity13m5, avecommunity14m5, avecommunity15m5, avecommunity1m6, avecommunity2m6, avecommunity3m6, avecommunity4m6, avecommunity5m6, avecommunity6m6, avecommunity7m6, avecommunity8m6, avecommunity9m6, avecommunity10m6, avecommunity11m6, avecommunity12m6, avecommunity13m6, avecommunity14m6, avecommunity15m6, avecommunity1m7, avecommunity2m7, avecommunity3m7, avecommunity4m7, avecommunity5m7, avecommunity6m7, avecommunity7m7, avecommunity8m7, avecommunity9m7, avecommunity10m7, avecommunity11m7, avecommunity12m7, avecommunity13m7, avecommunity14m7, avecommunity15m7, avecommunity1m8, avecommunity2m8, avecommunity3m8, avecommunity4m8, avecommunity5m8, avecommunity6m8, avecommunity7m8, avecommunity8m8, avecommunity9m8, avecommunity10m8, avecommunity11m8, avecommunity12m8, avecommunity13m8, avecommunity14m8, avecommunity15m8, avecommunity1m9, avecommunity2m9, avecommunity3m9, avecommunity4m9, avecommunity5m9, avecommunity6m9, avecommunity7m9, avecommunity8m9, avecommunity9m9, avecommunity10m9, avecommunity11m9, avecommunity12m9, avecommunity13m9, avecommunity14m9, avecommunity15m9, avecommunity1m10, avecommunity2m10, avecommunity3m10, avecommunity4m10, avecommunity5m10, avecommunity6m10, avecommunity7m10, avecommunity8m10, avecommunity9m10, avecommunity10m10, avecommunity11m10, avecommunity12m10, avecommunity13m10, avecommunity14m10, avecommunity15m10, avecommunity1m11, avecommunity2m11, avecommunity3m11, avecommunity4m11, avecommunity5m11, avecommunity6m11, avecommunity7m11, avecommunity8m11, avecommunity9m11, avecommunity10m11, avecommunity11m11, avecommunity12m11, avecommunity13m11, avecommunity14m11, avecommunity15m11, avecommunity1m12, avecommunity2m12, avecommunity3m12, avecommunity4m12, avecommunity5m12, avecommunity6m12, avecommunity7m12, avecommunity8m12, avecommunity9m12, avecommunity10m12, avecommunity11m12, avecommunity12m12, avecommunity13m12, avecommunity14m12, avecommunity15m12, avecommunity1m13, avecommunity2m13, avecommunity3m13, avecommunity4m13, avecommunity5m13, avecommunity6m13, avecommunity7m13, avecommunity8m13, avecommunity9m13, avecommunity10m13, avecommunity11m13, avecommunity12m13, avecommunity13m13, avecommunity14m13, avecommunity15m13, avecommunity1m14, avecommunity2m14, avecommunity3m14, avecommunity4m14, avecommunity5m14, avecommunity6m14, avecommunity7m14, avecommunity8m14, avecommunity9m14, avecommunity10m14, avecommunity11m14, avecommunity12m14, avecommunity13m14, avecommunity14m14, avecommunity15m14, avecommunity1m15, avecommunity2m15, avecommunity3m15, avecommunity4m15, avecommunity5m15, avecommunity6m15, avecommunity7m15, avecommunity8m15, avecommunity9m15, avecommunity10m15, avecommunity11m15, avecommunity12m15, avecommunity13m15, avecommunity14m15, avecommunity15m15, avecommunity1defend, avecommunity2defend, avecommunity3defend, avecommunity4defend, avecommunity5defend, avecommunity6defend, avecommunity7defend, avecommunity8defend, avecommunity9defend, avecommunity10defend, avecommunity11defend, avecommunity12defend, avecommunity13defend, avecommunity14defend, avecommunity15defend, aveoneandtwo , aveoneandthree, aveoneandfour, aveoneandfive, aveoneandsix , aveoneandseven, aveoneandeight, aveoneandnine, aveoneandten , aveoneandeleven, aveoneandtwelve, aveoneandthirteen, aveoneandfourteen, aveoneandfifteen, avetwoandthree, avetwoandfour, avetwoandfive, avetwoandsix , avetwoandseven, avetwoandeight, avetwoandnine, avetwoandten , avetwoandeleven, avetwoandtwelve, avetwoandthirteen, avetwoandfourteen, avetwoandfifteen, avethreeandfour, avethreeandfive, avethreeandsix, avethreeandseven, avethreeandeight, avethreeandnine, avethreeandten, avethreeandeleven, avethreeandtwelve, avethreeandthirteen, avethreeandfourteen, avethreeandfifteen, avefourandfive, avefourandsix, avefourandseven, avefourandeight, avefourandnine, avefourandten, avefourandeleven, avefourandtwelve, avefourandthirteen, avefourandfourteen, avefourandfifteen, avefiveandsix, avefiveandseven, avefiveandeight, avefiveandnine, avefiveandten, avefiveandeleven, avefiveandtwelve, avefiveandthirteen, avefiveandfourteen, avefiveandfifteen, avesixandseven, avesixandeight, avesixandnine, avesixandten , avesixandeleven, avesixandtwelve, avesixandthirteen, avesixandfourteen, avesixandfifteen, avesevenandeight, avesevenandnine, avesevenandten, avesevenandeleven, avesevenandtwelve, avesevenandthirteen, avesevenandfourteen, avesevenandfifteen, aveeightandnine, aveeightandten, aveeightandeleven, aveeightandtwelve, aveeightandthirteen, aveeightandfourteen, aveeightandfifteen, avenineandten, avenineandeleven, avenineandtwelve, avenineandthirteen, avenineandfourteen, avenineandfifteen, avetenandeleven, avetenandtwelve, avetenandthirteen, avetenandfourteen, avetenandfifteen, aveelevenandtwelve, aveelevenandthirteen, aveelevenandfourteen, aveelevenandfifteen, avetwelveandthirteen, avetwelveandfourteen, avetwelveandfifteen, avethirteenandfourteen, avethirteenandfifteen, avefourteenandfifteen
from application.model.simulatoronce import avestrength1 , avenotorietyratio1, avetotalextort1, avecountextort1, avecountbenefit1, avecountpunish1, avecountsupport1, avetotalsupport1, avecountdefend1, avestrength2 , avenotorietyratio2, avetotalextort2, avecountextort2, avecountbenefit2, avecountpunish2, avecountsupport2, avetotalsupport2, avecountdefend2, avestrength3 , avenotorietyratio3, avetotalextort3, avecountextort3, avecountbenefit3, avecountpunish3, avecountsupport3, avetotalsupport3, avecountdefend3, avestrength4 , avenotorietyratio4, avetotalextort4, avecountextort4, avecountbenefit4, avecountpunish4, avecountsupport4, avetotalsupport4, avecountdefend4, avestrength5 , avenotorietyratio5, avetotalextort5, avecountextort5, avecountbenefit5, avecountpunish5, avecountsupport5, avetotalsupport5, avecountdefend5, avestrength6 , avenotorietyratio6, avetotalextort6, avecountextort6, avecountbenefit6, avecountpunish6, avecountsupport6, avetotalsupport6, avecountdefend6, avestrength7 , avenotorietyratio7, avetotalextort7, avecountextort7, avecountbenefit7, avecountpunish7, avecountsupport7, avetotalsupport7, avecountdefend7, avestrength8 , avenotorietyratio8, avetotalextort8, avecountextort8, avecountbenefit8, avecountpunish8, avecountsupport8, avetotalsupport8, avecountdefend8, avestrength9 , avenotorietyratio9, avetotalextort9, avecountextort9, avecountbenefit9, avecountpunish9, avecountsupport9, avetotalsupport9, avecountdefend9, avestrength10, avenotorietyratio10, avetotalextort10, avecountextort10, avecountbenefit10, avecountpunish10, avecountsupport10, avetotalsupport10, avecountdefend10, avestrength11, avenotorietyratio11, avetotalextort11, avecountextort11, avecountbenefit11, avecountpunish11, avecountsupport11, avetotalsupport11, avecountdefend11, avestrength12, avenotorietyratio12, avetotalextort12, avecountextort12, avecountbenefit12, avecountpunish12, avecountsupport12, avetotalsupport12, avecountdefend12, avestrength13, avenotorietyratio13, avetotalextort13, avecountextort13, avecountbenefit13, avecountpunish13, avecountsupport13, avetotalsupport13, avecountdefend13, avestrength14, avenotorietyratio14, avetotalextort14, avecountextort14, avecountbenefit14, avecountpunish14, avecountsupport14, avetotalsupport14, avecountdefend14, avestrength15, avenotorietyratio15, avetotalextort15, avecountextort15, avecountbenefit15, avecountpunish15, avecountsupport15, avetotalsupport15, avecountdefend15, avecommunity1m1, avecommunity2m1, avecommunity3m1, avecommunity4m1, avecommunity5m1, avecommunity6m1, avecommunity7m1, avecommunity8m1, avecommunity9m1, avecommunity10m1, avecommunity11m1, avecommunity12m1, avecommunity13m1, avecommunity14m1, avecommunity15m1, avecommunity1m2, avecommunity2m2, avecommunity3m2, avecommunity4m2, avecommunity5m2, avecommunity6m2, avecommunity7m2, avecommunity8m2, avecommunity9m2, avecommunity10m2, avecommunity11m2, avecommunity12m2, avecommunity13m2, avecommunity14m2, avecommunity15m2, avecommunity1m3, avecommunity2m3, avecommunity3m3, avecommunity4m3, avecommunity5m3, avecommunity6m3, avecommunity7m3, avecommunity8m3, avecommunity9m3, avecommunity10m3, avecommunity11m3, avecommunity12m3, avecommunity13m3, avecommunity14m3, avecommunity15m3, avecommunity1m4, avecommunity2m4, avecommunity3m4, avecommunity4m4, avecommunity5m4, avecommunity6m4, avecommunity7m4, avecommunity8m4, avecommunity9m4, avecommunity10m4, avecommunity11m4, avecommunity12m4, avecommunity13m4, avecommunity14m4, avecommunity15m4, avecommunity1m5, avecommunity2m5, avecommunity3m5, avecommunity4m5, avecommunity5m5, avecommunity6m5, avecommunity7m5, avecommunity8m5, avecommunity9m5, avecommunity10m5, avecommunity11m5, avecommunity12m5, avecommunity13m5, avecommunity14m5, avecommunity15m5, avecommunity1m6, avecommunity2m6, avecommunity3m6, avecommunity4m6, avecommunity5m6, avecommunity6m6, avecommunity7m6, avecommunity8m6, avecommunity9m6, avecommunity10m6, avecommunity11m6, avecommunity12m6, avecommunity13m6, avecommunity14m6, avecommunity15m6, avecommunity1m7, avecommunity2m7, avecommunity3m7, avecommunity4m7, avecommunity5m7, avecommunity6m7, avecommunity7m7, avecommunity8m7, avecommunity9m7, avecommunity10m7, avecommunity11m7, avecommunity12m7, avecommunity13m7, avecommunity14m7, avecommunity15m7, avecommunity1m8, avecommunity2m8, avecommunity3m8, avecommunity4m8, avecommunity5m8, avecommunity6m8, avecommunity7m8, avecommunity8m8, avecommunity9m8, avecommunity10m8, avecommunity11m8, avecommunity12m8, avecommunity13m8, avecommunity14m8, avecommunity15m8, avecommunity1m9, avecommunity2m9, avecommunity3m9, avecommunity4m9, avecommunity5m9, avecommunity6m9, avecommunity7m9, avecommunity8m9, avecommunity9m9, avecommunity10m9, avecommunity11m9, avecommunity12m9, avecommunity13m9, avecommunity14m9, avecommunity15m9, avecommunity1m10, avecommunity2m10, avecommunity3m10, avecommunity4m10, avecommunity5m10, avecommunity6m10, avecommunity7m10, avecommunity8m10, avecommunity9m10, avecommunity10m10, avecommunity11m10, avecommunity12m10, avecommunity13m10, avecommunity14m10, avecommunity15m10, avecommunity1m11, avecommunity2m11, avecommunity3m11, avecommunity4m11, avecommunity5m11, avecommunity6m11, avecommunity7m11, avecommunity8m11, avecommunity9m11, avecommunity10m11, avecommunity11m11, avecommunity12m11, avecommunity13m11, avecommunity14m11, avecommunity15m11, avecommunity1m12, avecommunity2m12, avecommunity3m12, avecommunity4m12, avecommunity5m12, avecommunity6m12, avecommunity7m12, avecommunity8m12, avecommunity9m12, avecommunity10m12, avecommunity11m12, avecommunity12m12, avecommunity13m12, avecommunity14m12, avecommunity15m12, avecommunity1m13, avecommunity2m13, avecommunity3m13, avecommunity4m13, avecommunity5m13, avecommunity6m13, avecommunity7m13, avecommunity8m13, avecommunity9m13, avecommunity10m13, avecommunity11m13, avecommunity12m13, avecommunity13m13, avecommunity14m13, avecommunity15m13, avecommunity1m14, avecommunity2m14, avecommunity3m14, avecommunity4m14, avecommunity5m14, avecommunity6m14, avecommunity7m14, avecommunity8m14, avecommunity9m14, avecommunity10m14, avecommunity11m14, avecommunity12m14, avecommunity13m14, avecommunity14m14, avecommunity15m14, avecommunity1m15, avecommunity2m15, avecommunity3m15, avecommunity4m15, avecommunity5m15, avecommunity6m15, avecommunity7m15, avecommunity8m15, avecommunity9m15, avecommunity10m15, avecommunity11m15, avecommunity12m15, avecommunity13m15, avecommunity14m15, avecommunity15m15, avecommunity1defend, avecommunity2defend, avecommunity3defend, avecommunity4defend, avecommunity5defend, avecommunity6defend, avecommunity7defend, avecommunity8defend, avecommunity9defend, avecommunity10defend, avecommunity11defend, avecommunity12defend, avecommunity13defend, avecommunity14defend, avecommunity15defend, aveoneandtwo , aveoneandthree, aveoneandfour, aveoneandfive, aveoneandsix , aveoneandseven, aveoneandeight, aveoneandnine, aveoneandten , aveoneandeleven, aveoneandtwelve, aveoneandthirteen, aveoneandfourteen, aveoneandfifteen, avetwoandthree, avetwoandfour, avetwoandfive, avetwoandsix , avetwoandseven, avetwoandeight, avetwoandnine, avetwoandten , avetwoandeleven, avetwoandtwelve, avetwoandthirteen, avetwoandfourteen, avetwoandfifteen, avethreeandfour, avethreeandfive, avethreeandsix, avethreeandseven, avethreeandeight, avethreeandnine, avethreeandten, avethreeandeleven, avethreeandtwelve, avethreeandthirteen, avethreeandfourteen, avethreeandfifteen, avefourandfive, avefourandsix, avefourandseven, avefourandeight, avefourandnine, avefourandten, avefourandeleven, avefourandtwelve, avefourandthirteen, avefourandfourteen, avefourandfifteen, avefiveandsix, avefiveandseven, avefiveandeight, avefiveandnine, avefiveandten, avefiveandeleven, avefiveandtwelve, avefiveandthirteen, avefiveandfourteen, avefiveandfifteen, avesixandseven, avesixandeight, avesixandnine, avesixandten , avesixandeleven, avesixandtwelve, avesixandthirteen, avesixandfourteen, avesixandfifteen, avesevenandeight, avesevenandnine, avesevenandten, avesevenandeleven, avesevenandtwelve, avesevenandthirteen, avesevenandfourteen, avesevenandfifteen, aveeightandnine, aveeightandten, aveeightandeleven, aveeightandtwelve, aveeightandthirteen, aveeightandfourteen, aveeightandfifteen, avenineandten, avenineandeleven, avenineandtwelve, avenineandthirteen, avenineandfourteen, avenineandfifteen, avetenandeleven, avetenandtwelve, avetenandthirteen, avetenandfourteen, avetenandfifteen, aveelevenandtwelve, aveelevenandthirteen, aveelevenandfourteen, aveelevenandfifteen, avetwelveandthirteen, avetwelveandfourteen, avetwelveandfifteen, avethirteenandfourteen, avethirteenandfifteen, avefourteenandfifteen
# from app.model.simulatortwenty import avestrength1 , avenotorietyratio1, avetotalextort1, avecountextort1, avecountbenefit1, avecountpunish1, avecountsupport1, avetotalsupport1, avecountdefend1, avestrength2 , avenotorietyratio2, avetotalextort2, avecountextort2, avecountbenefit2, avecountpunish2, avecountsupport2, avetotalsupport2, avecountdefend2, avestrength3 , avenotorietyratio3, avetotalextort3, avecountextort3, avecountbenefit3, avecountpunish3, avecountsupport3, avetotalsupport3, avecountdefend3, avestrength4 , avenotorietyratio4, avetotalextort4, avecountextort4, avecountbenefit4, avecountpunish4, avecountsupport4, avetotalsupport4, avecountdefend4, avestrength5 , avenotorietyratio5, avetotalextort5, avecountextort5, avecountbenefit5, avecountpunish5, avecountsupport5, avetotalsupport5, avecountdefend5, avestrength6 , avenotorietyratio6, avetotalextort6, avecountextort6, avecountbenefit6, avecountpunish6, avecountsupport6, avetotalsupport6, avecountdefend6, avestrength7 , avenotorietyratio7, avetotalextort7, avecountextort7, avecountbenefit7, avecountpunish7, avecountsupport7, avetotalsupport7, avecountdefend7, avestrength8 , avenotorietyratio8, avetotalextort8, avecountextort8, avecountbenefit8, avecountpunish8, avecountsupport8, avetotalsupport8, avecountdefend8, avestrength9 , avenotorietyratio9, avetotalextort9, avecountextort9, avecountbenefit9, avecountpunish9, avecountsupport9, avetotalsupport9, avecountdefend9, avestrength10, avenotorietyratio10, avetotalextort10, avecountextort10, avecountbenefit10, avecountpunish10, avecountsupport10, avetotalsupport10, avecountdefend10, avestrength11, avenotorietyratio11, avetotalextort11, avecountextort11, avecountbenefit11, avecountpunish11, avecountsupport11, avetotalsupport11, avecountdefend11, avestrength12, avenotorietyratio12, avetotalextort12, avecountextort12, avecountbenefit12, avecountpunish12, avecountsupport12, avetotalsupport12, avecountdefend12, avestrength13, avenotorietyratio13, avetotalextort13, avecountextort13, avecountbenefit13, avecountpunish13, avecountsupport13, avetotalsupport13, avecountdefend13, avestrength14, avenotorietyratio14, avetotalextort14, avecountextort14, avecountbenefit14, avecountpunish14, avecountsupport14, avetotalsupport14, avecountdefend14, avestrength15, avenotorietyratio15, avetotalextort15, avecountextort15, avecountbenefit15, avecountpunish15, avecountsupport15, avetotalsupport15, avecountdefend15, avecommunity1m1, avecommunity2m1, avecommunity3m1, avecommunity4m1, avecommunity5m1, avecommunity6m1, avecommunity7m1, avecommunity8m1, avecommunity9m1, avecommunity10m1, avecommunity11m1, avecommunity12m1, avecommunity13m1, avecommunity14m1, avecommunity15m1, avecommunity1m2, avecommunity2m2, avecommunity3m2, avecommunity4m2, avecommunity5m2, avecommunity6m2, avecommunity7m2, avecommunity8m2, avecommunity9m2, avecommunity10m2, avecommunity11m2, avecommunity12m2, avecommunity13m2, avecommunity14m2, avecommunity15m2, avecommunity1m3, avecommunity2m3, avecommunity3m3, avecommunity4m3, avecommunity5m3, avecommunity6m3, avecommunity7m3, avecommunity8m3, avecommunity9m3, avecommunity10m3, avecommunity11m3, avecommunity12m3, avecommunity13m3, avecommunity14m3, avecommunity15m3, avecommunity1m4, avecommunity2m4, avecommunity3m4, avecommunity4m4, avecommunity5m4, avecommunity6m4, avecommunity7m4, avecommunity8m4, avecommunity9m4, avecommunity10m4, avecommunity11m4, avecommunity12m4, avecommunity13m4, avecommunity14m4, avecommunity15m4, avecommunity1m5, avecommunity2m5, avecommunity3m5, avecommunity4m5, avecommunity5m5, avecommunity6m5, avecommunity7m5, avecommunity8m5, avecommunity9m5, avecommunity10m5, avecommunity11m5, avecommunity12m5, avecommunity13m5, avecommunity14m5, avecommunity15m5, avecommunity1m6, avecommunity2m6, avecommunity3m6, avecommunity4m6, avecommunity5m6, avecommunity6m6, avecommunity7m6, avecommunity8m6, avecommunity9m6, avecommunity10m6, avecommunity11m6, avecommunity12m6, avecommunity13m6, avecommunity14m6, avecommunity15m6, avecommunity1m7, avecommunity2m7, avecommunity3m7, avecommunity4m7, avecommunity5m7, avecommunity6m7, avecommunity7m7, avecommunity8m7, avecommunity9m7, avecommunity10m7, avecommunity11m7, avecommunity12m7, avecommunity13m7, avecommunity14m7, avecommunity15m7, avecommunity1m8, avecommunity2m8, avecommunity3m8, avecommunity4m8, avecommunity5m8, avecommunity6m8, avecommunity7m8, avecommunity8m8, avecommunity9m8, avecommunity10m8, avecommunity11m8, avecommunity12m8, avecommunity13m8, avecommunity14m8, avecommunity15m8, avecommunity1m9, avecommunity2m9, avecommunity3m9, avecommunity4m9, avecommunity5m9, avecommunity6m9, avecommunity7m9, avecommunity8m9, avecommunity9m9, avecommunity10m9, avecommunity11m9, avecommunity12m9, avecommunity13m9, avecommunity14m9, avecommunity15m9, avecommunity1m10, avecommunity2m10, avecommunity3m10, avecommunity4m10, avecommunity5m10, avecommunity6m10, avecommunity7m10, avecommunity8m10, avecommunity9m10, avecommunity10m10, avecommunity11m10, avecommunity12m10, avecommunity13m10, avecommunity14m10, avecommunity15m10, avecommunity1m11, avecommunity2m11, avecommunity3m11, avecommunity4m11, avecommunity5m11, avecommunity6m11, avecommunity7m11, avecommunity8m11, avecommunity9m11, avecommunity10m11, avecommunity11m11, avecommunity12m11, avecommunity13m11, avecommunity14m11, avecommunity15m11, avecommunity1m12, avecommunity2m12, avecommunity3m12, avecommunity4m12, avecommunity5m12, avecommunity6m12, avecommunity7m12, avecommunity8m12, avecommunity9m12, avecommunity10m12, avecommunity11m12, avecommunity12m12, avecommunity13m12, avecommunity14m12, avecommunity15m12, avecommunity1m13, avecommunity2m13, avecommunity3m13, avecommunity4m13, avecommunity5m13, avecommunity6m13, avecommunity7m13, avecommunity8m13, avecommunity9m13, avecommunity10m13, avecommunity11m13, avecommunity12m13, avecommunity13m13, avecommunity14m13, avecommunity15m13, avecommunity1m14, avecommunity2m14, avecommunity3m14, avecommunity4m14, avecommunity5m14, avecommunity6m14, avecommunity7m14, avecommunity8m14, avecommunity9m14, avecommunity10m14, avecommunity11m14, avecommunity12m14, avecommunity13m14, avecommunity14m14, avecommunity15m14, avecommunity1m15, avecommunity2m15, avecommunity3m15, avecommunity4m15, avecommunity5m15, avecommunity6m15, avecommunity7m15, avecommunity8m15, avecommunity9m15, avecommunity10m15, avecommunity11m15, avecommunity12m15, avecommunity13m15, avecommunity14m15, avecommunity15m15, avecommunity1defend, avecommunity2defend, avecommunity3defend, avecommunity4defend, avecommunity5defend, avecommunity6defend, avecommunity7defend, avecommunity8defend, avecommunity9defend, avecommunity10defend, avecommunity11defend, avecommunity12defend, avecommunity13defend, avecommunity14defend, avecommunity15defend, aveoneandtwo , aveoneandthree, aveoneandfour, aveoneandfive, aveoneandsix , aveoneandseven, aveoneandeight, aveoneandnine, aveoneandten , aveoneandeleven, aveoneandtwelve, aveoneandthirteen, aveoneandfourteen, aveoneandfifteen, avetwoandthree, avetwoandfour, avetwoandfive, avetwoandsix , avetwoandseven, avetwoandeight, avetwoandnine, avetwoandten , avetwoandeleven, avetwoandtwelve, avetwoandthirteen, avetwoandfourteen, avetwoandfifteen, avethreeandfour, avethreeandfive, avethreeandsix, avethreeandseven, avethreeandeight, avethreeandnine, avethreeandten, avethreeandeleven, avethreeandtwelve, avethreeandthirteen, avethreeandfourteen, avethreeandfifteen, avefourandfive, avefourandsix, avefourandseven, avefourandeight, avefourandnine, avefourandten, avefourandeleven, avefourandtwelve, avefourandthirteen, avefourandfourteen, avefourandfifteen, avefiveandsix, avefiveandseven, avefiveandeight, avefiveandnine, avefiveandten, avefiveandeleven, avefiveandtwelve, avefiveandthirteen, avefiveandfourteen, avefiveandfifteen, avesixandseven, avesixandeight, avesixandnine, avesixandten , avesixandeleven, avesixandtwelve, avesixandthirteen, avesixandfourteen, avesixandfifteen, avesevenandeight, avesevenandnine, avesevenandten, avesevenandeleven, avesevenandtwelve, avesevenandthirteen, avesevenandfourteen, avesevenandfifteen, aveeightandnine, aveeightandten, aveeightandeleven, aveeightandtwelve, aveeightandthirteen, aveeightandfourteen, aveeightandfifteen, avenineandten, avenineandeleven, avenineandtwelve, avenineandthirteen, avenineandfourteen, avenineandfifteen, avetenandeleven, avetenandtwelve, avetenandthirteen, avetenandfourteen, avetenandfifteen, aveelevenandtwelve, aveelevenandthirteen, aveelevenandfourteen, aveelevenandfifteen, avetwelveandthirteen, avetwelveandfourteen, avetwelveandfifteen, avethirteenandfourteen, avethirteenandfifteen, avefourteenandfifteen
# from app.model.simulatorforty import avestrength1 , avenotorietyratio1, avetotalextort1, avecountextort1, avecountbenefit1, avecountpunish1, avecountsupport1, avetotalsupport1, avecountdefend1, avestrength2 , avenotorietyratio2, avetotalextort2, avecountextort2, avecountbenefit2, avecountpunish2, avecountsupport2, avetotalsupport2, avecountdefend2, avestrength3 , avenotorietyratio3, avetotalextort3, avecountextort3, avecountbenefit3, avecountpunish3, avecountsupport3, avetotalsupport3, avecountdefend3, avestrength4 , avenotorietyratio4, avetotalextort4, avecountextort4, avecountbenefit4, avecountpunish4, avecountsupport4, avetotalsupport4, avecountdefend4, avestrength5 , avenotorietyratio5, avetotalextort5, avecountextort5, avecountbenefit5, avecountpunish5, avecountsupport5, avetotalsupport5, avecountdefend5, avestrength6 , avenotorietyratio6, avetotalextort6, avecountextort6, avecountbenefit6, avecountpunish6, avecountsupport6, avetotalsupport6, avecountdefend6, avestrength7 , avenotorietyratio7, avetotalextort7, avecountextort7, avecountbenefit7, avecountpunish7, avecountsupport7, avetotalsupport7, avecountdefend7, avestrength8 , avenotorietyratio8, avetotalextort8, avecountextort8, avecountbenefit8, avecountpunish8, avecountsupport8, avetotalsupport8, avecountdefend8, avestrength9 , avenotorietyratio9, avetotalextort9, avecountextort9, avecountbenefit9, avecountpunish9, avecountsupport9, avetotalsupport9, avecountdefend9, avestrength10, avenotorietyratio10, avetotalextort10, avecountextort10, avecountbenefit10, avecountpunish10, avecountsupport10, avetotalsupport10, avecountdefend10, avestrength11, avenotorietyratio11, avetotalextort11, avecountextort11, avecountbenefit11, avecountpunish11, avecountsupport11, avetotalsupport11, avecountdefend11, avestrength12, avenotorietyratio12, avetotalextort12, avecountextort12, avecountbenefit12, avecountpunish12, avecountsupport12, avetotalsupport12, avecountdefend12, avestrength13, avenotorietyratio13, avetotalextort13, avecountextort13, avecountbenefit13, avecountpunish13, avecountsupport13, avetotalsupport13, avecountdefend13, avestrength14, avenotorietyratio14, avetotalextort14, avecountextort14, avecountbenefit14, avecountpunish14, avecountsupport14, avetotalsupport14, avecountdefend14, avestrength15, avenotorietyratio15, avetotalextort15, avecountextort15, avecountbenefit15, avecountpunish15, avecountsupport15, avetotalsupport15, avecountdefend15, avecommunity1m1, avecommunity2m1, avecommunity3m1, avecommunity4m1, avecommunity5m1, avecommunity6m1, avecommunity7m1, avecommunity8m1, avecommunity9m1, avecommunity10m1, avecommunity11m1, avecommunity12m1, avecommunity13m1, avecommunity14m1, avecommunity15m1, avecommunity1m2, avecommunity2m2, avecommunity3m2, avecommunity4m2, avecommunity5m2, avecommunity6m2, avecommunity7m2, avecommunity8m2, avecommunity9m2, avecommunity10m2, avecommunity11m2, avecommunity12m2, avecommunity13m2, avecommunity14m2, avecommunity15m2, avecommunity1m3, avecommunity2m3, avecommunity3m3, avecommunity4m3, avecommunity5m3, avecommunity6m3, avecommunity7m3, avecommunity8m3, avecommunity9m3, avecommunity10m3, avecommunity11m3, avecommunity12m3, avecommunity13m3, avecommunity14m3, avecommunity15m3, avecommunity1m4, avecommunity2m4, avecommunity3m4, avecommunity4m4, avecommunity5m4, avecommunity6m4, avecommunity7m4, avecommunity8m4, avecommunity9m4, avecommunity10m4, avecommunity11m4, avecommunity12m4, avecommunity13m4, avecommunity14m4, avecommunity15m4, avecommunity1m5, avecommunity2m5, avecommunity3m5, avecommunity4m5, avecommunity5m5, avecommunity6m5, avecommunity7m5, avecommunity8m5, avecommunity9m5, avecommunity10m5, avecommunity11m5, avecommunity12m5, avecommunity13m5, avecommunity14m5, avecommunity15m5, avecommunity1m6, avecommunity2m6, avecommunity3m6, avecommunity4m6, avecommunity5m6, avecommunity6m6, avecommunity7m6, avecommunity8m6, avecommunity9m6, avecommunity10m6, avecommunity11m6, avecommunity12m6, avecommunity13m6, avecommunity14m6, avecommunity15m6, avecommunity1m7, avecommunity2m7, avecommunity3m7, avecommunity4m7, avecommunity5m7, avecommunity6m7, avecommunity7m7, avecommunity8m7, avecommunity9m7, avecommunity10m7, avecommunity11m7, avecommunity12m7, avecommunity13m7, avecommunity14m7, avecommunity15m7, avecommunity1m8, avecommunity2m8, avecommunity3m8, avecommunity4m8, avecommunity5m8, avecommunity6m8, avecommunity7m8, avecommunity8m8, avecommunity9m8, avecommunity10m8, avecommunity11m8, avecommunity12m8, avecommunity13m8, avecommunity14m8, avecommunity15m8, avecommunity1m9, avecommunity2m9, avecommunity3m9, avecommunity4m9, avecommunity5m9, avecommunity6m9, avecommunity7m9, avecommunity8m9, avecommunity9m9, avecommunity10m9, avecommunity11m9, avecommunity12m9, avecommunity13m9, avecommunity14m9, avecommunity15m9, avecommunity1m10, avecommunity2m10, avecommunity3m10, avecommunity4m10, avecommunity5m10, avecommunity6m10, avecommunity7m10, avecommunity8m10, avecommunity9m10, avecommunity10m10, avecommunity11m10, avecommunity12m10, avecommunity13m10, avecommunity14m10, avecommunity15m10, avecommunity1m11, avecommunity2m11, avecommunity3m11, avecommunity4m11, avecommunity5m11, avecommunity6m11, avecommunity7m11, avecommunity8m11, avecommunity9m11, avecommunity10m11, avecommunity11m11, avecommunity12m11, avecommunity13m11, avecommunity14m11, avecommunity15m11, avecommunity1m12, avecommunity2m12, avecommunity3m12, avecommunity4m12, avecommunity5m12, avecommunity6m12, avecommunity7m12, avecommunity8m12, avecommunity9m12, avecommunity10m12, avecommunity11m12, avecommunity12m12, avecommunity13m12, avecommunity14m12, avecommunity15m12, avecommunity1m13, avecommunity2m13, avecommunity3m13, avecommunity4m13, avecommunity5m13, avecommunity6m13, avecommunity7m13, avecommunity8m13, avecommunity9m13, avecommunity10m13, avecommunity11m13, avecommunity12m13, avecommunity13m13, avecommunity14m13, avecommunity15m13, avecommunity1m14, avecommunity2m14, avecommunity3m14, avecommunity4m14, avecommunity5m14, avecommunity6m14, avecommunity7m14, avecommunity8m14, avecommunity9m14, avecommunity10m14, avecommunity11m14, avecommunity12m14, avecommunity13m14, avecommunity14m14, avecommunity15m14, avecommunity1m15, avecommunity2m15, avecommunity3m15, avecommunity4m15, avecommunity5m15, avecommunity6m15, avecommunity7m15, avecommunity8m15, avecommunity9m15, avecommunity10m15, avecommunity11m15, avecommunity12m15, avecommunity13m15, avecommunity14m15, avecommunity15m15, avecommunity1defend, avecommunity2defend, avecommunity3defend, avecommunity4defend, avecommunity5defend, avecommunity6defend, avecommunity7defend, avecommunity8defend, avecommunity9defend, avecommunity10defend, avecommunity11defend, avecommunity12defend, avecommunity13defend, avecommunity14defend, avecommunity15defend, aveoneandtwo , aveoneandthree, aveoneandfour, aveoneandfive, aveoneandsix , aveoneandseven, aveoneandeight, aveoneandnine, aveoneandten , aveoneandeleven, aveoneandtwelve, aveoneandthirteen, aveoneandfourteen, aveoneandfifteen, avetwoandthree, avetwoandfour, avetwoandfive, avetwoandsix , avetwoandseven, avetwoandeight, avetwoandnine, avetwoandten , avetwoandeleven, avetwoandtwelve, avetwoandthirteen, avetwoandfourteen, avetwoandfifteen, avethreeandfour, avethreeandfive, avethreeandsix, avethreeandseven, avethreeandeight, avethreeandnine, avethreeandten, avethreeandeleven, avethreeandtwelve, avethreeandthirteen, avethreeandfourteen, avethreeandfifteen, avefourandfive, avefourandsix, avefourandseven, avefourandeight, avefourandnine, avefourandten, avefourandeleven, avefourandtwelve, avefourandthirteen, avefourandfourteen, avefourandfifteen, avefiveandsix, avefiveandseven, avefiveandeight, avefiveandnine, avefiveandten, avefiveandeleven, avefiveandtwelve, avefiveandthirteen, avefiveandfourteen, avefiveandfifteen, avesixandseven, avesixandeight, avesixandnine, avesixandten , avesixandeleven, avesixandtwelve, avesixandthirteen, avesixandfourteen, avesixandfifteen, avesevenandeight, avesevenandnine, avesevenandten, avesevenandeleven, avesevenandtwelve, avesevenandthirteen, avesevenandfourteen, avesevenandfifteen, aveeightandnine, aveeightandten, aveeightandeleven, aveeightandtwelve, aveeightandthirteen, aveeightandfourteen, aveeightandfifteen, avenineandten, avenineandeleven, avenineandtwelve, avenineandthirteen, avenineandfourteen, avenineandfifteen, avetenandeleven, avetenandtwelve, avetenandthirteen, avetenandfourteen, avetenandfifteen, aveelevenandtwelve, aveelevenandthirteen, aveelevenandfourteen, aveelevenandfifteen, avetwelveandthirteen, avetwelveandfourteen, avetwelveandfifteen, avethirteenandfourteen, avethirteenandfifteen, avefourteenandfifteen
# from app.model.simulatorhundred import avestrength1 , avenotorietyratio1, avetotalextort1, avecountextort1, avecountbenefit1, avecountpunish1, avecountsupport1, avetotalsupport1, avecountdefend1, avestrength2 , avenotorietyratio2, avetotalextort2, avecountextort2, avecountbenefit2, avecountpunish2, avecountsupport2, avetotalsupport2, avecountdefend2, avestrength3 , avenotorietyratio3, avetotalextort3, avecountextort3, avecountbenefit3, avecountpunish3, avecountsupport3, avetotalsupport3, avecountdefend3, avestrength4 , avenotorietyratio4, avetotalextort4, avecountextort4, avecountbenefit4, avecountpunish4, avecountsupport4, avetotalsupport4, avecountdefend4, avestrength5 , avenotorietyratio5, avetotalextort5, avecountextort5, avecountbenefit5, avecountpunish5, avecountsupport5, avetotalsupport5, avecountdefend5, avestrength6 , avenotorietyratio6, avetotalextort6, avecountextort6, avecountbenefit6, avecountpunish6, avecountsupport6, avetotalsupport6, avecountdefend6, avestrength7 , avenotorietyratio7, avetotalextort7, avecountextort7, avecountbenefit7, avecountpunish7, avecountsupport7, avetotalsupport7, avecountdefend7, avestrength8 , avenotorietyratio8, avetotalextort8, avecountextort8, avecountbenefit8, avecountpunish8, avecountsupport8, avetotalsupport8, avecountdefend8, avestrength9 , avenotorietyratio9, avetotalextort9, avecountextort9, avecountbenefit9, avecountpunish9, avecountsupport9, avetotalsupport9, avecountdefend9, avestrength10, avenotorietyratio10, avetotalextort10, avecountextort10, avecountbenefit10, avecountpunish10, avecountsupport10, avetotalsupport10, avecountdefend10, avestrength11, avenotorietyratio11, avetotalextort11, avecountextort11, avecountbenefit11, avecountpunish11, avecountsupport11, avetotalsupport11, avecountdefend11, avestrength12, avenotorietyratio12, avetotalextort12, avecountextort12, avecountbenefit12, avecountpunish12, avecountsupport12, avetotalsupport12, avecountdefend12, avestrength13, avenotorietyratio13, avetotalextort13, avecountextort13, avecountbenefit13, avecountpunish13, avecountsupport13, avetotalsupport13, avecountdefend13, avestrength14, avenotorietyratio14, avetotalextort14, avecountextort14, avecountbenefit14, avecountpunish14, avecountsupport14, avetotalsupport14, avecountdefend14, avestrength15, avenotorietyratio15, avetotalextort15, avecountextort15, avecountbenefit15, avecountpunish15, avecountsupport15, avetotalsupport15, avecountdefend15, avecommunity1m1, avecommunity2m1, avecommunity3m1, avecommunity4m1, avecommunity5m1, avecommunity6m1, avecommunity7m1, avecommunity8m1, avecommunity9m1, avecommunity10m1, avecommunity11m1, avecommunity12m1, avecommunity13m1, avecommunity14m1, avecommunity15m1, avecommunity1m2, avecommunity2m2, avecommunity3m2, avecommunity4m2, avecommunity5m2, avecommunity6m2, avecommunity7m2, avecommunity8m2, avecommunity9m2, avecommunity10m2, avecommunity11m2, avecommunity12m2, avecommunity13m2, avecommunity14m2, avecommunity15m2, avecommunity1m3, avecommunity2m3, avecommunity3m3, avecommunity4m3, avecommunity5m3, avecommunity6m3, avecommunity7m3, avecommunity8m3, avecommunity9m3, avecommunity10m3, avecommunity11m3, avecommunity12m3, avecommunity13m3, avecommunity14m3, avecommunity15m3, avecommunity1m4, avecommunity2m4, avecommunity3m4, avecommunity4m4, avecommunity5m4, avecommunity6m4, avecommunity7m4, avecommunity8m4, avecommunity9m4, avecommunity10m4, avecommunity11m4, avecommunity12m4, avecommunity13m4, avecommunity14m4, avecommunity15m4, avecommunity1m5, avecommunity2m5, avecommunity3m5, avecommunity4m5, avecommunity5m5, avecommunity6m5, avecommunity7m5, avecommunity8m5, avecommunity9m5, avecommunity10m5, avecommunity11m5, avecommunity12m5, avecommunity13m5, avecommunity14m5, avecommunity15m5, avecommunity1m6, avecommunity2m6, avecommunity3m6, avecommunity4m6, avecommunity5m6, avecommunity6m6, avecommunity7m6, avecommunity8m6, avecommunity9m6, avecommunity10m6, avecommunity11m6, avecommunity12m6, avecommunity13m6, avecommunity14m6, avecommunity15m6, avecommunity1m7, avecommunity2m7, avecommunity3m7, avecommunity4m7, avecommunity5m7, avecommunity6m7, avecommunity7m7, avecommunity8m7, avecommunity9m7, avecommunity10m7, avecommunity11m7, avecommunity12m7, avecommunity13m7, avecommunity14m7, avecommunity15m7, avecommunity1m8, avecommunity2m8, avecommunity3m8, avecommunity4m8, avecommunity5m8, avecommunity6m8, avecommunity7m8, avecommunity8m8, avecommunity9m8, avecommunity10m8, avecommunity11m8, avecommunity12m8, avecommunity13m8, avecommunity14m8, avecommunity15m8, avecommunity1m9, avecommunity2m9, avecommunity3m9, avecommunity4m9, avecommunity5m9, avecommunity6m9, avecommunity7m9, avecommunity8m9, avecommunity9m9, avecommunity10m9, avecommunity11m9, avecommunity12m9, avecommunity13m9, avecommunity14m9, avecommunity15m9, avecommunity1m10, avecommunity2m10, avecommunity3m10, avecommunity4m10, avecommunity5m10, avecommunity6m10, avecommunity7m10, avecommunity8m10, avecommunity9m10, avecommunity10m10, avecommunity11m10, avecommunity12m10, avecommunity13m10, avecommunity14m10, avecommunity15m10, avecommunity1m11, avecommunity2m11, avecommunity3m11, avecommunity4m11, avecommunity5m11, avecommunity6m11, avecommunity7m11, avecommunity8m11, avecommunity9m11, avecommunity10m11, avecommunity11m11, avecommunity12m11, avecommunity13m11, avecommunity14m11, avecommunity15m11, avecommunity1m12, avecommunity2m12, avecommunity3m12, avecommunity4m12, avecommunity5m12, avecommunity6m12, avecommunity7m12, avecommunity8m12, avecommunity9m12, avecommunity10m12, avecommunity11m12, avecommunity12m12, avecommunity13m12, avecommunity14m12, avecommunity15m12, avecommunity1m13, avecommunity2m13, avecommunity3m13, avecommunity4m13, avecommunity5m13, avecommunity6m13, avecommunity7m13, avecommunity8m13, avecommunity9m13, avecommunity10m13, avecommunity11m13, avecommunity12m13, avecommunity13m13, avecommunity14m13, avecommunity15m13, avecommunity1m14, avecommunity2m14, avecommunity3m14, avecommunity4m14, avecommunity5m14, avecommunity6m14, avecommunity7m14, avecommunity8m14, avecommunity9m14, avecommunity10m14, avecommunity11m14, avecommunity12m14, avecommunity13m14, avecommunity14m14, avecommunity15m14, avecommunity1m15, avecommunity2m15, avecommunity3m15, avecommunity4m15, avecommunity5m15, avecommunity6m15, avecommunity7m15, avecommunity8m15, avecommunity9m15, avecommunity10m15, avecommunity11m15, avecommunity12m15, avecommunity13m15, avecommunity14m15, avecommunity15m15, avecommunity1defend, avecommunity2defend, avecommunity3defend, avecommunity4defend, avecommunity5defend, avecommunity6defend, avecommunity7defend, avecommunity8defend, avecommunity9defend, avecommunity10defend, avecommunity11defend, avecommunity12defend, avecommunity13defend, avecommunity14defend, avecommunity15defend, aveoneandtwo , aveoneandthree, aveoneandfour, aveoneandfive, aveoneandsix , aveoneandseven, aveoneandeight, aveoneandnine, aveoneandten , aveoneandeleven, aveoneandtwelve, aveoneandthirteen, aveoneandfourteen, aveoneandfifteen, avetwoandthree, avetwoandfour, avetwoandfive, avetwoandsix , avetwoandseven, avetwoandeight, avetwoandnine, avetwoandten , avetwoandeleven, avetwoandtwelve, avetwoandthirteen, avetwoandfourteen, avetwoandfifteen, avethreeandfour, avethreeandfive, avethreeandsix, avethreeandseven, avethreeandeight, avethreeandnine, avethreeandten, avethreeandeleven, avethreeandtwelve, avethreeandthirteen, avethreeandfourteen, avethreeandfifteen, avefourandfive, avefourandsix, avefourandseven, avefourandeight, avefourandnine, avefourandten, avefourandeleven, avefourandtwelve, avefourandthirteen, avefourandfourteen, avefourandfifteen, avefiveandsix, avefiveandseven, avefiveandeight, avefiveandnine, avefiveandten, avefiveandeleven, avefiveandtwelve, avefiveandthirteen, avefiveandfourteen, avefiveandfifteen, avesixandseven, avesixandeight, avesixandnine, avesixandten , avesixandeleven, avesixandtwelve, avesixandthirteen, avesixandfourteen, avesixandfifteen, avesevenandeight, avesevenandnine, avesevenandten, avesevenandeleven, avesevenandtwelve, avesevenandthirteen, avesevenandfourteen, avesevenandfifteen, aveeightandnine, aveeightandten, aveeightandeleven, aveeightandtwelve, aveeightandthirteen, aveeightandfourteen, aveeightandfifteen, avenineandten, avenineandeleven, avenineandtwelve, avenineandthirteen, avenineandfourteen, avenineandfifteen, avetenandeleven, avetenandtwelve, avetenandthirteen, avetenandfourteen, avetenandfifteen, aveelevenandtwelve, aveelevenandthirteen, aveelevenandfourteen, aveelevenandfifteen, avetwelveandthirteen, avetwelveandfourteen, avetwelveandfifteen, avethirteenandfourteen, avethirteenandfifteen, avefourteenandfifteen


# Graphing functions

# Generate x values
def genxvalues(list):
    x = []
    i = 1
    while i <= len(list):
        x.append(i)
        i += 1
    return x


def geninterventionvalues(startinit, interventionpoint, startpost, rounds):
    y = []
    i = 0
    while i < startinit:
        y.append(2)
        i += 1
    while i < interventionpoint:
        y.append(0)
        i += 1
    while i < startpost:
        y.append(2)
        i += 1
    while i < rounds:
        y.append(1)
        i += 1
    return y


def geninterventionstopvalues(startinit, interventionpoint, interventionpost, rounds):
    y = []
    i = 0
    while i < startinit:
        y.append(2)
        i += 1
    while i < interventionpoint:
        y.append(0)
        i += 1
    while i < interventionpost:
        y.append(2)
        i += 1
    while i < rounds:
        y.append(1)
        i += 1
    return y

x = genxvalues(avestrength1)
y = geninterventionvalues(156, 182, 208, 234)
z = geninterventionstopvalues(156, 182, 260, 286)
# Printing


# Export to Excel
# df2 = DataFrame({'rounds': x, 'intervention': y, 'avestrength1': avestrength1, 'avestrength2': avestrength2, 'avestrength3': avestrength3, 'avenotorietyratio1': avenotorietyratio1, 'avenotorietyratio2': avenotorietyratio2, 'avenotorietyratio3': avenotorietyratio3, 'avecommunity1m1': avecommunity1m1, 'avecommunity2m1': avecommunity2m1, 'avecommunity3m1': avecommunity3m1, 'avecommunity4m1': avecommunity4m1, 'avecommunity5m1': avecommunity5m1, 'avecommunity1m2': avecommunity1m2, 'avecommunity2m2': avecommunity2m2, 'avecommunity3m2': avecommunity3m2, 'avecommunity4m2': avecommunity4m2, 'avecommunity5m2': avecommunity5m2, 'avecommunity1m3': avecommunity1m3, 'avecommunity2m3': avecommunity2m3, 'avecommunity3m3': avecommunity3m3, 'avecommunity4m3': avecommunity4m3, 'avecommunity5m3': avecommunity5m3, 'aveoneandtwo': aveoneandtwo, 'aveoneandthree': aveoneandthree, 'avetwoandthree': avetwoandthree, 'avecommunity1defend': avecommunity1defend, 'avecommunity2defend': avecommunity2defend, 'avecommunity3defend': avecommunity3defend, 'avecommunity4defend': avecommunity4defend, 'avecommunity5defend': avecommunity5defend})
# df2 = df2[['rounds', 'intervention', 'avestrength1', 'avestrength2', 'avestrength3', 'avenotorietyratio1', 'avenotorietyratio2', 'avenotorietyratio3', 'avecommunity1m1', 'avecommunity2m1', 'avecommunity3m1', 'avecommunity4m1', 'avecommunity5m1', 'avecommunity1m2', 'avecommunity2m2', 'avecommunity3m2', 'avecommunity4m2', 'avecommunity5m2', 'avecommunity1m3', 'avecommunity2m3', 'avecommunity3m3', 'avecommunity4m3', 'avecommunity5m3', 'avecommunity1defend', 'avecommunity2defend', 'avecommunity3defend', 'avecommunity4defend', 'avecommunity5defend', 'aveoneandtwo', 'aveoneandthree', 'avetwoandthree']]
# df2.to_excel('data/test.xlsx', sheet_name='sheet1', index=False)

# Graphing

# fighting
plt.figure(0)
plt.plot(x, aveoneandtwo, label='oneandtwo')
plt.plot(x, aveoneandthree, label='oneandthree')
plt.plot(x, avetwoandthree, label='twoandthree')
# plt.xlim(2,50)
plt.xlabel('t')
plt.ylabel('fight prob')
plt.title("Fighting btw Militants")
plt.legend()

# defending
# plt.figure(0)
# plt.plot(x, avecountdefend1, label='militant1')
# plt.plot(x, avecountdefend2, label='militant2')
# plt.plot(x, avecountdefend3, label='militant3')
# plt.plot(x, avecountdefend4, label='militant4')
# plt.xlabel('t')
# plt.ylabel('defend count')
# plt.title("Civilians Defending")
# plt.legend()
#
# plt.figure(1)
# plt.plot(x, avecommunity1defend, label='community1')
# plt.plot(x, avecommunity2defend, label='community2')
# plt.plot(x, avecommunity3defend, label='community3')
# plt.plot(x, avecommunity4defend, label='community4')
# plt.plot(x, avecommunity5defend, label='community5')
# # plt.xlim(2,50)
# plt.xlabel('t')
# plt.ylabel('defend count')
# plt.title("Civilians Defending")
# plt.legend()

# support of militants by community
# plt.figure(2)
# plt.plot(x, avecommunity1m1, label='militant1')
# plt.plot(x, avecommunity1m2, label='militant2')
# plt.plot(x, avecommunity1m3, label='militant3')
# # plt.xlim(2,50)
# plt.xlabel('t')
# plt.ylabel('support')
# plt.title("Community1 support of militants")
# plt.legend()
#
# plt.figure(3)
# plt.plot(x, avecommunity2m1, label='militant1')
# plt.plot(x, avecommunity2m2, label='militant2')
# plt.plot(x, avecommunity2m3, label='militant3')
# # plt.xlim(2,50)
# plt.xlabel('t')
# plt.ylabel('support')
# plt.title("Community2 support of militants")
# plt.legend()
#
# plt.figure(4)
# plt.plot(x, avecommunity3m1, label='militant1')
# plt.plot(x, avecommunity3m2, label='militant2')
# plt.plot(x, avecommunity3m3, label='militant3')
# # plt.xlim(2,50)
# plt.xlabel('t')
# plt.ylabel('support')
# plt.title("Community3 support of militants")
# plt.legend()
#
# plt.figure(5)
# plt.plot(x, avecommunity4m1, label='militant1')
# plt.plot(x, avecommunity4m2, label='militant2')
# plt.plot(x, avecommunity4m3, label='militant3')
# # plt.xlim(2,50)
# plt.xlabel('t')
# plt.ylabel('support')
# plt.title("Community4 support of militants")
# plt.legend()
#
# plt.figure(6)
# plt.plot(x, avecommunity5m1, label='militant1')
# plt.plot(x, avecommunity5m2, label='militant2')
# plt.plot(x, avecommunity5m3, label='militant3')
# # plt.xlim(2,50)
# plt.xlabel('t')
# plt.ylabel('support')
# plt.title("Community5 support of militants")
# plt.legend()

# plt.figure(6)
# plt.plot(x, avecommunity6m1, label='militant1')
# plt.plot(x, avecommunity6m2, label='militant2')
# # plt.xlim(2,50)
# plt.xlabel('t')
# plt.ylabel('support')
# plt.title("Community6 support of militants")
# plt.legend()
#
# plt.figure(7)
# plt.plot(x, avecommunity7m1, label='militant1')
# plt.plot(x, avecommunity7m2, label='militant2')
# # plt.xlim(2,50)
# plt.xlabel('t')
# plt.ylabel('support')
# plt.title("Community7 support of militants")
# plt.legend()
#
# plt.figure(8)
# plt.plot(x, avecommunity8m1, label='militant1')
# plt.plot(x, avecommunity8m2, label='militant2')
# # plt.xlim(2,50)
# plt.xlabel('t')
# plt.ylabel('support')
# plt.title("Community8 support of militants")
# plt.legend()
#
# plt.figure(9)
# plt.plot(x, avecommunity9m1, label='militant1')
# plt.plot(x, avecommunity9m2, label='militant2')
# # plt.xlim(2,50)
# plt.xlabel('t')
# plt.ylabel('support')
# plt.title("Community9 support of militants")
# plt.legend()
#
# plt.figure(10)
# plt.plot(x, avecommunity10m1, label='militant1')
# plt.plot(x, avecommunity10m2, label='militant2')
# # plt.xlim(2,50)
# plt.xlabel('t')
# plt.ylabel('support')
# plt.title("Community10 support of militants")
# plt.legend()
#
# plt.figure(6)
# plt.plot(x, avecommunity4m1, label='militant1')
# plt.plot(x, avecommunity4m2, label='militant2')
# plt.plot(x, avecommunity4m3, label='militant3')
# plt.plot(x, avecommunity4m4, label='militant4')
# # plt.xlim(2,50)
# plt.xlabel('t')
# plt.ylabel('support')
# plt.title("Community4 support of militants")
# plt.legend()
#
# support of communities by militant
# plt.figure(1)
# plt.plot(x, avecommunity1m3, label='community1')
# plt.plot(x, avecommunity2m3, label='community2')
# plt.plot(x, avecommunity3m3, label='community3')
# plt.plot(x, avecommunity4m3, label='community4')
# # plt.xlim(2,50)
# plt.xlabel('t')
# plt.ylabel('support')
# plt.title("Militant3 communities support")
# plt.legend()

# plt.figure(2)
# plt.plot(x, avecommunity1m2, label='community1')
# plt.plot(x, avecommunity2m2, label='community2')
# plt.plot(x, avecommunity3m2, label='community3')
# plt.xlabel('t')
# plt.ylabel('support')
# plt.title("Militant2 communities support")
# plt.legend()

# plt.figure(3)
# plt.plot(x, avecommunity1m3, label='community1')
# plt.plot(x, avecommunity2m3, label='community2')
# plt.plot(x, avecommunity3m3, label='community3')
# plt.xlabel('t')
# plt.ylabel('support')
# plt.title("Militant3 communities support")
# plt.legend()

# notorieties
# plt.figure(2)
# plt.plot(x, avenotorietyratio1, label='militant1')
# plt.plot(x, avenotorietyratio2, label='militant2')
# plt.plot(x, avenotorietyratio3, label='militant3')
# # plt.xlim(2,50)
# plt.xlabel('t')
# plt.ylabel('notoriety')
# plt.title("Militant Notorieties")
# plt.legend()
#
# punishment
# plt.figure(0)
# plt.plot(x, avecountpunish1, label='militant1')
# plt.plot(x, avecountpunish2, label='militant2')
# plt.plot(x, avecountpunish3, label='militant3')
# plt.plot(x, avecountpunish4, label='militant4')
# # plt.xlim(2,50)
# plt.xlabel('t')
# plt.ylabel('punish')
# plt.title("Militant Punishing")
# plt.legend()
#

print(avestrength1)
plt.show()

def fetchoutput():
    print(avestrength1)
    # strength
    # plt.figure(0)
    # plt.plot(x, avestrength1, label='militant1')
    # plt.plot(x, avestrength2, label='militant2')
    # plt.plot(x, avestrength3, label='militant3')
    # # plt.xlim(2,50)
    # plt.xlabel('t')
    # plt.ylabel('strength')
    # plt.title("Militant Strength")
    # plt.legend()
    #
    # plt.show()
