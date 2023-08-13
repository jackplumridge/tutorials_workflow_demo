from django.test import TestCase
from django.urls import reverse
import pytest
from tutorials.models import Tutorial

# Create your tests here.

def test_homepage_access():
    url = reverse('home')
    assert url == "/"

# Integration tests determine whether multiple components in an application are able to integrate with one another.
# We will next write integration tests to see whether we can successfully interact with the database via Django models/ORM.
# This test verifies that we are able to successfully create a Tutorial object in the database.
# Adding the marker    @pytest.mark.django_db    directly above the test function declaration to allow access to the database.

"""
@pytest.mark.django_db                         # commenting this out for exercise
def test_create_tutorial():
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    assert tutorial.title == "Pytest"
"""

# This new_tutorials() fixture function will create a new tutorial object with the attributes described (title of 'Pytest') 
# Then, in that test function, that tutorial object will be available to use under the same name as the function name, new_tutorial.

@pytest.fixture
def new_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

"""
These test functions below use new_tutorial as a parameter. 
This causes the new_tutorial() fixture function to be run first when either of these tests is run.
The first test simply checks that the object created by the fixture exists, by searching for an object with the same title.
The second test updates the title of the new_tutorial object, saves it, & asserts that a tutorial with the new name exists in database. 
Inside this test function's body, new_tutorial refers not to the new_tutorial fixture function, but to the object returned from it.
"""

def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()

def test_update_tutorial(new_tutorial):
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()

# integration test with fixtures, to show how multiple fixtures may be used in a test function.
@pytest.fixture
def another_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='More-Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

# adding a test that uses both fixtures as parameters
def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk

# Both the objects returned from the new_tutorial and another_tutorial fixtures are passed in.
# Then, the test asserts that the .pk attributes are not equal to the other.
# The .pk attribute in the Django ORM refers to the primary key of a database object, which is automatically generated when its created.
# Thus, this is simply asserting that the two objects are not the same as each other. 