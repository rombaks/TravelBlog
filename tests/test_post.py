from http import HTTPStatus

import factory
from base_test_views import TestViewSetBase
from factories import PostFactory


class TestPostViewSet(TestViewSetBase):
    basename = "posts"
    post_attributes = factory.build(dict, FACTORY_CLASS=PostFactory)

    BATCH_SIZE = 3
    posts_attributes = factory.build_batch(dict, FACTORY_CLASS=PostFactory, size=BATCH_SIZE)

    @staticmethod
    def expected_details(entity: dict, attributes: dict):
        return {"id": entity["id"], **attributes, "author": None, "tags": []}

    def expected_list(self, entity_list: list[dict], attributes_list: list[dict]):
        expected_list = []
        for index, entity in enumerate(entity_list):
            entity_details = self.expected_details(entity, attributes_list[index])
            expected_list.append(entity_details)
        return expected_list

    def test_create(self):
        post = self.create(self.post_attributes)
        expected_response = self.expected_details(post, self.post_attributes)
        expected_response["slug"] = post["slug"]
        assert post == expected_response

    def test_retrieve(self):
        post = self.create(self.post_attributes)
        expected_response = self.expected_details(post, self.post_attributes)
        expected_response["slug"] = post["slug"]
        retrieved_post = self.retrieve(post["slug"])
        assert retrieved_post == expected_response

    def test_list(self):
        posts = self.create_batch(self.posts_attributes)
        expected_response = self.expected_list(posts, self.posts_attributes)
        post_list = self.list()
        for post in post_list:
            post["slug"] = "mock-super-puper-slug"
        assert post_list == expected_response

    def test_update(self):
        post = self.create(self.post_attributes)
        new_data = {"title": "backup"}
        updated_attributes = dict(self.post_attributes, **new_data)
        expected_response = self.expected_details(post, updated_attributes)
        expected_response["slug"] = post["slug"]
        response = self.update(new_data, post["slug"])
        assert response == expected_response

    def test_delete(self):
        post = self.create(self.post_attributes)
        response = self.delete(post["slug"])
        assert response.status_code == HTTPStatus.NO_CONTENT

    def test_not_found(self):
        response = self.client.get("/not_found")
        assert response.status_code == HTTPStatus.NOT_FOUND
