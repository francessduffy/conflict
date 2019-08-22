from app.model.main import envoutput, militantlist, militantoutputlist, rounds
from app.model.initconditions import communitylist, percentage

# Making x values
x = []
i = 1
while i <= rounds:
    x.append(i)
    i += 1

# Matrices of fighting results
oneandtwo = []
oneandthree = []
twoandthree = []
oneandfour = []
oneandfive = []
oneandsix = []
oneandseven = []
oneandeight = []
oneandnine = []
oneandten = []
oneandeleven = []
oneandtwelve = []
oneandthirteen = []
oneandfourteen = []
oneandfifteen = []
twoandfour = []
twoandfive = []
twoandsix = []
twoandseven = []
twoandeight = []
twoandnine = []
twoandten = []
twoandeleven = []
twoandtwelve = []
twoandthirteen = []
twoandfourteen = []
twoandfifteen = []
threeandfour = []
threeandfive = []
threeandsix = []
threeandseven = []
threeandeight = []
threeandnine = []
threeandten = []
threeandeleven = []
threeandtwelve = []
threeandthirteen = []
threeandfourteen = []
threeandfifteen = []
fourandfive = []
fourandsix = []
fourandseven = []
fourandeight = []
fourandnine = []
fourandten = []
fourandeleven = []
fourandtwelve = []
fourandthirteen = []
fourandfourteen = []
fourandfifteen = []
fiveandsix = []
fiveandseven = []
fiveandeight = []
fiveandnine = []
fiveandten = []
fiveandeleven = []
fiveandtwelve = []
fiveandthirteen = []
fiveandfourteen = []
fiveandfifteen = []
sixandseven = []
sixandeight = []
sixandnine = []
sixandten = []
sixandeleven = []
sixandtwelve = []
sixandthirteen = []
sixandfourteen = []
sixandfifteen = []
sevenandeight = []
sevenandnine = []
sevenandten = []
sevenandeleven = []
sevenandtwelve = []
sevenandthirteen = []
sevenandfourteen = []
sevenandfifteen = []
eightandnine = []
eightandten = []
eightandeleven = []
eightandtwelve = []
eightandthirteen = []
eightandfourteen = []
eightandfifteen = []
nineandten = []
nineandeleven = []
nineandtwelve = []
nineandthirteen = []
nineandfourteen = []
nineandfifteen = []
tenandeleven = []
tenandtwelve = []
tenandthirteen = []
tenandfourteen = []
tenandfifteen = []
elevenandtwelve = []
elevenandthirteen = []
elevenandfourteen = []
elevenandfifteen = []
twelveandthirteen = []
twelveandfourteen = []
twelveandfifteen = []
thirteenandfourteen = []
thirteenandfifteen = []
fourteenandfifteen = []

community1defend = []
community2defend = []
community3defend = []
community4defend = []
community5defend = []
community6defend = []
community7defend = []
community8defend = []
community9defend = []
community10defend = []
community11defend = []
community12defend = []
community13defend = []
community14defend = []
community15defend = []

for i in envoutput.defendlist:
    for j in i:
        if j[0] == 'community1':
            community1defend.append(j[1])
        elif j[0] == 'community2':
            community2defend.append(j[1])
        elif j[0] == 'community3':
            community3defend.append(j[1])
        elif j[0] == 'community4':
            community4defend.append(j[1])
        elif j[0] == 'community5':
            community5defend.append(j[1])
        elif j[0] == 'community6':
            community6defend.append(j[1])
        elif j[0] == 'community7':
            community7defend.append(j[1])
        elif j[0] == 'community8':
            community8defend.append(j[1])
        elif j[0] == 'community9':
            community9defend.append(j[1])
        elif j[0] == 'community10':
            community10defend.append(j[1])
        elif j[0] == 'community11':
            community11defend.append(j[1])
        elif j[0] == 'community12':
            community12defend.append(j[1])
        elif j[0] == 'community13':
            community13defend.append(j[1])
        elif j[0] == 'community14':
            community14defend.append(j[1])
        elif j[0] == 'community15':
            community15defend.append(j[1])


