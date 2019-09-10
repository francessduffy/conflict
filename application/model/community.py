class Community(object):

    def __init__(self, name, support, defend, propensityvalues, reference, population):
        self.name = name
        self.support = support
        self.defend = defend
        self.propensityvalues = propensityvalues
        self.reference = reference
        self.population = population

    # Setting initial propensity values
    def updatePropensity(self, x):
        self.propensityvalues.append(x)

    def updateDefend(self, value):
        if value == 1:
            self.defend += 1
        elif value == 0:
            self.defend = 0

    # Setting initial support values based on propensity values
    def initSupport(self):
        for i in self.propensityvalues:
            if i == -1:
                self.support.append('enemy')
            if i == 0:
                self.support.append('neutral')
            if i == 1:
                self.support.append('allied')

    # Updating support values based on civilian support
    def updateSupport(self, currentmilitant, supportvalue):
        self.support[currentmilitant.index] = supportvalue


def generateCommunities(communityvalues):
    communitylist = []
    numbercommunities = len(communityvalues)
    if numbercommunities > 0:
        community1 = Community(communityvalues[0], [], 0, [], 'community1', [])
        communitylist.append(community1)
    if numbercommunities > 1:
        community2 = Community(communityvalues[1], [], 0, [], 'community2', [])
        communitylist.append(community2)
    if numbercommunities > 2:
        community3 = Community(communityvalues[2], [], 0, [], 'community3', [])
        communitylist.append(community3)
    if numbercommunities > 3:
        community4 = Community(communityvalues[3], [], 0, [], 'community4', [])
        communitylist.append(community4)
    if numbercommunities > 4:
        community5 = Community(communityvalues[4], [], 0, [], 'community5', [])
        communitylist.append(community5)
    if numbercommunities > 5:
        community6 = Community(communityvalues[5], [], 0, [], 'community6', [])
        communitylist.append(community6)
    if numbercommunities > 6:
        community7 = Community(communityvalues[6], [], 0, [], 'community7', [])
        communitylist.append(community7)
    if numbercommunities > 7:
        community8 = Community(communityvalues[7], [], 0, [], 'community8', [])
        communitylist.append(community8)
    if numbercommunities > 8:
        community9 = Community(communityvalues[8], [], 0, [], 'community9', [])
        communitylist.append(community9)
    if numbercommunities > 9:
        community10 = Community(communityvalues[9], [], 0, [], 'community10', [])
        communitylist.append(community10)
    if numbercommunities > 10:
        community11 = Community(communityvalues[10], [], 0, [], 'community11', [])
        communitylist.append(community11)
    if numbercommunities > 11:
        community12 = Community(communityvalues[11], [], 0, [], 'community12', [])
        communitylist.append(community12)
    if numbercommunities > 12:
        community13 = Community(communityvalues[12], [], 0, [], 'community13', [])
        communitylist.append(community13)
    if numbercommunities > 13:
        community14 = Community(communityvalues[13], [], 0, [], 'community14', [])
        communitylist.append(community14)
    if numbercommunities > 14:
        community15 = Community(communityvalues[14], [], 0, [], 'community15', [])
        communitylist.append(community15)
    return communitylist

def generateCommunities2():
    # Used without web form
    communitylist = []
    community1 = Community('tribe1', [], 0, [], 'community1', [])
    communitylist.append(community1)
    community2 = Community('tribe2', [], 0, [], 'community2', [])
    communitylist.append(community2)
    community3 = Community('tribe3', [], 0, [], 'community3', [])
    communitylist.append(community3)
    community4 = Community('tribe4', [], 0, [], 'community4', [])
    communitylist.append(community4)
    community5 = Community('tribe5', [], 0, [], 'community5', [])
    communitylist.append(community5)
    return communitylist


def getCommunity(communityname, communitylist):
    community = 'name'
    for i in communitylist:
        if i.name == communityname:
            community = i
    return community


# Return total number of civilians in this community across all of a militant's regions
def totalcommunity(civilianlist, currentmilitant, currentcommunity):
    totalcommunity = 0
    for i in currentmilitant.regions:
        for j in civilianlist:
            if j.region == i:
                if j.community == currentcommunity:
                    totalcommunity += 1
    return totalcommunity


# For a community, return total current civilian support
def totalcommunitysupport(civilianlist, currentmilitant, currentcommunity):
    totalcommunitysupport = 0
    for i in currentmilitant.regions:
        for j in civilianlist:
            if j.region == i:
                if j.community == currentcommunity:
                    if j.militantsupport[currentmilitant.index] == 1:
                        totalcommunitysupport += 1
    return totalcommunitysupport


# Converting propensities into community-based format and adding to community propensities attribute
def addPropensities(communitylist, propensities):
    for i in communitylist:
        for j in propensities:
            i.updatePropensity(j[communitylist.index(i)])
