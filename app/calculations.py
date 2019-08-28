import pandas as pd
from numpy import mean

def calculations(df, militants, communities, militantnames, communitynames):
    dict = ['strength1', 'strength2', 'strength3', 'strength4', 'strength5', 'strength6', 'strength7', 'strength8', 'strength9', 'strength10', 'strength11', 'strength12', 'strength13', 'strength14', 'strength15', 'community1defend', 'community2defend', 'community3defend', 'community4defend', 'community5defend', 'community6defend', 'community7defend', 'community8defend', 'community9defend', 'community10defend', 'community11defend', 'community12defend', 'community13defend', 'community14defend', 'community15defend', 'oneandtwo', 'oneandthree', 'oneandfour', 'oneandfive', 'oneandsix', 'oneandseven', 'oneandeight', 'oneandnine', 'oneandten', 'oneandeleven', 'oneandtwelve', 'oneandthirteen', 'oneandfourteen', 'oneandfifteen', 'twoandthree', 'twoandfour', 'twoandfive', 'twoandsix', 'twoandseven', 'twoandeight', 'twoandnine', 'twoandten', 'twoandeleven', 'twoandtwelve', 'twoandthirteen', 'twoandfourteen', 'twoandfifteen', 'threeandfour', 'threeandfive', 'threeandsix', 'threeandseven', 'threeandeight', 'threeandnine', 'threeandten', 'threeandeleven', 'threeandtwelve', 'threeandthirteen', 'threeandfourteen', 'threeandfifteen', 'fourandfive', 'fourandsix', 'fourandseven', 'fourandeight', 'fourandnine', 'fourandten', 'fourandeleven', 'fourandtwelve', 'fourandthirteen', 'fourandfourteen', 'fourandfifteen', 'fiveandsix', 'fiveandseven', 'fiveandeight', 'fiveandnine', 'fiveandten', 'fiveandeleven', 'fiveandtwelve', 'fiveandthirteen', 'fiveandfourteen', 'fiveandfifteen', 'sixandseven', 'sixandeight', 'sixandnine', 'sixandten', 'sixandeleven', 'sixandtwelve', 'sixandthirteen', 'sixandfourteen', 'sixandfifteen', 'sevenandeight', 'sevenandnine', 'sevenandten', 'sevenandeleven', 'sevenandtwelve', 'sevenandthirteen', 'sevenandfourteen', 'sevenandfifteen', 'eightandnine', 'eightandten', 'eightandeleven', 'eightandtwelve', 'eightandthirteen', 'eightandfourteen', 'eightandfifteen', 'nineandten', 'nineandeleven', 'nineandtwelve', 'nineandthirteen', 'nineandfourteen', 'nineandfifteen', 'tenandeleven', 'tenandtwelve', 'tenandthirteen', 'tenandfourteen', 'tenandfifteen', 'elevenandtwelve', 'elevenandthirteen', 'elevenandfourteen', 'elevenandfifteen', 'twelveandthirteen', 'twelveandfourteen', 'twelveandfifteen', 'thirteenandfourteen', 'thirteenandfifteen', 'fourteenandfifteen']
    results_list = []
    for i in dict:
        column = df[i]
        pre = column[155:180]
        post = column[207:233]
        avepre = round(float(mean(pre)), 2)
        avepost = round(float(mean(post)), 2)
        if avepre == 0 and avepost == 0:
            change = int(0)
        elif avepre == 0 and avepost!= 0:
            change = int(100)
        else:
            change = int((-(avepre - avepost)/avepre)*100)
        list = [avepre, avepost, change]
        results_list.append(list)

    # Creating new column labels for results
    newmilitantnames = []
    for i in militantnames:
        newmilitantnames.append(i)
    newcommunitynames = []
    for i in communitynames:
        newcommunitynames.append(i)
    x = 15 - len(militantnames)
    while x > 0:
        newmilitantnames.append('None')
        x -= 1
    x = 15 - len(communitynames)
    while x > 0:
        newcommunitynames.append('None')
        x -= 1
    communitylist = []
    for i in newcommunitynames:
        newname = i + ' ' + 'defending'
        communitylist.append(newname)

    fightinglist = ['oneandtwo', 'oneandthree', 'oneandfour', 'oneandfive', 'oneandsix', 'oneandseven', 'oneandeight', 'oneandnine', 'oneandten', 'oneandeleven', 'oneandtwelve', 'oneandthirteen', 'oneandfourteen', 'oneandfifteen', 'twoandthree', 'twoandfour', 'twoandfive', 'twoandsix', 'twoandseven', 'twoandeight', 'twoandnine', 'twoandten', 'twoandeleven', 'twoandtwelve', 'twoandthirteen', 'twoandfourteen', 'twoandfifteen', 'threeandfour', 'threeandfive', 'threeandsix', 'threeandseven', 'threeandeight', 'threeandnine', 'threeandten', 'threeandeleven', 'threeandtwelve', 'threeandthirteen', 'threeandfourteen', 'threeandfifteen', 'fourandfive', 'fourandsix', 'fourandseven', 'fourandeight', 'fourandnine', 'fourandten', 'fourandeleven', 'fourandtwelve', 'fourandthirteen', 'fourandfourteen', 'fourandfifteen', 'fiveandsix', 'fiveandseven', 'fiveandeight', 'fiveandnine', 'fiveandten', 'fiveandeleven', 'fiveandtwelve', 'fiveandthirteen', 'fiveandfourteen', 'fiveandfifteen', 'sixandseven', 'sixandeight', 'sixandnine', 'sixandten', 'sixandeleven', 'sixandtwelve', 'sixandthirteen', 'sixandfourteen', 'sixandfifteen', 'sevenandeight', 'sevenandnine', 'sevenandten', 'sevenandeleven', 'sevenandtwelve', 'sevenandthirteen', 'sevenandfourteen', 'sevenandfifteen', 'eightandnine', 'eightandten', 'eightandeleven', 'eightandtwelve', 'eightandthirteen', 'eightandfourteen', 'eightandfifteen', 'nineandten', 'nineandeleven', 'nineandtwelve', 'nineandthirteen', 'nineandfourteen', 'nineandfifteen', 'tenandeleven', 'tenandtwelve', 'tenandthirteen', 'tenandfourteen', 'tenandfifteen', 'elevenandtwelve', 'elevenandthirteen', 'elevenandfourteen', 'elevenandfifteen', 'twelveandthirteen', 'twelveandfourteen', 'twelveandfifteen', 'thirteenandfourteen', 'thirteenandfifteen', 'fourteenandfifteen']
    newname = ''
    x = 0
    for i in fightinglist:
        if i.find('one') == 0:
            rightstring = i.lstrip('one')
            newname = newmilitantnames[0]+ ' ' + rightstring
        if i.find('two') == 0:
            rightstring = i.lstrip('two')
            newname = newmilitantnames[1]+ ' ' + rightstring
        if i.find('three') == 0:
            rightstring = i.lstrip('three')
            newname = newmilitantnames[2]+ ' ' + rightstring
        if i.find('four') == 0:
            rightstring = i.lstrip('four')
            newname = newmilitantnames[3]+ ' ' + rightstring
        if i.find('five') == 0:
            rightstring = i.lstrip('five')
            newname = newmilitantnames[4]+ ' ' + rightstring
        if i.find('six') == 0:
            rightstring = i.lstrip('six')
            newname = newmilitantnames[5]+ ' ' + rightstring
        if i.find('seven') == 0:
            rightstring = i.lstrip('seven')
            newname = newmilitantnames[6]+ ' ' + rightstring
        if i.find('eight') == 0:
            rightstring = i.lstrip('eight')
            newname = newmilitantnames[7]+ ' ' + rightstring
        if i.find('nine') == 0:
            rightstring = i.lstrip('nine')
            newname = newmilitantnames[8]+ ' ' + rightstring
        if i.find('ten') == 0:
            rightstring = i.lstrip('ten')
            newname = newmilitantnames[9]+ ' ' + rightstring
        if i.find('eleven') == 0:
            rightstring = i.lstrip('eleven')
            newname = newmilitantnames[10]+ ' ' + rightstring
        if i.find('twelve') == 0:
            rightstring = i.lstrip('twelve')
            newname = newmilitantnames[11]+ ' ' + rightstring
        if i.find('thirteen') == 0:
            rightstring = i.lstrip('thirteen')
            newname = newmilitantnames[12]+ ' ' + rightstring
        if i.find('fourteen') == 0:
            rightstring = i.lstrip('fourteen')
            newname = newmilitantnames[13]+ ' ' + rightstring
        if i.find('fifteen') == 0:
            rightstring = i.lstrip('fifteen')
            newname = newmilitantnames[14]+ ' ' + rightstring
        fightinglist[x] = newname
        x += 1
    x = 0
    for i in fightinglist:
        if i.find('one') > 0:
            rightstring = i.rstrip('one')
            newname = rightstring + ' ' + newmilitantnames[0]
        if i.find('two') > 0:
            rightstring = i.rstrip('two')
            newname = rightstring + ' ' + newmilitantnames[1]
        if i.find('three') > 0:
            rightstring = i.rstrip('three')
            newname = rightstring + ' ' + newmilitantnames[2]
        if i.find('four') > 0:
            rightstring = i.rstrip('four')
            newname = rightstring + ' ' + newmilitantnames[3]
        if i.find('five') > 0:
            rightstring = i.rstrip('five')
            newname = rightstring + ' ' + newmilitantnames[4]
        if i.find('six') > 0:
            rightstring = i.rstrip('six')
            newname = rightstring + ' ' + newmilitantnames[5]
        if i.find('seven') > 0:
            rightstring = i.rstrip('seven')
            newname = rightstring + ' ' + newmilitantnames[6]
        if i.find('eight') > 0:
            rightstring = i.rstrip('eight')
            newname = rightstring + ' ' + newmilitantnames[7]
        if i.find('nine') > 0:
            rightstring = i.rstrip('nine')
            newname = rightstring + ' ' + newmilitantnames[8]
        if i.find('ten') > 0:
            rightstring = i.rstrip('ten')
            newname = rightstring + ' ' + newmilitantnames[9]
        if i.find('eleven') > 0:
            rightstring = i.rstrip('eleven')
            newname = rightstring + ' ' + newmilitantnames[10]
        if i.find('twelve') > 0:
            rightstring = i.rstrip('twelve')
            newname = rightstring + ' ' + newmilitantnames[11]
        if i.find('thirteen') > 0:
            rightstring = i.rstrip('thirteen')
            newname = rightstring + ' ' + newmilitantnames[12]
        if i.find('fourteen') > 0:
            rightstring = i.rstrip('fourteen')
            newname = rightstring + ' ' + newmilitantnames[13]
        if i.find('fifteen') > 0:
            rightstring = i.rstrip('fifteen')
            newname = rightstring + ' ' + newmilitantnames[14]
        fightinglist[x] = newname
        x += 1

    # Creating full results dataframe
    results_df = pd.DataFrame(results_list, columns=['before', 'after', '% change'])
    # _index = ['militant 1', 'militant 2', 'militant 3', 'militant 4', 'militant 5', 'militant 6', 'militant 7', 'militant 8', 'militant 9', 'militant 10', 'militant 11', 'militant 12', 'militant 13', 'militant 14', 'militant 15', 'community1defend', 'community2defend', 'community3defend', 'community4defend', 'community5defend', 'community6defend', 'community7defend', 'community8defend', 'community9defend', 'community10defend', 'community11defend', 'community12defend', 'community13defend', 'community14defend', 'community15defend', 'oneandtwo', 'oneandthree', 'oneandfour', 'oneandfive', 'oneandsix', 'oneandseven', 'oneandeight', 'oneandnine', 'oneandten', 'oneandeleven', 'oneandtwelve', 'oneandthirteen', 'oneandfourteen', 'oneandfifteen', 'twoandthree', 'twoandfour', 'twoandfive', 'twoandsix', 'twoandseven', 'twoandeight', 'twoandnine', 'twoandten', 'twoandeleven', 'twoandtwelve', 'twoandthirteen', 'twoandfourteen', 'twoandfifteen', 'threeandfour', 'threeandfive', 'threeandsix', 'threeandseven', 'threeandeight', 'threeandnine', 'threeandten', 'threeandeleven', 'threeandtwelve', 'threeandthirteen', 'threeandfourteen', 'threeandfifteen', 'fourandfive', 'fourandsix', 'fourandseven', 'fourandeight', 'fourandnine', 'fourandten', 'fourandeleven', 'fourandtwelve', 'fourandthirteen', 'fourandfourteen', 'fourandfifteen', 'fiveandsix', 'fiveandseven', 'fiveandeight', 'fiveandnine', 'fiveandten', 'fiveandeleven', 'fiveandtwelve', 'fiveandthirteen', 'fiveandfourteen', 'fiveandfifteen', 'sixandseven', 'sixandeight', 'sixandnine', 'sixandten', 'sixandeleven', 'sixandtwelve', 'sixandthirteen', 'sixandfourteen', 'sixandfifteen', 'sevenandeight', 'sevenandnine', 'sevenandten', 'sevenandeleven', 'sevenandtwelve', 'sevenandthirteen', 'sevenandfourteen', 'sevenandfifteen', 'eightandnine', 'eightandten', 'eightandeleven', 'eightandtwelve', 'eightandthirteen', 'eightandfourteen', 'eightandfifteen', 'nineandten', 'nineandeleven', 'nineandtwelve', 'nineandthirteen', 'nineandfourteen', 'nineandfifteen', 'tenandeleven', 'tenandtwelve', 'tenandthirteen', 'tenandfourteen', 'tenandfifteen', 'elevenandtwelve', 'elevenandthirteen', 'elevenandfourteen', 'elevenandfifteen', 'twelveandthirteen', 'twelveandfourteen', 'twelveandfifteen', 'thirteenandfourteen', 'thirteenandfifteen', 'fourteenandfifteen']
    _index = newmilitantnames + communitylist + fightinglist
    results_df.index = _index
    results_df = results_df.transpose()

    # Creating strength dataframes and returning strongest militant
    # index between 0 and 15
    # ie, if # militants = 3,  DESIRED_INDEX = 3
    DESIRED_INDEX = militants
    strength_df = results_df.iloc[0:,:DESIRED_INDEX]


    # Ranked militants
    strength_df = strength_df.transpose()
    strength_labels1 = strength_df.index.values
    strength_labels = []
    for i in strength_labels1:
        strength_labels.append(i+' strength')
    ranked_by_strength_df = strength_df.sort_values(by=['after'], axis=0, ascending=False)

    # Creating fighting dataframe
    # sets of numbers between 30 and 135
    # ie, if # militants = 3, set = [30, 31, 44]
    fighting_df = results_df.iloc[0:, [30, 31, 44]]
    if militants == 2:
        fighting_df = results_df.iloc[0:, [30]]
    elif militants == 3:
        fighting_df = results_df.iloc[0:,[30, 31, 44]]
    elif militants == 4:
        fighting_df = results_df.iloc[0:, [30, 31, 32, 44, 45, 57]]
    elif militants == 5:
        fighting_df = results_df.iloc[0:, [30, 31, 32, 33, 44, 45, 46, 57, 58, 69]]
    elif militants == 6:
        fighting_df = results_df.iloc[0:, [30, 31, 32, 33, 34, 44, 45, 46, 47, 57, 58, 59, 69, 70, 80]]
    elif militants == 7:
        fighting_df = results_df.iloc[0:, [30, 31, 32, 33, 34, 35, 44, 45, 46, 47, 48, 57, 58, 59, 60, 69, 70, 71, 80, 81, 90]]
    elif militants == 8:
        fighting_df = results_df.iloc[0:, [30, 31, 32, 33, 34, 35, 36, 44, 45, 46, 47, 48, 49, 57, 58, 59, 60, 61, 69, 70, 71, 72, 80, 81, 82, 90, 91, 99]]
    elif militants == 9:
        fighting_df = results_df.iloc[0:, [30, 31, 32, 33, 34, 35, 36, 37, 44, 45, 46, 47, 48, 49, 50, 57, 58, 59, 60, 61, 62, 69, 70, 71, 72, 73, 80, 81, 82, 83, 90, 91, 92, 99, 100, 107]]
    elif militants == 10:
        fighting_df = results_df.iloc[0:, [30, 31, 32, 33, 34, 35, 36, 37, 38, 44, 45, 46, 47, 48, 49, 50, 51, 57, 58, 59, 60, 61, 62, 63, 69, 70, 71, 72, 73, 74, 80, 81, 82, 83, 84, 90, 91, 92, 93, 99, 100, 101, 107, 108, 114]]
    elif militants == 11:
        fighting_df = results_df.iloc[0:, [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 44, 45, 46, 47, 48, 49, 50, 51, 52, 57, 58, 59, 60, 61, 62, 63, 64, 69, 70, 71, 72, 73, 74, 75, 80, 81, 82, 83, 84, 85, 90, 91, 92, 93, 94, 99, 100, 101, 102, 107, 108, 109, 114, 115, 120]]
    elif militants == 12:
        fighting_df = results_df.iloc[0:, [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 57, 58, 59, 60, 61, 62, 63, 64, 65, 69, 70, 71, 72, 73, 74, 75, 76, 80, 81, 82, 83, 84, 85, 86, 90, 91, 92, 93, 94, 95, 99, 100, 101, 102, 103, 107, 108, 109, 110, 114, 115, 116, 120, 121, 125]]
    elif militants == 13:
        fighting_df = results_df.iloc[0:, [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 69, 70, 71, 72, 73, 74, 75, 76, 77, 80, 81, 82, 83, 84, 85, 86, 87, 90, 91, 92, 93, 94, 95, 96, 99, 100, 101, 102, 103, 104, 107, 108, 109, 110, 111, 114, 115, 116, 117, 120, 121, 122, 125, 126, 129]]
    elif militants == 14:
        fighting_df = results_df.iloc[0:, [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 107, 108, 109, 110, 111, 112, 114, 115, 116, 117, 118, 120, 121, 122, 123, 125, 126, 127, 129, 130, 132]]
    elif militants == 15:
        fighting_df = results_df.iloc[0:, 30:]
    fighting_df = fighting_df.transpose()
    fighting_labels = fighting_df.index.values

    # Creating defending dataframe
    # index between 16 and 29
    # ie, if # communities = 5, DESIRED_INDEX = 20
    defending_df = results_df.iloc[0:, 15:20]
    if communities == 1:
        defending_df = results_df.iloc[0:, 15]
    elif communities == 2:
        defending_df = results_df.iloc[0:, 15:17]
    elif communities == 3:
        defending_df = results_df.iloc[0:, 15:18]
    elif communities == 4:
        defending_df = results_df.iloc[0:, 15:19]
    elif communities == 5:
        defending_df = results_df.iloc[0:, 15:20]
    elif communities == 6:
        defending_df = results_df.iloc[0:, 15:21]
    elif communities == 7:
        defending_df = results_df.iloc[0:, 15:22]
    elif communities == 8:
        defending_df = results_df.iloc[0:, 15:23]
    elif communities == 9:
        defending_df = results_df.iloc[0:, 15:24]
    elif communities == 10:
        defending_df = results_df.iloc[0:, 15:25]
    elif communities == 11:
        defending_df = results_df.iloc[0:, 15:26]
    elif communities == 12:
        defending_df = results_df.iloc[0:, 15:27]
    elif communities == 13:
        defending_df = results_df.iloc[0:, 15:28]
    elif communities == 14:
        defending_df = results_df.iloc[0:, 15:29]
    elif communities == 15:
        defending_df = results_df.iloc[0:,15:30]
    defending_df = defending_df.transpose()
    defending_labels = defending_df.index.values

    return(strength_df, ranked_by_strength_df, fighting_df, defending_df, strength_labels, fighting_labels, defending_labels)


