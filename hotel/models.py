from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(
        max_length=250,
        verbose_name='Category_name:'
    )
    category_slug = models.SlugField(
        max_length=250,
        verbose_name='Slug:'
    )
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categorys'
    
    def __str__(self):
        return self.category_name

class Room(models.Model):
    room_name = models.CharField(
        max_length=250,
        verbose_name='Room_name:'
    )
    room_slug = models.SlugField(
        max_length=250,
        verbose_name='Slug:'
    )
    
    class Meta:
        verbose_name='Room'
        verbose_name_plural='Rooms'
    
    def __str__(self):
        return self.room_name
    


class Hotel(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=255,verbose_name='Hotel name:')
    hotel_phone = models.IntegerField(verbose_name='Phone number:')
    adress = models.CharField(max_length=255,verbose_name='Adress:')
    lokatsia = models.CharField(max_length=255,verbose_name='Lokatsia:')
    room_type = models.ForeignKey(Room,on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='price:')
    image1 = models.ImageField(verbose_name='Image_1:')
    image2 = models.ImageField(verbose_name='Image_2:')
    image3 = models.ImageField(verbose_name='Image_3:')
    descriptions = models.TextField(verbose_name='Descriptions:')
    
    class Meta:
        verbose_name='Hotel'
        verbose_name_plural='Hotels'
    
    def __str__(self):
        return self.hotel_name
    
    