for i in envoutput.fightlist:
    for j in i:
        if j.name1 == 'militant1' and j.name2 == 'militant2':
            if j.sameregion is True:
                oneandtwo.append(j.ratio)
            else:
                oneandtwo.append(0)
        if len(militantlist) > 2:
            if j.name1 == 'militant1' and j.name2 == 'militant3':
                if j.sameregion is True:
                    oneandthree.append(j.ratio)
                else:
                    oneandthree.append(0)
            if j.name1 == 'militant2' and j.name2 == 'militant3':
                if j.sameregion is True:
                    twoandthree.append(j.ratio)
                else:
                    twoandthree.append(0)
        if len(militantlist) > 3:
            if j.name1 == 'militant1' and j.name2 == 'militant4':
                if j.sameregion is True:
                    oneandfour.append(j.ratio)
                else:
                    oneandfour.append(0)
            if j.name1 == 'militant2' and j.name2 == 'militant4':
                if j.sameregion is True:
                    twoandfour.append(j.ratio)
                else:
                    twoandfour.append(0)
            if j.name1 == 'militant3' and j.name2 == 'militant4':
                if j.sameregion is True:
                    threeandfour.append(j.ratio)
                else:
                    threeandfour.append(0)
        if len(militantlist) > 4:
            if j.name1 == 'militant1' and j.name2 == 'militant5':
                if j.sameregion is True:
                    oneandfive.append(j.ratio)
                else:
                    oneandfive.append(0)
            if j.name1 == 'militant2' and j.name2 == 'militant5':
                if j.sameregion is True:
                    twoandfive.append(j.ratio)
                else:
                    twoandfive.append(0)
            if j.name1 == 'militant3' and j.name2 == 'militant5':
                if j.sameregion is True:
                    threeandfive.append(j.ratio)
                else:
                    threeandfive.append(0)
            if j.name1 == 'militant4' and j.name2 == 'militant5':
                if j.sameregion is True:
                    fourandfive.append(j.ratio)
                else:
                    fourandfive.append(0)
        if len(militantlist) > 5:
            if j.name1 == 'militant1' and j.name2 == 'militant6':
                if j.sameregion is True:
                    oneandsix.append(j.ratio)
                    oneandsix.append(0)
            if j.name1 == 'militant2' and j.name2 == 'militant6':
                if j.sameregion is True:
                    twoandsix.append(j.ratio)
                    twoandsix.append(0)
            if j.name1 == 'militant3' and j.name2 == 'militant6':
                if j.sameregion is True:
                    threeandsix.append(j.ratio)
                    threeandsix.append(0)
            if j.name1 == 'militant4' and j.name2 == 'militant6':
                if j.sameregion is True:
                    fourandsix.append(j.ratio)
                    fourandsix.append(0)
            if j.name1 == 'militant5' and j.name2 == 'militant6':
                if j.sameregion is True:
                    fiveandsix.append(j.ratio)
                    fiveandsix.append(0)
        if len(militantlist) > 6:
            if j.name1 == 'militant1' and j.name2 == 'militant7':
                if j.sameregion is True:
                    oneandseven.append(j.ratio)
                else:
                    oneandseven.append(0)
            if j.name1 == 'militant2' and j.name2 == 'militant7':
                if j.sameregion is True:
                    twoandseven.append(j.ratio)
                else:
                    twoandseven.append(0)
            if j.name1 == 'militant3' and j.name2 == 'militant7':
                if j.sameregion is True:
                    threeandseven.append(j.ratio)
                else:
                    threeandseven.append(0)
            if j.name1 == 'militant4' and j.name2 == 'militant7':
                if j.sameregion is True:
                    fourandseven.append(j.ratio)
                else:
                    fourandseven.append(0)
            if j.name1 == 'militant5' and j.name2 == 'militant7':
                if j.sameregion is True:
                    fiveandseven.append(j.ratio)
                else:
                    fiveandseven.append(0)
            if j.name1 == 'militant6' and j.name2 == 'militant7':
                if j.sameregion is True:
                    sixandseven.append(j.ratio)
                else:
                    sixandseven.append(0)
        if len(militantlist) > 7:
            if j.name1 == 'militant1' and j.name2 == 'militant8':
                if j.sameregion is True:
                    oneandeight.append(j.ratio)
                else:
                    oneandeight.append(0)
            if j.name1 == 'militant2' and j.name2 == 'militant8':
                if j.sameregion is True:
                    twoandeight.append(j.ratio)
                else:
                    twoandeight.append(0)
            if j.name1 == 'militant3' and j.name2 == 'militant8':
                if j.sameregion is True:
                    threeandeight.append(j.ratio)
                else:
                    threeandeight.append(0)
            if j.name1 == 'militant4' and j.name2 == 'militant8':
                if j.sameregion is True:
                    fourandeight.append(j.ratio)
                else:
                    fourandeight.append(0)
            if j.name1 == 'militant5' and j.name2 == 'militant8':
                if j.sameregion is True:
                    fiveandeight.append(j.ratio)
                else:
                    fiveandeight.append(0)
            if j.name1 == 'militant6' and j.name2 == 'militant8':
                if j.sameregion is True:
                    sixandeight.append(j.ratio)
                else:
                    sixandeight.append(0)
            if j.name1 == 'militant7' and j.name2 == 'militant8':
                if j.sameregion is True:
                    sevenandeight.append(j.ratio)
                else:
                    sevenandeight.append(0)
        if len(militantlist) > 8:
            if j.name1 == 'militant1' and j.name2 == 'militant9':
                if j.sameregion is True:
                    oneandnine.append(j.ratio)
                else:
                    oneandnine.append(0)
            if j.name1 == 'militant2' and j.name2 == 'militant9':
                if j.sameregion is True:
                    twoandnine.append(j.ratio)
                else:
                    twoandnine.append(0)
            if j.name1 == 'militant3' and j.name2 == 'militant9':
                if j.sameregion is True:
                    threeandnine.append(j.ratio)
                else:
                    threeandnine.append(0)
            if j.name1 == 'militant4' and j.name2 == 'militant9':
                if j.sameregion is True:
                    fourandnine.append(j.ratio)
                else:
                    fourandnine.append(0)
            if j.name1 == 'militant5' and j.name2 == 'militant9':
                if j.sameregion is True:
                    fiveandnine.append(j.ratio)
                else:
                    fiveandnine.append(0)
            if j.name1 == 'militant6' and j.name2 == 'militant9':
                if j.sameregion is True:
                    sixandnine.append(j.ratio)
                else:
                    sixandnine.append(0)
            if j.name1 == 'militant7' and j.name2 == 'militant9':
                if j.sameregion is True:
                    sevenandnine.append(j.ratio)
                else:
                    sevenandnine.append(0)
            if j.name1 == 'militant8' and j.name2 == 'militant9':
                if j.sameregion is True:
                    eightandnine.append(j.ratio)
                else:
                    eightandnine.append(0)
        if len(militantlist) > 9:
            if j.name1 == 'militant1' and j.name2 == 'militant10':
                if j.sameregion is True:
                    oneandten.append(j.ratio)
                else:
                    oneandten.append(0)
            if j.name1 == 'militant2' and j.name2 == 'militant10':
                if j.sameregion is True:
                    twoandten.append(j.ratio)
                else:
                    twoandten.append(0)
            if j.name1 == 'militant3' and j.name2 == 'militant10':
                if j.sameregion is True:
                    threeandten.append(j.ratio)
                else:
                    threeandten.append(0)
            if j.name1 == 'militant4' and j.name2 == 'militant10':
                if j.sameregion is True:
                    fourandten.append(j.ratio)
                else:
                    fourandten.append(0)
            if j.name1 == 'militant5' and j.name2 == 'militant10':
                if j.sameregion is True:
                    fiveandten.append(j.ratio)
                else:
                    fiveandten.append(0)
            if j.name1 == 'militant6' and j.name2 == 'militant10':
                if j.sameregion is True:
                    sixandten.append(j.ratio)
                else:
                    sixandten.append(0)
            if j.name1 == 'militant7' and j.name2 == 'militant10':
                if j.sameregion is True:
                    sevenandten.append(j.ratio)
                else:
                    sevenandten.append(0)
            if j.name1 == 'militant8' and j.name2 == 'militant10':
                if j.sameregion is True:
                    eightandten.append(j.ratio)
                else:
                    eightandten.append(0)
            if j.name1 == 'militant9' and j.name2 == 'militant10':
                if j.sameregion is True:
                    nineandten.append(j.ratio)
                else:
                    nineandten.append(0)
        if len(militantlist) > 10:
            if j.name1 == 'militant1' and j.name2 == 'militant11':
                if j.sameregion is True:
                    oneandeleven.append(j.ratio)
                else:
                    oneandeleven.append(0)
            if j.name1 == 'militant2' and j.name2 == 'militant11':
                if j.sameregion is True:
                    twoandeleven.append(j.ratio)
                else:
                    twoandeleven.append(0)
            if j.name1 == 'militant3' and j.name2 == 'militant11':
                if j.sameregion is True:
                    threeandeleven.append(j.ratio)
                else:
                    threeandeleven.append(0)
            if j.name1 == 'militant4' and j.name2 == 'militant11':
                if j.sameregion is True:
                    fourandeleven.append(j.ratio)
                else:
                    fourandeleven.append(0)
            if j.name1 == 'militant5' and j.name2 == 'militant11':
                if j.sameregion is True:
                    fiveandeleven.append(j.ratio)
                else:
                    fiveandeleven.append(0)
            if j.name1 == 'militant6' and j.name2 == 'militant11':
                if j.sameregion is True:
                    sixandeleven.append(j.ratio)
                else:
                    sixandeleven.append(0)
            if j.name1 == 'militant7' and j.name2 == 'militant11':
                if j.sameregion is True:
                    sevenandeleven.append(j.ratio)
                else:
                    sevenandeleven.append(0)
            if j.name1 == 'militant8' and j.name2 == 'militant11':
                if j.sameregion is True:
                    eightandeleven.append(j.ratio)
                else:
                    eightandeleven.append(0)
            if j.name1 == 'militant9' and j.name2 == 'militant11':
                if j.sameregion is True:
                    nineandeleven.append(j.ratio)
                else:
                    nineandeleven.append(0)
            if j.name1 == 'militant10' and j.name2 == 'militant11':
                if j.sameregion is True:
                    tenandeleven.append(j.ratio)
                else:
                    tenandeleven.append(0)
        if len(militantlist) > 11:
            if j.name1 == 'militant1' and j.name2 == 'militant12':
                if j.sameregion is True:
                    oneandtwelve.append(j.ratio)
                else:
                    oneandtwelve.append(0)
            if j.name1 == 'militant2' and j.name2 == 'militant12':
                if j.sameregion is True:
                    twoandtwelve.append(j.ratio)
                else:
                    twoandtwelve.append(0)
            if j.name1 == 'militant3' and j.name2 == 'militant12':
                if j.sameregion is True:
                    threeandtwelve.append(j.ratio)
                else:
                    threeandtwelve.append(0)
            if j.name1 == 'militant4' and j.name2 == 'militant12':
                if j.sameregion is True:
                    fourandtwelve.append(j.ratio)
                else:
                    fourandtwelve.append(0)
            if j.name1 == 'militant5' and j.name2 == 'militant12':
                if j.sameregion is True:
                    fiveandtwelve.append(j.ratio)
                else:
                    fiveandtwelve.append(0)
            if j.name1 == 'militant6' and j.name2 == 'militant12':
                if j.sameregion is True:
                    sixandtwelve.append(j.ratio)
                else:
                    sixandtwelve.append(0)
            if j.name1 == 'militant7' and j.name2 == 'militant12':
                if j.sameregion is True:
                    sevenandtwelve.append(j.ratio)
                else:
                    sevenandtwelve.append(0)
            if j.name1 == 'militant8' and j.name2 == 'militant12':
                if j.sameregion is True:
                    eightandtwelve.append(j.ratio)
                else:
                    eightandtwelve.append(0)
            if j.name1 == 'militant9' and j.name2 == 'militant12':
                if j.sameregion is True:
                    nineandtwelve.append(j.ratio)
                else:
                    nineandtwelve.append(0)
            if j.name1 == 'militant10' and j.name2 == 'militant12':
                if j.sameregion is True:
                    tenandtwelve.append(j.ratio)
                else:
                    tenandtwelve.append(0)
            if j.name1 == 'militant11' and j.name2 == 'militant12':
                if j.sameregion is True:
                    elevenandtwelve.append(j.ratio)
                else:
                    elevenandtwelve.append(0)
        if len(militantlist) > 12:
            if j.name1 == 'militant1' and j.name2 == 'militant13':
                if j.sameregion is True:
                    oneandthirteen.append(j.ratio)
                else:
                    oneandthirteen.append(0)
            if j.name1 == 'militant2' and j.name2 == 'militant13':
                if j.sameregion is True:
                    twoandthirteen.append(j.ratio)
                else:
                    twoandthirteen.append(0)
            if j.name1 == 'militant3' and j.name2 == 'militant13':
                if j.sameregion is True:
                    threeandthirteen.append(j.ratio)
                else:
                    threeandthirteen.append(0)
            if j.name1 == 'militant4' and j.name2 == 'militant13':
                if j.sameregion is True:
                    fourandthirteen.append(j.ratio)
                else:
                    fourandthirteen.append(0)
            if j.name1 == 'militant5' and j.name2 == 'militant13':
                if j.sameregion is True:
                    fiveandthirteen.append(j.ratio)
                else:
                    fiveandthirteen.append(0)
            if j.name1 == 'militant6' and j.name2 == 'militant13':
                if j.sameregion is True:
                    sixandthirteen.append(j.ratio)
                else:
                    sixandthirteen.append(0)
            if j.name1 == 'militant7' and j.name2 == 'militant13':
                if j.sameregion is True:
                    sevenandthirteen.append(j.ratio)
                else:
                    sevenandthirteen.append(0)
            if j.name1 == 'militant8' and j.name2 == 'militant13':
                if j.sameregion is True:
                    eightandthirteen.append(j.ratio)
                else:
                    eightandthirteen.append(0)
            if j.name1 == 'militant9' and j.name2 == 'militant13':
                if j.sameregion is True:
                    nineandthirteen.append(j.ratio)
                else:
                    nineandthirteen.append(0)
            if j.name1 == 'militant10' and j.name2 == 'militant13':
                if j.sameregion is True:
                    tenandthirteen.append(j.ratio)
                else:
                    tenandthirteen.append(0)
            if j.name1 == 'militant11' and j.name2 == 'militant13':
                if j.sameregion is True:
                    elevenandthirteen.append(j.ratio)
                else:
                    elevenandthirteen.append(0)
            if j.name1 == 'militant12' and j.name2 == 'militant13':
                if j.sameregion is True:
                    twelveandthirteen.append(j.ratio)
                else:
                    twelveandthirteen.append(0)
        if len(militantlist) > 13:
            if j.name1 == 'militant1' and j.name2 == 'militant14':
                if j.sameregion is True:
                    oneandfourteen.append(j.ratio)
                else:
                    oneandfourteen.append(0)
            if j.name1 == 'militant2' and j.name2 == 'militant14':
                if j.sameregion is True:
                    twoandfourteen.append(j.ratio)
                else:
                    twoandfourteen.append(0)
            if j.name1 == 'militant3' and j.name2 == 'militant14':
                if j.sameregion is True:
                    threeandfourteen.append(j.ratio)
                else:
                    threeandfourteen.append(0)
            if j.name1 == 'militant4' and j.name2 == 'militant14':
                if j.sameregion is True:
                    fourandfourteen.append(j.ratio)
                else:
                    fourandfourteen.append(0)
            if j.name1 == 'militant5' and j.name2 == 'militant14':
                if j.sameregion is True:
                    fiveandfourteen.append(j.ratio)
                else:
                    fiveandfourteen.append(0)
            if j.name1 == 'militant6' and j.name2 == 'militant14':
                if j.sameregion is True:
                    sixandfourteen.append(j.ratio)
                else:
                    sixandfourteen.append(0)
            if j.name1 == 'militant7' and j.name2 == 'militant14':
                if j.sameregion is True:
                    sevenandfourteen.append(j.ratio)
                else:
                    sevenandfourteen.append(0)
            if j.name1 == 'militant8' and j.name2 == 'militant14':
                if j.sameregion is True:
                    eightandfourteen.append(j.ratio)
                else:
                    eightandfourteen.append(0)
            if j.name1 == 'militant9' and j.name2 == 'militant14':
                if j.sameregion is True:
                    nineandfourteen.append(j.ratio)
                else:
                    nineandfourteen.append(0)
            if j.name1 == 'militant10' and j.name2 == 'militant14':
                if j.sameregion is True:
                    tenandfourteen.append(j.ratio)
                else:
                    tenandfourteen.append(0)
            if j.name1 == 'militant11' and j.name2 == 'militant14':
                if j.sameregion is True:
                    elevenandfourteen.append(j.ratio)
                else:
                    elevenandfourteen.append(0)
            if j.name1 == 'militant12' and j.name2 == 'militant14':
                if j.sameregion is True:
                    twelveandfourteen.append(j.ratio)
                else:
                    twelveandfourteen.append(0)
            if j.name1 == 'militant13' and j.name2 == 'militant14':
                if j.sameregion is True:
                    thirteenandfourteen.append(j.ratio)
                else:
                    thirteenandfourteen.append(0)
        if len(militantlist) > 14:
            if j.name1 == 'militant1' and j.name2 == 'militant15':
                if j.sameregion is True:
                    oneandfifteen.append(j.ratio)
                else:
                    oneandfifteen.append(0)
            if j.name1 == 'militant2' and j.name2 == 'militant15':
                if j.sameregion is True:
                    twoandfifteen.append(j.ratio)
                else:
                    twoandfifteen.append(0)
            if j.name1 == 'militant3' and j.name2 == 'militant15':
                if j.sameregion is True:
                    threeandfifteen.append(j.ratio)
                else:
                    threeandfifteen.append(0)
            if j.name1 == 'militant4' and j.name2 == 'militant15':
                if j.sameregion is True:
                    fourandfifteen.append(j.ratio)
                else:
                    fourandfifteen.append(0)
            if j.name1 == 'militant5' and j.name2 == 'militant15':
                if j.sameregion is True:
                    fiveandfifteen.append(j.ratio)
                else:
                    fiveandfifteen.append(0)
            if j.name1 == 'militant6' and j.name2 == 'militant15':
                if j.sameregion is True:
                    sixandfifteen.append(j.ratio)
                else:
                    sixandfifteen.append(0)
            if j.name1 == 'militant7' and j.name2 == 'militant15':
                if j.sameregion is True:
                    sevenandfifteen.append(j.ratio)
                else:
                    sevenandfifteen.append(0)
            if j.name1 == 'militant8' and j.name2 == 'militant15':
                if j.sameregion is True:
                    eightandfifteen.append(j.ratio)
                else:
                    eightandfifteen.append(0)
            if j.name1 == 'militant9' and j.name2 == 'militant15':
                if j.sameregion is True:
                    nineandfifteen.append(j.ratio)
                else:
                    nineandfifteen.append(0)
            if j.name1 == 'militant10' and j.name2 == 'militant15':
                if j.sameregion is True:
                    tenandfifteen.append(j.ratio)
                else:
                    tenandfifteen.append(0)
            if j.name1 == 'militant11' and j.name2 == 'militant15':
                if j.sameregion is True:
                    elevenandfifteen.append(j.ratio)
                else:
                    elevenandfifteen.append(0)
            if j.name1 == 'militant12' and j.name2 == 'militant15':
                if j.sameregion is True:
                    twelveandfifteen.append(j.ratio)
                else:
                    twelveandfifteen.append(0)
            if j.name1 == 'militant13' and j.name2 == 'militant15':
                if j.sameregion is True:
                    thirteenandfifteen.append(j.ratio)
                else:
                    thirteenandfifteen.append(0)
            if j.name1 == 'militant14' and j.name2 == 'militant15':
                if j.sameregion is True:
                    fourteenandfifteen.append(j.ratio)
                else:
                    fourteenandfifteen.append(0)

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


