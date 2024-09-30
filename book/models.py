from django.db import models



class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/",null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
