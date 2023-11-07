from django.db import models

class Lugar(models.Model):
    Id_Lugar = models.AutoField(primary_key=True)
    LugarEvento = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Tbl_Lugar'

class Formulario(models.Model):
    Id_Formulario = models.AutoField(primary_key=True)
    NombreCompleto = models.CharField(max_length=100)
    NumeroDocumento = models.CharField(max_length=20)
    Planta = models.CharField(max_length=100)
    Dependencia = models.CharField(max_length=100)
    Correo = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=20)
    Autorizacion = models.CharField(max_length=10)  
    LugarEvento_Id = models.ForeignKey(Lugar, on_delete=models.CASCADE, db_column='LugarEvento_Id')
    FechaCreacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Tbl_Formulario'