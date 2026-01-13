#  'add bits from other files'.
from django.conf import settings
from django.db import models
from django.utils import timezone

# defines the model (an object)
# 'class' is used to define an object.
# models.Model means the Post is a Django Model so that Django knows to save it in the database
class Post(models.Model):
  #properties and their characteristics
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #link to another model
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

# 'def' is used for methods
# indentation inside of the class Post links the methods to the class
  def publish(self):
      self.published_date = timezone.now()
      self.save()

  def __str__(self):
      return self.title