for m in militantlist:
    for i in militantoutputlist[m.index].communitysupport:
        for j in communitylist:
            counter = 0
            for k in i:
                if k[0] == j.name:
                    counter = 1
                    if percentage == False:
                        if j.reference == 'community1':
                            if m.index == 0:
                                community1m1.append(k[1])
                            elif m.index == 1:
                                community1m2.append(k[1])
                            elif m.index == 2:
                                community1m3.append(k[1])
                            elif m.index == 3:
                                community1m4.append(k[1])
                            elif m.index == 4:
                                community1m5.append(k[1])
                            elif m.index == 5:
                                community1m6.append(k[1])
                            elif m.index == 6:
                                community1m7.append(k[1])
                            elif m.index == 7:
                                community1m8.append(k[1])
                            elif m.index == 8:
                                community1m9.append(k[1])
                            elif m.index == 9:
                                community1m10.append(k[1])
                            elif m.index == 10:
                                community1m11.append(k[1])
                            elif m.index == 11:
                                community1m12.append(k[1])
                            elif m.index == 12:
                                community1m13.append(k[1])
                            elif m.index == 13:
                                community1m14.append(k[1])
                            elif m.index == 14:
                                community1m15.append(k[1])
                        if j.reference == 'community2':
                            if m.index == 0:
                                community2m1.append(k[1])
                            elif m.index == 1:
                                community2m2.append(k[1])
                            elif m.index == 2:
                                community2m3.append(k[1])
                            elif m.index == 3:
                                community2m4.append(k[1])
                            elif m.index == 4:
                                community2m5.append(k[1])
                            elif m.index == 5:
                                community2m6.append(k[1])
                            elif m.index == 6:
                                community2m7.append(k[1])
                            elif m.index == 7:
                                community2m8.append(k[1])
                            elif m.index == 8:
                                community2m9.append(k[1])
                            elif m.index == 9:
                                community2m10.append(k[1])
                            elif m.index == 10:
                                community2m11.append(k[1])
                            elif m.index == 11:
                                community2m12.append(k[1])
                            elif m.index == 12:
                                community2m13.append(k[1])
                            elif m.index == 13:
                                community2m14.append(k[1])
                            elif m.index == 14:
                                community2m15.append(k[1])
                        if j.reference == 'community3':
                            if m.index == 0:
                                community3m1.append(k[1])
                            elif m.index == 1:
                                community3m2.append(k[1])
                            elif m.index == 2:
                                community3m3.append(k[1])
                            elif m.index == 3:
                                community3m4.append(k[1])
                            elif m.index == 4:
                                community3m5.append(k[1])
                            elif m.index == 5:
                                community3m6.append(k[1])
                            elif m.index == 6:
                                community3m7.append(k[1])
                            elif m.index == 7:
                                community3m8.append(k[1])
                            elif m.index == 8:
                                community3m9.append(k[1])
                            elif m.index == 9:
                                community3m10.append(k[1])
                            elif m.index == 10:
                                community3m11.append(k[1])
                            elif m.index == 11:
                                community3m12.append(k[1])
                            elif m.index == 12:
                                community3m13.append(k[1])
                            elif m.index == 13:
                                community3m14.append(k[1])
                            elif m.index == 14:
                                community3m15.append(k[1])
                        if j.reference == 'community4':
                            if m.index == 0:
                                community4m1.append(k[1])
                            elif m.index == 1:
                                community4m2.append(k[1])
                            elif m.index == 2:
                                community4m3.append(k[1])
                            elif m.index == 3:
                                community4m4.append(k[1])
                            elif m.index == 4:
                                community4m5.append(k[1])
                            elif m.index == 5:
                                community4m6.append(k[1])
                            elif m.index == 6:
                                community4m7.append(k[1])
                            elif m.index == 7:
                                community4m8.append(k[1])
                            elif m.index == 8:
                                community4m9.append(k[1])
                            elif m.index == 9:
                                community4m10.append(k[1])
                            elif m.index == 10:
                                community4m11.append(k[1])
                            elif m.index == 11:
                                community4m12.append(k[1])
                            elif m.index == 12:
                                community4m13.append(k[1])
                            elif m.index == 13:
                                community4m14.append(k[1])
                            elif m.index == 14:
                                community4m15.append(k[1])
                        if j.reference == 'community5':
                            if m.index == 0:
                                community5m1.append(k[1])
                            elif m.index == 1:
                                community5m2.append(k[1])
                            elif m.index == 2:
                                community5m3.append(k[1])
                            elif m.index == 3:
                                community5m4.append(k[1])
                            elif m.index == 4:
                                community5m5.append(k[1])
                            elif m.index == 5:
                                community5m6.append(k[1])
                            elif m.index == 6:
                                community5m7.append(k[1])
                            elif m.index == 7:
                                community5m8.append(k[1])
                            elif m.index == 8:
                                community5m9.append(k[1])
                            elif m.index == 9:
                                community5m10.append(k[1])
                            elif m.index == 10:
                                community5m11.append(k[1])
                            elif m.index == 11:
                                community5m12.append(k[1])
                            elif m.index == 12:
                                community5m13.append(k[1])
                            elif m.index == 13:
                                community5m14.append(k[1])
                            elif m.index == 14:
                                community5m15.append(k[1])
                        if j.reference == 'community6':
                            if m.index == 0:
                                community6m1.append(k[1])
                            elif m.index == 1:
                                community6m2.append(k[1])
                            elif m.index == 2:
                                community6m3.append(k[1])
                            elif m.index == 3:
                                community6m4.append(k[1])
                            elif m.index == 4:
                                community6m5.append(k[1])
                            elif m.index == 5:
                                community6m6.append(k[1])
                            elif m.index == 6:
                                community6m7.append(k[1])
                            elif m.index == 7:
                                community6m8.append(k[1])
                            elif m.index == 8:
                                community6m9.append(k[1])
                            elif m.index == 9:
                                community6m10.append(k[1])
                            elif m.index == 10:
                                community6m11.append(k[1])
                            elif m.index == 11:
                                community6m12.append(k[1])
                            elif m.index == 12:
                                community6m13.append(k[1])
                            elif m.index == 13:
                                community6m14.append(k[1])
                            elif m.index == 14:
                                community6m15.append(k[1])
                        if j.reference == 'community7':
                            if m.index == 0:
                                community7m1.append(k[1])
                            elif m.index == 1:
                                community7m2.append(k[1])
                            elif m.index == 2:
                                community7m3.append(k[1])
                            elif m.index == 3:
                                community7m4.append(k[1])
                            elif m.index == 4:
                                community7m5.append(k[1])
                            elif m.index == 5:
                                community7m6.append(k[1])
                            elif m.index == 6:
                                community7m7.append(k[1])
                            elif m.index == 7:
                                community7m8.append(k[1])
                            elif m.index == 8:
                                community7m9.append(k[1])
                            elif m.index == 9:
                                community7m10.append(k[1])
                            elif m.index == 10:
                                community7m11.append(k[1])
                            elif m.index == 11:
                                community7m12.append(k[1])
                            elif m.index == 12:
                                community7m13.append(k[1])
                            elif m.index == 13:
                                community7m14.append(k[1])
                            elif m.index == 14:
                                community7m15.append(k[1])
                        if j.reference == 'community8':
                            if m.index == 0:
                                community8m1.append(k[1])
                            elif m.index == 1:
                                community8m2.append(k[1])
                            elif m.index == 2:
                                community8m3.append(k[1])
                            elif m.index == 3:
                                community8m4.append(k[1])
                            elif m.index == 4:
                                community8m5.append(k[1])
                            elif m.index == 5:
                                community8m6.append(k[1])
                            elif m.index == 6:
                                community8m7.append(k[1])
                            elif m.index == 7:
                                community8m8.append(k[1])
                            elif m.index == 8:
                                community8m9.append(k[1])
                            elif m.index == 9:
                                community8m10.append(k[1])
                            elif m.index == 10:
                                community8m11.append(k[1])
                            elif m.index == 11:
                                community8m12.append(k[1])
                            elif m.index == 12:
                                community8m13.append(k[1])
                            elif m.index == 13:
                                community8m14.append(k[1])
                            elif m.index == 14:
                                community8m15.append(k[1])
                        if j.reference == 'community9':
                            if m.index == 0:
                                community9m1.append(k[1])
                            elif m.index == 1:
                                community9m2.append(k[1])
                            elif m.index == 2:
                                community9m3.append(k[1])
                            elif m.index == 3:
                                community9m4.append(k[1])
                            elif m.index == 4:
                                community9m5.append(k[1])
                            elif m.index == 5:
                                community9m6.append(k[1])
                            elif m.index == 6:
                                community9m7.append(k[1])
                            elif m.index == 7:
                                community9m8.append(k[1])
                            elif m.index == 8:
                                community9m9.append(k[1])
                            elif m.index == 9:
                                community9m10.append(k[1])
                            elif m.index == 10:
                                community9m11.append(k[1])
                            elif m.index == 11:
                                community9m12.append(k[1])
                            elif m.index == 12:
                                community9m13.append(k[1])
                            elif m.index == 13:
                                community9m14.append(k[1])
                            elif m.index == 14:
                                community9m15.append(k[1])
                        if j.reference == 'community10':
                            if m.index == 0:
                                community10m1.append(k[1])
                            elif m.index == 1:
                                community10m2.append(k[1])
                            elif m.index == 2:
                                community10m3.append(k[1])
                            elif m.index == 3:
                                community10m4.append(k[1])
                            elif m.index == 4:
                                community10m5.append(k[1])
                            elif m.index == 5:
                                community10m6.append(k[1])
                            elif m.index == 6:
                                community10m7.append(k[1])
                            elif m.index == 7:
                                community10m8.append(k[1])
                            elif m.index == 8:
                                community10m9.append(k[1])
                            elif m.index == 9:
                                community10m10.append(k[1])
                            elif m.index == 10:
                                community10m11.append(k[1])
                            elif m.index == 11:
                                community10m12.append(k[1])
                            elif m.index == 12:
                                community10m13.append(k[1])
                            elif m.index == 13:
                                community10m14.append(k[1])
                            elif m.index == 14:
                                community10m15.append(k[1])
                        if j.reference == 'community11':
                            if m.index == 0:
                                community11m1.append(k[1])
                            elif m.index == 1:
                                community11m2.append(k[1])
                            elif m.index == 2:
                                community11m3.append(k[1])
                            elif m.index == 3:
                                community11m4.append(k[1])
                            elif m.index == 4:
                                community11m5.append(k[1])
                            elif m.index == 5:
                                community11m6.append(k[1])
                            elif m.index == 6:
                                community11m7.append(k[1])
                            elif m.index == 7:
                                community11m8.append(k[1])
                            elif m.index == 8:
                                community11m9.append(k[1])
                            elif m.index == 9:
                                community11m10.append(k[1])
                            elif m.index == 10:
                                community11m11.append(k[1])
                            elif m.index == 11:
                                community11m12.append(k[1])
                            elif m.index == 12:
                                community11m13.append(k[1])
                            elif m.index == 13:
                                community11m14.append(k[1])
                            elif m.index == 14:
                                community11m15.append(k[1])
                        if j.reference == 'community12':
                            if m.index == 0:
                                community12m1.append(k[1])
                            elif m.index == 1:
                                community12m2.append(k[1])
                            elif m.index == 2:
                                community12m3.append(k[1])
                            elif m.index == 3:
                                community12m4.append(k[1])
                            elif m.index == 4:
                                community12m5.append(k[1])
                            elif m.index == 5:
                                community12m6.append(k[1])
                            elif m.index == 6:
                                community12m7.append(k[1])
                            elif m.index == 7:
                                community12m8.append(k[1])
                            elif m.index == 8:
                                community12m9.append(k[1])
                            elif m.index == 9:
                                community12m10.append(k[1])
                            elif m.index == 10:
                                community12m11.append(k[1])
                            elif m.index == 11:
                                community12m12.append(k[1])
                            elif m.index == 12:
                                community12m13.append(k[1])
                            elif m.index == 13:
                                community12m14.append(k[1])
                            elif m.index == 14:
                                community12m15.append(k[1])
                        if j.reference == 'community13':
                            if m.index == 0:
                                community13m1.append(k[1])
                            elif m.index == 1:
                                community13m2.append(k[1])
                            elif m.index == 2:
                                community13m3.append(k[1])
                            elif m.index == 3:
                                community13m4.append(k[1])
                            elif m.index == 4:
                                community13m5.append(k[1])
                            elif m.index == 5:
                                community13m6.append(k[1])
                            elif m.index == 6:
                                community13m7.append(k[1])
                            elif m.index == 7:
                                community13m8.append(k[1])
                            elif m.index == 8:
                                community13m9.append(k[1])
                            elif m.index == 9:
                                community13m10.append(k[1])
                            elif m.index == 10:
                                community13m11.append(k[1])
                            elif m.index == 11:
                                community13m12.append(k[1])
                            elif m.index == 12:
                                community13m13.append(k[1])
                            elif m.index == 13:
                                community13m14.append(k[1])
                            elif m.index == 14:
                                community13m15.append(k[1])
                        if j.reference == 'community14':
                            if m.index == 0:
                                community14m1.append(k[1])
                            elif m.index == 1:
                                community14m2.append(k[1])
                            elif m.index == 2:
                                community14m3.append(k[1])
                            elif m.index == 3:
                                community14m4.append(k[1])
                            elif m.index == 4:
                                community14m5.append(k[1])
                            elif m.index == 5:
                                community14m6.append(k[1])
                            elif m.index == 6:
                                community14m7.append(k[1])
                            elif m.index == 7:
                                community14m8.append(k[1])
                            elif m.index == 8:
                                community14m9.append(k[1])
                            elif m.index == 9:
                                community14m10.append(k[1])
                            elif m.index == 10:
                                community14m11.append(k[1])
                            elif m.index == 11:
                                community14m12.append(k[1])
                            elif m.index == 12:
                                community14m13.append(k[1])
                            elif m.index == 13:
                                community14m14.append(k[1])
                            elif m.index == 14:
                                community14m15.append(k[1])
                        if j.reference == 'community15':
                            if m.index == 0:
                                community15m1.append(k[1])
                            elif m.index == 1:
                                community15m2.append(k[1])
                            elif m.index == 2:
                                community15m3.append(k[1])
                            elif m.index == 3:
                                community15m4.append(k[1])
                            elif m.index == 4:
                                community15m5.append(k[1])
                            elif m.index == 5:
                                community15m6.append(k[1])
                            elif m.index == 6:
                                community15m7.append(k[1])
                            elif m.index == 7:
                                community15m8.append(k[1])
                            elif m.index == 8:
                                community15m9.append(k[1])
                            elif m.index == 9:
                                community15m10.append(k[1])
                            elif m.index == 10:
                                community15m11.append(k[1])
                            elif m.index == 11:
                                community15m12.append(k[1])
                            elif m.index == 12:
                                community15m13.append(k[1])
                            elif m.index == 13:
                                community15m14.append(k[1])
                            elif m.index == 14:
                                community15m15.append(k[1])
                    elif percentage == True:
                        if j.reference == 'community1':
                            if m.index == 0:
                                community1m1.append(k[1] / j.population[m.index])
                            elif m.index == 1:
                                community1m2.append(k[1] / j.population[m.index])
                            elif m.index == 2:
                                community1m3.append(k[1] / j.population[m.index])
                            elif m.index == 3:
                                community1m4.append(k[1] / j.population[m.index])
                            elif m.index == 4:
                                community1m5.append(k[1] / j.population[m.index])
                            elif m.index == 5:
                                community1m6.append(k[1] / j.population[m.index])
                            elif m.index == 6:
                                community1m7.append(k[1] / j.population[m.index])
                            elif m.index == 7:
                                community1m8.append(k[1] / j.population[m.index])
                            elif m.index == 8:
                                community1m9.append(k[1] / j.population[m.index])
                            elif m.index == 9:
                                community1m10.append(k[1] / j.population[m.index])
                            elif m.index == 10:
                                community1m11.append(k[1] / j.population[m.index])
                            elif m.index == 11:
                                community1m12.append(k[1] / j.population[m.index])
                            elif m.index == 12:
                                community1m13.append(k[1] / j.population[m.index])
                            elif m.index == 13:
                                community1m14.append(k[1] / j.population[m.index])
                            elif m.index == 14:
                                community1m15.append(k[1] / j.population[m.index])
                        if j.reference == 'community2':
                            if m.index == 0:
                                community2m1.append(k[1] / j.population[m.index])
                            elif m.index == 1:
                                community2m2.append(k[1] / j.population[m.index])
                            elif m.index == 2:
                                community2m3.append(k[1] / j.population[m.index])
                            elif m.index == 3:
                                community2m4.append(k[1] / j.population[m.index])
                            elif m.index == 4:
                                community2m5.append(k[1] / j.population[m.index])
                            elif m.index == 5:
                                community2m6.append(k[1] / j.population[m.index])
                            elif m.index == 6:
                                community2m7.append(k[1] / j.population[m.index])
                            elif m.index == 7:
                                community2m8.append(k[1] / j.population[m.index])
                            elif m.index == 8:
                                community2m9.append(k[1] / j.population[m.index])
                            elif m.index == 9:
                                community2m10.append(k[1] / j.population[m.index])
                            elif m.index == 10:
                                community2m11.append(k[1] / j.population[m.index])
                            elif m.index == 11:
                                community2m12.append(k[1] / j.population[m.index])
                            elif m.index == 12:
                                community2m13.append(k[1] / j.population[m.index])
                            elif m.index == 13:
                                community2m14.append(k[1] / j.population[m.index])
                            elif m.index == 14:
                                community2m15.append(k[1] / j.population[m.index])
                        if j.reference == 'community3':
                            if m.index == 0:
                                community3m1.append(k[1] / j.population[m.index])
                            elif m.index == 1:
                                community3m2.append(k[1] / j.population[m.index])
                            elif m.index == 2:
                                community3m3.append(k[1] / j.population[m.index])
                            elif m.index == 3:
                                community3m4.append(k[1] / j.population[m.index])
                            elif m.index == 4:
                                community3m5.append(k[1] / j.population[m.index])
                            elif m.index == 5:
                                community3m6.append(k[1] / j.population[m.index])
                            elif m.index == 6:
                                community3m7.append(k[1] / j.population[m.index])
                            elif m.index == 7:
                                community3m8.append(k[1] / j.population[m.index])
                            elif m.index == 8:
                                community3m9.append(k[1] / j.population[m.index])
                            elif m.index == 9:
                                community3m10.append(k[1] / j.population[m.index])
                            elif m.index == 10:
                                community3m11.append(k[1] / j.population[m.index])
                            elif m.index == 11:
                                community3m12.append(k[1] / j.population[m.index])
                            elif m.index == 12:
                                community3m13.append(k[1] / j.population[m.index])
                            elif m.index == 13:
                                community3m14.append(k[1] / j.population[m.index])
                            elif m.index == 14:
                                community3m15.append(k[1] / j.population[m.index])
                        if j.reference == 'community4':
                            if m.index == 0:
                                community4m1.append(k[1] / j.population[m.index])
                            elif m.index == 1:
                                community4m2.append(k[1] / j.population[m.index])
                            elif m.index == 2:
                                community4m3.append(k[1] / j.population[m.index])
                            elif m.index == 3:
                                community4m4.append(k[1] / j.population[m.index])
                            elif m.index == 4:
                                community4m5.append(k[1] / j.population[m.index])
                            elif m.index == 5:
                                community4m6.append(k[1] / j.population[m.index])
                            elif m.index == 6:
                                community4m7.append(k[1] / j.population[m.index])
                            elif m.index == 7:
                                community4m8.append(k[1] / j.population[m.index])
                            elif m.index == 8:
                                community4m9.append(k[1] / j.population[m.index])
                            elif m.index == 9:
                                community4m10.append(k[1] / j.population[m.index])
                            elif m.index == 10:
                                community4m11.append(k[1] / j.population[m.index])
                            elif m.index == 11:
                                community4m12.append(k[1] / j.population[m.index])
                            elif m.index == 12:
                                community4m13.append(k[1] / j.population[m.index])
                            elif m.index == 13:
                                community4m14.append(k[1] / j.population[m.index])
                            elif m.index == 14:
                                community4m15.append(k[1] / j.population[m.index])
                        if j.reference == 'community5':
                            if m.index == 0:
                                community5m1.append(k[1] / j.population[m.index])
                            elif m.index == 1:
                                community5m2.append(k[1] / j.population[m.index])
                            elif m.index == 2:
                                community5m3.append(k[1] / j.population[m.index])
                            elif m.index == 3:
                                community5m4.append(k[1] / j.population[m.index])
                            elif m.index == 4:
                                community5m5.append(k[1] / j.population[m.index])
                            elif m.index == 5:
                                community5m6.append(k[1] / j.population[m.index])
                            elif m.index == 6:
                                community5m7.append(k[1] / j.population[m.index])
                            elif m.index == 7:
                                community5m8.append(k[1] / j.population[m.index])
                            elif m.index == 8:
                                community5m9.append(k[1] / j.population[m.index])
                            elif m.index == 9:
                                community5m10.append(k[1] / j.population[m.index])
                            elif m.index == 10:
                                community5m11.append(k[1] / j.population[m.index])
                            elif m.index == 11:
                                community5m12.append(k[1] / j.population[m.index])
                            elif m.index == 12:
                                community5m13.append(k[1] / j.population[m.index])
                            elif m.index == 13:
                                community5m14.append(k[1] / j.population[m.index])
                            elif m.index == 14:
                                community5m15.append(k[1] / j.population[m.index])
                        if j.reference == 'community6':
                            if m.index == 0:
                                community6m1.append(k[1] / j.population[m.index])
                            elif m.index == 1:
                                community6m2.append(k[1] / j.population[m.index])
                            elif m.index == 2:
                                community6m3.append(k[1] / j.population[m.index])
                            elif m.index == 3:
                                community6m4.append(k[1] / j.population[m.index])
                            elif m.index == 4:
                                community6m5.append(k[1] / j.population[m.index])
                            elif m.index == 5:
                                community6m6.append(k[1] / j.population[m.index])
                            elif m.index == 6:
                                community6m7.append(k[1] / j.population[m.index])
                            elif m.index == 7:
                                community6m8.append(k[1] / j.population[m.index])
                            elif m.index == 8:
                                community6m9.append(k[1] / j.population[m.index])
                            elif m.index == 9:
                                community6m10.append(k[1] / j.population[m.index])
                            elif m.index == 10:
                                community6m11.append(k[1] / j.population[m.index])
                            elif m.index == 11:
                                community6m12.append(k[1] / j.population[m.index])
                            elif m.index == 12:
                                community6m13.append(k[1] / j.population[m.index])
                            elif m.index == 13:
                                community6m14.append(k[1] / j.population[m.index])
                            elif m.index == 14:
                                community6m15.append(k[1] / j.population[m.index])
                        if j.reference == 'community7':
                            if m.index == 0:
                                community7m1.append(k[1] / j.population[m.index])
                            elif m.index == 1:
                                community7m2.append(k[1] / j.population[m.index])
                            elif m.index == 2:
                                community7m3.append(k[1] / j.population[m.index])
                            elif m.index == 3:
                                community7m4.append(k[1] / j.population[m.index])
                            elif m.index == 4:
                                community7m5.append(k[1] / j.population[m.index])
                            elif m.index == 5:
                                community7m6.append(k[1] / j.population[m.index])
                            elif m.index == 6:
                                community7m7.append(k[1] / j.population[m.index])
                            elif m.index == 7:
                                community7m8.append(k[1] / j.population[m.index])
                            elif m.index == 8:
                                community7m9.append(k[1] / j.population[m.index])
                            elif m.index == 9:
                                community7m10.append(k[1] / j.population[m.index])
                            elif m.index == 10:
                                community7m11.append(k[1] / j.population[m.index])
                            elif m.index == 11:
                                community7m12.append(k[1] / j.population[m.index])
                            elif m.index == 12:
                                community7m13.append(k[1] / j.population[m.index])
                            elif m.index == 13:
                                community7m14.append(k[1] / j.population[m.index])
                            elif m.index == 14:
                                community7m15.append(k[1] / j.population[m.index])
                        if j.reference == 'community8':
                            if m.index == 0:
                                community8m1.append(k[1] / j.population[m.index])
                            elif m.index == 1:
                                community8m2.append(k[1] / j.population[m.index])
                            elif m.index == 2:
                                community8m3.append(k[1] / j.population[m.index])
                            elif m.index == 3:
                                community8m4.append(k[1] / j.population[m.index])
                            elif m.index == 4:
                                community8m5.append(k[1] / j.population[m.index])
                            elif m.index == 5:
                                community8m6.append(k[1] / j.population[m.index])
                            elif m.index == 6:
                                community8m7.append(k[1] / j.population[m.index])
                            elif m.index == 7:
                                community8m8.append(k[1] / j.population[m.index])
                            elif m.index == 8:
                                community8m9.append(k[1] / j.population[m.index])
                            elif m.index == 9:
                                community8m10.append(k[1] / j.population[m.index])
                            elif m.index == 10:
                                community8m11.append(k[1] / j.population[m.index])
                            elif m.index == 11:
                                community8m12.append(k[1] / j.population[m.index])
                            elif m.index == 12:
                                community8m13.append(k[1] / j.population[m.index])
                            elif m.index == 13:
                                community8m14.append(k[1] / j.population[m.index])
                            elif m.index == 14:
                                community8m15.append(k[1] / j.population[m.index])
                        if j.reference == 'community9':
                            if m.index == 0:
                                community9m1.append(k[1] / j.population[m.index])
                            elif m.index == 1:
                                community9m2.append(k[1] / j.population[m.index])
                            elif m.index == 2:
                                community9m3.append(k[1] / j.population[m.index])
                            elif m.index == 3:
                                community9m4.append(k[1] / j.population[m.index])
                            elif m.index == 4:
                                community9m5.append(k[1] / j.population[m.index])
                            elif m.index == 5:
                                community9m6.append(k[1] / j.population[m.index])
                            elif m.index == 6:
                                community9m7.append(k[1] / j.population[m.index])
                            elif m.index == 7:
                                community9m8.append(k[1] / j.population[m.index])
                            elif m.index == 8:
                                community9m9.append(k[1] / j.population[m.index])
                            elif m.index == 9:
                                community9m10.append(k[1] / j.population[m.index])
                            elif m.index == 10:
                                community9m11.append(k[1] / j.population[m.index])
                            elif m.index == 11:
                                community9m12.append(k[1] / j.population[m.index])
                            elif m.index == 12:
                                community9m13.append(k[1] / j.population[m.index])
                            elif m.index == 13:
                                community9m14.append(k[1] / j.population[m.index])
                            elif m.index == 14:
                                community9m15.append(k[1] / j.population[m.index])
                        if j.reference == 'community10':
                            if m.index == 0:
                                community10m1.append(k[1] / j.population[m.index])
                            elif m.index == 1:
                                community10m2.append(k[1] / j.population[m.index])
                            elif m.index == 2:
                                community10m3.append(k[1] / j.population[m.index])
                            elif m.index == 3:
                                community10m4.append(k[1] / j.population[m.index])
                            elif m.index == 4:
                                community10m5.append(k[1] / j.population[m.index])
                            elif m.index == 5:
                                community10m6.append(k[1] / j.population[m.index])
                            elif m.index == 6:
                                community10m7.append(k[1] / j.population[m.index])
                            elif m.index == 7:
                                community10m8.append(k[1] / j.population[m.index])
                            elif m.index == 8:
                                community10m9.append(k[1] / j.population[m.index])
                            elif m.index == 9:
                                community10m10.append(k[1] / j.population[m.index])
                            elif m.index == 10:
                                community10m11.append(k[1] / j.population[m.index])
                            elif m.index == 11:
                                community10m12.append(k[1] / j.population[m.index])
                            elif m.index == 12:
                                community10m13.append(k[1] / j.population[m.index])
                            elif m.index == 13:
                                community10m14.append(k[1] / j.population[m.index])
                            elif m.index == 14:
                                community10m15.append(k[1] / j.population[m.index])
                        if j.reference == 'community11':
                            if m.index == 0:
                                community11m1.append(k[1] / j.population[m.index])
                            elif m.index == 1:
                                community11m2.append(k[1] / j.population[m.index])
                            elif m.index == 2:
                                community11m3.append(k[1] / j.population[m.index])
                            elif m.index == 3:
                                community11m4.append(k[1] / j.population[m.index])
                            elif m.index == 4:
                                community11m5.append(k[1] / j.population[m.index])
                            elif m.index == 5:
                                community11m6.append(k[1] / j.population[m.index])
                            elif m.index == 6:
                                community11m7.append(k[1] / j.population[m.index])
                            elif m.index == 7:
                                community11m8.append(k[1] / j.population[m.index])
                            elif m.index == 8:
                                community11m9.append(k[1] / j.population[m.index])
                            elif m.index == 9:
                                community11m10.append(k[1] / j.population[m.index])
                            elif m.index == 10:
                                community11m11.append(k[1] / j.population[m.index])
                            elif m.index == 11:
                                community11m12.append(k[1] / j.population[m.index])
                            elif m.index == 12:
                                community11m13.append(k[1] / j.population[m.index])
                            elif m.index == 13:
                                community11m14.append(k[1] / j.population[m.index])
                            elif m.index == 14:
                                community11m15.append(k[1] / j.population[m.index])
                        if j.reference == 'community12':
                            if m.index == 0:
                                community12m1.append(k[1] / j.population[m.index])
                            elif m.index == 1:
                                community12m2.append(k[1] / j.population[m.index])
                            elif m.index == 2:
                                community12m3.append(k[1] / j.population[m.index])
                            elif m.index == 3:
                                community12m4.append(k[1] / j.population[m.index])
                            elif m.index == 4:
                                community12m5.append(k[1] / j.population[m.index])
                            elif m.index == 5:
                                community12m6.append(k[1] / j.population[m.index])
                            elif m.index == 6:
                                community12m7.append(k[1] / j.population[m.index])
                            elif m.index == 7:
                                community12m8.append(k[1] / j.population[m.index])
                            elif m.index == 8:
                                community12m9.append(k[1] / j.population[m.index])
                            elif m.index == 9:
                                community12m10.append(k[1] / j.population[m.index])
                            elif m.index == 10:
                                community12m11.append(k[1] / j.population[m.index])
                            elif m.index == 11:
                                community12m12.append(k[1] / j.population[m.index])
                            elif m.index == 12:
                                community12m13.append(k[1] / j.population[m.index])
                            elif m.index == 13:
                                community12m14.append(k[1] / j.population[m.index])
                            elif m.index == 14:
                                community12m15.append(k[1] / j.population[m.index])
                        if j.reference == 'community13':
                            if m.index == 0:
                                community13m1.append(k[1] / j.population[m.index])
                            elif m.index == 1:
                                community13m2.append(k[1] / j.population[m.index])
                            elif m.index == 2:
                                community13m3.append(k[1] / j.population[m.index])
                            elif m.index == 3:
                                community13m4.append(k[1] / j.population[m.index])
                            elif m.index == 4:
                                community13m5.append(k[1] / j.population[m.index])
                            elif m.index == 5:
                                community13m6.append(k[1] / j.population[m.index])
                            elif m.index == 6:
                                community13m7.append(k[1] / j.population[m.index])
                            elif m.index == 7:
                                community13m8.append(k[1] / j.population[m.index])
                            elif m.index == 8:
                                community13m9.append(k[1] / j.population[m.index])
                            elif m.index == 9:
                                community13m10.append(k[1] / j.population[m.index])
                            elif m.index == 10:
                                community13m11.append(k[1] / j.population[m.index])
                            elif m.index == 11:
                                community13m12.append(k[1] / j.population[m.index])
                            elif m.index == 12:
                                community13m13.append(k[1] / j.population[m.index])
                            elif m.index == 13:
                                community13m14.append(k[1] / j.population[m.index])
                            elif m.index == 14:
                                community13m15.append(k[1] / j.population[m.index])
                        if j.reference == 'community14':
                            if m.index == 0:
                                community14m1.append(k[1] / j.population[m.index])
                            elif m.index == 1:
                                community14m2.append(k[1] / j.population[m.index])
                            elif m.index == 2:
                                community14m3.append(k[1] / j.population[m.index])
                            elif m.index == 3:
                                community14m4.append(k[1] / j.population[m.index])
                            elif m.index == 4:
                                community14m5.append(k[1] / j.population[m.index])
                            elif m.index == 5:
                                community14m6.append(k[1] / j.population[m.index])
                            elif m.index == 6:
                                community14m7.append(k[1] / j.population[m.index])
                            elif m.index == 7:
                                community14m8.append(k[1] / j.population[m.index])
                            elif m.index == 8:
                                community14m9.append(k[1] / j.population[m.index])
                            elif m.index == 9:
                                community14m10.append(k[1] / j.population[m.index])
                            elif m.index == 10:
                                community14m11.append(k[1] / j.population[m.index])
                            elif m.index == 11:
                                community14m12.append(k[1] / j.population[m.index])
                            elif m.index == 12:
                                community14m13.append(k[1] / j.population[m.index])
                            elif m.index == 13:
                                community14m14.append(k[1] / j.population[m.index])
                            elif m.index == 14:
                                community14m15.append(k[1] / j.population[m.index])
                        if j.reference == 'community15':
                            if m.index == 0:
                                community15m1.append(k[1] / j.population[m.index])
                            elif m.index == 1:
                                community15m2.append(k[1] / j.population[m.index])
                            elif m.index == 2:
                                community15m3.append(k[1] / j.population[m.index])
                            elif m.index == 3:
                                community15m4.append(k[1] / j.population[m.index])
                            elif m.index == 4:
                                community15m5.append(k[1] / j.population[m.index])
                            elif m.index == 5:
                                community15m6.append(k[1] / j.population[m.index])
                            elif m.index == 6:
                                community15m7.append(k[1] / j.population[m.index])
                            elif m.index == 7:
                                community15m8.append(k[1] / j.population[m.index])
                            elif m.index == 8:
                                community15m9.append(k[1] / j.population[m.index])
                            elif m.index == 9:
                                community15m10.append(k[1] / j.population[m.index])
                            elif m.index == 10:
                                community15m11.append(k[1] / j.population[m.index])
                            elif m.index == 11:
                                community15m12.append(k[1] / j.population[m.index])
                            elif m.index == 12:
                                community15m13.append(k[1] / j.population[m.index])
                            elif m.index == 13:
                                community15m14.append(k[1] / j.population[m.index])
                            elif m.index == 14:
                                community15m15.append(k[1] / j.population[m.index])
            if counter == 0:
                if j.reference == 'community1':
                    if m.index == 0:
                        community1m1 = []
                    if m.index == 1:
                        community1m2 = []
                    if m.index == 2:
                        community1m3 = []
                    if m.index == 3:
                        community1m4 = []
                    if m.index == 4:
                        community1m5 = []
                    if m.index == 5:
                        community1m6 = []
                    if m.index == 6:
                        community1m7 = []
                    if m.index == 7:
                        community1m8 = []
                    if m.index == 8:
                        community1m9 = []
                    if m.index == 9:
                        community1m10 = []
                    if m.index == 10:
                        community1m11 = []
                    if m.index == 11:
                        community1m12 = []
                    if m.index == 12:
                        community1m13 = []
                    if m.index == 13:
                        community1m14 = []
                    if m.index == 14:
                        community1m15 = []
                if j.reference == 'community2':
                    if m.index == 0:
                        community2m1 = []
                    if m.index == 1:
                        community2m2 = []
                    if m.index == 2:
                        community2m3 = []
                    if m.index == 3:
                        community2m4 = []
                    if m.index == 4:
                        community2m5 = []
                    if m.index == 5:
                        community2m6 = []
                    if m.index == 6:
                        community2m7 = []
                    if m.index == 7:
                        community2m8 = []
                    if m.index == 8:
                        community2m9 = []
                    if m.index == 9:
                        community2m10 = []
                    if m.index == 10:
                        community2m11 = []
                    if m.index == 11:
                        community2m12 = []
                    if m.index == 12:
                        community2m13 = []
                    if m.index == 13:
                        community2m14 = []
                    if m.index == 14:
                        community2m15 = []
                if j.reference == 'community3':
                    if m.index == 0:
                        community3m1 = []
                    if m.index == 1:
                        community3m2 = []
                    if m.index == 2:
                        community3m3 = []
                    if m.index == 3:
                        community3m4 = []
                    if m.index == 4:
                        community3m5 = []
                    if m.index == 5:
                        community3m6 = []
                    if m.index == 6:
                        community3m7 = []
                    if m.index == 7:
                        community3m8 = []
                    if m.index == 8:
                        community3m9 = []
                    if m.index == 9:
                        community3m10 = []
                    if m.index == 10:
                        community3m11 = []
                    if m.index == 11:
                        community3m12 = []
                    if m.index == 12:
                        community3m13 = []
                    if m.index == 13:
                        community3m14 = []
                    if m.index == 14:
                        community3m15 = []
                if j.reference == 'community4':
                    if m.index == 0:
                        community4m1 = []
                    if m.index == 1:
                        community4m2 = []
                    if m.index == 2:
                        community4m3 = []
                    if m.index == 3:
                        community4m4 = []
                    if m.index == 4:
                        community4m5 = []
                    if m.index == 5:
                        community4m6 = []
                    if m.index == 6:
                        community4m7 = []
                    if m.index == 7:
                        community4m8 = []
                    if m.index == 8:
                        community4m9 = []
                    if m.index == 9:
                        community4m10 = []
                    if m.index == 10:
                        community4m11 = []
                    if m.index == 11:
                        community4m12 = []
                    if m.index == 12:
                        community4m13 = []
                    if m.index == 13:
                        community4m14 = []
                    if m.index == 14:
                        community4m15 = []
                if j.reference == 'community5':
                    if m.index == 0:
                        community5m1 = []
                    if m.index == 1:
                        community5m2 = []
                    if m.index == 2:
                        community5m3 = []
                    if m.index == 3:
                        community5m4 = []
                    if m.index == 4:
                        community5m5 = []
                    if m.index == 5:
                        community5m6 = []
                    if m.index == 6:
                        community5m7 = []
                    if m.index == 7:
                        community5m8 = []
                    if m.index == 8:
                        community5m9 = []
                    if m.index == 9:
                        community5m10 = []
                    if m.index == 10:
                        community5m11 = []
                    if m.index == 11:
                        community5m12 = []
                    if m.index == 12:
                        community5m13 = []
                    if m.index == 13:
                        community5m14 = []
                    if m.index == 14:
                        community5m15 = []
                if j.reference == 'community6':
                    if m.index == 0:
                        community6m1 = []
                    if m.index == 1:
                        community6m2 = []
                    if m.index == 2:
                        community6m3 = []
                    if m.index == 3:
                        community6m4 = []
                    if m.index == 4:
                        community6m5 = []
                    if m.index == 5:
                        community6m6 = []
                    if m.index == 6:
                        community6m7 = []
                    if m.index == 7:
                        community6m8 = []
                    if m.index == 8:
                        community6m9 = []
                    if m.index == 9:
                        community6m10 = []
                    if m.index == 10:
                        community6m11 = []
                    if m.index == 11:
                        community6m12 = []
                    if m.index == 12:
                        community6m13 = []
                    if m.index == 13:
                        community6m14 = []
                    if m.index == 14:
                        community6m15 = []
                if j.reference == 'community7':
                    if m.index == 0:
                        community7m1 = []
                    if m.index == 1:
                        community7m2 = []
                    if m.index == 2:
                        community7m3 = []
                    if m.index == 3:
                        community7m4 = []
                    if m.index == 4:
                        community7m5 = []
                    if m.index == 5:
                        community7m6 = []
                    if m.index == 6:
                        community7m7 = []
                    if m.index == 7:
                        community7m8 = []
                    if m.index == 8:
                        community7m9 = []
                    if m.index == 9:
                        community7m10 = []
                    if m.index == 10:
                        community7m11 = []
                    if m.index == 11:
                        community7m12 = []
                    if m.index == 12:
                        community7m13 = []
                    if m.index == 13:
                        community7m14 = []
                    if m.index == 14:
                        community7m15 = []
                if j.reference == 'community8':
                    if m.index == 0:
                        community8m1 = []
                    if m.index == 1:
                        community8m2 = []
                    if m.index == 2:
                        community8m3 = []
                    if m.index == 3:
                        community8m4 = []
                    if m.index == 4:
                        community8m5 = []
                    if m.index == 5:
                        community8m6 = []
                    if m.index == 6:
                        community8m7 = []
                    if m.index == 7:
                        community8m8 = []
                    if m.index == 8:
                        community8m9 = []
                    if m.index == 9:
                        community8m10 = []
                    if m.index == 10:
                        community8m11 = []
                    if m.index == 11:
                        community8m12 = []
                    if m.index == 12:
                        community8m13 = []
                    if m.index == 13:
                        community8m14 = []
                    if m.index == 14:
                        community8m15 = []
                if j.reference == 'community9':
                    if m.index == 0:
                        community9m1 = []
                    if m.index == 1:
                        community9m2 = []
                    if m.index == 2:
                        community9m3 = []
                    if m.index == 3:
                        community9m4 = []
                    if m.index == 4:
                        community9m5 = []
                    if m.index == 5:
                        community9m6 = []
                    if m.index == 6:
                        community9m7 = []
                    if m.index == 7:
                        community9m8 = []
                    if m.index == 8:
                        community9m9 = []
                    if m.index == 9:
                        community9m10 = []
                    if m.index == 10:
                        community9m11 = []
                    if m.index == 11:
                        community9m12 = []
                    if m.index == 12:
                        community9m13 = []
                    if m.index == 13:
                        community9m14 = []
                    if m.index == 14:
                        community9m15 = []
                if j.reference == 'community10':
                    if m.index == 0:
                        community10m1 = []
                    if m.index == 1:
                        community10m2 = []
                    if m.index == 2:
                        community10m3 = []
                    if m.index == 3:
                        community10m4 = []
                    if m.index == 4:
                        community10m5 = []
                    if m.index == 5:
                        community10m6 = []
                    if m.index == 6:
                        community10m7 = []
                    if m.index == 7:
                        community10m8 = []
                    if m.index == 8:
                        community10m9 = []
                    if m.index == 9:
                        community10m10 = []
                    if m.index == 10:
                        community10m11 = []
                    if m.index == 11:
                        community10m12 = []
                    if m.index == 12:
                        community10m13 = []
                    if m.index == 13:
                        community10m14 = []
                    if m.index == 14:
                        community10m15 = []
                if j.reference == 'community11':
                    if m.index == 0:
                        community11m1 = []
                    if m.index == 1:
                        community11m2 = []
                    if m.index == 2:
                        community11m3 = []
                    if m.index == 3:
                        community11m4 = []
                    if m.index == 4:
                        community11m5 = []
                    if m.index == 5:
                        community11m6 = []
                    if m.index == 6:
                        community11m7 = []
                    if m.index == 7:
                        community11m8 = []
                    if m.index == 8:
                        community11m9 = []
                    if m.index == 9:
                        community11m10 = []
                    if m.index == 10:
                        community11m11 = []
                    if m.index == 11:
                        community11m12 = []
                    if m.index == 12:
                        community11m13 = []
                    if m.index == 13:
                        community11m14 = []
                    if m.index == 14:
                        community11m15 = []
                if j.reference == 'community12':
                    if m.index == 0:
                        community12m1 = []
                    if m.index == 1:
                        community12m2 = []
                    if m.index == 2:
                        community12m3 = []
                    if m.index == 3:
                        community12m4 = []
                    if m.index == 4:
                        community12m5 = []
                    if m.index == 5:
                        community12m6 = []
                    if m.index == 6:
                        community12m7 = []
                    if m.index == 7:
                        community12m8 = []
                    if m.index == 8:
                        community12m9 = []
                    if m.index == 9:
                        community12m10 = []
                    if m.index == 10:
                        community12m11 = []
                    if m.index == 11:
                        community12m12 = []
                    if m.index == 12:
                        community12m13 = []
                    if m.index == 13:
                        community12m14 = []
                    if m.index == 14:
                        community12m15 = []
                if j.reference == 'community13':
                    if m.index == 0:
                        community13m1 = []
                    if m.index == 1:
                        community13m2 = []
                    if m.index == 2:
                        community13m3 = []
                    if m.index == 3:
                        community13m4 = []
                    if m.index == 4:
                        community13m5 = []
                    if m.index == 5:
                        community13m6 = []
                    if m.index == 6:
                        community13m7 = []
                    if m.index == 7:
                        community13m8 = []
                    if m.index == 8:
                        community13m9 = []
                    if m.index == 9:
                        community13m10 = []
                    if m.index == 10:
                        community13m11 = []
                    if m.index == 11:
                        community13m12 = []
                    if m.index == 12:
                        community13m13 = []
                    if m.index == 13:
                        community13m14 = []
                    if m.index == 14:
                        community13m15 = []
                if j.reference == 'community14':
                    if m.index == 0:
                        community14m1 = []
                    if m.index == 1:
                        community14m2 = []
                    if m.index == 2:
                        community14m3 = []
                    if m.index == 3:
                        community14m4 = []
                    if m.index == 4:
                        community14m5 = []
                    if m.index == 5:
                        community14m6 = []
                    if m.index == 6:
                        community14m7 = []
                    if m.index == 7:
                        community14m8 = []
                    if m.index == 8:
                        community14m9 = []
                    if m.index == 9:
                        community14m10 = []
                    if m.index == 10:
                        community14m11 = []
                    if m.index == 11:
                        community14m12 = []
                    if m.index == 12:
                        community14m13 = []
                    if m.index == 13:
                        community14m14 = []
                    if m.index == 14:
                        community14m15 = []
                if j.reference == 'community15':
                    if m.index == 0:
                        community15m1 = []
                    if m.index == 1:
                        community15m2 = []
                    if m.index == 2:
                        community15m3 = []
                    if m.index == 3:
                        community15m4 = []
                    if m.index == 4:
                        community15m5 = []
                    if m.index == 5:
                        community15m6 = []
                    if m.index == 6:
                        community15m7 = []
                    if m.index == 7:
                        community15m8 = []
                    if m.index == 8:
                        community15m9 = []
                    if m.index == 9:
                        community15m10 = []
                    if m.index == 10:
                        community15m11 = []
                    if m.index == 11:
                        community15m12 = []
                    if m.index == 12:
                        community15m13 = []
                    if m.index == 13:
                        community15m14 = []
                    if m.index == 14:
                        community15m15 = []

