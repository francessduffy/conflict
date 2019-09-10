from random import choices
from application.model.initconditions import scatter
import numpy as np


def benefitProb(militant, ratiocutoff, benefitintervention):
    if militant.maxsupportincome == 0:
        militant.maxsupportincome = 1
    benefitratio = militant.extincome / militant.maxsupportincome
    x = np.random.logistic(ratiocutoff, 1)
    if x < 0:
        x = .001
    p1 = 1-((benefitratio/x)/2)
    if p1 < 0:
        p1 = 0
    for i in benefitintervention[0]:
        if i == militant.name:
            p1 = p1 + (p1*benefitintervention[1])
    if p1 > 1:
        p1 = 1
    truefalse = [True, False]
    probability = [p1, 1-p1]
    benefit = choices(truefalse, probability)
    return benefit[0]

# Graphing distribution
# def graphbenefitProb(ratiocutoff):
#     array = []
#     i = 1
#     while i < 101:
#         benefitratio = i/10
#         x = np.random.logistic(ratiocutoff, .2)
#         if x < 0:
#             x = .001
#         p1 = 1 - ((benefitratio / x) / 2)
#         if p1 < 0:
#             p1 = 0
#         array.append((benefitratio, p1))
#         i += 1
#     scatter(array)
#
# graphbenefitProb(1)




# Determines whether militant benefits based on probability given extincome/maxsupport
# If the ratio is about equal to a cutoff value, there is a 50% chance of benefiting that decreases as external income
# increases

# First generates cutoff ratio value that varies around a mean
# Then creates probability such that when the ratio equals the cutoff value, there is a 50/50 chance that the group does
# not provide benefits, and the probability increases as the ratio approaches being twice that of the cutoff. The
# probability of benefits increases as the ratio gets increasingly less than the cutoff
# 1-((benefitratio/x)/2) because otherwise the probability approaches 1 as external income increases
