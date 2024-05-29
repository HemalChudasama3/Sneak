from django.db import models

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Image(models.Model):
    shoe = models.ForeignKey(Shoe, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shoe_images/')

    def __str__(self):
        return self.shoe.name