blanks = []
rounds = len(community1m1)
i = 0
while i < rounds:
    blanks.append(0)
    i += 1

if community1m1 == []:
    community1m1 = blanks
if community2m1 == []:
    community2m1 = blanks
if community3m1 == []:
    community3m1 = blanks
if community4m1 == []:
    community4m1 = blanks
if community5m1 == []:
    community5m1 = blanks
if community6m1 == []:
    community6m1 = blanks
if community7m1 == []:
    community7m1 = blanks
if community8m1 == []:
    community8m1 = blanks
if community9m1 == []:
    community9m1 = blanks
if community10m1 == []:
    community10m1 = blanks
if community11m1 == []:
    community11m1 = blanks
if community12m1 == []:
    community12m1 = blanks
if community13m1 == []:
    community13m1 = blanks
if community14m1 == []:
    community14m1 = blanks
if community15m1 == []:
    community15m1 = blanks
if community1m2 == []:
    community1m2 = blanks
if community2m2 == []:
    community2m2 = blanks
if community3m2 == []:
    community3m2 = blanks
if community4m2 == []:
    community4m2 = blanks
if community5m2 == []:
    community5m2 = blanks
if community6m2 == []:
    community6m2 = blanks
if community7m2 == []:
    community7m2 = blanks
if community8m2 == []:
    community8m2 = blanks
