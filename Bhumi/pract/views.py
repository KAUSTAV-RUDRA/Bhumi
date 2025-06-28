from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CustomUser  # Assuming you have a role field in CustomUser
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import CustomUser, Bill
from django.db.models import Sum
import json
@login_required
def manager_dashboard(request):
    if request.user.role != 'manager':
        return redirect('signin')

    if request.method == 'POST' and 'name' in request.POST:
        CustomUser.objects.create_user(
            username=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password'],
            role='teacher',
            area=request.POST['area']
        )

    teachers = CustomUser.objects.filter(role='teacher')
    bills = Bill.objects.all()

    summary = bills.values('type').annotate(total=Sum('amount'))
    chart_labels = [entry['type'] for entry in summary]
    chart_data = [float(entry['total']) for entry in summary]

    return render(request, 'manager_dashboard.html', {
        'teachers': teachers,
        'bills': bills,
        'chart_labels': json.dumps(chart_labels),
        'chart_data': json.dumps(chart_data),
    })

@login_required
def toggle_permission(request, id):
    teacher = get_object_or_404(CustomUser, id=id)
    teacher.can_upload_bills = not teacher.can_upload_bills
    teacher.save()
    return redirect('manager_dashboard')
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.role == 'manager':
                return redirect('manager_dashboard')
            else:
                messages.error(request, "Only managers can access this panel.")
        else:
            messages.error(request, 'Invalid credentials.')

    return render(request, 'signin.html')
