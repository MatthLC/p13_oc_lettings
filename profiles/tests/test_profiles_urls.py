import pytest

from django.urls import reverse, resolve
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profile_list_url():
    path = reverse('profiles_index')

    assert path == '/profiles/'
    assert resolve(path).view_name == 'profiles_index'


@pytest.mark.django_db
def test_profile_retrieve_url():
    user = User.objects.create(username='testman', password='testpassword')

    profile = Profile.objects.create(user=user, favorite_city='moon space')

    path = reverse('profile', kwargs={'username': profile.user.username})

    assert path == '/profiles/testman/'
    assert resolve(path).view_name == 'profile'