if community9m2 == []:
    community9m2 = blanks
if community10m2 == []:
    community10m2 = blanks
if community11m2 == []:
    community11m2 = blanks
if community12m2 == []:
    community12m2 = blanks
if community13m2 == []:
    community13m2 = blanks
if community14m2 == []:
    community14m2 = blanks
if community15m2 == []:
    community15m2 = blanks
if community1m3 == []:
    community1m3 = blanks
if community2m3 == []:
    community2m3 = blanks
if community3m3 == []:
    community3m3 = blanks
if community4m3 == []:
    community4m3 = blanks
if community5m3 == []:
    community5m3 = blanks
if community6m3 == []:
    community6m3 = blanks
if community7m3 == []:
    community7m3 = blanks
if community8m3 == []:
    community8m3 = blanks
if community9m3 == []:
    community9m3 = blanks
if community10m3 == []:
    community10m3 = blanks
if community11m3 == []:
    community11m3 = blanks
if community12m3 == []:
    community12m3 = blanks
if community13m3 == []:
    community13m3 = blanks
if community14m3 == []:
    community14m3 = blanks
if community15m3 == []:
    community15m3 = blanks
if community1m4 == []:
    community1m4 = blanks
if community2m4 == []:
    community2m4 = blanks
if community3m4 == []:
    community3m4 = blanks
