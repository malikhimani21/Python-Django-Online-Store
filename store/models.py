from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class TshirtProperty(models.Model):
    title = models.CharField(max_length=20, null=False)
    slug = models.CharField(max_length=30, null=False, unique=True)

    # User Meta class and abstract which means dont create table fot
    # TshirtProperty class
    class Meta:
        abstract = True


class Occasion(TshirtProperty):
    pass


class IdealFor(TshirtProperty):
    pass


class NeckType(TshirtProperty):
    pass


class Sleeve(TshirtProperty):
    pass


class Brand(TshirtProperty):
    pass


class Color(TshirtProperty):
    pass


class Tshirt(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=500, null=True)
    discount = models.IntegerField(default=0)
    image = models.ImageField(upload_to='upload/images', null=False)
    occasion = models.ForeignKey(Occasion, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    sleeve = models.ForeignKey(Sleeve, on_delete=models.CASCADE)
    neck_type = models.ForeignKey(NeckType, on_delete=models.CASCADE)
    ideal_for = models.ForeignKey(IdealFor, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
