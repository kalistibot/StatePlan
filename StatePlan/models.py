from django.db import models

from django.utils import timezone


class Record(models.Model):
    RowID = models.Field.primary_key=True
    Subject = models.CharField(max_length=200,null=True)
    Program= models.CharField(max_length=200,null=True)
    Section= models.CharField(max_length=200,null=True)
    Section_Number= models.CharField(max_length=200,null=True)
    Contents= models.CharField(max_length=200,null=True)
    Attachments= models.CharField(max_length=200,null=True)
    Plan_Page= models.CharField(max_length=200,null=True)
    Page_No= models.CharField(max_length=200,null=True)
    Effective_Date= models.CharField(max_length=200,null=True)
    Transmittal_Number= models.CharField(max_length=200,null=True)
    Superseded1= models.CharField(max_length=200,null=True)
    Superseded2= models.CharField(max_length=200,null=True)
    Superseded3= models.CharField(max_length=200,null=True)
    Superseded4= models.CharField(max_length=200,null=True)
    Superseded5= models.CharField(max_length=200,null=True)
    Superseded6= models.CharField(max_length=200,null=True)
    Superseded7= models.CharField(max_length=200, null=True)

def publish(self):
    #self.published_date = timezone.now()
    self.save()
                                            
def __str__(self):
    return self.Subject




