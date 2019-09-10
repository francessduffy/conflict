class FightCombo(object):
    def __init__(self, name1, name2, ratio, sameregion, regions):
        self.name1 = name1
        self.name2 = name2
        self.ratio = ratio
        self.sameregion = sameregion
        self.regions = regions

# Updates indicator to be TRUE from condition that 2 militants operate in the same region; appends shared regions
    def update(self, x):
        self.sameregion = True
        self.regions.append(x)


# Generates list of all possible militant combos, attributes, and updates same region to indicate if they share regions
def fight(militantlist, militantoutputlist, r, negotiatemil):
    combos = []
    i = 0
    j = 1
    while i < len(militantlist)-1:
        while j < len(militantlist):
            combo = FightCombo(militantoutputlist[i].name, militantoutputlist[j].name,
                               militantoutputlist[i].strength[r]/militantoutputlist[j].strength[r], False, [])
            combos.append(combo)
            for x in militantlist[i].regions:
                for y in militantlist[j].regions:
                    if x == y:
                        combo.update(x)
            j += 1
        i += 1
        j = i + 1
    # Uses militant strength ratio as probability p5: the more equal the more likely they are to fight
    for i in combos:
        if i.ratio > 1:
            i.ratio = 1/i.ratio
    # For reducing fight probability by intervention amount
    for i in combos:
        for j in negotiatemil:
            if i.name1 == j[0] or i.name1 == j[1]:
                if i.name2 == j[0] or i.name2 == j[1]:
                    i.ratio -= j[2]
                    if i.ratio < 0:
                        i.ratio = 0
    # Changing names in combos to 'militantx' to match logic needed in results.py
    for i in combos:
        for j in militantlist:
            if i.name1 == j.name:
                if j.index == 0:
                    i.name1 = 'militant1'
                if j.index == 1:
                    i.name1 = 'militant2'
                if j.index == 2:
                    i.name1 = 'militant3'
                if j.index == 3:
                    i.name1 = 'militant4'
                if j.index == 4:
                    i.name1 = 'militant5'
                if j.index == 5:
                    i.name1 = 'militant6'
                if j.index == 6:
                    i.name1 = 'militant7'
                if j.index == 7:
                    i.name1 = 'militant8'
                if j.index == 8:
                    i.name1 = 'militant9'
                if j.index == 9:
                    i.name1 = 'militant10'
                if j.index == 10:
                    i.name1 = 'militant11'
                if j.index == 11:
                    i.name1 = 'militant12'
                if j.index == 12:
                    i.name1 = 'militant13'
                if j.index == 13:
                    i.name1 = 'militant14'
                if j.index == 14:
                    i.name1 = 'militant15'
            if i.name2 == j.name:
                if j.index == 0:
                    i.name2 = 'militant1'
                if j.index == 1:
                    i.name2 = 'militant2'
                if j.index == 2:
                    i.name2 = 'militant3'
                if j.index == 3:
                    i.name2 = 'militant4'
                if j.index == 4:
                    i.name2 = 'militant5'
                if j.index == 5:
                    i.name2 = 'militant6'
                if j.index == 6:
                    i.name2 = 'militant7'
                if j.index == 7:
                    i.name2 = 'militant8'
                if j.index == 8:
                    i.name2 = 'militant9'
                if j.index == 9:
                    i.name2 = 'militant10'
                if j.index == 10:
                    i.name2 = 'militant11'
                if j.index == 11:
                    i.name2 = 'militant12'
                if j.index == 12:
                    i.name2 = 'militant13'
                if j.index == 13:
                    i.name2 = 'militant14'
                if j.index == 14:
                    i.name2 = 'militant15'
    return combos
