from django.db import models


class VisitorsDetails(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1,choices=[('M' ,'males'), ('F', 'females' )])
    age = models.PositiveIntegerField()
    ticket_price =  models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

