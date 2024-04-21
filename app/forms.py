#forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

class CreditForm(FlaskForm):
    CHK_ACCT = SelectField('Checking Account', choices=[('0DM', '0DM'), ('less-200DM', 'less-200DM'), ('no-account', 'no-account'), ('over-200DM', 'over-200DM')], validators=[DataRequired()])
    Duration = IntegerField('Duration', validators=[DataRequired()])
    History = SelectField('History', choices=[('critical', 'critical'), ('duly-till-now', 'duly-till-now'), ('all-paid-duly', 'all-paid-duly'), ('bank-paid-duly', 'bank-paid-duly'), ('delay', 'delay')], validators=[DataRequired()])
    Purpose_of_credit = SelectField('Purpose of Credit', choices=[('radio-tv', 'radio-tv'), ('education', 'education'), ('furniture', 'furniture'), ('new-car', 'new-car'), ('used-car', 'used-car'), ('domestic-app', 'domestic-app'), ('repairs', 'repairs'), ('business', 'business')], validators=[DataRequired()])
    Credit_Amount = IntegerField('Credit Amount', validators=[DataRequired()])
    Balance_in_Savings_A_C = SelectField('Balance in Savings A/C', choices=[('unknown', 'unknown'), ('less100DM', 'less100DM'), ('less500DM', 'less500DM'),('less1000DM', 'less1000DM'), ('over1000DM', 'over1000DM')], validators=[DataRequired()])
    Employment = SelectField('Employment', choices=[('over-seven', 'over-seven'), ('four-years', 'four-years'), ('seven-years', 'seven-years'), ('unemployed', 'unemployed'), ('one-year', 'one-year'), ('bank-paid-duly', 'bank-paid-duly')], validators=[DataRequired()])
    Install_rate = IntegerField('Install rate', validators=[DataRequired()])
    Marital_status = SelectField('Marital status', choices=[('single-male', 'single-male'), ('female-divorced', 'female-divorced'), ('male-divorced', 'male-divorced'), ('married-male', 'married-male')], validators=[DataRequired()])
    Co_applicant = SelectField('Co-applicant', choices=[('none', 'none'), ('guarantor', 'guarantor'), ('co-applicant', 'co-applicant')], validators=[DataRequired()])
    Present_Resident = IntegerField('Present Resident', validators=[DataRequired()])
    Real_Estate = SelectField('Real Estate', choices=[('real-estate', 'real-estate'), ('building-society', 'building-society'), ('car', 'car'), ('none', 'none')], validators=[DataRequired()])
    Age = IntegerField('Age', validators=[DataRequired()])
    Other_installment = SelectField('Other installment', choices=[('none', 'none'), ('bank', 'bank'), ('stores', 'stores')], validators=[DataRequired()])
    Residence = SelectField('Residence', choices=[('own', 'own'), ('rent', 'rent'), ('free', 'free')], validators=[DataRequired()])
    Num_Credits = IntegerField('Number of Credits', validators=[DataRequired()])
    Job = SelectField('Job', choices=[('skilled', 'skilled'), ('unskilled-resident', 'unskilled-resident'), ('management', 'management'), ('unemployed-non-resident', 'unemployed-non-resident')], validators=[DataRequired()])
    No_dependents = IntegerField('Number of Dependents', validators=[DataRequired()])
    Phone = SelectField('Phone', choices=[('no', 'no'), ('yes', 'yes')], validators=[DataRequired()])
    Foreign = SelectField('Foreign', choices=[('no', 'no'), ('yes', 'yes')], validators=[DataRequired()])
    submit = SubmitField('Submit')