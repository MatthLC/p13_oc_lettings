import pytest

from django.urls import reverse, resolve
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_Address_list_url():
    path = reverse('lettings_index')

    assert path == '/lettings/'
    assert resolve(path).view_name == 'lettings_index'


@pytest.mark.django_db
def test_Address_retrive_url():
    address = Address.objects.create(
        number=1,
        street='somewhere',
        city='Paris',
        state='fr',
        zip_code='75000',
        country_iso_code='FRA'
    )

    letting = Letting.objects.create(title='osef', address=address)

    path = reverse('letting', kwargs={'letting_id': letting.id})

    assert path == '/lettings/1/'
    assert resolve(path).view_name == 'letting'
