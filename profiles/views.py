from django.shortcuts import render

def profiles_list(request):
	return render(request, 'profiles/profiles_list.html', {})

def individual_profile(request, id):
	user = request.user
	if user.is_authenticated and user == Caregiver.objects.get(id=id):
		return render(request, 'caretaker/about.html', {})
		
	else:
		return render()


# def profile(request, id):
#     user = request.user
#     #which form should I use here-and should I change forms.py in caretaker? make a form in behavior?
#     #do i need to use a csrf token somewhere in here?
#     if request.method == 'POST':
#         #if user.is_authenticated:
#         return render(request, 'caretaker/about.html', {})
#         #else: reject 403
#     else:
#         #how to check if user is logged in to view this particular profile?
#         if user.is_authenticated: #does this really check if the current user is logged in?
#             return render(request, 'caretaker/about.html', {})


