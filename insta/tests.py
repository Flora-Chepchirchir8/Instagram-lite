from django.test import TestCase

from .models import Comment, Profile, Image
from django.contrib.auth.models import User


class ProfileTestCase(TestCase):
    
    def setUp(self):
        self.user = User(username='Kipkorir')
        self.user.save()

        self.profile = Profile(id=12 ,profile_picture='image.jpg', bio='Test profile',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) >0)

    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.user_id)
        self.profile.save_profile()
        self.assertTrue(Profile,self.profile.user)

class ImageTestClass(TestCase):
   
    def setUp(self):
        self.user = User.objects.create_user("username", "password")
        self.new_profile = Profile(id = 12,profile_picture='image.png',bio='Test profile',user=self.user)
        self.new_profile.save()
        self.new_image = Image(image='image.png',image_caption="image", image_profile=self.new_profile)

    def test_instance_true(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_image(self):
        self.new_image.save_image()
        img = Image.objects.all()
        self.assertTrue(len(img) == 1)

    def test_delete_imae(self):
        self.new_image.save_image()
        img = Profile.objects.all()
        self.assertTrue(len(img) <= 1)

    def test_get_image_by_id(self):
        self.new_image.save_image()
        img = self.new_image.get_image_by_id(self.new_image.id)
        images = Image.objects.filter(id=self.new_image.id)
        self.assertTrue(img, images)    

class CommentTestCase(TestCase):
    def setUp(self):
        self.user = User(username='Kipkorir')
        self.user.save()

        self.new_profile = Profile(profile_picture='image.png',bio='Test profile description',user=self.user)
        self.new_profile.save()
        self.new_image = Image(image='image.png',image_caption="image", image_profile=self.new_profile)
        self.comment = Comment(comment='Your Best Image', user=self.new_profile, post = self.new_image, date="14-10-2021")

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        self.comment.save_comment()
        comment = Comment.objects.all()
        self.assertFalse(len(comment) > 1)

    def test_delete_comment(self):
        self.comment.save_comment()
        comment = Comment.objects.all()
        self.assertTrue(len(comment)  <= 1)