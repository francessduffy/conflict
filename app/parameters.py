import pandas as pd
import copy

def create_name_lists(communityvalues, regionvalues, militantvalues):
    regionnames = []
    militantnames = []
    communitynames = communityvalues
    for i in regionvalues:
        regionnames.append(i[0])
    for j in militantvalues:
        militantnames.append(j[0])
    return (communitynames, regionnames, militantnames)


def generate_grievances(boxlist):
    if boxlist == []:
        boxlist = [[]]
    grievances = []
    z = 0
    for i in boxlist:
        list = []
        x = 0
        for j in i:
            y = 0
            if j == True:
                y = 1
            else:
                y = 0
            if z == x:
                list.append(0)
                list.append(y)
            else:
                list.append(y)
            x += 1
        grievances.append(list)
        z += 1
    grievances[len(grievances)-1].append(0)
    return grievances


def generate_affiliations(boxmlist):
    affiliations = []
    x = 0
    while x < len(boxmlist[0]):
        y = 0
        list = []
        for i in boxmlist:
            if i[x] == True:
                y = 1
            else:
                y = 0
            list.append(y)
        x += 1
        affiliations.append(list)
    return affiliations


def generate_wealths(regionpercents, communitypercents, wealthdistributions, totalpopulation):
    wealths = []
    count = 0
    for i in regionpercents:
        regpop = i * totalpopulation
        list = []
        count2 = 0
        for j in communitypercents[count]:
            commpop = j * regpop
            sublist = []
            for k in wealthdistributions[count2]:
                x = k * commpop
                sublist.append(x)
            list.append(sublist)
            count2 += 1
        wealths.append(list)
        count += 1

    # Round all numbers to closest int or up to 1
    for i in wealths:
        for j in i:
            x = 0
            for k in j:
                if k > 1:
                    j[x] = round(k)
                else:
                    j[x] = 1
                x += 1

    # Find the smallest number in the matrix and determine factor value
    factor = 1
    x = wealths[0][0][0]
    for i in wealths:
        for j in i:
            for k in j:
                if k < x and k != 0:
                    x = k
    if x/1 >1 and x/1 < 10:
        factor = 1
    if x/10 >1 and x/10 < 10:
        factor = 10
    if x/100 >1 and x/100 < 10:
        factor = 100
    if x/1000 >1 and x/1000 < 10:
        factor = 1000
    if x/10000 >1 and x/10000 < 10:
        factor = 10000
    if x/100000 >1 and x/100000 < 10:
        factor = 100000

    # Reduce all numbers by factor value and round
    for i in wealths:
        for j in i:
            x = 0
            for k in j:
                if j[x] > factor:
                    j[x] = round(k/factor)
                else:
                    j[x] = 1
                x += 1

    # If the sum of all civilians is greater than 1000, reduce values again
    sum = 0
    for i in wealths:
        for j in i:
            for k in j:
                sum = sum + k
    if sum > 1000:
        for i in wealths:
            for j in i:
                x = 0
                for k in j:
                    if j[x] > 10:
                        j[x] = round(k / 10)
                    else:
                        j[x] = 1
                    x += 1

    return wealths


def create_militant_regionlist(militantregionlist, militantvalues, regionnames):
    allregions = []
    x = 0
    for i in militantvalues:
        list = []
        y = 0
        for j in militantregionlist[x]:
            if j is True:
                list.append(regionnames[y])
            y += 1
        x += 1
        allregions.append(list)
    x = 0
    for i in militantvalues:
        i.append(allregions[x])
        x += 1
    return militantvalues


def create_region_communitylist(communitynames, communitypercents, regionvalues):
    allcommunities = []
    x = 0
    for i in regionvalues:
        list = []
        y = 0
        for j in communitypercents[x]:
            if j > 0:
                list.append(communitynames[y])
            y +=1
        x += 1
        allcommunities.append(list)
    x = 0
    for i in regionvalues:
        i.append(allcommunities[x])
        x += 1
    return regionvalues

