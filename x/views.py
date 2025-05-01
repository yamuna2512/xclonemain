from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from .models import X
from pprint import pprint
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from .models import X
from pprint import pprint
from datetime import datetime
from .forms import XForm
import cloudinary

def xListView(request):
  # Get all xs, limit = 20
  xs = X.objects.order_by('created_at').reverse().all()[:20]

  # Show output with xs
  return render(request, 'x/x_List.html',
    {'xs': xs})

def xEditView(request, x_id):
  # Get requested x
  x = X.objects.get(id = x_id)

  # If the method is POST
  if request.method == 'POST':
    form = XForm(request.POST, request.FILES, instance=x)
    if form.is_valid():
      # Save and redirect to home
      form.save()
      return HttpResponseRedirect('/')
    else:
      print(form.errors)

  else:
    # Show editting screen
    form = XForm
    return render(request, 'x_edit.html',
    {'x': x, 'form': form})

def xAdd(request):
  # If the method is POST
  if request.method == 'POST':
    form = XForm(request.POST, request.FILES)
    if form.is_valid():
      # Save and redirect to home
      form.save()
    else:
      print(form.errors)

  return HttpResponseRedirect('/')

def xDelete(request, x_id):
  # Get x
  x_to_delete = X.objects.get(id=x_id)
  
  # Delete
  x_to_delete.delete()

  return HttpResponseRedirect('/')

def xLikeAdd(request, x_id):
  # Get requested x
  x = X.objects.get(id = x_id)

  # Add count
  new_like_count = x.like_count + 1
  x.like_count = new_like_count

  # Save
  x.save()

  return JsonResponse({'result': 'successful'})

def xLikeSubtract(request, x_id):
  # Get requested x
  x =X.objects.get(id = x_id)

  # Subtract count
  new_like_count = x.like_count - 1
  x.like_count = new_like_count

  # Save
  x.save()

  return JsonResponse({'result': 'successful'})