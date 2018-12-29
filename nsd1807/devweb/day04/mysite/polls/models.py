from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    q = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s" % (self.choice_text, self.q)
