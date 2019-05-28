from django.db import models


class Municipality(models.Model):
    dian_code = models.CharField(
        max_length=255
    )

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.dian_code + ' - ' + self.name