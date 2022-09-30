import pytest
from .models import Participant
from django.urls import reverse


@pytest.mark.django_db
def test_get_participants(client):
    Participant.objects.create(
        reference_number="KGF-123",
        name="john",
        date_of_birth="2022-09-30",
        phone_number="+123456789",
        address="Baker Street London",
    )
    url = reverse("participants_list_create")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_participant(client):
    payload = {
        "reference_number": "AJS-4412",
        "name": "string",
        "date_of_birth": "2022-09-30",
        "phone_number": "string",
        "address": "string",
    }
    url = reverse("participants_list_create")
    response = client.post(url, data=payload)
    assert response.status_code == 201


@pytest.mark.django_db
def test_get_participant(client):
    Participant.objects.create(
        reference_number="KGF-123",
        name="john",
        date_of_birth="2022-09-30",
        phone_number="+123456789",
        address="Baker Street London",
    )
    url = reverse("participants_retrive_update_delete",
                  kwargs={"pk": "KGF-123"})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_participant(client):
    Participant.objects.create(
        reference_number="KGF-123",
        name="john",
        date_of_birth="2022-09-30",
        phone_number="+123456789",
        address="Baker Street London",
    )
    url = reverse("participants_retrive_update_delete",
                  kwargs={"pk": "KGF-123"})
    response = client.delete(url)
    assert response.status_code == 204


@pytest.mark.django_db
def test_put_participant(client):
    Participant.objects.create(
        reference_number="KGF-123",
        name="john",
        date_of_birth="2022-09-30",
        phone_number="+123456789",
        address="Baker Street London",
    )
    payload = {
        "name": "put-name",
        "date_of_birth": "2022-09-30",
        "phone_number": "put-phone",
        "address": "put-address",
    }
    url = reverse("participants_retrive_update_delete",
                  kwargs={"pk": "KGF-123"})
    response = client.put(url, data=payload, content_type="application/json",)
    assert response.data['name'] == payload['name']
    assert response.data['date_of_birth'] == payload['date_of_birth']
    assert response.data['phone_number'] == payload['phone_number']
    assert response.data['address'] == payload['address']
    assert response.status_code == 200


@pytest.mark.django_db
def test_patch_participant(client):
    Participant.objects.create(
        reference_number="KGF-123",
        name="john",
        date_of_birth="2022-09-30",
        phone_number="+123456789",
        address="Baker Street London",
    )
    payload = {
        "name": "updated-name"
    }
    url = reverse("participants_retrive_update_delete",
                  kwargs={"pk": "KGF-123"})
    response = client.patch(
        url, data=payload, content_type="application/json",)
    updated_name = response.data['name']
    assert updated_name == payload['name']
    assert response.status_code == 200
