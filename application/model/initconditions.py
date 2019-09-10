from application.model.civilian import generateCivilians
from application.model.region import generateRegions, generateRegions2
from application.model.community import generateCommunities, generateCommunities2, addPropensities, totalcommunity
from application.model.militant import generateMilitants, generateMilitants2
from application.model.propensities import calculatePropensities
from application.model.variables import generateOutputList, EnvOutput
from application.parameters import get_parameters, intervention_values

import random
import matplotlib.pyplot as plt

parameters = get_parameters()
wealthValues = parameters[0]
extortionrate = parameters[1]
civsupportrate = parameters[2]
terrorfactor = parameters[3]
regionvalues = parameters[4]
militantvalues = parameters[5]
wealths = parameters[6]
affiliations = parameters[7]
grievances = parameters[8]
communityvalues = parameters[9]


# wealths = [[[20, 168, 12], [70, 28, 2], [14, 5, 1], [56, 23, 1], [15, 126, 9]]]
# grievances = [[0, 0, 0, 0, -1], [-1, 0, 0, 0, 0], [-1, 0, 0, -1, -1], [0, 0, 0, 0, -1], [-1, 0, 0, 0, 0]]
# affiliations = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]]
# wealthValues = [20, 100, 500]
# extortionrate = .1
# civsupportrate = .1
# terrorfactor = .9

# Number of rounds by which steady state is reached (for intervention)
rounds = 234
interventionpoint = 182
interventionstop = 2340

# Community support standard deviation
commsuppstdv = 3

# Whether to print support in terms of percentages or numbers
percentage = True

# Generating list of region objects from region.py
regionlist = generateRegions(regionvalues)
# regionlist = generateRegions2()

# Generating list of community objects from community.py
communitylist = generateCommunities(communityvalues)
# communitylist = generateCommunities2()

# Generating list of militant objects from militant.py
militantlist = generateMilitants(militantvalues)
# militantlist = generateMilitants2()

# Generating list of civilian objects from civilianclass.py
civilianlist = generateCivilians(regionlist, communitylist, militantlist, wealths, wealthValues)
random.shuffle(civilianlist)

# Generating endogenous attributes for militant objects
for m in militantlist:
    m.calculate(civilianlist, civsupportrate)

# Generating communities attribute based on regions
for m in militantlist:
    m.generateCommunities(regionlist)

# Generating list of propensities from propensities.py
propensities = calculatePropensities(communitylist, militantlist, grievances, affiliations)

# Generating propensityvalues attribute for communities from community.py
addPropensities(communitylist, propensities)

# Generating list of initial community support based on propensities from community.py
for i in communitylist:
    i.initSupport()

# Generating community population attribute: populations of community per militant
for i in communitylist:
    for m in militantlist:
        communitypop = totalcommunity(civilianlist, m, i.name)
        i.population.append(communitypop)

# Generating list of (empty) output values from variables.py
militantoutputlist = generateOutputList(militantlist)

# Generating matrix of fighting activity from fight.py
envoutput = EnvOutput()

# Generating intervention values
interventionvalues = intervention_values(grievances, affiliations, militantlist)
varnegotiate = interventionvalues[0]
varnegotiatemil = interventionvalues[1]
varinfocampaign = interventionvalues[2]
varbenefitintervention = interventionvalues[3]
wealthregions = interventionvalues[4]
wealthcommunities = interventionvalues[5]
varopponents = interventionvalues[6]
varfundmilitants = interventionvalues[7]
varcuttingoff = interventionvalues[8]
varattacking = interventionvalues[9]
weaponsregions = interventionvalues[10]
vartrainbump = interventionvalues[11]
interventionlist = interventionvalues[12]
varleaderbenefits = interventionvalues[13]
varmilitantbenefits = interventionvalues[14]

# Make scatter plots of any values of interest from throughout program
def scatter(array):
    xvalues, yvalues = zip(*array)
    plt.figure(0)

    # plt.xlabel('percentage of civilians providing support to militant')
    # plt.ylabel('community support: enemy = 1, neutral = 2, allied = 3')
    # plt.title("Community Support Distribution")
    # plt.legend()
    plt.scatter(xvalues, yvalues)

    # Probability of Benefiting p1
    # plt.xlabel('ratio of external income over maximum internal support')
    # plt.ylabel('probability of militant providing benefits')
    # plt.title("Benefit Probability (p1) at benefit threshold = 1")
    # xvaluestrimmed = xvalues[:21]
    # yvaluestrimmed = yvalues[:21]
    # print(xvaluestrimmed)
    # z = np.polyfit(xvaluestrimmed, yvaluestrimmed, 1)
    # p = np.poly1d(z)
    # plt.plot(xvalues, p(xvalues), "r--")
    # plt.ylim(0, 1)

    plt.show()

