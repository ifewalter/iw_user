from iw_utils.utils import Util

from iw_user.models.user_model import UserModel
from iw_user.services.user_service import UserService


class User(object):

    """
       Create a user user and save to db immediately
    """
    def create(self):
        return self.user_service.create_user()

    def update(self):
        return self.user_service.update_user_details()

    def generate_otp_token(self):
        return self.user_service.generate_user_otp()

    def verify_otp_token(self):
        return self.user_service.verify_user_otp()

    def delete_user(self):
        """
        Delete a user acccount.

        :return:
        """
        raise NotImplementedError("Function not yet implemented contact package creator")

    def get_user_by_token(self):
        return self.user_service.get_user_from_token()

    def get_user_by_id(self):
        self.user_object = self.user_object.find(self.user_object)

    def __init__(self, user_dict: dict):
        self.user_object = UserModel(**user_dict)
        self.user_service = UserService(self.user_object)
        self.util = Util()
