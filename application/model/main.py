from application.model.initconditions import civilianlist, regionlist, communitylist, militantlist, extortionrate, civsupportrate, \
    militantoutputlist, envoutput, terrorfactor, scatter, interventionpoint, interventionstop, affiliations, grievances,\
    rounds, varnegotiate, varnegotiatemil, varinfocampaign, varbenefitintervention, wealthregions,\
    wealthcommunities, varopponents, varfundmilitants, varcuttingoff, varattacking, weaponsregions, vartrainbump, interventionlist,\
    varleaderbenefits, varmilitantbenefits
from application.model.defend import checkDefend
from application.model.community import getCommunity
from application.model.support import getCivsupport, updateCommunitySupport, checkOppSupport, whichOpponent, checkIntimidated
from application.model.benefit import benefitProb
from application.model.punish import enemyList, strengthRatios, punishDecide, punishing
from application.model.variables import updateOpps, communityMatrix, addCivilians, generateDefend
from application.model.fight import fight
from application.model.intervention import negotiate, infocampaign, supportgovernance, increasewealth, leaderbenefits, militantbenefits, \
conditionalbenefits, fundmilitants, cuttingoff, attackmilitants, attacksupporters, weaponsremoval, \
    trainassist, protection, negotiatemilitants

# Array for graphing support distribution
communitysupportgraph = []

r = 0


