from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
        return redirect('articles:list')
    else:
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})
