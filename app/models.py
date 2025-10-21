from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)


class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование", null=False, blank=False)
    country = models.CharField(max_length=255, verbose_name="Страна", null=False, blank=False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    desc = models.TextField(max_length=1000, null=False, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=9, null=False, blank=False)
    image_url = models.URLField(null=False, blank=False)

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
