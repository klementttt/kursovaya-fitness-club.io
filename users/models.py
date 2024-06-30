# users/models.py
from django.db import models
from django.contrib.auth.models import User

# Ваши модели

def get_trainer():
    from products.models import Trainer
    return Trainer

class Appointment(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.DateTimeField()
    field3 = models.TextField()
    # добавьте другие поля по необходимости

    def __str__(self):
        return self.field1
# Пример использования
# trainer = get_trainer().objects.get(id=1)
