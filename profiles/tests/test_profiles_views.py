import pytest

from django.urls import reverse
from django.test import Client
from profiles.models import Profile
from pytest_django.asserts import assertTemplateUsed
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profile_list_view():
    client = Client()

    user1 = User.objects.create(username='testman1', password='testpassword1')
    user2 = User.objects.create(username='testman2', password='testpassword2')

    Profile.objects.create(user=user1, favorite_city='moon space')
    Profile.objects.create(user=user2, favorite_city='sun space')

    path = reverse('profiles_index')
    response = client.get(path)
    content = response.content.decode()

    expected_title = 'title>Profiles</title>'
    expected_content1 = 'testman1'
    expected_content2 = 'testman2'

    assert content.find(expected_title) != -1
    assert content.find(expected_content1) != -1
    assert content.find(expected_content2) != -1
    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/index.html')


@pytest.mark.django_db
def test_profile_retrieve_view():
    client = Client()

    user = User.objects.create(username='testman', password='testpassword')
    profile = Profile.objects.create(user=user, favorite_city='moon space')

    path = reverse('profile', kwargs={'username': profile.user.username})
    response = client.get(path)
    content = response.content.decode()
    expected_content = 'title>testman</title>'

    assert content.find(expected_content) != -1
    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/profile.html')
