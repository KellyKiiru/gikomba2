from django.db import models


class Bale(models.Model):
    clothe_type = models.CharField(blank=False, max_length=100)
    material = models.CharField(blank=False, max_length=100)
    origin_country = models.CharField(blank=False, max_length=100)
    weight = models.DecimalField(max_digits=7, decimal_places=1,default=40, blank=False, null=False)
    age = models.DecimalField(max_digits=7, decimal_places=1,default=18)
    gender = models.CharField(blank=False, max_length=100)
    season = models.CharField(blank=False, max_length=100)
    grade = models.CharField(blank=False, max_length=100)
    code = models.CharField(blank=False, max_length=100)
    pieces = models.DecimalField(max_digits=7, decimal_places=1,default=100)
    price = models.DecimalField(max_digits=7, decimal_places=1,default=7999)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):        
        super().save(*args, **kwargs)

    def __str__(self):
        return f' {self.clothe_type} - {self.code}'
    
    class Meta:
        ordering = ['created']