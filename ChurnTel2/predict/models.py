from django.db import models

class PredResults(models.Model):
    Monthly_Charges = models.FloatField()
    Tenure_Months = models.IntegerField()
    Senior_Citizen = models.CharField(max_length=130)
    Partner = models.CharField(max_length=130)
    Dependents = models.CharField(max_length=130)
    Internet_Service = models.CharField(max_length=130)
    Online_Security = models.CharField(max_length=130)
    Online_Backup = models.CharField(max_length=130)
    Device_Protection = models.CharField(max_length=130)
    Tech_Support = models.CharField(max_length=130)
    Streaming_TV = models.CharField(max_length=130)
    Streaming_Movies = models.CharField(max_length=130)
    Contract = models.CharField(max_length=130)
    Paperless_Billing = models.CharField(max_length=130)

    Payment_Method = models.CharField(max_length=130)


    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification

