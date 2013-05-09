"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flaskext import wtf
from flaskext.wtf import validators

"""
class ExampleForm(wtf.Form):
    example_name = wtf.TextField('Name', validators=[validators.Required()])
    example_description = wtf.TextAreaField('Description', validators=[validators.Required()])
"""


class SurveyForm(wtf.Form):
    q01_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q01_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q02_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q02_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q03_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q03_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q04_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q04_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q05_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q05_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q06_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q06_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q07_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q07_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q08_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q08_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q09_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q09_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q10_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q10_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q11_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q11_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q12_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q12_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q13_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q13_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q14_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q14_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q15_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q15_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q16_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q16_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q17_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q17_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q18_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q18_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q19_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q19_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q20_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q20_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q21_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q21_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q22_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q22_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q23_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q23_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q24_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q24_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q25_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q25_2 = wtf.RadioField('Importance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q26_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    q27_1 = wtf.RadioField('GAP', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[validators.Required()])
    sex = wtf.RadioField('Sex', choices=[('male', 'Male'), ('female', 'Female')], validators=[validators.Required()])
    comment = wtf.TextAreaField('Comment', validators=[validators.Optional()])
    martial_status = wtf.SelectField('Martial Status', choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('other', 'Other')], validators=[validators.Required()])
    age = wtf.SelectField('Age', choices=[('18-24', '18 - 24'), ('25-31', '25 - 31'), ('32-38', '32 - 38'), ('above 39', '39 above')], validators=[validators.Required()])
    internet_usage = wtf.SelectField('How long have you been using internet ?', choices=[('less 1', 'Less than 1 year'), ('1-5', '1 - 5 years'), ('above 5', '5 or above')], validators=[validators.Required()])
    internet_frequency = wtf.SelectField('How often do you use internet ?', choices=[('everyday', 'Everyday'), ('few times a week', 'Few times a week'), ('less than 5 times a month', 'Less than 5 times a month')], validators=[validators.Required()])
    purchase_online = wtf.RadioField('Have you ever purchased apparel online ?', choices=[('true', 'Yes'), ('false', 'No')], validators=[validators.Required()])
    purchase_frequency = wtf.SelectField('How often do you purchase apparel online ?', choices=[('every week', 'Every week'), ('every month', 'Every month'), ('every season', 'Every season'), ('random', 'Random')], validators=[validators.Optional()])
    last_purchase = wtf.RadioField('Have you purchased apparel online in the past 30 days ?', choices=[('true', 'Yes'), ('false', 'No')], validators=[validators.Optional()])
    employment_status = wtf.SelectField('Employment Status', choices=[('employed', 'Employed'), ('unemployed', 'Unemployed'), ('self-employed', 'Self-employed')], validators=[validators.Required()])
    income_range = wtf.SelectField('Income range (HKD)', choices=[('0', '0 - 10,000'), ('1', '10,001 - 20,000'), ('2', '20,001 - 30,000'), ('3', '30,001 - 40,000'), ('4', '40,001 & above')], validators=[validators.Required()])

