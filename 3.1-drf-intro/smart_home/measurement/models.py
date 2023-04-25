from django.db import models

# review:  опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.id) +' - '+ self.name
class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', blank=False)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='imgs',height_field=None, width_field=None, max_length=100, null=True, blank=True)

