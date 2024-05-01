from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=4, db_index=True)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    
    # class Meta:
    #     indexes = [models.Index(fields=['fullname', 'emp_code', 'mobile','email', 'position'])]