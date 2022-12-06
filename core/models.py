from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    yaratgan = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    toifalar = models.CharField(max_length=55)
    fotografiya = models.CharField(max_length=30)
    tegs = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    shaharlar = models.CharField(max_length=255)
    fasl = models.CharField(max_length=255)
    rasm = models.CharField(max_length=255)
    vidiografiya = models.CharField(max_length=255)
    raqam = models.IntegerField(default=1)
    raqamcha = models.IntegerField(default=1)
    kubok = models.IntegerField(default=1)
    lop = models.IntegerField(default=1)
    mening = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name
