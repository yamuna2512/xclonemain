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
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST




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
      # return HttpResponseRedirect('second/first/')
      return redirect('post1')
    else:
      print(form.errors)

  else:
    # Show editting screen
    form = XForm
  return render(request, 'x/x_edit.html', 
    {'x': x, 'form': form})


def xAdd(request):
    if request.method == 'POST':
        form = XForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return redirect('post1')  # Use name from urls.py

def xDelete(request, x_id):
    x_to_delete = get_object_or_404(X, id=x_id)
    x_to_delete.delete()
    
    return redirect('post1') 



@require_POST
def xLikeAdd(request, x_id):
    x = get_object_or_404(X, id=x_id)
    x.like_count += 1
    x.save()
    return JsonResponse({'like_count': x.like_count})


@require_POST
def xLikeSubtract(request, x_id):
    x = get_object_or_404(X, id=x_id)
    if x.like_count > 0:
        x.like_count -= 1
        x.save()
    return JsonResponse({'like_count': x.like_count})