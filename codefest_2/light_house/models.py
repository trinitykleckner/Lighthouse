
# Create your models here.
from django.db import models


class Page(models.Model):
    header = models.CharField(max_length=1000)
    content1 = models.CharField(max_length=10000, default="")
    content2 = models.CharField(max_length=10000, default="")
    prompt = models.CharField(max_length=1000, default="")



    def toDict(self):
        d = {
            "header": self.header,
            "body": self.content1,
            "options/response": self.content2,
            "prompt": self.prompt,
        }
        return d

    def getOptions(self):
        return self.content2[5:].split(",")

    def __str__(self):
        return self.header
