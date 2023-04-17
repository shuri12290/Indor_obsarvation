from django.db import models

# Create your models here.

class RoomEnvironment(models.Model):
    measure_time = models.DateTimeField()
    temperature = models.FloatField()
    relative_humidity = models.FloatField()
    ambient_light = models.FloatField()
    barometric_pressure = models.FloatField()
    sound_noise = models.FloatField()
    etvoc = models.FloatField()
    eco2 = models.FloatField()
    discomfort_index = models.FloatField()
    heat_stroke = models.FloatField()
    vibration_information = models.FloatField()
    si_value = models.FloatField()
    pga = models.FloatField()
    seismic_intensity = models.FloatField()
    place = models.CharField(max_length=50,null=False,blank=False)
    
    def __str__(self):
        return self.measure_time
    
    class Meta:
        db_table = 'environment'
        ordering = ["-measure_time"]
        verbose_name_plural = "環境データ"
        
        