from django.shortcuts import render

def vista_realidad_virtual(request):
    return render(request, 'VirtualW/vr_template.html')
