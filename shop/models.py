from django.db import models

# Create your models here.
class Trusted_Partner(models.Model):
    Partner_name = models.CharField(max_length=100)
    Partner_logo = models.ImageField(upload_to='images/')
    class Meta:
        verbose_name = ("Trusted_Partner")
        verbose_name_plural = ("Trusted_Partners")

    def __str__(self):
        return self.Partner_name



class shoe(models.Model):
    gender = [
        ('male','male'),
        ('female','female'),
    ]
    shoe_name = models.CharField(max_length=70)
    shoe_brand = models.ForeignKey("Trusted_Partner", on_delete=models.PROTECT,null=True,blank=True)
    shoe_desc = models.CharField( max_length=250)
    shoe_num = models.IntegerField()
    shoe_type =models.CharField(max_length=50,choices=gender)
    shoe_image =models.ImageField(upload_to='images/')
    shoe_price = models.IntegerField()
    class Meta:
        verbose_name = ("shoe")
        verbose_name_plural = ("shoes")

    def __str__(self):
        return self.shoe_name


