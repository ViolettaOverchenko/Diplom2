from django.test import TestCase
from analysis_material.models import Document
from django.urls import reverse

from django.contrib.auth.models import User # Необходимо для представления User как borrower

class DocumentByUserListViewTest(TestCase):

    def setUp(self):
        # Создание двух пользователей
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()
        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        test_user2.save()

        number_of_documents = 13
        for document_num in range(number_of_documents):
            if document_num % 2:
                usertest = test_user1
            else:
                usertest = test_user2
            Document.objects.create(user = usertest, name_document ='Материал %s' % document_num, path_file='Файл %s' % document_num,)

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('personal_account'))

        # Проверка что пользователь залогинился
        self.assertEqual(str(resp.context['user']), 'testuser1')
        # Проверка ответа на запрос
        self.assertEqual(resp.status_code, 200)

        # Проверка того, что мы используем правильный шаблон
        self.assertTemplateUsed(resp, 'analysis_material/personal_account.html')

        #Подтверждение, что все документы принадлежат testuser1
        for document in resp.context['document_list']:
            self.assertEqual(resp.context['user'], document.user)
