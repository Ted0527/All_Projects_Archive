from django.db import models

class Menu(models.Model):
    name      = models.CharField(max_length=20)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name      = models.CharField(max_length=20)
    menu      = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Drink(models.Model):
    ko_name      = models.CharField(max_length=30)
    en_name      = models.CharField(max_length=30)
    description  = models.TextField(max_length=200, null=True)
    category  = models.ForeignKey('Category', on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'drinks'

class AllergyDrink(models.Model):
    drink     = models.ForeignKey('Drink', on_delete=models.CASCADE)
    allergy   = models.ForeignKey('Allergy', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_drink'

class Allergy(models.Model):
    name      = models.CharField(max_length=20)

    class Meta:
        db_table = 'allergies'

class Images(models.Model):
    image_url = models.CharField(max_length=2000)
    drink     = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Size(models.Model):
    name             = models.CharField(max_length=20)
    size_ml          = models.CharField(max_length=20, null=True)
    size_fluid_ounce = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'sizes'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    sodium_mg        = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    saturated_fat_g  = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    sugars_g         = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    protein_g        = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    caffeine_mg      = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    drink            = models.ForeignKey('Drink', on_delete=models.CASCADE, null=True)
    size             = models.ForeignKey('Size', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'nutritions'

# Create your models here.
