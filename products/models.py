from django.db import models
from django.contrib.auth.models import User

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    image = models.ImageField(upload_to='trainers/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_favorite = models.BooleanField(default=False)
    is_best = models.BooleanField(default=False)  # Новое поле

    def __str__(self):
        return self.name

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='subscriptions/', default='default_product_image.jpg')

    def __str__(self):
        return self.name

class Appointment(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.trainer.name} - {self.user.username} - {self.date} {self.time}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} booked {self.trainer.name} on {self.date}"

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscriptions = models.ManyToManyField(Subscription)
    bookings = models.ManyToManyField(Booking)

    def __str__(self):
        return f"Cart for {self.user.username}"