def get_parameters():
    form1 = pd.read_csv('/Users/Frances/python/conflict/app/model/static2/form1.csv')
    regionvalues = pd.read_csv('/Users/Frances/python/conflict/app/model/static2/regionvalues.csv')
    communityvalues = pd.read_csv('/Users/Frances/python/conflict/app/model/static2/communityvalues.csv')
    militantvalues = pd.read_csv('/Users/Frances/python/conflict/app/model/static2/militantvalues.csv')
    communitypercents = pd.read_csv('/Users/Frances/python/conflict/app/model/static2/communitypercents.csv')
    boxlist = pd.read_csv('/Users/Frances/python/conflict/app/model/static2/boxlist.csv')
    boxmlist = pd.read_csv('/Users/Frances/python/conflict/app/model/static2/boxmlist.csv')
    militantregionlist = pd.read_csv('/Users/Frances/python/conflict/app/model/static2/militantregionlist.csv')
    form1 = form1.values.tolist()
    regionvalues = regionvalues.values.tolist()
    communityvalues = communityvalues.values.tolist()
    militantvalues = militantvalues.values.tolist()
    communitypercents = communitypercents.values.tolist()
    boxlist = boxlist.values.tolist()
    boxmlist = boxmlist.values.tolist()
    militantregionlist = militantregionlist.values.tolist()

    # Form1 variables
    totalpopulation = form1[0][0]
    numberregions = form1[0][1]
    numbercommunities = form1[0][2]
    numbermilitants = form1[0][3]
    l_wealth = form1[0][4]
    m_wealth = form1[0][5]
    h_wealth = form1[0][6]
    wealthValues = [l_wealth, m_wealth, h_wealth]
    extortionrate = form1[0][7]
    civsupportrate = form1[0][8]
    terrorfactor = form1[0][9]

    # Remove indices
    for i in regionvalues:
        i.pop(0)
    for i in communityvalues:
        i.pop(0)
    for i in militantvalues:
        i.pop(0)
    for i in communitypercents:
        i.pop(0)
    for i in boxlist:
        i.pop(0)
    for i in boxmlist:
        i.pop(0)
    for i in militantregionlist:
        i.pop(0)

    # Make wealth distributions and limit communityvalues to names
    new_communityvalues = []
    for i in communityvalues:
        new_communityvalues.append(i[0])
        i.pop(0)
    wealthdistributions = communityvalues
    communityvalues = new_communityvalues

    # Make regionpercents and remove percent values from regionvalues
    regionpercents = []
    for i in regionvalues:
        regionpercents.append(i[1])
        i.pop(1)

    # Swap terrorist & benefitcutoff values in militantvalues
    for i in militantvalues:
        x = i[3]
        i.pop(3)
        i.append(x)

    name_lists = create_name_lists(communityvalues, regionvalues, militantvalues)
    communitynames = name_lists[0]
    regionnames = name_lists[1]
    militantnames = name_lists[2]

    wealths = generate_wealths(regionpercents, communitypercents, wealthdistributions, totalpopulation)
    militantvalues = create_militant_regionlist(militantregionlist, militantvalues, regionnames)
    regionvalues = create_region_communitylist(communitynames, communitypercents, regionvalues)
    grievances = generate_grievances(boxlist)
    affiliations = generate_affiliations(boxmlist)

    return wealthValues, extortionrate, civsupportrate, terrorfactor, regionvalues, militantvalues, wealths, affiliations, grievances, communitynames, regionnames, militantnames, boxlist, boxmlist


