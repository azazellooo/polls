from django.db import models


QUESTION_TYPES = [
    ('text', 'text'),
    ('choice', 'choice'),
    ('choices', 'choices'),
]

class Poll(models.Model):
    name = models.CharField(max_length=200)
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=3000)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=300)
    type = models.CharField(max_length=200, choices=QUESTION_TYPES, default=QUESTION_TYPES[0])
    poll = models.ForeignKey('api.Poll', on_delete=models.CASCADE, related_name='polls')

    def __str__(self):
        return self.text

class Answer(models.Model):
    poll = models.ForeignKey('api.Poll', on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey('api.Question', on_delete=models.CASCADE, related_name='questions')
    participant = models.PositiveIntegerField()
    text = models.CharField(max_length=400)

    def __str__(self):
        return f"User #{self.participant}'s answer to question '{self.question}'. "

# Create your models here.

