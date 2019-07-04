from django.test import TestCase
from webapp.models import RIG
from django.utils import timezone


class RIGTest(TestCase):

    def create_webapp(self, title="only a test", body="yes, this is only a test"):
        return RIG.objects.create(rig_name=title, rig_sname=body)

    def test_webapp_creation(self):
        w = self.create_webapp()
        self.assertTrue(isinstance(w, RIG))
        self.assertEqual(w.__str__(), w.rig_sname)