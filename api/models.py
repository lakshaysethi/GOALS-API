from django.db import models

# Create your models here.





class Goal(models.Model):
    name = models.CharField(max_length=25)


class Task(Goal):
    goal = models.ForeignKey(to= Goal, related_name='tasks', on_delete = models.CASCADE)



