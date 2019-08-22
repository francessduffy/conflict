class Militant(object):

    def __init__(self, name, index, extincome, strength, initstrength, notorietycount, regions, communities, totalcivilians,
                 maxsupportincome, tempprop, civilians, deviants, notorietyratio, terrorist, ratiocutoff):
        self.name = name
        self.index = index
        self.extincome = extincome
        self.strength = strength
        self.initstrength = initstrength
        self.notorietycount = notorietycount
        self.regions = regions
        self.communities = communities
        self.totalcivilians = totalcivilians
        self.maxsupportincome = maxsupportincome
        self.tempprop = tempprop
        self.civilians = civilians
        self.deviants = deviants
        self.notorietyratio = notorietyratio
        self.terrorist = terrorist
        self.ratiocutoff = ratiocutoff

    # Generates attribute list of communities based on active regions
    def generateCommunities(self, regionlist):
        for i in self.regions:
            for j in regionlist:
                if i == j.name:
                    for k in j.communities:
                        self.communities.append(k)
        self.communities = set(self.communities)
        self.communities = list(self.communities)

    # Extorts civilian and adds strength to self
    def extort(self, civilianwealth, extortionrate):
        self.strength += civilianwealth * extortionrate
        return civilianwealth * extortionrate

    # Adds support value to strength if the civilian supports the militant
    def addSupport(self, civilianwealth, civsupportrate, civsupport, trainbump):
        supportamt = 0
        if civsupport is True:
            self.strength += civilianwealth * civsupportrate
            for i in trainbump:
                if self.name == i[0]:
                    self.strength += i[1]
            supportamt = civilianwealth * civsupportrate
        return supportamt

    # Calculates total number of civilians in militant regions and their total incomes, makes civilian lists
    def calculate(self, civilianlist, civsupportrate):
        self.strength += self.extincome + self.initstrength
        totalcivilians = 0
        maxsupportincome = 0
        for i in self.regions:
            for j in civilianlist:
                if i == j.region:
                    maxsupportincome += j.wealthnum
                    totalcivilians += 1
                    self.civilians.append(j)
        self.totalcivilians = totalcivilians
        self.maxsupportincome = maxsupportincome * civsupportrate

    # Adds one (or can subtract one) civilian to its notoriety count and updates current notoriety count
    def notorietyRatio(self, count):
        self.notorietycount += count


