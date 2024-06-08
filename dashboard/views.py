from django.shortcuts import render

def dashboard(request):
    # Add any context data you want to pass to the template
    context = {
        # Add context data here if needed
    }
    return render(request, 'dashboard.html', context)
