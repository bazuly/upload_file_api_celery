from django.db import models


class File(models.Model):
    title = models.CharField(max_length=128, null=True, blank=True)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        if self.title:
            return self.title
