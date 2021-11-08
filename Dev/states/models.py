from django.db import models
import uuid

# Create your models here.
class States(models.Model):
    name = models.CharField(max_length=200,)
    stateCode = models.CharField(max_length=100,)
    isMerchBuyState = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)


    def __str__(self):
        return self.name 