def intervention_values(grievances, affiliations, militantlist):
    form4 = pd.read_csv('/Users/Frances/python/conflict/app/model/static2/form4.csv')
    supported_militants = str(form4.at[0,'supported_militants'])
    opposed_militants = str(form4.at[0, 'opposed_militants'])
    negotiating_militants = [form4.at[0, 'mil1'], form4.at[0, 'mil2']]
    percentcutoff = form4.at[0, 'cutoffamt']
    fundsupport = form4.at[0, 'fundmilamt']
    wealthregions = str(form4.at[0, 'wealthregions'])
    wealthcommunities = str(form4.at[0, 'wealthcomms'])
    weaponsregions = str(form4.at[0, 'weaponsregions'])
    interventionlist = [form4.at[0, 'negotiate'], form4.at[0, 'negotiate2'], form4.at[0, 'infocampaign'], form4.at[0, 'supportmilgov'], form4.at[0, 'civwealth'], form4.at[0, 'commbenefits'], form4.at[0, 'milbenefits'], form4.at[0, 'civbenefits'], form4.at[0, 'fundmil'], form4.at[0, 'cutoff'], form4.at[0, 'attack'], form4.at[0, 'punish'], form4.at[0, 'weapons'], form4.at[0, 'trainequip'], form4.at[0, 'protect']]

    # Trimming commas and spaces to create lists
    if supported_militants == 'nan':
        supported_militants = ['None']
    else:
        supported_militants = supported_militants.split(',')
    if opposed_militants == 'nan':
        opposed_militants = ['None']
    else:
        opposed_militants = opposed_militants.split(',')
    if wealthregions == 'nan':
        wealthregions = ['None']
    else:
        wealthregions = wealthregions.split(',')
    if wealthcommunities == 'nan':
        wealthcommunities = ['None']
    else:
        wealthcommunities = wealthcommunities.split(',')
    if weaponsregions == 'nan':
        weaponsregions = ['None']
    else:
        weaponsregions = weaponsregions.split(',')
    x = 0
    for i in supported_militants:
        supported_militants[x] = i.strip()
        x += 1
    x = 0
    for i in opposed_militants:
        opposed_militants[x] = i.strip()
        x += 1
    x = 0
    for i in wealthregions:
        wealthregions[x] = i.strip()
        x += 1
    x = 0
    for i in wealthcommunities:
        wealthcommunities[x] = i.strip()
        x += 1
    x = 0
    for i in weaponsregions:
        weaponsregions[x] = i.strip()
        x += 1


    # Indices for supported and opposed militants
    supported_indices = []
    opposed_indices = []
    for i in supported_militants:
        for j in militantlist:
            if i == j.name:
                supported_indices.append(j.index)
    for i in opposed_militants:
        for j in militantlist:
            if i == j.name:
                opposed_indices.append(j.index)


    # varnegotiate
    varnegotiate = []
    x = 0
    while x < len(grievances):
        list = []
        y = 0
        while y < len(grievances):
            list.append(0)
            y += 1
        varnegotiate.append(list)
        x += 1

    # varnegotiatemil
    varnegotiatemil = [[negotiating_militants[0], negotiating_militants[1], .5]]

    # varinfocampaign
    varinfocampaign = copy.deepcopy(affiliations)
    x = 0
    while x < len(varinfocampaign):
        y = 0
        while y < len(varinfocampaign[0]):
            for i in supported_indices:
                if i == x:
                    varinfocampaign[x][y] = 1
            y += 1
        x += 1
    x = 0
    while x < len(varinfocampaign):
        y = 0
        while y < len(varinfocampaign[0]):
            for i in opposed_indices:
                if i == x:
                    varinfocampaign[x][y] = 0
            y += 1
        x += 1


    # varbenefitintervention
    varbenefitintervention = [supported_militants, .5]


    # varleaderbenefits
    varleaderbenefits = copy.deepcopy(affiliations)
    x = 0
    while x < len(varleaderbenefits):
        y = 0
        while y < len(varleaderbenefits[0]):
            for i in opposed_indices:
                if i == x:
                    varleaderbenefits[x][y] = 0
            y += 1
        x += 1

    # varmilitantbenefits
    varmilitantbenefits = copy.deepcopy(affiliations)
    x = 0
    while x < len(varmilitantbenefits):
        y = 0
        while y < len(varmilitantbenefits[0]):
            for i in supported_indices:
                if i == x:
                    varmilitantbenefits[x][y] = 1
            y += 1
        x += 1

    # varerodesupport, varpunishsupport, varextprotect
    varopponents = [opposed_militants, .5]

    # varfundmilitants
    varfundmilitants = []
    for i in supported_militants:
        list = []
        list.append(i)
        list.append(fundsupport)
        varfundmilitants.append(list)

    # varcuttingoff
    varcuttingoff = []
    income = 1000
    for i in opposed_militants:
        for j in militantlist:
            if j.name == i:
                income = j.extincome
        list = []
        list.append(i)
        list.append(income*percentcutoff)
        varcuttingoff.append(list)

    # varattacking
    varattacking = []
    strength = 1000
    for i in opposed_militants:
        for j in militantlist:
            if j.name == i:
                strength = j.strength
        list = []
        list.append(i)
        list.append(strength*.5)
        varattacking.append(list)

    # vartrainbump
    vartrainbump = []
    for i in supported_militants:
        list = []
        list.append(i)
        list.append(10)
        vartrainbump.append(list)

    return varnegotiate, varnegotiatemil, varinfocampaign, varbenefitintervention, wealthregions, wealthcommunities, varopponents, varfundmilitants, varcuttingoff, varattacking, weaponsregions, vartrainbump, interventionlist, varleaderbenefits, varmilitantbenefits


