from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField, SubmitField, FieldList, FormField, Label, TextAreaField, SelectField
from wtforms.validators import DataRequired, InputRequired, Optional, ValidationError

def percentage_check(form, field):
    try:
        if field.data > 1:
            raise ValidationError('Field must be in decimal form')
        if field.data < 0:
            raise ValidationError('Field must be a positive decimal')
    except TypeError:
        raise ValidationError('Field must be a decimal value between 0 - 1')

def percentage_check2(form, field):
    try:
        if field.data > 1:
            raise ValidationError('Percent field must be in decimal form')
        if field.data < 0:
            raise ValidationError('Percent field must be a positive decimal')
    except TypeError:
        raise ValidationError('Percent field must be a decimal value between 0 - 1')

def percentage_check3(form, field):
    try:
        if field.data > 1:
            raise ValidationError('Percent fields must be in decimal form')
        if field.data < 0:
            raise ValidationError('Percent fields must be a positive decimal')
    except TypeError:
        raise ValidationError('Percent fields must be a decimal value between 0 - 1')

def benefit_check(form, field):
    try:
        if field.data < 1 or field.data > 10:
            raise ValidationError('Benefit threshold must be an integer from 1 to 10')
    except TypeError:
        raise ValidationError('Benefit threshold must be an integer from 1 to 10')

def extincome_check(form, field):
    try:
        if field.data > 0 and field.data < 1:
            raise ValidationError('External Income must be an integer of 0 or greater')
        elif field.data < 0:
            raise ValidationError('External Income must be an integer of 0 or greater')
    except TypeError:
        raise ValidationError('External Income must be an integer of 0 or greater')

def initstrength_check(form, field):
    try:
        if field.data > 0 and field.data < 1 or field.data < 0:
            raise ValidationError('Initial Strength must be an integer of 0 or greater')
    except TypeError:
        raise ValidationError('Initial Strength must be an integer of 0 or greater')

def integer_check(form, field):
    try:
        if field.data < 1:
            raise ValidationError('Must be an integer of 1 or greater')
    except TypeError:
        raise ValidationError('Must be an integer of 1 or greater')

def integer2_check(form, field):
    try:
        if field.data < 2:
            raise ValidationError('Must be an integer of 2 or greater')
    except TypeError:
        raise ValidationError('Must be an integer of 2 or greater')

def integer3_check(form, field):
    try:
        if field.data < 100:
            raise ValidationError('Recommended integer greater than 100')
    except TypeError:
        raise ValidationError('Must be an integer of 100 or greater')

class Contact(FlaskForm):
    name = StringField('Name:', validators = [DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])
    subject = SelectField('Subject:', choices=[('question', 'Ask a Question'), ('feedback', 'Leave Feedback'), ('request', 'Request Information'), ('report', 'Report an Error'), ('message', 'Other')], validators=[DataRequired()])
    message = TextAreaField('Message:', validators=[DataRequired()], render_kw={"rows": 15, "cols": 100})
    submit = SubmitField('Submit')

class FirstForm(FlaskForm):
    totalpopulation = IntegerField('Total Population:', validators = [InputRequired(), integer3_check])
    numberregions = IntegerField('Number of Regions:', validators=[InputRequired(), integer_check])
    numbercommunities = IntegerField('Number of Communities:', validators=[InputRequired(), integer_check])
    numbermilitants = IntegerField('Number of Militants:', validators=[InputRequired(), integer2_check])
    l = IntegerField('L:', validators = [InputRequired(), integer_check])
    m = IntegerField('M:', validators = [InputRequired(), integer_check])
    h = IntegerField('H:', validators = [InputRequired(), integer_check])
    extortionrate = FloatField('Percent Extortion Rate:', validators = [DataRequired(), percentage_check])
    civsupportrate = FloatField('Percent Civilian Support Rate:', validators=[DataRequired(), percentage_check])
    terrorfactor = FloatField('Terrorism Factor:', validators=[DataRequired(), percentage_check])
    submit = SubmitField('Submit')

class RegionForm(FlaskForm):
    regionname = StringField('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Region Name:', validators=[InputRequired()])
    regpercent = FloatField('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Percent of Total Population: &nbsp;', validators=[InputRequired(), percentage_check2])
    weapons = BooleanField('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Weapons?', validators=None)

class CommunityForm(FlaskForm):
    communityname = StringField('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Community Name: &nbsp;', validators=[DataRequired()])
    l = FloatField('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; % L:', validators=[DataRequired(), percentage_check3])
    m = FloatField('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; % M:', validators=[DataRequired(), percentage_check3])
    h = FloatField('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; % H:', validators=[DataRequired(), percentage_check3])

class MilitantForm(FlaskForm):
    militantname = StringField('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Militant Name:', validators=[DataRequired()])
    extincome = IntegerField('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; External Income:', validators=[InputRequired(), extincome_check])
    initstrength = IntegerField('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Initial Strength:', validators=[InputRequired(), initstrength_check])
    benefitcutoff = IntegerField('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Benefit Threshold: &nbsp;', validators=[benefit_check, InputRequired()])
    terrorist = BooleanField('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Terrorist?', validators=None)

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
    x = FloatField(validators=[InputRequired(), percentage_check])

    def __init__(self, labels=None, **kwargs):
        super().__init__(**kwargs)
        if labels is None:
            labels = [' ']
        self.x.label = Label(self.x.id, labels[0])

class GrievancesForm(FlaskForm):
    box = BooleanField(validators=None)

    def __init__(self, labels=None, **kwargs):
        super().__init__(**kwargs)
        if labels is None:
            labels = [' ']
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
            labels = [' ']
        self.boxm.label = Label(self.boxm.id, labels[0])

class MilitantForm2(FlaskForm):
    reg = BooleanField(validators=None)

    def __init__(self, labels=None, **kwargs):
        super().__init__(**kwargs)
        if labels is None:
            labels = [' ']
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
    fundmilamt = IntegerField(validators=[Optional(), extincome_check])
    cutoff = BooleanField(validators=None)
    cutoffamt = FloatField(validators=[Optional(), percentage_check])
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
            labels = ['1. List the names of any militants that the intervention supports, separated by a comma:', '2. List the names of any militants that the intervention opposes, separated by a comma:', 'Negotiate disputes between all communities:', 'Negotiate between two militant groups:', 'First Militant:', 'Second Militant:', 'Wage information campaign:', 'Support militant governance:', 'Increase civilian wealth:', 'List regions separated by a comma:', 'List communities separated by a comma:', 'Provide community leaders with benefits:', 'Provide militants with benefits to pass to civilians:', 'Provide civilians with benefits conditional on ceasing militant support:', 'Fund supported militants:', 'Amount of funding:', 'Cut off resources from opposed militants:', 'Percent of resources to cut off (decimal form):', 'Attack opposed militants:', 'Punish civilian support of opposed militants:', 'Remove available weapons:', 'List regions separated by a comma:', 'Provide training and equipment to supported militants:', 'Protect civilians from opposed militants:']
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

