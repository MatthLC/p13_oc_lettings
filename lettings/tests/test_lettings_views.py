import pytest

from django.urls import reverse
from django.test import Client
from lettings.models import Address, Letting
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_letting_list_view():
    client = Client()

    address1 = Address.objects.create(
        number=1,
        street='somewhere',
        city='Paris',
        state='fr',
        zip_code='75000',
        country_iso_code='FRA'
    )

    address2 = Address.objects.create(
        number=1,
        street='moon',
        city='space',
        state='MO',
        zip_code='00000',
        country_iso_code='MOO'
    )

    Letting.objects.create(title='test letting view 1', address=address1)
    Letting.objects.create(title='test letting view 2', address=address2)

    path = reverse('lettings_index')
    response = client.get(path)
    content = response.content.decode()
    expected_title = 'title>Lettings</title>'
    expected_content1 = 'test letting view 1'
    expected_content2 = 'test letting view 2'

    assert content.find(expected_title) != -1
    assert content.find(expected_content1) != -1
    assert content.find(expected_content2) != -1
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/index.html')


@pytest.mark.django_db
def test_letting_retrieve_view():
    client = Client()
    address = Address.objects.create(
        number=1,
        street='somewhere',
        city='Paris',
        state='fr',
        zip_code='75000',
        country_iso_code='FRA'
    )

    letting = Letting.objects.create(title='test letting view', address=address)

    path = reverse('letting', kwargs={'letting_id': letting.id})
    response = client.get(path)
    content = response.content.decode()
    expected_content = 'title>test letting view</title>'

    assert content.find(expected_content) != -1
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/letting.html')
