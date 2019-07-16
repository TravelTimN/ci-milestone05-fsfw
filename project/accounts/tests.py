from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import reverse
from accounts.forms import (
    UserLoginForm, UserRegistrationForm,
    UserUpdateForm, ProfileUpdateForm)


# ----- FORMS ----- #
class TestUserLoginForm(TestCase):
    def test_log_in_valid(self):
        form = UserLoginForm(
            {"username": "TestUser", "password": "TestPassword"})
        self.assertTrue(form.is_valid())

    def test_correct_error_message(self):
        form = UserLoginForm({"username": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["username"], [u"This field is required."])


class TestUserRegistrationForm(TestCase):
    def test_register_form_valid(self):
        form = UserRegistrationForm(
            {"username": "TestUser", "email": "Test@Email.com",
                "first_name": "TestFirstName", "last_name": "TestLastName",
                "password1": "TestPassw0rd?", "password2": "TestPassw0rd?"})
        self.assertTrue(form.is_valid())

    def test_passwords_do_not_match(self):
        form = UserRegistrationForm(
            {"username": "TestUser", "email": "Test@Email.com",
                "first_name": "TestFirstName", "last_name": "TestLastName",
                "password1": "TestPassw0rd?", "password2": "TestPassword?"})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["password2"], [u"Passwords must match!"])


class TestUserUpdateForm(TestCase):
    def test_email_updated(self):
        form = UserUpdateForm({"email": "New@email.com"})
        form.save()
        self.assertTrue(form.is_valid())


class TestProfileUpdateForm(TestCase):
    def test_profile_image_updated(self):
        photo = ProfileUpdateForm
        photo.image = SimpleUploadedFile(
            "test-image.png", b"file_content", content_type="image/png")
        self.client.post(reverse("profile"), {"photo": photo})
        self.assertIsNotNone(ProfileUpdateForm)


# ----- VIEWS ----- #
class TestIndexView(TestCase):
    def test_index_view(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")


class TestSuperuserView(TestCase):
    def test_superuser_view(self):
        page = self.client.get("/admin/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse("superuser"))


class TestLoginView(TestCase):
    def test_login_view(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")


class TestLogoutView(TestCase):
    def test_logout_view(self):
        page = self.client.get("/accounts/logout/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse("login"))


class TestRegisterView(TestCase):
    def test_register_view(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "register.html")


class TestProfileView(TestCase):
    def test_profile_view(self):
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse("profile"))
