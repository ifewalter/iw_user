from datetime import datetime
from umongo import Document, fields

from iw_user.dao.db_client import db_instance,db


@db_instance.register
class UserModel(Document):
    fullname = fields.StringField(allow_none=True)
    username = fields.StringField(required=True)
    email = fields.EmailField(allow_none=True)
    phone_number = fields.StringField(allow_none=True)
    password = fields.StringField(required=True, load_only=True)
    birth_date = fields.StringField(required=False)
    auth_token = fields.StringField()
    auth_provider = fields.StringField(load_only=True)
    random_seed = fields.StringField(load_only=True)
    auth_nonce = fields.StringField()
    created_at = fields.DateTimeField(default=datetime.utcnow(), missing=datetime.utcnow(), load_only=True)
    modified_at = fields.DateTimeField(default=datetime.utcnow(), missing=datetime.utcnow(), load_only=True)

    class Meta:
        collection = db.user
