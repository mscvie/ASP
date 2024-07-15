from mongoengine import Document, StringField, ListField, ReferenceField, DateTimeField
from models.user_model import User

class Message(Document):
    text = StringField(required=True)
    users = ListField()
    sender = ReferenceField(User, required=True)
    timestamp = DateTimeField(required=True)

    meta = {
        'collection': 'messages',  # MongoDB collection name
        'indexes': [
            {'fields': ['sender', 'timestamp']}
        ]
    }
