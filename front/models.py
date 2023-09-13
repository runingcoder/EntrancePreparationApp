from pyexpat import model
from re import M
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
import random

DIFF_CHOICES = (
    ("easy", "easy"),
    ("medium", "medium"),
    ("hard", "hard"),
)


class MockTest(models.Model):
    text = models.CharField(max_length=200)
    test_number = models.IntegerField(default=0)

    def __str__(self):
        return str(self.text) 


class Quiz(models.Model):
    name = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="required score in %")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)
    mock = models.ForeignKey(MockTest, on_delete=models.CASCADE, related_name="mocker")

    def __str__(self):
        return str(self.name) + " test number = " + str(self.mock.test_number)
    def getNameInResult(self):
        return str(self.name) + ' in ' +str(self.mock.text)


    def get_questions(self):
        questions = list(self.question_set.all())
        #         random.shuffle(questions)
        return questions[: self.number_of_questions]

    class Meta:
        verbose_name_plural = "Quizzes"


class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    date_attempted = models.DateTimeField(auto_now_add=True, null=True)  # Date and time of the attempt
    resultsField = models.JSONField(null=True)
    passed = models.BooleanField(null=True)
    progresschartid = models.IntegerField(null=True)


    def __str__(self):
        return f" {str(self.pk)} and score is {str(self.score)}"
    