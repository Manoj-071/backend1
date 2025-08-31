from django.db import models

# Create your models here.
class landing(models.Model):
    # Define your model fields here
    name = models.CharField(max_length=100, primary_key=True)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class tracker(models.Model):
    # Define your model fields here
    user = models.ForeignKey(landing, on_delete=models.CASCADE)
    activity = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    platform = models.CharField(max_length=50, choices=[('LeetCode', 'LeetCode'), ('HackerRank', 'HackerRank'), ('CodeChef', 'CodeChef'), ('GeeksforGeeks', 'GeeksforGeeks'), ('Codeforces', 'Codeforces'), ('Others', 'Others')], default='Others')
    description = models.CharField(blank=True, null=True,max_length=10000)
    status = models.CharField(max_length=50, choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], default='Medium')
    tag = models.ForeignKey('tags', on_delete=models.CASCADE)
    link=models.CharField(max_length=500, blank=True, null=True)

class tags(models.Model):
    # Define your model fields here
    tagid = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=50)

class mquotes(models.Model):
    id = models.IntegerField(primary_key=True)
    quote = models.TextField()
   
