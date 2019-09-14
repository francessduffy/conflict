def reset_variables():
    from application.model.main import envoutput, militantlist, militantoutputlist, rounds, regionlist, communitylist, civilianlist, fightlist, defendlist
    from application.model.initconditions import varfundmilitants
    from runpy import run_path

    for i in militantoutputlist:
        del i
    x = 0
    for i in militantoutputlist:
        militantoutputlist[x].strength = []
        militantoutputlist[x].notorietyratio = []
        militantoutputlist[x].communitysupport = []
        militantoutputlist[x].totalextort = []
        militantoutputlist[x].countextort = []
        militantoutputlist[x].countbenefit = []
        militantoutputlist[x].countpunish =[]
        militantoutputlist[x].countsupport = []
        militantoutputlist[x].totalsupport = []
        militantoutputlist[x].countdefend = []
        militantoutputlist[x].oppsupport = 0
        militantoutputlist[x].oppsupportcount = 0
        x += 1

    envoutput.fightlist = []
    envoutput.defendlist = []

    for m in militantlist:
        for i in varfundmilitants:
            if i[0] == m.name:
                m.extincome = m.extincome - i[1]

    for i in civilianlist:
        del i
    for i in regionlist:
        del i
    for i in communitylist:
        del i
    for i in militantlist:
        del i
    for i in fightlist:
        del i
    for i in defendlist:
        del i
    run_path('/opt/python/current/app/application/model/initconditions.py')
    run_path('/opt/python/current/app/application/model/main.py')


    # print('civilianlist values before:')
    # print('region:', civilianlist[0].region)
    # print('community:', civilianlist[0].community)
    # print('wealth:', civilianlist[0].wealth)
    # print('wealthnum:', civilianlist[0].wealthnum)
    # print('militantsupport:', civilianlist[0].militantsupport)
    #
    # print('regionlist values before:')
    # print('name:', regionlist[0].name)
    # print('weapons:', regionlist[0].weapons)
    # print('communities:', regionlist[0].communities)
    #
    # print('communitylist values before:')
    # print('name:', communitylist[0].name)
    # print('support:', communitylist[0].support)
    # print('defend:', communitylist[0].defend)
    # print('propensityvalues:', communitylist[0].propensityvalues)
    # print('reference:', communitylist[0].reference)
    # print('population:', communitylist[0].population)

    # x = 0
    # for i in civilianlist:
    #     civilianlist[x].region = ''
    #     civilianlist[x].community = ''
    #     civilianlist[x].wealth = ''
    #     civilianlist[x].wealthnum = 0
    #     civilianlist[x].militantsupport = []
    #     x += 1
    #
    # x = 0
    # for i in regionlist:
    #     regionlist[x].name = ''
    #     regionlist[x].weapons = True
    #     regionlist[x].communities = []
    #     x += 1
    #
    # x = 0
    # for i in communitylist:
    #     communitylist[x].name = ''
    #     communitylist[x].support = []
    #     communitylist[x].defend = 0
    #     communitylist[x].propensityvalues = []
    #     communitylist[x].reference = ''
    #     communitylist[x].population = []
    #     x += 1
    #
    # x = 0
    # for i in militantlist:
    #     militantlist[x].name = ''
    #     militantlist[x].index = 0
    #     militantlist[x].extincome = 0
    #     militantlist[x].strength = 1
    #     militantlist[x].initstrength = 0
    #     militantlist[x].notorietycount = 0
    #     militantlist[x].regions = []
    #     militantlist[x].communities = []
    #     militantlist[x].totalcivilians = 0
    #     militantlist[x].maxsupportincome = 0
    #     militantlist[x].tempprop = ''
    #     militantlist[x].civilians = []
    #     militantlist[x].deviants = 1
    #     militantlist[x].notorietyratio = 0
    #     militantlist[x].terrorist = False
    #     militantlist[x].ratiocutoff = 4
    #     x += 1