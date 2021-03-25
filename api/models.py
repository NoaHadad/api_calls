from django.core.exceptions import ValidationError

from django.db import models

from django.utils import timezone

from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import HStoreField

# Create your models here.


class Quote(models.Model):
      name=models.CharField(max_length=200)

      def validation_positive(value):
          if value<0:
             raise ValidationError(('%(value)s is not an even number'),params={'value': value},)

      price=models.IntegerField(validators=[validation_positive])
      items=ArrayField(models.JSONField())
      deleted=models.IntegerField(default=0)
      
      def __str__(self):
          return "id: "+str(self.id)+", name: "+self.name+", price: "+str(self.price)+", items: "+str(self.items)+", deleted: "+str(self.deleted)

class QuoteLog(models.Model):
      created_date=models.DateTimeField(default=timezone.now)
      quote_id=models.IntegerField(default=-1)
      error_code=ArrayField(models.IntegerField(),default=list)
      message=ArrayField(models.CharField(max_length=200))

      class Operation(models.IntegerChoices):
        CREATE = 1
        UPDATE = 2
        DELETE = 3

      operation = models.IntegerField(choices=Operation.choices)

      def __str__(self):
          return "quote_id: "+str(self.quote_id)+", messege: "+str(self.message)+", error code: "+str(self.error_code)+", operation "+str(self.Operation.choices[self.operation])
