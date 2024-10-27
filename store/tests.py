from django.test import TestCase
from django.urls import reverse
from store import factories, models

# Create your tests here.


class StoreTesrCase(TestCase):

    def setUp(self):
        self.store = factories.StoryFactory()

    def test_get_store_list(self):
        url = reverse("store-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, second=200)
        self.assertEqual(
            response.context["store"].count(), models.store.objects.count()
        )
        print(response.context["store"].count(), models.store.objects.count())

    def test_get_store_list(self):
        url = reverse("store-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["store"].count(), models.store.objects.count()
        )

    def test_get_store_detail(self):

        url = reverse("store-detail", kwargs={"pk": self.store.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_store(self):
        url = reverse("store-update", kwargs={"pk": self.store.pk})
        old_title = self.store.title
        old_description = self.store.description
        response = self.client.post(url, {"title": "new_title"})
        self.store.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(self.store.title, old_title)
        self.assertEqual(self.store.description, old_description)

    def test_delete_store(self):
        url = reverse("store_delete", kwargs={"pk": self.store.pk})
        old_store_count = models.store.objects.count()
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 302)
        self.assertGreater(old_store_count, models.store.objects.count())
        print(old_store_count, models.store.objects.count())

    def test_create_store(self):
        url = reverse("store-create")
        old_store_count = models.store.objects.count()

        response = self.client.post(
            url,
            {
                "name": "New store Title",
                "description": "This is a new store description",
            },
        )

        new_store_count = models.store.objects.count()

        self.assertEqual(response.status_code, 302)
        self.assertGreater(new_store_count, old_store_count)