while r < rounds:
    negotiatemil = [['None', 'None', 0]]
    erodesupport = [['None'], 0]
    punishsupport = [['None'], 0]
    benefitintervention = [['None'], 0]
    trainbump = [['None', 0]]
    extprotect = [['None'], 0]
    attackingmilitants = False

    if r >= interventionpoint and r < interventionstop:
        if interventionlist[0] == True:
            negotiate(communitylist, militantlist, affiliations, r, interventionpoint, varnegotiate)
        if interventionlist[1] == True:
            negotiatemil = negotiatemilitants(varnegotiatemil) #no effectiveness change
        if interventionlist[2] == True:
            infocampaign(communitylist, militantlist, grievances, r, interventionpoint, varinfocampaign) #take ave of 20 rounds on/off
        if interventionlist[3] == True:
            benefitintervention = supportgovernance(varbenefitintervention) #no effectiveness change
        if interventionlist[4] == True:
            increasewealth(civilianlist, wealthregions, wealthcommunities, r, interventionpoint, interventionstop) #done, see comments
        if interventionlist[5] == True:
            leaderbenefits(communitylist, militantlist, grievances, r, interventionpoint, varleaderbenefits)
        if interventionlist[6] == True:
            militantbenefits(communitylist, militantlist, grievances, r, interventionpoint, varmilitantbenefits)
        if interventionlist[7] == True:
            erodesupport = conditionalbenefits(varopponents) #no effectiveness change
        if interventionlist[8] == True:
            fundmilitants(militantlist, varfundmilitants, r, interventionpoint) #no effectiveness change
        if interventionlist[9] == True:
            cuttingoff(militantlist, varcuttingoff, r, interventionpoint) #no effectiveness change
        if interventionlist[10] == True:
            attackingmilitants = True #no effectiveness change
        if interventionlist[11] == True:
            punishsupport = attacksupporters(varopponents) #no effectiveness change
        if interventionlist[12] == True:
            weaponsremoval(regionlist, weaponsregions, r, interventionpoint, False) #take ave of 20 rounds on/off
        if interventionlist[13] == True:
            trainbump = trainassist(vartrainbump) #no effectiveness change
        if interventionlist[14] == True:
            extprotect = protection(varopponents) #no effectiveness change


    for m in militantlist:
        # Reset militant attributes at the beginning of each round
        m.deviants = 1
        m.notorietycount = 0
        m.strength = m.extincome + m.initstrength
        if m.strength < 1:
            m.strength = 1
        # Reset counter variable storage for militant output variables
        totalextort = 0
        countextort = 0
        countbenefit = 0
        countpunish = 0
        countsupport = 0
        totalsupport = 0
        countdefend = 0
        communitysupport = communityMatrix(m.communities)
        civ = 0
        # Approaching one civilian at a time
        for c in m.civilians:
            currentcommunity = getCommunity(c.community, communitylist)
            # Interactions with civilians with allied communities
            if currentcommunity.support[m.index] == 'allied':
                extortion = m.extort(c.wealthnum, extortionrate)
                totalextort += extortion  # Output variable counter
                countextort += 1  # Output variable counter
                benefit = benefitProb(m, m.ratiocutoff, benefitintervention)
                if benefit is True:
                    countbenefit += 1  # Output variable counter
                intimidated = checkIntimidated(c, m, militantlist)
                civsupport = getCivsupport(benefit, m, currentcommunity, intimidated, erodesupport)
                c.updateSupport(m, civsupport)
                supportamt = m.addSupport(c.wealthnum, civsupportrate, civsupport, trainbump)  # For counter
                totalsupport += supportamt  # Output variable counter
                if civsupport is True:
                    countsupport += 1  # Output variable counter

            # Interactions with civilians with neutral communities
            elif currentcommunity.support[m.index] == 'neutral':
                extortion = m.extort(c.wealthnum, extortionrate)
                totalextort += extortion  # Output variable counter
                countextort += 1  # Output variable counter
                enemylist = enemyList(c, m, militantlist)
                if len(enemylist) != 0:
                    m.deviants += 1
                    ratiolist = strengthRatios(m, enemylist)
                    punish = punishDecide(ratiolist, m.terrorist, terrorfactor, extprotect, m)
                    if punish is True:
                        countpunish += 1  # Output variable counter
                    punishing(m, punish)
                benefit = benefitProb(m, m.ratiocutoff, benefitintervention)
                if benefit is True:
                    countbenefit += 1  # Output variable counter
                intimidated = checkIntimidated(c, m, militantlist)
                civsupport = getCivsupport(benefit, m, currentcommunity, intimidated, erodesupport)
                c.updateSupport(m, civsupport)
                supportamt = m.addSupport(c.wealthnum, civsupportrate, civsupport, trainbump)  # For counter
                totalsupport += supportamt  # Output variable counter
                if civsupport is True:
                    countsupport += 1  # Output variable counter
                else:
                    if checkOppSupport(m) is True:
                        supported_opponent = whichOpponent(m, militantlist, c, punishsupport)
                        if supported_opponent[0] is True:
                            supported_opponent = supported_opponent[1]
                            c.updateSupport(supported_opponent, True)
                            supportamount = supported_opponent.addSupport(c.wealthnum, civsupportrate, True, trainbump)
                            updateOpps(supportamount, supported_opponent, militantoutputlist)

            # Interactions with civilians with enemy communities
            # Always punishes if there are no opponents to protect
            elif currentcommunity.support[m.index] == 'enemy':
                m.deviants += 1
                punish = False
                enemylist = enemyList(c, m, militantlist)
                if len(enemylist) != 0:
                    ratiolist = strengthRatios(m, enemylist)
                    punish = punishDecide(ratiolist, m.terrorist, terrorfactor, extprotect, m)
                    punishing(m, punish)
                else:
                    punish = True
                    punishing(m, punish)
                # Civilian may choose to defend
                if punish is True:
                    countpunish += 1  # Output variable counter
                    defend = checkDefend(c, m, regionlist)
                    if defend is True:
                        countdefend += 1
                        currentcommunity.updateDefend(1)
                    else:
                        countsupport += 1  # Output variable counter
                # If militant doesn't punish, it may benefit
                else:
                    benefit = benefitProb(m, m.ratiocutoff, benefitintervention)
                    if benefit is True:
                        countbenefit += 1  # Output variable counter
                    intimidated = checkIntimidated(c, m, militantlist)
                    civsupport = getCivsupport(benefit, m, currentcommunity, intimidated, erodesupport)
                    c.updateSupport(m, civsupport)
                    supportamt = m.addSupport(c.wealthnum, civsupportrate, civsupport, trainbump)
                    totalsupport += supportamt  # Output variable counter
                    if civsupport is True:
                        countsupport += 1  # Output variable counter
            civ += 1

        if attackingmilitants is True:
            attackmilitants(militantlist, varattacking)

        # Updating militant notoriety ratio at the end of one militant's interactions with all civilians
        m.notorietyratio = m.notorietycount / m.deviants

        # Updating total community support at the end of one militant's interactions with all civilians
        communitysupportgraph.append(updateCommunitySupport(m, civilianlist, communitylist))
        communitysupport = addCivilians(civilianlist, communitysupport, m)

        # Updating list of variables of interest and adding them to a militant output object
        militantoutputlist[m.index].updateCounts(m.strength, m.notorietyratio, communitysupport, totalextort,
                                                 countextort, countbenefit, countpunish, countsupport, totalsupport,
                                                 countdefend, m.deviants)
    # Compiling list of fighting militants and adding them to an environment output object
    fightlist = fight(militantlist, militantoutputlist, r, negotiatemil)
    envoutput.updateFighting(fightlist)

    # Compiling list of community defending and adding them to an environment output object
    defendlist = generateDefend(communitylist)
    envoutput.updateDefending(defendlist)
    for i in communitylist:
        i.updateDefend(0)

    # Next round
    r += 1

