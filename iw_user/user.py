from iw_utils.utils import Util

from iw_user.models import UserModel
from iw_user.services.user_service import UserService


class User(object):

    """
       Create a user user and save to db immediately
    """
    def create(self):
        self.user_object.commit()

    def update(self):
        pass

    def generate_otp_token(self):
        pass

    def verify_otp_token(self):
        pass

    def delete_user(self):
        pass

    def get_user_by_token(self):
        pass

    def get_user_by_id(self):
        self.user_object = self.user_object.find(self.user_object)

    def __init__(self, user_dict: dict):
        self.user_object = UserModel(**user_dict)
        self.user_service = UserService(self.user_object)
        self.util = Util()
