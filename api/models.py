from django.db import models

# Create your models here.





class Goal(models.Model):
    name = models.CharField(max_length=25)
    achieved = models.BooleanField(default=False)
    archieved = models.BooleanField(default=False)



class Task(Goal):
    super_goal = models.ForeignKey(blank = True, null=True,to= Goal, related_name='task_list', on_delete = models.CASCADE)



