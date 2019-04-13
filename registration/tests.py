from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

#Validate the link of a profile when an user have been created
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test','test@test.com', 'test1234')
    
    def test_profile_exists(self):
        exist = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exist, True)