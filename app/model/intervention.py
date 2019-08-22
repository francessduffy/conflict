from app.model.initconditions import calculatePropensities, addPropensities, wealthValues
from app.model.community import totalcommunity


# 1. Negotiating disputes between communities: remove grievances
def negotiate(communitylist, militantlist, affiliations, r, interventionpoint, newgrievances):
    if r == interventionpoint:
        grievances = newgrievances
        propensities = calculatePropensities(communitylist, militantlist, grievances, affiliations)
        for i in communitylist:
            i.propensityvalues = []
            i.support = []
        addPropensities(communitylist, propensities)
        for i in communitylist:
            i.initSupport()


# WORKING
# 2. Negotiating agreements between militant groups
def negotiatemilitants(militants):
    negotiatemil = militants
    return negotiatemil


# WORKING
# 3. Waging information campaigns against ideology: remove affiliations
def infocampaign(communitylist, militantlist, grievances, r, interventionpoint, newaffiliations):
    if r == interventionpoint:
        affiliations = newaffiliations
        propensities = calculatePropensities(communitylist, militantlist, grievances, affiliations)
        for i in communitylist:
            i.propensityvalues = []
            i.support = []
        addPropensities(communitylist, propensities)
        for i in communitylist:
            i.initSupport()


# WORKING
# 4. Providing governance benefits for militants to pass on: increase benefit probability
def supportgovernance(militants):
    benefitintervention = militants
    return benefitintervention


# WORKING
# 5. Increasing the wealth of civilians: make more civilians richer
def increasewealth(civilianlist, regions, communities, r, interventionpoint, interventionstop):
    if r == interventionpoint:
        for i in civilianlist:
            if i.wealth == 'L':
                for k in regions:
                    if i.region == k:
                        for j in communities:
                            if i.community == j:
                                i.wealth = 'MM'
                                i.wealthnum = wealthValues[1]
    # for 50% effectiveness
    # if r == interventionpoint:
    #     x = 1
    #     for i in civilianlist:
    #         if x % 2 != 0:
    #             if i.wealth == 'L':
    #                 if i.region == region:
    #                     for j in communities:
    #                         if i.community == j:
    #                             i.wealth = 'MM'
    #                             i.wealthnum = wealthValues[1]
    #         x += 1
    if r == interventionstop:
        for i in civilianlist:
            if i.wealth == 'MM':
                i.wealth = 'L'
                i.wealthnum = wealthValues[0]


# WORKING
# 6. Providing in-kind benefits to community leaders: remove affiliations
def leaderbenefits(communitylist, militantlist, grievances, r, interventionpoint, newaffiliations):
    if r == interventionpoint:
        affiliations = newaffiliations
        propensities = calculatePropensities(communitylist, militantlist, grievances, affiliations)
        for i in communitylist:
            i.propensityvalues = []
            i.support = []
        addPropensities(communitylist, propensities)
        for i in communitylist:
            i.initSupport()


# WORKING
# 7. Providing in-kind benefits to militants to pass on: add affiliations
def militantbenefits(communitylist, militantlist, grievances, r, interventionpoint, newaffiliations):
    if r == interventionpoint:
        affiliations = newaffiliations
        propensities = calculatePropensities(communitylist, militantlist, grievances, affiliations)
        for i in communitylist:
            i.propensityvalues = []
            i.support = []
        addPropensities(communitylist, propensities)
        for i in communitylist:
            i.initSupport()


# WORKING
# 8. Providing civilians with conditional benefits: remove civilian support/reduce probability
def conditionalbenefits(militants):
    erodesupport = militants
    return erodesupport


# WORKING
# 9. Supporting militants income: add external income to militants
# Format of variable "militants": [['militant1', 1000], ['militant2', 2000]]
# Variable "conditionality" should be set equal to initconditions ratiocutoff if there is no conditionality that raises it
def fundmilitants(militantlist, militants, r, interventionpoint):
    if r == interventionpoint:
        for i in militants:
            for j in militantlist:
                if j.name == i[0]:
                    j.extincome += i[1]


# WORKING
# 10. Cutting off resources to militants: subtract external income
# Format of variable "militants": [['militant1', 1000], ['militant2', 2000]]
def cuttingoff(militantlist, militants, r, interventionpoint):
    if r == interventionpoint:
        for i in militants:
            for j in militantlist:
                if j.name == i[0]:
                    if j.extincome - i[1] > 1:
                        j.extincome -= i[1]
                    else:
                        j.extincome = 1


# WORKING
# 11. Attacking militants: subtract strength
# Format of variable "militants": [['militant1', 1000], ['militant2', 2000]]
def attackmilitants(militantlist, militants):
    for i in militants:
        for j in militantlist:
            if j.name == i[0]:
                j.initstrength -= i[1]


# WORKING
# 12. Punishing support: remove civilian support/reduce probability
def attacksupporters(militants):
    punishsupport = militants
    return punishsupport


# WORKING
# 13. Weapons removal: remove weapons presence
def weaponsremoval(regionlist, regionnames, r, interventionpoint, value):
    if r == interventionpoint:
        for i in regionlist:
            for j in regionnames:
                if i.name == j:
                    i.weapons = value

# WORKING
# 14. Providing military training & assistance: add strength outside external income
# Format of variable "trainbump": [['militant1', 10], ['militant2', 20]]
def trainassist(militants):
    trainbump = militants
    return trainbump


# WORKING
# 15. Protection from punishment: remove punishment
def protection(militants):
    extprotect = militants
    return extprotect




# # 11. Denying physical access: remove militants from regions
# def denyaccess(militantlist, civilianlist, regionlist, communitylist, civsupportrate, r, interventionpoint, matrix):
#     if r == interventionpoint:
#         for i in militantlist:
#             for j in matrix:
#                 if i.name == j[0]:
#                     for k in j[1]:
#                         i.regions.remove(k)
#                         i.civilians = []
#                         for x in civilianlist:
#                             if x.region == j[0]:
#                                 x.updateSupport(i, False)
#                         for c in communitylist:
#                             c.updateSupport(i, False)
#             i.calculate(civilianlist, civsupportrate)
#             i.generateCommunities(regionlist)
#         for c in communitylist:
#             for m in militantlist:
#                 communitypop = totalcommunity(civilianlist, m, c.name)
#                 c.population.append(communitypop)