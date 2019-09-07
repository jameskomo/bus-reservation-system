from django.test import TestCase
from .forms import UserRegisterForm


class TestUserRegisterForm(TestCase):
  
  def test_registration_form(self):
    # test invalid data
    invalid_data = {
      "username": "user@test.com",
      "password": "secret",
      "confirm": "not secret"
    }
    form = UserRegisterForm(data=invalid_data)
    form.is_valid()
    self.assertTrue(form.errors)

    # test valid data
    valid_data = {
      "email": "user@test.com",
      "username": "username",
      "password1": "secretPassWord2",
      "password2": "secretPassWord2",
    }
    form = UserRegisterForm(data=valid_data)
    form.is_valid()
    self.assertFalse(form.errors)