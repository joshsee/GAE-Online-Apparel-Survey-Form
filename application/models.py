"""
models.py

App Engine datastore models

"""

from google.appengine.ext import db

"""
class ExampleModel(ndb.Model):
    "Example Model""
    example_name = ndb.StringProperty(required=True)
    example_description = ndb.TextProperty(required=True)
    added_by = ndb.UserProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

class AdNetwork(db.Model):
    "Newsletter Model""
    app_title = ndb.StringProperty(required=True)
    app_category = db.CategoryProperty(required=True)
    app_url = db.BlobProperty()
    app_name = db.StringProperty()
    ext = db.StringProperty()
    content_type = db.StringProperty()
    app_link = db.LinkProperty()
    new = db.BooleanProperty()
    exclusive = db.BooleanProperty()
"""


class Survey(db.Model):
    """Survey Model"""
    timestamp = db.DateTimeProperty(auto_now_add=True)
    sex = db.StringProperty(required=True, choices=set(["male", "female"]))
    comment = db.TextProperty()
    martial_status = db.CategoryProperty(required=True)
    internet_usage = db.CategoryProperty(required=True)
    internet_frequency = db.CategoryProperty(required=True)
    purchase_online = db.StringProperty(required=True)
    purchase_frequency = db.CategoryProperty()
    last_purchase = db.StringProperty()
    employment_status = db.CategoryProperty(required=True)
    income_range = db.CategoryProperty(required=True)
    q01_1 = db.RatingProperty(required=True)
    q01_2 = db.RatingProperty(required=True)
    q02_1 = db.RatingProperty(required=True)
    q02_2 = db.RatingProperty(required=True)
    q03_1 = db.RatingProperty(required=True)
    q03_2 = db.RatingProperty(required=True)
    q04_1 = db.RatingProperty(required=True)
    q04_2 = db.RatingProperty(required=True)
    q05_1 = db.RatingProperty(required=True)
    q05_2 = db.RatingProperty(required=True)
    q06_1 = db.RatingProperty(required=True)
    q06_2 = db.RatingProperty(required=True)
    q07_1 = db.RatingProperty(required=True)
    q07_2 = db.RatingProperty(required=True)
    q08_1 = db.RatingProperty(required=True)
    q08_2 = db.RatingProperty(required=True)
    q09_1 = db.RatingProperty(required=True)
    q09_2 = db.RatingProperty(required=True)
    q10_1 = db.RatingProperty(required=True)
    q10_2 = db.RatingProperty(required=True)
    q11_1 = db.RatingProperty(required=True)
    q11_2 = db.RatingProperty(required=True)
    q12_1 = db.RatingProperty(required=True)
    q12_2 = db.RatingProperty(required=True)
    q13_1 = db.RatingProperty(required=True)
    q13_2 = db.RatingProperty(required=True)
    q14_1 = db.RatingProperty(required=True)
    q14_2 = db.RatingProperty(required=True)
    q15_1 = db.RatingProperty(required=True)
    q15_2 = db.RatingProperty(required=True)
    q16_1 = db.RatingProperty(required=True)
    q16_2 = db.RatingProperty(required=True)
    q17_1 = db.RatingProperty(required=True)
    q17_2 = db.RatingProperty(required=True)
    q18_1 = db.RatingProperty(required=True)
    q18_2 = db.RatingProperty(required=True)
    q19_1 = db.RatingProperty(required=True)
    q19_2 = db.RatingProperty(required=True)
    q20_1 = db.RatingProperty(required=True)
    q20_2 = db.RatingProperty(required=True)
    q21_1 = db.RatingProperty(required=True)
    q21_2 = db.RatingProperty(required=True)
    q22_1 = db.RatingProperty(required=True)
    q22_2 = db.RatingProperty(required=True)
    q23_1 = db.RatingProperty(required=True)
    q23_2 = db.RatingProperty(required=True)
    q24_1 = db.RatingProperty(required=True)
    q24_2 = db.RatingProperty(required=True)
    q25_1 = db.RatingProperty(required=True)
    q25_2 = db.RatingProperty(required=True)
    q26_1 = db.RatingProperty(required=True)
    q26_2 = db.RatingProperty(required=True)
    q27_1 = db.RatingProperty(required=True)
    q27_2 = db.RatingProperty(required=True)
