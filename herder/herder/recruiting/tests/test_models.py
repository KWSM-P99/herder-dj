from django.test import TestCase
from django.utils import timezone
from ..models import Application, CharacterClass, ApplicationStatus
from herder.users.models import User

class ApplicationModelTest(TestCase):

    def setUp(self):
        # this is a test of a good user submission
        self.test_user_one = User.objects.create_user(username='test_user_one', password='test_password_one')
        self.test_application_one = Application.objects.create(
            main_character='test_character_one',
            class_name=CharacterClass.WARRIOR,
            level=15,
            reason='test_reason_one',
            know_anyone='test_know_anyone_one',
            grouped_with_anyone='test_grouped_with_anyone_one',
            expectations='test_expectations_one',
            characteristics='test_characteristics_one',
            group_in_fireplace='test_group_in_fireplace_one',
            alts='test_alts_one',
            comments='test_comments_one',
            user=self.test_user_one
        )


    def test_application_one_creation(self):
        self.assertIsInstance(self.test_application_one, Application)
        self.assertEqual(self.test_application_one.user.username, 'test_user_one')
        self.assertEqual(self.test_application_one.main_character, 'test_character_one')
        self.assertEqual(self.test_application_one.status, ApplicationStatus.PENDING)

    def test_application_one_status(self):
        self.assertEqual(self.test_application_one.status, ApplicationStatus.PENDING)

    def test_application_str(self):
        self.assertEqual(str(self.test_application_one), 'test_character_one')

    def test_application_timestamps(self):
        self.assertIsInstance(self.test_application_one.created_at, timezone.datetime)
        self.assertIsInstance(self.test_application_one.updated_at, timezone.datetime)

    # test approval
    def test_application_approval(self):
        self.test_application_one.approve()
        self.assertEqual(self.test_application_one.status, ApplicationStatus.APPROVED)
        
    # test rejection
    def test_application_rejection(self):
        self.test_application_one.reject()
        self.assertEqual(self.test_application_one.status, ApplicationStatus.REJECTED)

    # test level too low
    def test_application_level_too_low(self):
        self.assertEqual(self.test_application_two.level, 10)
        
    # test creating application with level too low, should fail validation
    def test_application_level_too_low(self):
        with self.assertRaises(Exception):
            self.test_application_two = Application.objects.create(
                main_character='test_character_two',
                class_name=CharacterClass.WARRIOR,
                level=10,
                reason='test_reason_two',
                know_anyone='test_know_anyone_two',
                grouped_with_anyone='test_grouped_with_anyone_two',
                expectations='test_expectations_two',
                characteristics='test_characteristics_two',
                group_in_fireplace='test_group_in_fireplace_two',
                alts='test_alts_two',
                comments='test_comments_two',
                user=self.test_user_one
            )
            self.test_application_two.full_clean()