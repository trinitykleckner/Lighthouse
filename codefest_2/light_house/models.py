
# Create your models here.
from django.db import models


class Page(models.Model):
    header = models.CharField(max_length=1000)
    content = models.CharField(max_length=5000)

    def toDict(self):
        d = {
            "header": self.header,
            "content": self.content
        }

        return d


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)