def generateMilitants(militantvalues):
    militantlist = []
    numbermilitants = len(militantvalues)
    if numbermilitants > 0:
        militant1 = Militant(militantvalues[0][0], 0, militantvalues[0][1], 1, militantvalues[0][2], 0, militantvalues[0][5], [], 0, 0, '', [], 1, 0, militantvalues[0][3], militantvalues[0][4])
        militantlist.append(militant1)
    if numbermilitants > 1:
        militant2 = Militant(militantvalues[1][0], 1, militantvalues[1][1], 1, militantvalues[1][2], 0, militantvalues[1][5], [], 0, 0, '', [], 1, 0, militantvalues[1][3], militantvalues[1][4])
        militantlist.append(militant2)
    if numbermilitants > 2:
        militant3 = Militant(militantvalues[2][0], 2, militantvalues[2][1], 1, militantvalues[2][2], 0, militantvalues[2][5], [], 0, 0, '', [], 1, 0, militantvalues[2][3], militantvalues[2][4])
        militantlist.append(militant3)
    if numbermilitants > 3:
        militant4 = Militant(militantvalues[3][0], 3, militantvalues[3][1], 1, militantvalues[3][2], 0, militantvalues[3][5], [], 0, 0, '', [], 1, 0, militantvalues[3][3], militantvalues[3][4])
        militantlist.append(militant4)
    if numbermilitants > 4:
        militant5 = Militant(militantvalues[4][0], 4, militantvalues[4][1], 1, militantvalues[4][2], 0, militantvalues[4][5], [], 0, 0, '', [], 1, 0, militantvalues[4][3], militantvalues[4][4])
        militantlist.append(militant5)
    if numbermilitants > 5:
        militant6 = Militant(militantvalues[5][0], 5, militantvalues[5][1], 1, militantvalues[5][2], 0, militantvalues[5][5], [], 0, 0, '', [], 1, 0, militantvalues[5][3], militantvalues[5][4])
        militantlist.append(militant6)
    if numbermilitants > 6:
        militant7 = Militant(militantvalues[6][0], 6, militantvalues[6][1], 1, militantvalues[6][2], 0, militantvalues[6][5], [], 0, 0, '', [], 1, 0, militantvalues[6][3], militantvalues[6][4])
        militantlist.append(militant7)
    if numbermilitants > 7:
        militant8 = Militant(militantvalues[7][0], 7, militantvalues[7][1], 1, militantvalues[7][2], 0, militantvalues[7][5], [], 0, 0, '', [], 1, 0, militantvalues[7][3], militantvalues[7][4])
        militantlist.append(militant8)
    if numbermilitants > 8:
        militant9 = Militant(militantvalues[8][0], 8, militantvalues[8][1], 1, militantvalues[8][2], 0, militantvalues[8][5], [], 0, 0, '', [], 1, 0, militantvalues[8][3], militantvalues[8][4])
        militantlist.append(militant9)
    if numbermilitants > 9:
        militant10 = Militant(militantvalues[9][0], 9, militantvalues[9][1], 1, militantvalues[9][2], 0, militantvalues[9][5], [], 0, 0, '', [], 1, 0, militantvalues[9][3], militantvalues[9][4])
        militantlist.append(militant10)
    if numbermilitants > 10:
        militant11 = Militant(militantvalues[10][0], 10, militantvalues[10][1], 1, militantvalues[10][2], 0, militantvalues[10][5], [], 0, 0, '', [], 1, 0, militantvalues[10][3], militantvalues[10][4])
        militantlist.append(militant11)
    if numbermilitants > 11:
        militant12 = Militant(militantvalues[11][0], 11, militantvalues[11][1], 1, militantvalues[11][2], 0, militantvalues[11][5], [], 0, 0, '', [], 1, 0, militantvalues[11][3], militantvalues[11][4])
        militantlist.append(militant12)
    if numbermilitants > 12:
        militant13 = Militant(militantvalues[12][0], 12, militantvalues[12][1], 1, militantvalues[12][2], 0, militantvalues[12][5], [], 0, 0, '', [], 1, 0, militantvalues[12][3], militantvalues[12][4])
        militantlist.append(militant13)
    if numbermilitants > 13:
        militant14 = Militant(militantvalues[13][0], 13, militantvalues[13][1], 1, militantvalues[13][2], 0, militantvalues[13][5], [], 0, 0, '', [], 1, 0, militantvalues[13][3], militantvalues[13][4])
        militantlist.append(militant14)
    if numbermilitants > 14:
        militant15 = Militant(militantvalues[14][0], 14, militantvalues[14][1], 1, militantvalues[14][2], 0, militantvalues[14][5], [], 0, 0, '', [], 1, 0, militantvalues[14][3], militantvalues[14][4])
        militantlist.append(militant15)
    return militantlist
    # ! Strength must be a value > 1

def generateMilitants2():
    # Used without web form
    militantlist = []
    militant1 = Militant('militant1', 0, 1000, 1, 500, 0, ['region1'], [], 0, 0, '', [], 1, 0, False, 4)
    militantlist.append(militant1)
    militant2 = Militant('militant2', 1, 2000, 1, 0, 0, ['region1'], [], 0, 0, '', [], 1, 0, False, 4)
    militantlist.append(militant2)
    militant3 = Militant('militant3', 2, 500, 1, 0, 0, ['region1'], [], 0, 0, '', [], 1, 0, True, 4)
    militantlist.append(militant3)
    return militantlist