def summary_results(results_dataframes, militantnames):
    ranked_by_strength_df = results_dataframes[1]
    fighting_df = results_dataframes[2]
    defending_df = results_dataframes[3]

    # Finding strongest militant
    # strongest_militant_name = 'militant1'
    # strongest_militant_index = ranked_by_strength_df.index[0]
    # strongest_militant_index = int(strongest_militant_index[8:])
    # x = 0
    # for i in militantnames:
    #     if x == (strongest_militant_index - 1):
    #         strongest_militant_name = i
    #         x += 1
    strongest_militant_name = ranked_by_strength_df.index[0]
    if strongest_militant_name == 'government' or strongest_militant_name == 'Government':
        strongest_militant_name = 'the government'
    strongest_militant_strength = int(ranked_by_strength_df.iloc[0,1])
    # print('The strongest militant is', strongest_militant_name, 'with a strength of', strongest_militant_strength)

    # Finding the average change in percent likelihood of fighting
    list = []
    listpre = []
    listpost = []
    fighting_df = fighting_df.transpose()
    for i in fighting_df:
        list.append(fighting_df[i]['% change'])
        listpre.append(fighting_df[i]['before'])
        listpost.append(fighting_df[i]['after'])
    fighting_average_change = int(mean(list))
    fightingpre = round(float(mean(listpre)), 2)
    fightingpost = round(float(mean(listpost)), 2)
    if fighting_average_change == 0:
        fightingchange = 'not changed'
        fighting_average_change = ''
    else:
        if fighting_average_change > 0:
            fightingchange = 'increased by '
            fighting_average_change = str(fighting_average_change) + '%'
        else:
            fightingchange = 'decreased by '
            fighting_average_change = str(fighting_average_change) + '%'

    # Finding the total change in defending
    listpre = []
    listpost = []
    defending_df = defending_df.transpose()
    for i in defending_df:
       listpre.append(defending_df[i]['before'])
    for i in defending_df:
        listpost.append(defending_df[i]['after'])
    pretotal = sum(listpre)
    posttotal = sum(listpost)
    try:
        defending_total_change = int(-((pretotal-posttotal)/pretotal)*100)
    except ValueError:
        defending_total_change = 0
    if defending_total_change == 0:
        defendingchange = 'not changed'
        defending_total_change = ''
    else:
        if defending_total_change > 0:
            defendingchange = 'increased by '
            defending_total_change = str(defending_total_change) + '%'
        else:
            defendingchange = 'decreased by '
            defending_total_change = str(defending_total_change) + '%'

    return strongest_militant_name, strongest_militant_strength, fighting_average_change, defending_total_change, fightingchange, fightingpre, fightingpost, defendingchange
