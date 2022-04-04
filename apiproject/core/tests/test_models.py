from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successfull(self):
        emailtest = 'test@test.com'
        passwordtest = 'TestPassword123'

        user = get_user_model().objects.create_user(
            email = emailtest,
            password = passwordtest
        )

        self.assertEqual(user.email, emailtest)
        self.assertTrue(user.check_password(passwordtest))