from django.db import models

class Lugar(models.Model):
    Id_Lugar = models.AutoField(primary_key=True)
    LugarEvento = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Tbl_Lugar'