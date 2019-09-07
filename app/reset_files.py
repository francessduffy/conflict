import os
from shutil import copyfile

def reset_files():
    os.remove('/Users/Frances/python/conflict/app/static/form1.csv')
    os.remove('/Users/Frances/python/conflict/app/model/static2/form1.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/threemil_form1.csv', '/Users/Frances/python/conflict/app/static/form1.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/threemil_form1.csv', '/Users/Frances/python/conflict/app/model/static2/form1.csv')

    os.remove('/Users/Frances/python/conflict/app/static/regionvalues.csv')
    os.remove('/Users/Frances/python/conflict/app/model/static2/regionvalues.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/threemil_regionvalues.csv', '/Users/Frances/python/conflict/app/static/regionvalues.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/threemil_regionvalues.csv', '/Users/Frances/python/conflict/app/model/static2/regionvalues.csv')

    os.remove('/Users/Frances/python/conflict/app/static/communityvalues.csv')
    os.remove('/Users/Frances/python/conflict/app/model/static2/communityvalues.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/threemil_communityvalues.csv', '/Users/Frances/python/conflict/app/static/communityvalues.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/threemil_communityvalues.csv', '/Users/Frances/python/conflict/app/model/static2/communityvalues.csv')

    os.remove('/Users/Frances/python/conflict/app/static/militantvalues.csv')
    os.remove('/Users/Frances/python/conflict/app/model/static2/militantvalues.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/threemil_militantvalues.csv', '/Users/Frances/python/conflict/app/static/militantvalues.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/threemil_militantvalues.csv', '/Users/Frances/python/conflict/app/model/static2/militantvalues.csv')

    os.remove('/Users/Frances/python/conflict/app/static/communitypercents.csv')
    os.remove('/Users/Frances/python/conflict/app/model/static2/communitypercents.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/threemil_communitypercents.csv', '/Users/Frances/python/conflict/app/static/communitypercents.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/threemil_communitypercents.csv', '/Users/Frances/python/conflict/app/model/static2/communitypercents.csv')

    os.remove('/Users/Frances/python/conflict/app/static/boxlist.csv')
    os.remove('/Users/Frances/python/conflict/app/model/static2/boxlist.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/threemil_boxlist.csv', '/Users/Frances/python/conflict/app/static/boxlist.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/threemil_boxlist.csv', '/Users/Frances/python/conflict/app/model/static2/boxlist.csv')

    os.remove('/Users/Frances/python/conflict/app/static/boxmlist.csv')
    os.remove('/Users/Frances/python/conflict/app/model/static2/boxmlist.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/threemil_boxmlist.csv', '/Users/Frances/python/conflict/app/static/boxmlist.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/threemil_boxmlist.csv', '/Users/Frances/python/conflict/app/model/static2/boxmlist.csv')

    os.remove('/Users/Frances/python/conflict/app/static/militantregionlist.csv')
    os.remove('/Users/Frances/python/conflict/app/model/static2/militantregionlist.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/threemil_militantregionlist.csv', '/Users/Frances/python/conflict/app/static/militantregionlist.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/threemil_militantregionlist.csv', '/Users/Frances/python/conflict/app/model/static2/militantregionlist.csv')

    os.remove('/Users/Frances/python/conflict/app/static/form1.csv')
    os.remove('/Users/Frances/python/conflict/app/model/static2/form1.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/twomil_form1.csv', '/Users/Frances/python/conflict/app/static/form1.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/twomil_form1.csv', '/Users/Frances/python/conflict/app/model/static2/form1.csv')

    os.remove('/Users/Frances/python/conflict/app/static/regionvalues.csv')
    os.remove('/Users/Frances/python/conflict/app/model/static2/regionvalues.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/twomil_regionvalues.csv', '/Users/Frances/python/conflict/app/static/regionvalues.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/twomil_regionvalues.csv', '/Users/Frances/python/conflict/app/model/static2/regionvalues.csv')

    os.remove('/Users/Frances/python/conflict/app/static/communityvalues.csv')
    os.remove('/Users/Frances/python/conflict/app/model/static2/communityvalues.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/twomil_communityvalues.csv', '/Users/Frances/python/conflict/app/static/communityvalues.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/twomil_communityvalues.csv', '/Users/Frances/python/conflict/app/model/static2/communityvalues.csv')

    os.remove('/Users/Frances/python/conflict/app/static/militantvalues.csv')
    os.remove('/Users/Frances/python/conflict/app/model/static2/militantvalues.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/twomil_militantvalues.csv', '/Users/Frances/python/conflict/app/static/militantvalues.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/twomil_militantvalues.csv', '/Users/Frances/python/conflict/app/model/static2/militantvalues.csv')

    os.remove('/Users/Frances/python/conflict/app/static/communitypercents.csv')
    os.remove('/Users/Frances/python/conflict/app/model/static2/communitypercents.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/twomil_communitypercents.csv', '/Users/Frances/python/conflict/app/static/communitypercents.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/twomil_communitypercents.csv', '/Users/Frances/python/conflict/app/model/static2/communitypercents.csv')

    os.remove('/Users/Frances/python/conflict/app/static/boxlist.csv')
    os.remove('/Users/Frances/python/conflict/app/model/static2/boxlist.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/twomil_boxlist.csv', '/Users/Frances/python/conflict/app/static/boxlist.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/twomil_boxlist.csv', '/Users/Frances/python/conflict/app/model/static2/boxlist.csv')

    os.remove('/Users/Frances/python/conflict/app/static/boxmlist.csv')
    os.remove('/Users/Frances/python/conflict/app/model/static2/boxmlist.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/twomil_boxmlist.csv', '/Users/Frances/python/conflict/app/static/boxmlist.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/twomil_boxmlist.csv', '/Users/Frances/python/conflict/app/model/static2/boxmlist.csv')

    os.remove('/Users/Frances/python/conflict/app/static/militantregionlist.csv')
    os.remove('/Users/Frances/python/conflict/app/model/static2/militantregionlist.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/twomil_militantregionlist.csv', '/Users/Frances/python/conflict/app/static/militantregionlist.csv')
    copyfile('/Users/Frances/python/conflict/app/static/examples/twomil_militantregionlist.csv', '/Users/Frances/python/conflict/app/model/static2/militantregionlist.csv')

reset_files()