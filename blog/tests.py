from django.test import TestCase
from .models import Post
from users.models import User
from django.urls import reverse


class PostsViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(email='admin@admin.com', password='1234', username='admin')
        Post.objects.create(content='Content', user=user)


    def test_postView_url_exist_at_descriibed_location(self):
        resp = self.client.get(reverse('index'))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'main.html')


    def test_createPostView_url_exist_at_descriibed_location(self):
        user = User.objects.get(id=1)
        data = {
            'user': user.id,
            'new_post':"content"
        }
        resp = self.client.post(reverse('blog-post-create'), data)
        self.assertEquals(resp.status_code, 200)

