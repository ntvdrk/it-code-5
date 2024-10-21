from django.db import models

# Create your models here.
class store(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', verbose_name="Product Image")
    price = models.PositiveIntegerField(blank=True, null=True, verbose_name="Price")

    def str(self):
        return self.name
    
    class Meta:
        verbose_name='продукт'
        verbose_name_plural='продукты'
        

        

    


