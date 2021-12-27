from django.test import TestCase
from content_app.repositories import PostRepository
from content_app.models import Post
from account_app.models import UserModel
from category_app.models import Category

from mixer.backend.django import mixer


class PostRepositoryTestCase(TestCase):

    def setUp(self):
        self.post_repository : PostRepository = PostRepository()
        self.category = mixer.blend(scheme=Category, name='Tech', description='About Tech')
        self.user = mixer.blend(scheme=UserModel)
        self.gues_user = mixer.blend(scheme=UserModel, email='gues@user.com')
        self.post = mixer.blend(scheme=Post, title='Hello', content='Test your content', user=self.user)
        self.post.categories.add(self.category)

        self.banner_post = mixer.blend(scheme=Post, title='Banner', is_banner=True)

    def test_contain_favourite_user_false(self):
        self.post_repository.favourite(user=self.gues_user, slug=self.post.slug)
        self.assertTrue(self.post_repository.is_users_liked_contain(self.post.slug, self.gues_user))

    def test_favourite_success(self):
        self.post_repository.favourite(user=self.user, slug=self.post.slug)
        self.assertEqual(1, self.post.users_liked.count())

    def test_un_favourite_success(self):
        self.post_repository.favourite_unfavourite(user=self.user, slug=self.post.slug)
        self.post_repository.favourite_unfavourite(user=self.user, slug=self.post.slug)
        self.assertEqual(0, self.post.users_liked.count())

    def test_count_size_1_true(self):
        self.assertEqual(2, self.post_repository.count())

    def test_is_favourite_attribute_available(self):
        self.post_repository.favourite(self.gues_user
                                       , self.post.slug)
        result = self.post_repository.find(user=self.gues_user)
        self.assertEqual(1, result[0].is_favourite)

    def test_filter_by_own_post_size_1(self):
        self.assertEqual(1, self.post_repository.filter(user=self.user).count())

    def test_filter_title_content_size_1(self):
        self.assertEqual(1, self.post_repository.filter(user=self.user, params={
                                                            'title' : 'He',
                                                            'content' : 'content'
                                                        },
                                                        category=self.category.id).count())

    def test_filter_banner_content_size1(self):
        self.assertEqual(1, self.post_repository.find_banner().count())
