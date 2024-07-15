from mongoengine import Document, StringField, BooleanField

class User(Document):
    username = StringField(required=True, min_length=3, max_length=20, unique=True)
    email = StringField(required=True, max_length=50, unique=True)
    password = StringField(required=True, min_length=6)
    isAvatarImageSet = BooleanField(default=False)
    avatarImage = StringField(default="")

    meta = {
        'collection': 'users' 
    }