if community4m4 == []:
    community4m4 = blanks
if community5m4 == []:
    community5m4 = blanks
if community6m4 == []:
    community6m4 = blanks
if community7m4 == []:
    community7m4 = blanks
if community8m4 == []:
    community8m4 = blanks
if community9m4 == []:
    community9m4 = blanks
if community10m4 == []:
    community10m4 = blanks
if community11m4 == []:
    community11m4 = blanks
if community12m4 == []:
    community12m4 = blanks
if community13m4 == []:
    community13m4 = blanks
if community14m4 == []:
    community14m4 = blanks
if community15m4 == []:
    community15m4 = blanks
if community1m5 == []:
    community1m5 = blanks
if community2m5 == []:
    community2m5 = blanks
if community3m5 == []:
    community3m5 = blanks
if community4m5 == []:
    community4m5 = blanks
if community5m5 == []:
    community5m5 = blanks
if community6m5 == []:
    community6m5 = blanks
if community7m5 == []:
    community7m5 = blanks
if community8m5 == []:
    community8m5 = blanks
if community9m5 == []:
    community9m5 = blanks
if community10m5 == []:
    community10m5 = blanks
if community11m5 == []:
    community11m5 = blanks
if community12m5 == []:
    community12m5 = blanks
if community13m5 == []:
    community13m5 = blanks
if community14m5 == []:
    community14m5 = blanks
if community15m5 == []:
    community15m5 = blanks
if community1m6 == []:
    community1m6 = blanks
if community2m6 == []:
    community2m6 = blanks
if community3m6 == []:
    community3m6 = blanks
if community4m6 == []:
    community4m6 = blanks
if community5m6 == []:
    community5m6 = blanks
if community6m6 == []:
    community6m6 = blanks
if community7m6 == []:
    community7m6 = blanks
if community8m6 == []:
    community8m6 = blanks
if community9m6 == []:
    community9m6 = blanks
if community10m6 == []:
    community10m6 = blanks
if community11m6 == []:
    community11m6 = blanks
if community12m6 == []:
    community12m6 = blanks
if community13m6 == []:
    community13m6 = blanks
if community14m6 == []:
    community14m6 = blanks
if community15m6 == []:
    community15m6 = blanks
if community1m7 == []:
    community1m7 = blanks
if community2m7 == []:
    community2m7 = blanks
if community3m7 == []:
    community3m7 = blanks
if community4m7 == []:
    community4m7 = blanks
if community5m7 == []:
    community5m7 = blanks
if community6m7 == []:
    community6m7 = blanks
if community7m7 == []:
    community7m7 = blanks
if community8m7 == []:
    community8m7 = blanks
if community9m7 == []:
    community9m7 = blanks
if community10m7 == []:
    community10m7 = blanks
if community11m7 == []:
    community11m7 = blanks
if community12m7 == []:
    community12m7 = blanks
if community13m7 == []:
    community13m7 = blanks
if community14m7 == []:
    community14m7 = blanks
if community15m7 == []:
    community15m7 = blanks
if community1m8 == []:
    community1m8 = blanks
if community2m8 == []:
    community2m8 = blanks
if community3m8 == []:
    community3m8 = blanks
if community4m8 == []:
    community4m8 = blanks
if community5m8 == []:
    community5m8 = blanks
if community6m8 == []:
    community6m8 = blanks
if community7m8 == []:
    community7m8 = blanks
if community8m8 == []:
    community8m8 = blanks
if community9m8 == []:
    community9m8 = blanks
if community10m8 == []:
    community10m8 = blanks
if community11m8 == []:
    community11m8 = blanks
if community12m8 == []:
    community12m8 = blanks
if community13m8 == []:
    community13m8 = blanks
if community14m8 == []:
    community14m8 = blanks
if community15m8 == []:
    community15m8 = blanks
if community1m9 == []:
    community1m9 = blanks
if community2m9 == []:
    community2m9 = blanks
if community3m9 == []:
    community3m9 = blanks
if community4m9 == []:
    community4m9 = blanks
if community5m9 == []:
    community5m9 = blanks
if community6m9 == []:
    community6m9 = blanks
if community7m9 == []:
    community7m9 = blanks
if community8m9 == []:
    community8m9 = blanks
if community9m9 == []:
    community9m9 = blanks
if community10m9 == []:
    community10m9 = blanks
if community11m9 == []:
    community11m9 = blanks
if community12m9 == []:
    community12m9 = blanks
if community13m9 == []:
    community13m9 = blanks
if community14m9 == []:
    community14m9 = blanks
if community15m9 == []:
    community15m9 = blanks
if community1m10 == []:
    community1m10 = blanks
if community2m10 == []:
    community2m10 = blanks
if community3m10 == []:
    community3m10 = blanks
if community4m10 == []:
    community4m10 = blanks
if community5m10 == []:
    community5m10 = blanks
if community6m10 == []:
    community6m10 = blanks
if community7m10 == []:
    community7m10 = blanks
if community8m10 == []:
    community8m10 = blanks
if community9m10 == []:
    community9m10 = blanks
if community10m10 == []:
    community10m10 = blanks
if community11m10 == []:
    community11m10 = blanks
if community12m10 == []:
    community12m10 = blanks
if community13m10 == []:
    community13m10 = blanks
if community14m10 == []:
    community14m10 = blanks
if community15m10 == []:
    community15m10 = blanks
if community1m11 == []:
    community1m11 = blanks
if community2m11 == []:
    community2m11 = blanks
if community3m11 == []:
    community3m11 = blanks
if community4m11 == []:
    community4m11 = blanks
if community5m11 == []:
    community5m11 = blanks
if community6m11 == []:
    community6m11 = blanks
if community7m11 == []:
    community7m11 = blanks
if community8m11 == []:
    community8m11 = blanks
if community9m11 == []:
    community9m11 = blanks
if community10m11 == []:
    community10m11 = blanks
if community11m11 == []:
    community11m11 = blanks
if community12m11 == []:
    community12m11 = blanks
if community13m11 == []:
    community13m11 = blanks
if community14m11 == []:
    community14m11 = blanks
if community15m11 == []:
    community15m11 = blanks
if community1m12 == []:
    community1m12 = blanks
if community2m12 == []:
    community2m12 = blanks
if community3m12 == []:
    community3m12 = blanks
if community4m12 == []:
    community4m12 = blanks
if community5m12 == []:
    community5m12 = blanks
if community6m12 == []:
    community6m12 = blanks
if community7m12 == []:
    community7m12 = blanks
if community8m12 == []:
    community8m12 = blanks
if community9m12 == []:
    community9m12 = blanks
if community10m12 == []:
    community10m12 = blanks
if community11m12 == []:
    community11m12 = blanks
if community12m12 == []:
    community12m12 = blanks
if community13m12 == []:
    community13m12 = blanks
if community14m12 == []:
    community14m12 = blanks
if community15m12 == []:
    community15m12 = blanks
if community1m13 == []:
    community1m13 = blanks
if community2m13 == []:
    community2m13 = blanks
if community3m13 == []:
    community3m13 = blanks
if community4m13 == []:
    community4m13 = blanks
if community5m13 == []:
    community5m13 = blanks
if community6m13 == []:
    community6m13 = blanks
if community7m13 == []:
    community7m13 = blanks
if community8m13 == []:
    community8m13 = blanks
if community9m13 == []:
    community9m13 = blanks
if community10m13 == []:
    community10m13 = blanks
if community11m13 == []:
    community11m13 = blanks
if community12m13 == []:
    community12m13 = blanks
if community13m13 == []:
    community13m13 = blanks
if community14m13 == []:
    community14m13 = blanks
if community15m13 == []:
    community15m13 = blanks
if community1m14 == []:
    community1m14 = blanks
if community2m14 == []:
    community2m14 = blanks
if community3m14 == []:
    community3m14 = blanks
if community4m14 == []:
    community4m14 = blanks
if community5m14 == []:
    community5m14 = blanks
if community6m14 == []:
    community6m14 = blanks
if community7m14 == []:
    community7m14 = blanks
if community8m14 == []:
    community8m14 = blanks
if community9m14 == []:
    community9m14 = blanks
if community10m14 == []:
    community10m14 = blanks
if community11m14 == []:
    community11m14 = blanks
if community12m14 == []:
    community12m14 = blanks
if community13m14 == []:
    community13m14 = blanks
if community14m14 == []:
    community14m14 = blanks
if community15m14 == []:
    community15m14 = blanks
if community1m15 == []:
    community1m15 = blanks
if community2m15 == []:
    community2m15 = blanks
if community3m15 == []:
    community3m15 = blanks
if community4m15 == []:
    community4m15 = blanks
if community5m15 == []:
    community5m15 = blanks
if community6m15 == []:
    community6m15 = blanks
if community7m15 == []:
    community7m15 = blanks
if community8m15 == []:
    community8m15 = blanks
if community9m15 == []:
    community9m15 = blanks
if community10m15 == []:
    community10m15 = blanks
if community11m15 == []:
    community11m15 = blanks
if community12m15 == []:
    community12m15 = blanks
if community13m15 == []:
    community13m15 = blanks
if community14m15 == []:
    community14m15 = blanks
if community15m15 == []:
    community15m15 = blanks

if community1defend == []:
    community1defend = blanks
if community2defend == []:
    community2defend = blanks
if community3defend == []:
    community3defend = blanks
if community4defend == []:
    community4defend = blanks
if community5defend == []:
    community5defend = blanks
if community6defend == []:
    community6defend = blanks
if community7defend == []:
    community7defend = blanks
if community8defend == []:
    community8defend = blanks
if community9defend == []:
    community9defend = blanks
if community10defend == []:
    community10defend = blanks
if community11defend == []:
    community11defend = blanks
if community12defend == []:
    community12defend = blanks
if community13defend == []:
    community13defend = blanks
if community14defend == []:
    community14defend = blanks
if community15defend == []:
    community15defend = blanks
if oneandtwo == []:
    oneandtwo = blanks
if oneandthree == []:
    oneandthree = blanks
if oneandfour == []:
    oneandfour = blanks
if oneandfive == []:
    oneandfive = blanks
if oneandsix == []:
    oneandsix = blanks
if oneandseven == []:
    oneandseven = blanks
if oneandeight == []:
    oneandeight = blanks
if oneandnine == []:
    oneandnine = blanks
if oneandten == []:
    oneandten = blanks
if oneandeleven == []:
    oneandeleven = blanks
if oneandtwelve == []:
    oneandtwelve = blanks
if oneandthirteen == []:
    oneandthirteen = blanks
if oneandfourteen == []:
    oneandfourteen = blanks
