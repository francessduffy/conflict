from random import choices
from application.model.initconditions import scatter


def enemyList(currentcivilian, currentmilitant, militantlist):
    # Returns indices of civilian support matrix, representing the militants the civilian supports
    enemyindex = [i for i, e in enumerate(currentcivilian.militantsupport) if e == 1]
    enemylist = []
    # Makes list of militants with matching indices
    for i in enemyindex:
        for j in militantlist:
            if j.index  == i:
                enemylist.append(j)
    # Removes militant that matches current militant
    for i in enemylist:
        if i == currentmilitant:
            enemylist.remove(i)
    return enemylist


# Calculate strength ratios to each of other supported groups
# Only implement if enemylist does not equal 0. if it equals 0, militant doesnt punish and move to next action.
# If this is an enemy, skip to punish(True) regardless; free to punish enemies without protection.
def strengthRatios(currentmilitant, enemylist):
    ratiolist = []
    for i in enemylist:
        strengthratios = []
        ratio = i.strength/currentmilitant.strength
        strengthratios.append(i.name)
        strengthratios.append(ratio)
        ratioList(strengthratios, ratiolist)
    return ratiolist


# Create new matrix item for strengthRatios(). Form: [[militant name, ratio], [militant name, ratio]]
def ratioList(strengthRatios, ratiolist):
    ratiolist.append(strengthRatios)


# Compare strength ratios, determine if group will punish support for another group
def punishDecide(ratiolist, terrorist, terrorfactor, extprotect, m):
    punish = False
    i = 0
    while i < len(ratiolist):
        if ratiolist[i][1] > 2:
            ratiolist[i][1] = 2
        p3 = (2- ratiolist[i][1])/2
        if terrorist == True:
            p3 = terrorfactor
        for j in extprotect[0]:
            if j == m.name:
                p3 -= p3*extprotect[1]
        truefalse = [True, False]
        probability = [p3, 1 - p3]
        punish = choices(truefalse, probability)
        punish = punish[0]
        if punish == False:
            i = len(ratiolist)+1
        i += 1
    if len(ratiolist) == 0:
        punish = False
    return punish


# Implement punish
def punishing(currentmilitant, punish):
    if punish == True:
        currentmilitant.notorietyRatio(1)

# Plot p3 distribution
# x = 0
# punisharray = []
# while x <= 2:
#     p3 = (2-x)/2
#     x += .1
#     punisharray.append((x, p3))
# scatter(punisharray)