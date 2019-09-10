def checkDefend(currentcivilian, currentmilitant, regionlist):
    defend = False
    weapons = False
    for i in regionlist:
        if i.name == currentcivilian.region:
            weapons = i.weapons
    if weapons == True and currentcivilian.wealth != 'L':
        defend = True
        currentcivilian.updateSupport(currentmilitant, False)
    else:
        currentcivilian.updateSupport(currentmilitant, True)
    return defend

# weapons is boolean from initconditions, civilian must have medium or high wealth
