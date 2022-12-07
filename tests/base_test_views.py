from http import HTTPStatus
from typing import List, Optional, Union

from django.urls import reverse

import factory
from factories import UserFactory
from rest_framework.test import APIClient, APITestCase
from travel_blog.main.models import User


class TestViewSetBase(APITestCase):
    user: Optional[User] = None
    client: APIClient = None
    basename: str

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.user = cls.create_api_user()
        cls.client = APIClient()

    @staticmethod
    def create_api_user():
        user_attributes = factory.build(dict, FACTORY_CLASS=UserFactory)
        return User.objects.create(**user_attributes)

    @classmethod
    def detail_url(cls, key: Optional[int]) -> str:
        return reverse(f"{cls.basename}-detail", args=[key])

    @classmethod
    def list_url(cls, args: List[Union[str, int]] = None) -> str:
        return reverse(f"{cls.basename}-list", args=args)

    def create(self, data: dict, args: List[Union[str, int]] = None) -> dict:
        self.client.force_login(self.user)
        response = self.client.post(self.list_url(args), data=data)
        assert response.status_code == HTTPStatus.CREATED, response.content
        return response.data

    def request_create(self, data: dict, args: List[Union[str, int]] = None) -> dict:
        self.client.force_login(self.user)
        response = self.client.post(self.list_url(args), data=data)
        return response

    def create_batch(self, batch_attributes: list[dict]) -> list[dict]:
        batch = [self.create(data) for data in batch_attributes]
        return batch

    def retrieve(self, id: int = None) -> dict:
        self.client.force_login(self.user)
        response = self.client.get(self.detail_url(id))
        assert response.status_code == HTTPStatus.OK, response.content
        return response.data

    def list(self) -> dict:
        self.client.force_login(self.user)
        response = self.client.get(self.list_url())
        assert response.status_code == HTTPStatus.OK, response.content
        return response.data

    def update(self, data: dict, id: int = None) -> dict:
        self.client.force_login(self.user)
        response = self.client.patch(self.detail_url(id), data=data)
        assert response.status_code == HTTPStatus.OK, response.content
        return response.data

    def delete(self, id: int = None) -> dict:
        self.client.force_login(self.user)
        response = self.client.delete(self.detail_url(id))
        assert response.status_code == HTTPStatus.NO_CONTENT
        return response

    def anonymous_create(self, data: dict, args: List[Union[str, int]] = None) -> dict:
        self.client.logout()
        response = self.client.post(self.list_url(args), data=data)
        assert response.status_code == HTTPStatus.FORBIDDEN
        return response.data
