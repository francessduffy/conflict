import copy

class Civilian(object):

    def __init__(self, region, community, wealth, wealthnum, militantsupport):
        self.region = region
        self.community = community
        self.wealth = wealth
        self.wealthnum = wealthnum
        self.militantsupport = militantsupport

    def updateSupport(self, currentmilitant, civsupport):
        if civsupport == True:
            self.militantsupport[currentmilitant.index] = 1
        else:
            self.militantsupport[currentmilitant.index] = 0

# Using wealths matrix from initconditions to compile total list of civilians
def generateCivilians(regionlist, communitylist, militantlist, wealths, wealthValues):
    civilianlist = []
    r = 1
    militantsupportdummy = []
    for i in range(len(militantlist)):
        militantsupportdummy.append(0)
    while r <= len(regionlist):
        c = 1
        while c <= len(communitylist):
            wealthindex = 1
            w = 1
            while w <= 3:
                x = 1
                while x <= wealths[r - 1][c - 1][wealthindex - 1]:
                    if wealthindex == 1:
                        wealth = 'L'
                        wealthnum = wealthValues[0]
                    elif wealthindex == 2:
                        wealth = 'M'
                        wealthnum = wealthValues[1]
                    else:
                        wealth = 'H'
                        wealthnum = wealthValues[2]
                    militantsupport = copy.deepcopy(militantsupportdummy)
                    p = Civilian(regionlist[r-1].name,communitylist[c-1].name, wealth, wealthnum, militantsupport)
                    civilianlist.append(p)
                    x = x + 1
                wealthindex += 1
                w = w + 1
            c = c + 1
        r = r + 1
    return civilianlist


