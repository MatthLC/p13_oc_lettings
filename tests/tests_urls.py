import pytest

from django.urls import reverse, resolve


@pytest.mark.django_db
def test_home_page_url():
    path = reverse('index')

    assert path == '/'
    assert resolve(path).view_name == 'index'
