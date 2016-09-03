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


class AttachmentPages_record(models.Model):
    ID = models.Field.primary_key=True
    Subject = models.CharField(max_length=200,null=True)
    Services = models.CharField(max_length=200,null=True)
    ProgramServiceSubject= models.CharField(max_length=200,null=True)
    Section = models.CharField(max_length=200,null=True)
    SectionItem = models.CharField(max_length=200,null=True)
    Contents = models.CharField(max_length=200,null=True)
    StatePlanSection = models.CharField(max_length=200,null=True)
    PlanPage= models.CharField(max_length=200,null=True)
    pdfPageNumber= models.CharField(max_length=200,null=True)
    EffectiveDate= models.CharField(max_length=200,null=True)
    TransmittalNumber= models.CharField(max_length=200,null=True)
    Superseded1= models.CharField(max_length=200,null=True)
    Superseded2= models.CharField(max_length=200,null=True)
    Superseded3= models.CharField(max_length=200,null=True)
    Superseded4= models.CharField(max_length=200,null=True)
    Superseded5= models.CharField(max_length=200,null=True)
    Superseded6= models.CharField(max_length=200,null=True)
    Superseded7= models.CharField(max_length=200, null=True)
    Superseded8= models.CharField(max_length=200,null=True)
    Superseded9= models.CharField(max_length=200,null=True)
    Superseded10= models.CharField(max_length=200,null=True)
    Superseded11= models.CharField(max_length=200,null=True)
    Superseded12= models.CharField(max_length=200,null=True)
    Superseded13= models.CharField(max_length=200,null=True)
    Superseded14= models.CharField(max_length=200, null=True)
    Superseded15= models.CharField(max_length=200,null=True)
    Superseded16= models.CharField(max_length=200,null=True)
    Superseded17= models.CharField(max_length=200,null=True)
    Superseded18= models.CharField(max_length=200,null=True)
    Superseded19= models.CharField(max_length=200,null=True)
    Superseded20= models.CharField(max_length=200,null=True)
    Superseded21= models.CharField(max_length=200, null=True)
    Superseded22= models.CharField(max_length=200,null=True)
    Superseded23= models.CharField(max_length=200,null=True)
    Superseded24= models.CharField(max_length=200,null=True)
    Superseded25= models.CharField(max_length=200,null=True)



def publish(self):
    #self.published_date = timezone.now()
    self.save()
                                            
def __str__(self):
    return self.Subject