if oneandfifteen == []:
    oneandfifteen = blanks
if twoandthree == []:
    twoandthree = blanks
if twoandfour == []:
    twoandfour = blanks
if twoandfive == []:
    twoandfive = blanks
if twoandsix == []:
    twoandsix = blanks
if twoandseven == []:
    twoandseven = blanks
if twoandeight == []:
    twoandeight = blanks
if twoandnine == []:
    twoandnine = blanks
if twoandten == []:
    twoandten = blanks
if twoandeleven == []:
    twoandeleven = blanks
if twoandtwelve == []:
    twoandtwelve = blanks
if twoandthirteen == []:
    twoandthirteen = blanks
if twoandfourteen == []:
    twoandfourteen = blanks
if twoandfifteen == []:
    twoandfifteen = blanks
if threeandfour == []:
    threeandfour = blanks
if threeandfive == []:
    threeandfive = blanks
if threeandsix == []:
    threeandsix = blanks
if threeandseven == []:
    threeandseven = blanks
if threeandeight == []:
    threeandeight = blanks
if threeandnine == []:
    threeandnine = blanks
if threeandten == []:
    threeandten = blanks
if threeandeleven == []:
    threeandeleven = blanks
if threeandtwelve == []:
    threeandtwelve = blanks
if threeandthirteen == []:
    threeandthirteen = blanks
if threeandfourteen == []:
    threeandfourteen = blanks
if threeandfifteen == []:
    threeandfifteen = blanks
if fourandfive == []:
    fourandfive = blanks
if fourandsix == []:
    fourandsix = blanks
if fourandseven == []:
    fourandseven = blanks
if fourandeight == []:
    fourandeight = blanks
if fourandnine == []:
    fourandnine = blanks
if fourandten == []:
    fourandten = blanks
if fourandeleven == []:
    fourandeleven = blanks
if fourandtwelve == []:
    fourandtwelve = blanks
if fourandthirteen == []:
    fourandthirteen = blanks
if fourandfourteen == []:
    fourandfourteen = blanks
if fourandfifteen == []:
    fourandfifteen = blanks
if fiveandsix == []:
    fiveandsix = blanks
if fiveandseven == []:
    fiveandseven = blanks
if fiveandeight == []:
    fiveandeight = blanks
if fiveandnine == []:
    fiveandnine = blanks
if fiveandten == []:
    fiveandten = blanks
if fiveandeleven == []:
    fiveandeleven = blanks
if fiveandtwelve == []:
    fiveandtwelve = blanks
if fiveandthirteen == []:
    fiveandthirteen = blanks
if fiveandfourteen == []:
    fiveandfourteen = blanks
if fiveandfifteen == []:
    fiveandfifteen = blanks
if sixandseven == []:
    sixandseven = blanks
if sixandeight == []:
    sixandeight = blanks
if sixandnine == []:
    sixandnine = blanks
if sixandten == []:
    sixandten = blanks
if sixandeleven == []:
    sixandeleven = blanks
if sixandtwelve == []:
    sixandtwelve = blanks
if sixandthirteen == []:
    sixandthirteen = blanks
if sixandfourteen == []:
    sixandfourteen = blanks
if sixandfifteen == []:
    sixandfifteen = blanks
if sevenandeight == []:
    sevenandeight = blanks
if sevenandnine == []:
    sevenandnine = blanks
if sevenandten == []:
    sevenandten = blanks
if sevenandeleven == []:
    sevenandeleven = blanks
if sevenandtwelve == []:
    sevenandtwelve = blanks
if sevenandthirteen == []:
    sevenandthirteen = blanks
if sevenandfourteen == []:
    sevenandfourteen = blanks
if sevenandfifteen == []:
    sevenandfifteen = blanks
if eightandnine == []:
    eightandnine = blanks
if eightandten == []:
    eightandten = blanks
if eightandeleven == []:
    eightandeleven = blanks
if eightandtwelve == []:
    eightandtwelve = blanks
if eightandthirteen == []:
    eightandthirteen = blanks
if eightandfourteen == []:
    eightandfourteen = blanks
if eightandfifteen == []:
    eightandfifteen = blanks
if nineandten == []:
    nineandten = blanks
if nineandeleven == []:
    nineandeleven = blanks
if nineandtwelve == []:
    nineandtwelve = blanks
if nineandthirteen == []:
    nineandthirteen = blanks
if nineandfourteen == []:
    nineandfourteen = blanks
if nineandfifteen == []:
    nineandfifteen = blanks
if tenandeleven == []:
    tenandeleven = blanks
if tenandtwelve == []:
    tenandtwelve = blanks
if tenandthirteen == []:
    tenandthirteen = blanks
if tenandfourteen == []:
    tenandfourteen = blanks
if tenandfifteen == []:
    tenandfifteen = blanks
if elevenandtwelve == []:
    elevenandtwelve = blanks
if elevenandthirteen == []:
    elevenandthirteen = blanks
if elevenandfourteen == []:
    elevenandfourteen = blanks
if elevenandfifteen == []:
    elevenandfifteen = blanks
if twelveandthirteen == []:
    twelveandthirteen = blanks
if twelveandfourteen == []:
    twelveandfourteen = blanks
if twelveandfifteen == []:
    twelveandfifteen = blanks
if thirteenandfourteen == []:
    thirteenandfourteen = blanks
if thirteenandfifteen == []:
    thirteenandfifteen = blanks
if fourteenandfifteen == []:
    fourteenandfifteen = blanks


# Printing results
def printing():
    militantmatrix = []
    for m in militantlist:
        militantmatrix.append([m.name, militantoutputlist[m.index].strength, militantoutputlist[m.index].notorietyratio,
              militantoutputlist[m.index].totalextort, militantoutputlist[m.index].countextort,
              militantoutputlist[m.index].countbenefit, militantoutputlist[m.index].countpunish,
              militantoutputlist[m.index].countsupport, militantoutputlist[m.index].totalsupport,
              militantoutputlist[m.index].countdefend])

    if len(militantmatrix) >= 1:
        militant1matrix = militantmatrix[0]
    else:
        militant1matrix = []
    if len(militantmatrix) >= 2:
        militant2matrix = militantmatrix[0]
    else:
        militant2matrix = []
    if len(militantmatrix) >= 3:
        militant3matrix = militantmatrix[0]
    else:
        militant3matrix = []
    if len(militantmatrix) >= 4:
        militant4matrix = militantmatrix[0]
    else:
        militant4matrix = []
    if len(militantmatrix) >= 5:
        militant5matrix = militantmatrix[0]
    else:
        militant5matrix = []
    if len(militantmatrix) >= 6:
        militant6matrix = militantmatrix[0]
    else:
        militant6matrix = []
    if len(militantmatrix) >= 7:
        militant7matrix = militantmatrix[0]
    else:
        militant7matrix = []
    if len(militantmatrix) >= 8:
        militant8matrix = militantmatrix[0]
    else:
        militant8matrix = []
    if len(militantmatrix) >= 9:
        militant9matrix = militantmatrix[0]
    else:
        militant9matrix = []
    if len(militantmatrix) >= 10:
        militant10matrix = militantmatrix[0]
    else:
        militant10matrix = []
    if len(militantmatrix) >= 11:
        militant11matrix = militantmatrix[0]
    else:
        militant11matrix = []
    if len(militantmatrix) >= 12:
        militant12matrix = militantmatrix[0]
    else:
        militant12matrix = []
    if len(militantmatrix) >= 13:
        militant13matrix = militantmatrix[0]
    else:
        militant13matrix = []
    if len(militantmatrix) >= 14:
        militant14matrix = militantmatrix[0]
    else:
        militant14matrix = []
    if len(militantmatrix) >= 15:
        militant15matrix = militantmatrix[0]
    else:
        militant15matrix = []

    militantstring = ''
    for m in militantlist:
        militantindivstring = str(m.name)+' * '+str(militantoutputlist[m.index].strength)+' * '+str(militantoutputlist[m.index].notorietyratio)+' * '+str(militantoutputlist[m.index].totalextort)+' * '+str(militantoutputlist[m.index].countextort)+' * '+str(militantoutputlist[m.index].countbenefit)+' * '+str(militantoutputlist[m.index].countpunish)+' * '+str(militantoutputlist[m.index].countsupport)+' * '+str(militantoutputlist[m.index].totalsupport)+' * '+str(militantoutputlist[m.index].countdefend)+' * '
        militantstring = militantstring+militantindivstring
    communitystring1 = ' * '+str(community1m1)+' * '+str(community2m1)+' * '+str(community3m1)+' * '+str( community4m1)+' * '+str(community5m1)+' * '+str(community6m1)+' * '+str(community7m1)+' * '+str(community8m1)+' * '+str(community9m1)+' * '+str(community10m1)+' * '+str(community11m1)+' * '+str(community12m1)+' * '+str(community13m1)+' * '+str(community14m1)+' * '+str(community15m1)+' * '+str(community1m2)+' * '+str(community2m2)+' * '+str(community3m2)+' * '+str(community4m2)+' * '+str(community5m2)+' * '+str(community6m2)+' * '+str(community7m2)+' * '+str(community8m2)+' * '+str(community9m2)+' * '+str(community10m2)+' * '+str(community11m2)+' * '+str(community12m2)+' * '+str(community13m2)+' * '+str(community14m2)+' * '+str(community15m2)+' * '+str(community1m3)+' * '+str(community2m3)+' * '+str(community3m3)+' * '+str(community4m3)+' * '+str(community5m3)+' * '+str(community6m3)+' * '+str(community7m3)+' * '+str(community8m3)+' * '+str(community9m3)+' * '+str(community10m3)+' * '+str(community11m3)+' * '+str(community12m3)+' * '+str(community13m3)+' * '+str(community14m3)+' * '+str(community15m3)+' * '+str(community1m4)+' * '+str(community2m4)+' * '+str(community3m4)+' * '+str(community4m4)+' * '+str(community5m4)+' * '+str(community6m4)+' * '+str(community7m4)+' * '+str(community8m4)+' * '+str(community9m4)+' * '+str(community10m4)+' * '+str(community11m4)+' * '+str(community12m4)+' * '+str(community13m4)+' * '+str(community14m4)+' * '+str(community15m4)+' * '+str(community1m5)+' * '+str(community2m5)+' * '+str(community3m5)+' * '+str(community4m5)+' * '+str(community5m5)+' * '+str(community6m5)+' * '+str(community7m5)+' * '+str(community8m5)+' * '+str(community9m5)+' * '+str(community10m5)+' * '+str(community11m5)+' * '+str(community12m5)+' * '+str(community13m5)+' * '+str(community14m5)+' * '+str(community15m5)+' * '+str(community1m6)+' * '+str(community2m6)+' * '+str(community3m6)+' * '+str(community4m6)+' * '+str(community5m6)+' * '+str(community6m6)+' * '+str(community7m6)+' * '+str(community8m6)+' * '+str(community9m6)+' * '+str(community10m6)+' * '+str(community11m6)+' * '+str(community12m6)+' * '+str(community13m6)+' * '+str(community14m6)+' * '+str(community15m6)+' * '+str(community1m7)+' * '+str(community2m7)+' * '+str(community3m7)+' * '+str( community4m7)+' * '+str(community5m7)+' * '+str(community6m7)+' * '+str(community7m7)+' * '+str(community8m7)+' * '+str(community9m7)+' * '+str(community10m7)+' * '+str(community11m7)+' * '+str(community12m7)+' * '+str(community13m7)+' * '+str(community14m7)+' * '+str(community15m7)+' * '+str(community1m8)+' * '+str(community2m8)+' * '+str(community3m8)+' * '+str(community4m8)+' * '+str(community5m8)+' * '+str(community6m8)+' * '+str(community7m8)+' * '
    communitystring2 = ' * '+str(community8m8)+' * '+str(community9m8)+' * '+str(community10m8)+' * '+str(community11m8)+' * '+str(community12m8)+' * '+str(community13m8)+' * '+str(community14m8)+' * '+str(community15m8)+' * '+str(community1m9)+' * '+str(community2m9)+' * '+str(community3m9)+' * '+str(community4m9)+' * '+str(community5m9)+' * '+str(community6m9)+' * '+str(community7m9)+' * '+str(community8m9)+' * '+str(community9m9)+' * '+str(community10m9)+' * '+str(community11m9)+' * '+str(community12m9)+' * '+str(community13m9)+' * '+str(community14m9)+' * '+str(community15m9)+' * '+str(community1m10)+' * '+str(community2m10)+' * '+str(community3m10)+' * '+str(community4m10)+' * '+str(community5m10)+' * '+str(community6m10)+' * '+str(community7m10)+' * '+str(community8m10)+' * '+str(community9m10)+' * '+str(community10m10)+' * '+str(community11m10)+' * '+str(community12m10)+' * '+str(community13m10)+' * '+str(community14m10)+' * '+str(community15m10)+' * '+str(community1m11)+' * '+str(community2m11)+' * '+str(community3m11)+' * '+str(community4m11)+' * '+str(community5m11)+' * '+str(community6m11)+' * '+str(community7m11)+' * '+str(community8m11)+' * '+str(community9m11)+' * '+str(community10m11)+' * '+str(community11m11)+' * '+str(community12m11)+' * '+str(community13m11)+' * '+str(community14m11)+' * '+str(community15m11)+' * '+str(community1m12)+' * '+str(community2m12)+' * '+str(community3m12)+' * '+str(community4m12)+' * '+str(community5m12)+' * '+str(community6m12)+' * '+str(community7m12)+' * '+str(community8m12)+' * '+str(community9m12)+' * '+str(community10m12)+' * '+str(community11m12)+' * '+str(community12m12)+' * '+str(community13m12)+' * '+str(community14m12)+' * '+str(community15m12)+' * '+str(community1m13)+' * '+str(community2m13)+' * '+str(community3m13)+' * '+str(community4m13)+' * '+str(community5m13)+' * '+str(community6m13)+' * '+str(community7m13)+' * '+str(community8m13)+' * '+str(community9m13)+' * '+str(community10m13)+' * '+str(community11m13)+' * '+str(community12m13)+' * '+str(community13m13)+' * '+str(community14m13)+' * '+str(community15m13)+' * '+str(community1m14)+' * '+str(community2m14)+' * '+str(community3m14)+' * '+str(community4m14)+' * '+str(community5m14)+' * '+str(community6m14)+' * '+str(community7m14)+' * '+str(community8m14)+' * '+str(community9m14)+' * '+str(community10m14)+' * '+str(community11m14)+' * '+str(community12m14)+' * '+str(community13m14)+' * '+str(community14m14)+' * '+str(community15m14)+' * '+str(community1m15)+' * '+str(community2m15)+' * '+str(community3m15)+' * '+str(community4m15)+' * '+str(community5m15)+' * '+str(community6m15)+' * '+str(community7m15)+' * '+str(community8m15)+' * '+str(community9m15)+' * '+str(community10m15)+' * '+str(community11m15)+' * '+str(community12m15)+' * '+str(community13m15)+' * '+str(community14m15)+' * '+str(community15m15)+' * '
    defendstring = ' * '+str(community1defend)+' * '+str(community2defend)+' * '+str(community3defend)+' * '+str(community4defend)+' * '+str(community5defend)+' * '+str(community6defend)+' * '+str(community7defend)+' * '+str(community8defend)+' * '+str(community9defend)+' * '+str(community10defend)+' * '+str(community11defend)+' * '+str(community12defend)+' * '+str(community13defend)+' * '+str(community14defend)+' * '+str(community15defend)+' * '
    fightstring = ' * '+str(oneandtwo)+' * '+str(oneandthree)+' * '+str(oneandfour)+' * '+str(oneandfive)+' * '+str(oneandsix)+' * '+str(oneandseven)+' * '+str(oneandeight)+' * '+str(oneandnine)+' * '+str(oneandten)+' * '+str(oneandeleven)+' * '+str(oneandtwelve)+' * '+str(oneandthirteen)+' * '+str(oneandfourteen)+' * '+str(oneandfifteen)+' * '+str(twoandthree)+' * '+str(twoandfour)+' * '+str(twoandfive)+' * '+str(twoandsix)+' * '+str(twoandseven)+' * '+str(twoandeight)+' * '+str(twoandnine)+' * '+str(twoandten)+' * '+str(twoandeleven)+' * '+str(twoandtwelve)+' * '+str(twoandthirteen)+' * '+str(twoandfourteen)+' * '+str(twoandfifteen)+' * '+str(threeandfour)+' * '+str(threeandfive)+' * '+str(threeandsix)+' * '+str(threeandseven)+' * '+str(threeandeight)+' * '+str(threeandnine)+' * '+str(threeandten)+' * '+str(threeandeleven)+' * '+str(threeandtwelve)+' * '+str(threeandthirteen)+' * '+str(threeandfourteen)+' * '+str(threeandfifteen)+' * '+str(fourandfive)+' * '+str(fourandsix)+' * '+str(fourandseven)+' * '+str(fourandeight)+' * '+str(fourandnine)+' * '+str(fourandten)+' * '+str(fourandeleven)+' * '+str(fourandtwelve)+' * '+str(fourandthirteen)+' * '+str(fourandfourteen)+' * '+str(fourandfifteen)+' * '+str(fiveandsix)+' * '+str(fiveandseven)+' * '+str(fiveandeight)+' * '+str(fiveandnine)+' * '+str(fiveandten)+' * '+str(fiveandeleven)+' * '+str(fiveandtwelve)+' * '+str(fiveandthirteen)+' * '+str(fiveandfourteen)+' * '+str(fiveandfifteen)+' * '+str(sixandseven)+' * '+str(sixandeight)+' * '+str(sixandnine)+' * '+str(sixandten)+' * '+str(sixandeleven)+' * '+str(sixandtwelve)+' * '+str(sixandthirteen)+' * '+str(sixandfourteen)+' * '+str(sixandfifteen)+' * '+str(sevenandeight)+' * '+str(sevenandnine)+' * '+str(sevenandten)+' * '+str(sevenandeleven)+' * '+str(sevenandtwelve)+' * '+str(sevenandthirteen)+' * '+str(sevenandfourteen)+' * '+str(sevenandfifteen)+' * '+str(eightandnine)+' * '+str(eightandten)+' * '+str(eightandeleven)+' * '+str(eightandtwelve)+' * '+str(eightandthirteen)+' * '+str(eightandfourteen)+' * '+str(eightandfifteen)+' * '+str(nineandten)+' * '+str(nineandeleven)+' * '+str(nineandtwelve)+' * '+str(nineandthirteen)+' * '+str(nineandfourteen)+' * '+str(nineandfifteen)+' * '+str(tenandeleven)+' * '+str(tenandtwelve)+' * '+str(tenandthirteen)+' * '+str(tenandfourteen)+' * '+str(tenandfifteen)+' * '+str(elevenandtwelve)+' * '+str(elevenandthirteen)+' * '+str(elevenandfourteen)+' * '+str(elevenandfifteen)+' * '+str(twelveandthirteen)+' * '+str(twelveandfourteen)+' * '+str(twelveandfifteen)+' * '+str(thirteenandfourteen)+' * '+str(thirteenandfifteen)+' * '+str(fourteenandfifteen)
    datastring = militantstring+' @ '+communitystring1+' @ '+communitystring2+' @ '+defendstring+' @ '+fightstring

    return datastring

