from django.db import models

class SensorData(models.Model):
    temp = models.FloatField()
    humidity = models.FloatField()
    status = models.CharField(max_length=10)
    chemical = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.status} - {self.time}"

class ThresholdSetting(models.Model):
    temp_limit = models.FloatField(default=35.0)
    hum_limit = models.FloatField(default=70.0)

    def __str__(self):
        return f"Temp Limit: {self.temp_limit}, Humidity Limit: {self.hum_limit}"