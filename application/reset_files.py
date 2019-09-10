import os
from shutil import copyfile
from application.reset_queues import reset_queues

def reset_files():

    os.remove('/opt/python/current/app/application/static/form1.csv')
    copyfile('/opt/python/current/app/application/static/examples/threemil_form1.csv', '/opt/python/current/app/application/static/form1.csv')

    os.remove('/opt/python/current/app/application/static/regionvalues.csv')
    copyfile('/opt/python/current/app/application/static/examples/threemil_regionvalues.csv', '/opt/python/current/app/application/static/regionvalues.csv')

    os.remove('/opt/python/current/app/application/static/communityvalues.csv')
    copyfile('/opt/python/current/app/application/static/examples/threemil_communityvalues.csv', '/opt/python/current/app/application/static/communityvalues.csv')

    os.remove('/opt/python/current/app/application/static/militantvalues.csv')
    copyfile('/opt/python/current/app/application/static/examples/threemil_militantvalues.csv', '/opt/python/current/app/application/static/militantvalues.csv')

    os.remove('/opt/python/current/app/application/static/communitypercents.csv')
    copyfile('/opt/python/current/app/application/static/examples/threemil_communitypercents.csv', '/opt/python/current/app/application/static/communitypercents.csv')

    os.remove('/opt/python/current/app/application/static/boxlist.csv')
    copyfile('/opt/python/current/app/application/static/examples/threemil_boxlist.csv', '/opt/python/current/app/application/static/boxlist.csv')

    os.remove('/opt/python/current/app/application/static/boxmlist.csv')
    copyfile('/opt/python/current/app/application/static/examples/threemil_boxmlist.csv', '/opt/python/current/app/application/static/boxmlist.csv')

    os.remove('/opt/python/current/app/application/static/militantregionlist.csv')
    copyfile('/opt/python/current/app/application/static/examples/threemil_militantregionlist.csv', '/opt/python/current/app/application/static/militantregionlist.csv')

    os.remove('/opt/python/current/app/application/static/form1.csv')
    copyfile('/opt/python/current/app/application/static/examples/twomil_form1.csv', '/opt/python/current/app/application/static/form1.csv')

    os.remove('/opt/python/current/app/application/static/regionvalues.csv')
    copyfile('/opt/python/current/app/application/static/examples/twomil_regionvalues.csv', '/opt/python/current/app/application/static/regionvalues.csv')

    os.remove('/opt/python/current/app/application/static/communityvalues.csv')
    copyfile('/opt/python/current/app/application/static/examples/twomil_communityvalues.csv', '/opt/python/current/app/application/static/communityvalues.csv')

    os.remove('/opt/python/current/app/application/static/militantvalues.csv')
    copyfile('/opt/python/current/app/application/static/examples/twomil_militantvalues.csv', '/opt/python/current/app/application/static/militantvalues.csv')

    os.remove('/opt/python/current/app/application/static/communitypercents.csv')
    copyfile('/opt/python/current/app/application/static/examples/twomil_communitypercents.csv', '/opt/python/current/app/application/static/communitypercents.csv')

    os.remove('/opt/python/current/app/application/static/boxlist.csv')
    copyfile('/opt/python/current/app/application/static/examples/twomil_boxlist.csv', '/opt/python/current/app/application/static/boxlist.csv')

    os.remove('/opt/python/current/app/application/static/boxmlist.csv')
    copyfile('/opt/python/current/app/application/static/examples/twomil_boxmlist.csv', '/opt/python/current/app/application/static/boxmlist.csv')

    os.remove('/opt/python/current/app/application/static/militantregionlist.csv')
    copyfile('/opt/python/current/app/application/static/examples/twomil_militantregionlist.csv', '/opt/python/current/app/application/static/militantregionlist.csv')

    # os.remove('/Users/Frances/python/conflict/application/static/form1.csv')
    # os.remove('/Users/Frances/python/conflict/application/model/static2/form1.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/threemil_form1.csv', '/Users/Frances/python/conflict/application/static/form1.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/threemil_form1.csv', '/Users/Frances/python/conflict/application/model/static2/form1.csv')
    #
    # os.remove('/Users/Frances/python/conflict/application/static/regionvalues.csv')
    # os.remove('/Users/Frances/python/conflict/application/model/static2/regionvalues.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/threemil_regionvalues.csv', '/Users/Frances/python/conflict/application/static/regionvalues.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/threemil_regionvalues.csv', '/Users/Frances/python/conflict/application/model/static2/regionvalues.csv')
    #
    # os.remove('/Users/Frances/python/conflict/application/static/communityvalues.csv')
    # os.remove('/Users/Frances/python/conflict/application/model/static2/communityvalues.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/threemil_communityvalues.csv', '/Users/Frances/python/conflict/application/static/communityvalues.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/threemil_communityvalues.csv', '/Users/Frances/python/conflict/application/model/static2/communityvalues.csv')
    #
    # os.remove('/Users/Frances/python/conflict/application/static/militantvalues.csv')
    # os.remove('/Users/Frances/python/conflict/application/model/static2/militantvalues.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/threemil_militantvalues.csv', '/Users/Frances/python/conflict/application/static/militantvalues.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/threemil_militantvalues.csv', '/Users/Frances/python/conflict/application/model/static2/militantvalues.csv')
    #
    # os.remove('/Users/Frances/python/conflict/application/static/communitypercents.csv')
    # os.remove('/Users/Frances/python/conflict/application/model/static2/communitypercents.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/threemil_communitypercents.csv', '/Users/Frances/python/conflict/application/static/communitypercents.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/threemil_communitypercents.csv', '/Users/Frances/python/conflict/application/model/static2/communitypercents.csv')
    #
    # os.remove('/Users/Frances/python/conflict/application/static/boxlist.csv')
    # os.remove('/Users/Frances/python/conflict/application/model/static2/boxlist.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/threemil_boxlist.csv', '/Users/Frances/python/conflict/application/static/boxlist.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/threemil_boxlist.csv', '/Users/Frances/python/conflict/application/model/static2/boxlist.csv')
    #
    # os.remove('/Users/Frances/python/conflict/application/static/boxmlist.csv')
    # os.remove('/Users/Frances/python/conflict/application/model/static2/boxmlist.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/threemil_boxmlist.csv', '/Users/Frances/python/conflict/application/static/boxmlist.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/threemil_boxmlist.csv', '/Users/Frances/python/conflict/application/model/static2/boxmlist.csv')
    #
    # os.remove('/Users/Frances/python/conflict/application/static/militantregionlist.csv')
    # os.remove('/Users/Frances/python/conflict/application/model/static2/militantregionlist.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/threemil_militantregionlist.csv', '/Users/Frances/python/conflict/application/static/militantregionlist.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/threemil_militantregionlist.csv', '/Users/Frances/python/conflict/application/model/static2/militantregionlist.csv')
    #
    # os.remove('/Users/Frances/python/conflict/application/static/form1.csv')
    # os.remove('/Users/Frances/python/conflict/application/model/static2/form1.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/twomil_form1.csv', '/Users/Frances/python/conflict/application/static/form1.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/twomil_form1.csv', '/Users/Frances/python/conflict/application/model/static2/form1.csv')
    #
    # os.remove('/Users/Frances/python/conflict/application/static/regionvalues.csv')
    # os.remove('/Users/Frances/python/conflict/application/model/static2/regionvalues.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/twomil_regionvalues.csv', '/Users/Frances/python/conflict/application/static/regionvalues.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/twomil_regionvalues.csv', '/Users/Frances/python/conflict/application/model/static2/regionvalues.csv')
    #
    # os.remove('/Users/Frances/python/conflict/application/static/communityvalues.csv')
    # os.remove('/Users/Frances/python/conflict/application/model/static2/communityvalues.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/twomil_communityvalues.csv', '/Users/Frances/python/conflict/application/static/communityvalues.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/twomil_communityvalues.csv', '/Users/Frances/python/conflict/application/model/static2/communityvalues.csv')
    #
    # os.remove('/Users/Frances/python/conflict/application/static/militantvalues.csv')
    # os.remove('/Users/Frances/python/conflict/application/model/static2/militantvalues.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/twomil_militantvalues.csv', '/Users/Frances/python/conflict/application/static/militantvalues.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/twomil_militantvalues.csv', '/Users/Frances/python/conflict/application/model/static2/militantvalues.csv')
    #
    # os.remove('/Users/Frances/python/conflict/application/static/communitypercents.csv')
    # os.remove('/Users/Frances/python/conflict/application/model/static2/communitypercents.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/twomil_communitypercents.csv', '/Users/Frances/python/conflict/application/static/communitypercents.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/twomil_communitypercents.csv', '/Users/Frances/python/conflict/application/model/static2/communitypercents.csv')
    #
    # os.remove('/Users/Frances/python/conflict/application/static/boxlist.csv')
    # os.remove('/Users/Frances/python/conflict/application/model/static2/boxlist.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/twomil_boxlist.csv', '/Users/Frances/python/conflict/application/static/boxlist.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/twomil_boxlist.csv', '/Users/Frances/python/conflict/application/model/static2/boxlist.csv')
    #
    # os.remove('/Users/Frances/python/conflict/application/static/boxmlist.csv')
    # os.remove('/Users/Frances/python/conflict/application/model/static2/boxmlist.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/twomil_boxmlist.csv', '/Users/Frances/python/conflict/application/static/boxmlist.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/twomil_boxmlist.csv', '/Users/Frances/python/conflict/application/model/static2/boxmlist.csv')
    #
    # os.remove('/Users/Frances/python/conflict/application/static/militantregionlist.csv')
    # os.remove('/Users/Frances/python/conflict/application/model/static2/militantregionlist.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/twomil_militantregionlist.csv', '/Users/Frances/python/conflict/application/static/militantregionlist.csv')
    # copyfile('/Users/Frances/python/conflict/application/static/examples/twomil_militantregionlist.csv', '/Users/Frances/python/conflict/application/model/static2/militantregionlist.csv')
