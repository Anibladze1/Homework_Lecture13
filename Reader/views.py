from django.shortcuts import render, redirect
from .forms import UserForm


def createUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-info')

    else:
        form = UserForm()

    return render(request, 'Reader/user.html', {'form': form})
