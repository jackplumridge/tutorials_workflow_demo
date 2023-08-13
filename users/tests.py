from django.test import TestCase
from django.urls import reverse
import pytest

# Create your tests here.
# add a fixture for creating a test user object in the database:
# The django_user_model fixture is a built-in fixture. It acts as a shortcut to accessing the User model for this project.
# This fixture creates a new user with the Django create_user() method and sets a username and password.
# Then it returns the username and password as a tuple.  

@pytest.fixture
def test_user(db, django_user_model):
    django_user_model.objects.create_user(
        username="test_username", password="test_password")
    return "test_username", "test_password"   # this returns a tuple

# write a function to test that logging into the app works, using the test_user fixture as a parameter to first add a user:
# In the below code, the client passed in as a parameter is a built-in "dummy web client" provided by Django as part of testing tools.
# It mimics some of the functionality of a web browser and helps us test interacting with a Django app. 
# Its login() method helps us test that we can log into the app, the test_user fixture makes sure that we have valid user to test with.

def test_login_user(client, test_user):
    test_username, test_password = test_user                    # this unpacks the tuple
    login_result = client.login(username=test_username, password=test_password)
    assert login_result == True

