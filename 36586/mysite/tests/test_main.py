import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('user', 'user@mail.ru', 'password')
    assert User.objects.count() == 1
    
    
@pytest.mark.django_db
def test_view(admin_client):
    # url = reverse('')
    response = admin_client.get('http://localhost:8000/home/')
    print(response.content)
    assert response.status_code == 200
