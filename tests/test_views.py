import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_home_page_view():
    client = Client()

    path = reverse('index')
    response = client.get(path)
    content = response.content.decode()
    expected_title = 'title>Holiday Homes</title>'

    assert content.find(expected_title) != -1
    assert response.status_code == 200
    assertTemplateUsed(response, 'index.html')
