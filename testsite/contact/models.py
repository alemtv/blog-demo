from django.db import models


class Contact(models.Model):
    subject = models.CharField(max_length=255)
    email = models.EmailField(max_length=300)
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.subject