from django.db import models

# Create your models here.

# class mitesh(models.Model):
#     name=models.CharField(max_length=50)
#     age=models.IntegerField()
#     email=models.EmailField(max_length=254)
#     message=models.TextField()
#     contact=models.IntegerField()
 

# class bike(models.Model):
#     name=models.CharField(max_length=50)
#     speed=models.IntegerField()
#     model = models.IntegerField()

#     def _str__(self) ->str:
#         return self.bike

class h(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    message=models.TextField(max_length=500)
    image=models.ImageField(upload_to="tcp/")   

class m(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.CharField(max_length=50)
    password=models.CharField()

    

class data(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()

    def __str__(self):
        return self.name
    

class movie(models.Model):
    year=models.IntegerField()
    acter=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class news(models.Model):
    message=models.CharField(max_length=500)
    name=models.CharField(max_length=250)
    email=models.EmailField()
    subject=models.CharField(max_length=250)


class contactus(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contactu=models.IntegerField()
    password=models.CharField(max_length=50)
    confirm =models.CharField(max_length=50)
    # return redirect    

    # class meta:
    #     db_tabele="contactus"
    #     user = user.objects.create_user(username = username, password = passwoerd , first_name = first_name , last_name = last_name)
    #     return redirect

class Contact(models.Model):
    message=models.TextField()
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.TextField()





