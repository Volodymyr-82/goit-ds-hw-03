# models.py
from mongoengine import Document, StringField, ListField

class Quote(Document):
    quote = StringField(required=True)
    author = StringField(required=True)
    tags = ListField(StringField())

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()
