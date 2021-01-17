from django.db import models


class Block(models.Model):
    """Blockhain element with some parameters"""

    height = models.IntegerField(editable=False)
    hash = models.CharField(max_length=200)
    timestamp = models.IntegerField()
    miner = models.CharField(max_length=200)
    transactionCount = models.IntegerField()
    date_time = models.DateTimeField()

    class Meta(object):
        ordering = ['-height']

    def __str__(self):
        return str(self.height)
