from django.shortcuts import render, redirect
from .models import SensorData, ThresholdSetting

def dashboard(request):
    # Fetch all data, sorted by time (latest first)
    data = SensorData.objects.all().order_by('-time')[:10]
    
    # Get the latest threshold settings (or create default if none exist)
    config = ThresholdSetting.objects.last()
    if not config:
        config = ThresholdSetting.objects.create(temp_limit=35.0, hum_limit=70.0)

    # Handle the Form Submission to update Thresholds
    if request.method == 'POST':
        temp_limit = request.POST.get('temp_limit')
        hum_limit = request.POST.get('hum_limit')
        
        if config:
            config.temp_limit = float(temp_limit)
            config.hum_limit = float(hum_limit)
            config.save()
            
        return redirect('dashboard')  # Refresh the page
        
    return render(request, 'dashboard.html', {
        'data': data, 
        'config': config
    })