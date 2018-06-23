from unittest import TestCase, mock

from iw_user.models.user_model import UserModel
from iw_user.services.user_service import UserService


class UserServiceTests(TestCase):

    @mock.patch('iw_user.dao.db_client.setup_db', autospec=True)
    @mock.patch('iw_user.models.user_model.UserModel', autospec=True)
    def test_create_user(self, mockedsetup, mockedusermodel):
        test_user = dict(username="ifewalter@gmail.com", password="hello", fullname="ife", phone_number="76543456")

        # with mockedsetup:
        user_model = UserModel(**test_user)

        user_service = UserService(user_model)

        user_service.create_user()
        self.assertEqual(user_service.user_model.username, test_user.get('username'))

