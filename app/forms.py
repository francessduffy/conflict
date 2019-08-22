from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField, SubmitField, FieldList, FormField, Label
from wtforms.validators import DataRequired, InputRequired, Optional



class FirstForm(FlaskForm):
    totalpopulation = IntegerField('Total Population:', validators = [DataRequired()])
    numberregions = IntegerField('Number of Regions:', validators=[DataRequired()])
    numbercommunities = IntegerField('Number of Communities:', validators=[DataRequired()])
    numbermilitants = IntegerField('Number of Militants:', validators=[DataRequired()])
    l = IntegerField('L:', validators = [DataRequired()])
    m = IntegerField('M:', validators = [DataRequired()])
    h = IntegerField('H:', validators = [DataRequired()])
    extortionrate = FloatField('Percent Extortion Rate:', validators = [DataRequired()])
    civsupportrate = FloatField('Civilian Support Rate:', validators=[DataRequired()])
    terrorfactor = FloatField('Terrorism Factor:', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegionForm(FlaskForm):
    regionname = StringField('Region Name', validators=[InputRequired()])
    regpercent = FloatField('Percent of Total Population:', validators=[InputRequired()])
    weapons = BooleanField('Weapons:', validators=None)

class CommunityForm(FlaskForm):
    communityname = StringField('Community Name', validators=[InputRequired()])
    l = FloatField('% L:', validators=[InputRequired()])
    m = FloatField('% M:', validators=[InputRequired()])
    h = FloatField('% H:', validators=[InputRequired()])

class MilitantForm(FlaskForm):
    militantname = StringField('Militant Name', validators=[InputRequired()])
    extincome = IntegerField('External Income:', validators=[InputRequired()])
    initstrength = IntegerField('Initial Strength:', validators=[InputRequired()])
    benefitcutoff = IntegerField('Benefit Threshold:', validators=[InputRequired()])
    terrorist = BooleanField('Terrorist?:', validators=None)

class SecondForm(FlaskForm):
    regions = FieldList(FormField(RegionForm))
    communities = FieldList(FormField(CommunityForm))
    militants = FieldList(FormField(MilitantForm))
    submit = SubmitField('Submit')

def get_labels(labels=None):
    if labels is None:
        labels = ['Percentage of Each Community Present in Each Region', 'Grievances Between Communities',
                  'Affiliation of Communities with Militants', 'Active Militants in Each Region']
        return labels

class RegionForm2(FlaskForm):
    x = FloatField(validators=[InputRequired()])

    def __init__(self, labels=None, **kwargs):
        super().__init__(**kwargs)
        if labels is None:
            labels = ['percent of the population:']
        self.x.label = Label(self.x.id, labels[0])

class GrievancesForm(FlaskForm):
    box = BooleanField(validators=None)

    def __init__(self, labels=None, **kwargs):
        super().__init__(**kwargs)
        if labels is None:
            labels = ['Grievance?:']
        self.box.label = Label(self.box.id, labels[0])

class ExamplesForm(FlaskForm):
    threemil = BooleanField(validators=None)
    twomil = BooleanField(validators=None)
    submit = SubmitField('Submit')

    def __init__(self, labels=None, **kwargs):
        super().__init__(**kwargs)
        if labels is None:
            labels = ['Theoretical Example 1:', 'Theoretical Example 2:']
        self['threemil'].label = Label(self['threemil'].id, labels[0])
        self['twomil'].label = Label(self['twomil'].id, labels[1])

class AffiliationsForm(FlaskForm):
    boxm = BooleanField(validators=None)

    def __init__(self, labels=None, **kwargs):
        super().__init__(**kwargs)
        if labels is None:
            labels = ['Affiliation?:']
        self.boxm.label = Label(self.boxm.id, labels[0])

class MilitantForm2(FlaskForm):
    reg = BooleanField(validators=None)

    def __init__(self, labels=None, **kwargs):
        super().__init__(**kwargs)
        if labels is None:
            labels = ['Active?:']
        self.reg.label = Label(self.reg.id, labels[0])

class ThirdForm(FlaskForm):
    regionpercent = FieldList(FormField(RegionForm2))
    grievances = FieldList(FormField(GrievancesForm))
    affiliations = FieldList(FormField(AffiliationsForm))
    milactive = FieldList(FormField(MilitantForm2))
    submit = SubmitField('Submit')

    def __init__(self, labels=None, **kwargs):
        super().__init__(**kwargs)
        if labels is None:
            labels = ['Percentage of Each Community Present in Each Region', 'Grievances Between Communities', 'Affiliation of Communities with Militants', 'Active Militants in Each Region']
        self['regionpercent'].label = Label(self['regionpercent'].id, labels[0])
        self['grievances'].label = Label(self['grievances'].id, labels[1])
        self['affiliations'].label = Label(self['affiliations'].id, labels[2])
        self['milactive'].label = Label(self['milactive'].id, labels[3])

class FourthForm(FlaskForm):
    supported_militants = StringField(validators=[DataRequired()])
    opposed_militants = StringField(validators=[DataRequired()])
    negotiate = BooleanField(validators=None)
    negotiate2 = BooleanField(validators=None)
    mil1 = StringField(validators=[Optional()])
    mil2 = StringField(validators=[Optional()])
    infocampaign = BooleanField(validators=None)
    supportmilgov = BooleanField(validators=None)
    civwealth = BooleanField(validators=None)
    wealthregions = StringField(validators=[Optional()])
    wealthcomms = StringField(validators=[Optional()])
    commbenefits = BooleanField(validators=None)
    milbenefits = BooleanField(validators=None)
    civbenefits = BooleanField(validators=None)
    fundmil = BooleanField(validators=None)
    fundmilamt = FloatField(validators=[Optional()])
    cutoff = BooleanField(validators=None)
    cutoffamt = FloatField(validators=[Optional()])
    attack = BooleanField(validators=None)
    punish = BooleanField(validators=None)
    weapons = BooleanField(validators=None)
    weaponsregions = StringField(validators=[Optional()])
    trainequip = BooleanField(validators=None)
    protect = BooleanField(validators=None)
    submit = SubmitField('Initiate the Simulator')

    def __init__(self, labels=None, **kwargs):
        super().__init__(**kwargs)
        if labels is None:
            labels = ['1. List the names of the militants that the intervention supports, separated by a comma:', '2. List the names of the militants that the intervention opposes, separated by a comma:', 'Negotiate between all communities:', 'Negotiate between two militant groups:', 'First Militant:', 'Second Militant:', 'Wage information campaign:', 'Support militant governance:', 'Increase civilian wealth:', 'List regions separated by a comma:', 'List communities separated by a comma:', 'Provide community leaders with benefits:', 'Provide militants with benefits to pass to civilians:', 'Provide civilians with conditional benefits:', 'Fund supported militants:', 'Amount of funding:', 'Cut off resources from opposed militants:', 'Percent of resources to cut off (decimal form):', 'Attack opposed militants:', 'Punish support of opposed militants:', 'Remove available weapons:', 'List regions separated by a comma:', 'Provide training and equipment to supported militants:', 'Protect civilians from opposed militants:']
        self['supported_militants'].label = Label(self['supported_militants'].id, labels[0])
        self['opposed_militants'].label = Label(self['opposed_militants'].id, labels[1])
        self['negotiate'].label = Label(self['negotiate'].id, labels[2])
        self['negotiate2'].label = Label(self['negotiate2'].id, labels[3])
        self['mil1'].label = Label(self['mil1'].id, labels[4])
        self['mil2'].label = Label(self['mil2'].id, labels[5])
        self['infocampaign'].label = Label(self['infocampaign'].id, labels[6])
        self['supportmilgov'].label = Label(self['supportmilgov'].id, labels[7])
        self['civwealth'].label = Label(self['civwealth'].id, labels[8])
        self['wealthregions'].label = Label(self['wealthregions'].id, labels[9])
        self['wealthcomms'].label = Label(self['wealthcomms'].id, labels[10])
        self['commbenefits'].label = Label(self['commbenefits'].id, labels[11])
        self['milbenefits'].label = Label(self['milbenefits'].id, labels[12])
        self['civbenefits'].label = Label(self['civbenefits'].id, labels[13])
        self['fundmil'].label = Label(self['fundmil'].id, labels[14])
        self['fundmilamt'].label = Label(self['fundmilamt'].id, labels[15])
        self['cutoff'].label = Label(self['cutoff'].id, labels[16])
        self['cutoffamt'].label = Label(self['cutoffamt'].id, labels[17])
        self['attack'].label = Label(self['attack'].id, labels[18])
        self['punish'].label = Label(self['punish'].id, labels[19])
        self['weapons'].label = Label(self['weapons'].id, labels[20])
        self['weaponsregions'].label = Label(self['weaponsregions'].id, labels[21])
        self['trainequip'].label = Label(self['trainequip'].id, labels[22])
        self['protect'].label = Label(self['protect'].id, labels[23])

