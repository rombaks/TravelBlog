import factory
from base import faker
from travel_blog.main.models import Post, Tag, User


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.LazyAttribute(lambda _: faker.unique.word())
    email = factory.LazyAttribute(lambda _: faker.unique.email())
    first_name = factory.LazyAttribute(lambda _: faker.first_name())
    last_name = factory.LazyAttribute(lambda _: faker.last_name())

    class Meta:
        model = User


class TagFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda _: faker.unique.word())

    class Meta:
        model = Tag


class PostFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda _: faker.text(max_nb_chars=10))
    content = factory.LazyAttribute(lambda _: faker.text(max_nb_chars=50))
    author = factory.SubFactory(UserFactory)
    created_at = factory.LazyAttribute(lambda _: faker.past_datetime().strftime("%Y-%m-%dT%XZ"))
    updated_at = factory.LazyAttribute(lambda _: faker.past_datetime().strftime("%Y-%m-%dT%XZ"))

    status = factory.LazyAttribute(
        lambda _: faker.word(
            ext_word_list=[
                "new",
                "in_development",
            ]
        )
    )

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.groups.add(*extracted)

    class Meta:
        model = Post