def fetchoutput():
    militantmatrix = []
    for m in militantlist:
        militantmatrix.append([militantoutputlist[m.index].strength, militantoutputlist[m.index].notorietyratio,
              militantoutputlist[m.index].totalextort, militantoutputlist[m.index].countextort,
              militantoutputlist[m.index].countbenefit, militantoutputlist[m.index].countpunish,
              militantoutputlist[m.index].countsupport, militantoutputlist[m.index].totalsupport,
              militantoutputlist[m.index].countdefend])

    empty = []
    blanks = []
    rounds = len(militantmatrix[0][0])
    i = 0
    j = 0
    while i < 9:
        while j < rounds:
            empty.append(0)
            j += 1
        blanks.append(empty)
        i += 1

    if len(militantmatrix) >= 1:
        militant1matrix = militantmatrix[0]
    else:
        militant1matrix = blanks
    if len(militantmatrix) >= 2:
        militant2matrix = militantmatrix[1]
    else:
        militant2matrix = blanks
    if len(militantmatrix) >= 3:
        militant3matrix = militantmatrix[2]
    else:
        militant3matrix = blanks
    if len(militantmatrix) >= 4:
        militant4matrix = militantmatrix[3]
    else:
        militant4matrix = blanks
    if len(militantmatrix) >= 5:
        militant5matrix = militantmatrix[4]
    else:
        militant5matrix = blanks
    if len(militantmatrix) >= 6:
        militant6matrix = militantmatrix[5]
    else:
        militant6matrix = blanks
    if len(militantmatrix) >= 7:
        militant7matrix = militantmatrix[6]
    else:
        militant7matrix = blanks
    if len(militantmatrix) >= 8:
        militant8matrix = militantmatrix[7]
    else:
        militant8matrix = blanks
    if len(militantmatrix) >= 9:
        militant9matrix = militantmatrix[8]
    else:
        militant9matrix = blanks
    if len(militantmatrix) >= 10:
        militant10matrix = militantmatrix[9]
    else:
        militant10matrix = blanks
    if len(militantmatrix) >= 11:
        militant11matrix = militantmatrix[10]
    else:
        militant11matrix = blanks
    if len(militantmatrix) >= 12:
        militant12matrix = militantmatrix[11]
    else:
        militant12matrix = blanks
    if len(militantmatrix) >= 13:
        militant13matrix = militantmatrix[12]
    else:
        militant13matrix = blanks
    if len(militantmatrix) >= 14:
        militant14matrix = militantmatrix[13]
    else:
        militant14matrix = blanks
    if len(militantmatrix) >= 15:
        militant15matrix = militantmatrix[14]
    else:
        militant15matrix = blanks

    communitysupport1 = [community1m1, community2m1, community3m1,  community4m1, community5m1,
      community6m1, community7m1, community8m1, community9m1, community10m1, community11m1,
      community12m1, community13m1, community14m1, community15m1]
    communitysupport2 = [community1m2,
      community2m2, community3m2, community4m2, community5m2, community6m2, community7m2,
      community8m2, community9m2, community10m2, community11m2, community12m2, community13m2,
      community14m2, community15m2]
    communitysupport3 = [community1m3, community2m3, community3m3,
      community4m3, community5m3, community6m3, community7m3, community8m3, community9m3,
      community10m3, community11m3, community12m3, community13m3, community14m3, community15m3]
    communitysupport4 = [community1m4, community2m4, community3m4, community4m4, community5m4, community6m4,
      community7m4, community8m4, community9m4, community10m4, community11m4,
      community12m4, community13m4, community14m4, community15m4]
    communitysupport5 = [community1m5, community2m5,
      community3m5, community4m5, community5m5, community6m5, community7m5, community8m5,
      community9m5, community10m5, community11m5, community12m5, community13m5,
      community14m5, community15m5]
    communitysupport6 = [community1m6, community2m6, community3m6, community4m6,
      community5m6, community6m6, community7m6, community8m6, community9m6, community10m6,
      community11m6, community12m6, community13m6, community14m6, community15m6]
    communitysupport7 = [community1m7, community2m7, community3m7,  community4m7, community5m7, community6m7,
      community7m7, community8m7, community9m7, community10m7, community11m7, community12m7,
      community13m7, community14m7, community15m7]
    communitysupport8 = [community1m8, community2m8,
      community3m8, community4m8, community5m8, community6m8, community7m8, community8m8, community9m8, community10m8,
      community11m8, community12m8, community13m8, community14m8, community15m8]
    communitysupport9 = [community1m9, community2m9,
      community3m9, community4m9, community5m9, community6m9, community7m9, community8m9,
      community9m9, community10m9, community11m9, community12m9, community13m9,
      community14m9, community15m9]
    communitysupport10 = [community1m10, community2m10, community3m10, community4m10,
      community5m10, community6m10, community7m10, community8m10, community9m10,
      community10m10, community11m10, community12m10, community13m10, community14m10,
      community15m10]
    communitysupport11 = [community1m11, community2m11, community3m11, community4m11,
      community5m11, community6m11, community7m11, community8m11, community9m11,
      community10m11, community11m11, community12m11, community13m11, community14m11,
      community15m11]
    communitysupport12 = [community1m12, community2m12, community3m12, community4m12,
      community5m12, community6m12, community7m12, community8m12, community9m12,
      community10m12, community11m12, community12m12, community13m12, community14m12,
      community15m12]
    communitysupport13 = [community1m13, community2m13, community3m13, community4m13,
      community5m13, community6m13, community7m13, community8m13, community9m13,
      community10m13, community11m13, community12m13, community13m13, community14m13,
      community15m13]
    communitysupport14 = [community1m14, community2m14, community3m14, community4m14,
      community5m14, community6m14, community7m14, community8m14, community9m14,
      community10m14, community11m14, community12m14, community13m14, community14m14,
      community15m14]
    communitysupport15 = [community1m15, community2m15, community3m15, community4m15,
      community5m15, community6m15, community7m15, community8m15, community9m15,
      community10m15, community11m15, community12m15, community13m15, community14m15,
      community15m15]
    communitydefendmatrix=[community1defend, community2defend, community3defend, community4defend,
      community5defend, community6defend, community7defend, community8defend, community9defend,
      community10defend, community11defend, community12defend, community13defend, community14defend,
      community15defend]
    fightmatrix=[oneandtwo, oneandthree, oneandfour, oneandfive, oneandsix, oneandseven,
      oneandeight, oneandnine, oneandten, oneandeleven, oneandtwelve, oneandthirteen,
      oneandfourteen, oneandfifteen, twoandthree, twoandfour, twoandfive, twoandsix,
      twoandseven, twoandeight, twoandnine, twoandten, twoandeleven, twoandtwelve,
      twoandthirteen, twoandfourteen, twoandfifteen, threeandfour, threeandfive, threeandsix,
      threeandseven, threeandeight, threeandnine, threeandten, threeandeleven,
      threeandtwelve, threeandthirteen, threeandfourteen, threeandfifteen, fourandfive,
      fourandsix, fourandseven, fourandeight, fourandnine, fourandten, fourandeleven,
      fourandtwelve, fourandthirteen, fourandfourteen, fourandfifteen, fiveandsix,
      fiveandseven, fiveandeight, fiveandnine, fiveandten, fiveandeleven, fiveandtwelve,
      fiveandthirteen, fiveandfourteen, fiveandfifteen, sixandseven, sixandeight, sixandnine,
      sixandten, sixandeleven, sixandtwelve, sixandthirteen, sixandfourteen,
      sixandfifteen, sevenandeight, sevenandnine, sevenandten, sevenandeleven, sevenandtwelve,
      sevenandthirteen, sevenandfourteen, sevenandfifteen, eightandnine, eightandten,
      eightandeleven, eightandtwelve, eightandthirteen, eightandfourteen, eightandfifteen,
      nineandten, nineandeleven, nineandtwelve, nineandthirteen, nineandfourteen,
      nineandfifteen, tenandeleven, tenandtwelve, tenandthirteen, tenandfourteen,
      tenandfifteen, elevenandtwelve, elevenandthirteen, elevenandfourteen, elevenandfifteen,
      twelveandthirteen, twelveandfourteen, twelveandfifteen, thirteenandfourteen,
      thirteenandfifteen, fourteenandfifteen]
    return (militant1matrix, militant2matrix, militant3matrix, militant4matrix, militant5matrix, militant6matrix,
            militant7matrix, militant8matrix, militant9matrix, militant10matrix, militant11matrix, militant12matrix,
            militant13matrix, militant14matrix, militant15matrix, communitysupport1, communitysupport2, communitysupport3,
            communitysupport4, communitysupport5, communitysupport6, communitysupport7, communitysupport8,
            communitysupport9, communitysupport10, communitysupport11, communitysupport12, communitysupport13,
            communitysupport14, communitysupport15, communitydefendmatrix, fightmatrix)
