class Region(object):

    def __init__(self, name, communities, weapons):
        self.name = name
        self.weapons = weapons
        self.communities = communities

    def updateWeapons(self, weapons):
        self.weapons = weapons
        return self.weapons


def generateRegions(regionvalues):
    regionlist = []
    numberregions = len(regionvalues)
    if numberregions > 0:
        region1 = Region(regionvalues[0][0], regionvalues[0][2], regionvalues[0][1])
        regionlist.append(region1)
    if numberregions > 1:
        region2 = Region(regionvalues[1][0], regionvalues[1][2], regionvalues[1][1])
        regionlist.append(region2)
    if numberregions > 2:
        region3 = Region(regionvalues[2][0], regionvalues[2][2], regionvalues[2][1])
        regionlist.append(region3)
    if numberregions > 3:
        region4 = Region(regionvalues[3][0], regionvalues[3][2], regionvalues[3][1])
        regionlist.append(region4)
    if numberregions > 4:
        region5 = Region(regionvalues[4][0], regionvalues[4][2], regionvalues[4][1])
        regionlist.append(region5)
    if numberregions > 5:
        region6 = Region(regionvalues[5][0], regionvalues[5][2], regionvalues[5][1])
        regionlist.append(region6)
    if numberregions > 6:
        region7 = Region(regionvalues[6][0], regionvalues[6][2], regionvalues[6][1])
        regionlist.append(region7)
    if numberregions > 7:
        region8 = Region(regionvalues[7][0], regionvalues[7][2], regionvalues[7][1])
        regionlist.append(region8)
    if numberregions > 8:
        region9 = Region(regionvalues[8][0], regionvalues[8][2], regionvalues[8][1])
        regionlist.append(region9)
    if numberregions > 9:
        region10 = Region(regionvalues[9][0], regionvalues[9][2], regionvalues[9][1])
        regionlist.append(region10)
    if numberregions > 10:
        region11 = Region(regionvalues[10][0], regionvalues[10][2], regionvalues[10][1])
        regionlist.append(region11)
    if numberregions > 11:
        region12 = Region(regionvalues[11][0], regionvalues[11][2], regionvalues[11][1])
        regionlist.append(region12)
    if numberregions > 12:
        region13 = Region(regionvalues[12][0], regionvalues[12][2], regionvalues[12][1])
        regionlist.append(region13)
    if numberregions > 13:
        region14 = Region(regionvalues[13][0], regionvalues[13][2], regionvalues[13][1])
        regionlist.append(region14)
    if numberregions > 14:
        region15 = Region(regionvalues[14][0], regionvalues[14][2], regionvalues[14][1])
        regionlist.append(region15)
    return regionlist

def generateRegions2():
    # Used without web form
    regionlist = []
    region1 = Region('region1', ['tribe1', 'tribe2', 'tribe3', 'tribe4', 'tribe5'], True)
    regionlist.append(region1)
    return regionlist
