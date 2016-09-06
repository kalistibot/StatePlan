from django.db import models

from django.utils import timezone
class TMACSP_record(models.Model):
    ID = models.Field.primary_key=True
    SPA_BSP = models.CharField(max_length=200,null=True)
    Subject_Population = models.CharField(max_length=200,null=True)
    Program_Category = models.CharField(max_length=200,null=True)
    Services_Requirements = models.CharField(max_length=200,null=True)
    Section = models.CharField(max_length=200,null=True)
    StatePlanSection= models.CharField(max_length=200,null=True)
    PageContents= models.CharField(max_length=200,null=True)
    PlanPage= models.CharField(max_length=200,null=True)
    pdfPage= models.CharField(max_length=200,null=True)
    EffectiveDate= models.CharField(max_length=200,null=True)
    TransmittalNumber= models.CharField(max_length=200,null=True)
    Superseded= models.CharField(max_length=200,null=True)




def publish(self):
    #self.published_date = timezone.now()
    self.save()
                                            
def __str__(self):
    return self.Subject




