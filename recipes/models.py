from django.db import models
from django.contrib.auth.models import User
from  gdstorage.storage  import  GoogleDriveStorage

gd_storage  =  GoogleDriveStorage()
# Create your models here.

class Recipes(models.Model):

    user = models.ManyToManyField(User, related_name = 'userRecipe')
    reName = models.CharField(max_length = 128)
    solution = models.TextField()
    ingredient = models.TextField()
    Image  =  models.ImageField ( upload_to = 'images/' ,  storage = gd_storage ,default="")
    voteUp = models.ManyToManyField(User, related_name = 'recipeVoteUp')
    voteDown = models.ManyToManyField(User, related_name = 'recipeVoteDown')

    def __str__(self):
	    return f"ID: {self.pk} | Recipe: {self.reName} "

class Tags(models.Model):
    tagName = models.CharField(max_length = 64)
    tagID = models.ManyToManyField(Recipes)

    def __str__(self):
        return f"Tag = {self.tagName}"
