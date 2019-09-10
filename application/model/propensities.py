import copy

def calculatePropensities(communitylist, militantlist, grievances, affiliations):
    propensities = copy.deepcopy(affiliations)
    # creating initial values to be replaced, making a copy of affiliations just for its dimensions
    m = 0
    while m < len(militantlist):
        c = 0
        x = 0
        while c < len(communitylist):
            dummy = 0
            x = 0
            while x <(len(grievances[c])):
                if grievances[c][x] ==0:
                    x=x+1
                else:
                    if affiliations[m][x] < 1:
                        dummy = dummy + 1
                    else:
                        dummy = dummy -1
                    x=x+1
            dummy = dummy + affiliations[m][c]
            if dummy > 0:
                propensities[m][c] = 1
            if dummy == 0:
                propensities[m][c] = 0
            if dummy < 0:
                propensities[m][c] = -1
            c = c+1
        m=m+1
    return(propensities)


# for each row (i.e. community)
# 1: If a community has a grievance towards another community x, check x propensity towards the militant
# 2: If the value is 0 or -1, add +1 to dummy value. If the value is 1, subtract -1 from dummy value
# 3: If a community has a grievance towards another community x, check x propensity towards the militant
# 4: If the value is 0 or -1, add +1 to dummy value. If the value is 1, subtract -1 from dummy value
# 5: Add original community affiliation to dummy value. If >0, change its propensity towards the group to 1. If = 0,
# change to 0. If <0, change to -1
