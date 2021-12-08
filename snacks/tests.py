from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class TestSnack(TestCase):

    def test_status_code(self):
        url1=reverse('snack_list')
        res1=self.client.get(url1)
        self.assertEqual(res1.status_code , 200)


    def test_template_Use(self):
        url1=reverse('snack_list')
        res1=self.client.get(url1)
        self.assertTemplateUsed(res1 , 'snacks/snack_list.html')
        self.assertTemplateUsed(res1 , 'snacks/_parent.html')

    def test_status_code2(self):
        url1=reverse('snack_detail')
        res1=self.client.get(url1 , kwargs={'id':1})
        self.assertEqual(res1.status_code , 200)


    # def test_template_Use2(self):
    #     url1=reverse('snack_detail/1')
    #     res1=self.client.get(url1)
    #     self.assertTemplateUsed(res1 , 'snacks/snack_detail.html')
    #     self.assertTemplateUsed(res1 , 'snacks/_parent.html')
