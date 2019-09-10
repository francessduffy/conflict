class MilitantOutput(object):

    def __init__(self, name, strength, notorietyratio, communitysupport, totalextort, countextort, countbenefit,
                 countpunish, countsupport, totalsupport, countdefend, oppsupport, oppsupportcount):
        self.name = name
        self.strength = strength
        self.notorietyratio = notorietyratio
        self.communitysupport = communitysupport
        self.totalextort = totalextort
        self.countextort = countextort
        self.countbenefit = countbenefit
        self.countpunish = countpunish
        self.countsupport = countsupport
        self.totalsupport = totalsupport
        self.countdefend = countdefend
        self.oppsupport = oppsupport
        self.oppsupportcount = oppsupportcount


    def updateCounts(self, strength, notorietyratio, communitysupport, totalextort, countextort, countbenefit,
                     countpunish, countsupport, totalsupport, countdefend, deviants):
        self.strength.append(strength)
        self.notorietyratio.append(notorietyratio)
        self.communitysupport.append(communitysupport)
        self.totalextort.append(totalextort)
        self.countextort.append(countextort)
        self.countbenefit.append(countbenefit)
        self.countpunish.append(countpunish)
        self.countsupport.append(countsupport + self.oppsupportcount)
        self.totalsupport.append(totalsupport + self.oppsupport)
        self.countdefend.append(countdefend)


class EnvOutput(object):

    def __init__(self):
        self.fightlist = []
        self.defendlist = []

    def updateFighting(self, fightlist):
        self.fightlist.append(fightlist)

    def updateDefending(self, defendlist):
        self.defendlist.append(defendlist)


def generateDefend(communitylist):
    defendlist = []
    for i in communitylist:
        matrix = [i.reference, i.defend]
        defendlist.append(matrix)
    return defendlist


def generateOutputList(militantlist):
    militantoutputlist = []
    for i in militantlist:
        x = MilitantOutput(i.name, [], [], [], [], [], [], [], [], [], [], 0, 0)
        militantoutputlist.append(x)
    return militantoutputlist


def communityMatrix(communities):
    communitysupport = []
    for i in communities:
        x = communityMatrixInstance(i)
        communitysupport.append(x)
    return communitysupport


def communityMatrixInstance(i):
    communitymatrix = []
    communitymatrix.append(i)
    communitymatrix.append(0)
    return communitymatrix


def addCivilians(civilianlist, communitysupport, currentmilitant):
    for i in communitysupport:
        for j in civilianlist:
            if i[0] == j.community:
                if j.militantsupport[currentmilitant.index] == 1:
                    i[1] += 1
    return communitysupport


def updateOpps(supportamt, supported_opponent, militantoutputlist):
    for i in militantoutputlist:
        if i.name == supported_opponent.name:
            i.oppsupport += supportamt
            i.oppsupportcount += 1
