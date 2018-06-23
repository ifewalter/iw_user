import bcrypt
from iw_utils.utils import Util
from models.user_model import UserModel


class UserService(object):
    def create_user(self):
        self.user_model.password = bcrypt.hashpw(self.user_model.password.encode('utf-8'), bcrypt.gensalt(14)).decode(
            'utf-8')
        self.user_model.auth_token = self.util.generate_token()
        self.user_model.auth_nonce = self.util.generate_token()
        self.user_model.random_seed = self.util.generate_random_base32()
        self.user_model.commit()
        return self.user_model

    # TODO: Make this function return user details including tokens and stuff
    def authenticate_user(self):

        self.user_model = self.user_model.find_one({"username": self.user_model.username})

        if bcrypt.checkpw(self.user_model.password.encode('utf-8'), self.user_model.password.encode('utf-8')):
            self.user_model.auth_token = Util.generate_token()

            self.user_model.commit(conditions={'username': self.user_model.username})
            return self.user_model

        return None

    def verify_identity_by_token(self):
        self.user_model = self.user_model.find_one({"auth_token":self.user_model.auth_token})
        
        if self.user_model:
                return True
        return False

    def get_user_id_from_token(self):

        self.user_model = self.user_model.find_one({"auth_token":self.user_model.auth_token})
        return self.user_model['_id']


    def generate_user_otp(self):
        return pyotp.TOTP(user.random_seed, interval=300).now()

    def regenerate_user_otp(self, nonce):
        user_model = User.find_one({'auth_nonce': nonce})

        user_model_2 = copy.deepcopy(user_model)
        user_model.auth_nonce = Util.generate_token()
        user_model.commit(conditions={'auth_nonce': user_model_2.auth_nonce})

    def verify_user_otp(self, nonce, otp):
        user_model = self.util.find_one({'auth_nonce': nonce})

        if user_model is not None:
            return pyotp.TOTP(user_model.random_seed, interval=300).verify(otp), user_model
        return False, user_model

    def __init__(self, user_model: dict):
        self.user_model = UserModel()
        self.util = Util()
