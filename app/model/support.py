from app.model.initconditions import commsuppstdv, communitylist, scatter
from app.model.community import totalcommunity, totalcommunitysupport
import random
from random import choices
import numpy as np


# Determining whether or not a civilian supports a militant- generates probability and then uses it
def getCivsupport(benefit, currentmilitant, currentcommunity, intimidated, erodesupport):
    p2 = 0
    if currentcommunity.support[currentmilitant.index] == 'allied':
        if benefit is True:
            if currentcommunity.propensityvalues[currentmilitant.index] == -1:
                p2 = .5
            if currentcommunity.propensityvalues[currentmilitant.index] == 0:
                p2 = .75
            if currentcommunity.propensityvalues[currentmilitant.index] == 1:
                p2 = 1
        if benefit is False:
            if currentcommunity.propensityvalues[currentmilitant.index] == -1:
                p2 = .2
            if currentcommunity.propensityvalues[currentmilitant.index] == 0:
                p2 = .45
            if currentcommunity.propensityvalues[currentmilitant.index] == 1:
                p2 = .7
    if currentcommunity.support[currentmilitant.index] == 'neutral':
        if benefit is True:
            if currentcommunity.propensityvalues[currentmilitant.index] == -1:
                p2 = .25
            if currentcommunity.propensityvalues[currentmilitant.index] == 0:
                p2 = .5
            if currentcommunity.propensityvalues[currentmilitant.index] == 1:
                p2 = .75
        if benefit is False:
            if currentcommunity.propensityvalues[currentmilitant.index] == -1:
                p2 = 0
            if currentcommunity.propensityvalues[currentmilitant.index] == 0:
                p2 = .2
            if currentcommunity.propensityvalues[currentmilitant.index] == 1:
                p2 = .45
    if currentcommunity.support[currentmilitant.index] == 'enemy':
        if benefit is True:
            if currentcommunity.propensityvalues[currentmilitant.index] == -1:
                p2 = 0
            if currentcommunity.propensityvalues[currentmilitant.index] == 0:
                p2 = .25
            if currentcommunity.propensityvalues[currentmilitant.index] == 1:
                p2 = .5
    notorietyreduction = intimidated * p2
    p2 = p2 - notorietyreduction
    for i in erodesupport[0]:
        if i == currentmilitant.name:
            p2 = p2 - (p2*erodesupport[1])
    truefalse = [True, False]
    probability = [p2, 1 - p2]
    civsupport = choices(truefalse, probability)
    return civsupport[0]


def checkIntimidated(c, currentmilitant, militantlist):
    i = 0
    intimidated = 0
    while i < len(c.militantsupport):
        if c.militantsupport[i] == 1:
            for j in militantlist:
                if j.index != currentmilitant.index:
                    if j.index == i:
                        if j.notorietyratio > currentmilitant.notorietyratio:
                            if j.notorietyratio > intimidated:
                                intimidated = j.notorietyratio
        i += 1
    return intimidated


# Use notoriety ratio to randomly determine if civilian supports an opponent
# Ratio equals probability; the more notorious the less likely to support opponent
def checkOppSupport(currentmilitant):
    p4 = currentmilitant.notorietyratio
    truefalse = [True, False]
    probability = [1-p4, p4]
    supportopponentvalue = choices(truefalse, probability)
    return supportopponentvalue[0]


def whichOpponent(militant, militantlist, currentcivilian, punishsupport):
    currentregion = currentcivilian.region
    currentcommunity = currentcivilian.community
    opponents = []
    # for intervention, finding likelihood of ruling out support of militant
    truefalse = [True, False]
    probability = [punishsupport[1], 1-punishsupport[1]]
    removal = choices(truefalse, probability)
    # finds all other militants operating in the same region
    for i in militantlist:
        if i.name != militant.name:
            for x in punishsupport[0]:
                if i.name != x or removal is False:
                    i.tempprop = []
                    for j in i.regions:
                        if j == currentregion:
                            opponents.append(i)
    # Assigns propensity towards current community for each opponent
    x = True
    if len(opponents) == 1:
        supported_opponent = opponents[0]
    if len(opponents) == 0:
        supported_opponent = 'None'
        x = False
    if len(opponents) > 1:
        for i in opponents:
            for j in communitylist:
                if currentcommunity == j.name:
                    i.tempprop = j.propensityvalues[i.index]
        # Selects opponent of maximum propensity and creates list of its equals
        supported_opponent = opponents[0]
        equals = [opponents[0]]
        i = 0
        j = 1
        while j < len(opponents):
            if opponents[j].tempprop > supported_opponent.tempprop:
                supported_opponent = opponents[j]
                equals = [opponents[j]]
            elif opponents[j].tempprop == equals[0].tempprop:
                equals.append(opponents[j])
            i += 1
            j += 1
        # If there are opponents of equal propensities, selects randomly between them
        if len(equals) > 1:
            supported_opponent = random.choice(equals)
    return x, supported_opponent


# Updating all communities' support matrices at the end of current militant interactions with all civilians
def updateCommunitySupport(currentmilitant, civilianlist, communitylist):
    supportvalue = 'neutral'
    supportratio = 50
    yvalue = 2
    for i in currentmilitant.communities:
        threshold1 = int(np.random.logistic(66, commsuppstdv))
        threshold2 = int(np.random.logistic(33, commsuppstdv))
        total = totalcommunity(civilianlist, currentmilitant, i)
        if total == 0:
            total = 1
        count = totalcommunitysupport(civilianlist, currentmilitant, i)
        supportratio = int((count/total) * 100)
        if supportratio >= threshold1:
            supportvalue = 'allied'
            yvalue = 3
        elif supportratio > threshold2:
            supportvalue = 'neutral'
            yvalue = 2
        if supportratio < threshold2:
            supportvalue = 'enemy'
            yvalue = 1
        for j in communitylist:
            if j.name == i:
                j.updateSupport(currentmilitant, supportvalue)
    return supportratio, yvalue

# Plot p4 distribution
# x = 0
# supportenemyarray = []
# while x < .9:
#     p4 = 1-x
#     x += .1
#     supportenemyarray.append((x, p4))
# scatter(supportenemyarray)
