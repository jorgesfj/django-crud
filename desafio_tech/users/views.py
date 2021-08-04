from django.shortcuts import redirect, render
from .models import User
from .forms import UserForm

def list_users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def create_user(request):
    form = UserForm(request.POST or None)
    err = 0
    if form.is_valid():
        if cpf_validate(form.cleaned_data['cpf']+""):
            form.save()
            return redirect('list_users')
        else:
            err = 1
    
    return render(request, 'users-form.html', {'form': form, 'error':err})

def update_user(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST or None, instance=user)
    err =  0

    if form.is_valid():
        if cpf_validate(form.cleaned_data['cpf']+""):
            form.save()
            return redirect('list_users')
        else:
            err = 1

    return render(request, 'users-form.html', {'form': form, 'person': user, 'error': err})

def delete_user(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        user.delete()
        return redirect('list_users')

    return render(request, 'user-delete-confirm.html', {'user': user})

def about(request):
    return render(request, 'about.html')

def cpf_validate(numbers):
    cpf = [int(char) for char in numbers if char.isdigit()]
    if len(cpf) != 11:
        return False
    if cpf == cpf[::-1]:
        return False
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True
