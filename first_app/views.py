from django.shortcuts import render,redirect
from first_app.models import back_mart
from first_app.forms import back_martForm
# Create your views here.
def home(request):
    return render(request,'home.html')

def find_data(request):
    value=back_mart.objects.all()
    
    #print(value)
    return render(request, 'data_table.html',  {'value': value})


def store_data(request):
    if request.method =='POST':
        value= back_martForm(request.POST)
        if value.is_valid():
            value.save()
            #print(value.cleaned_data)
            return redirect('find_data')
    else:
        value=back_martForm()
    return render(request,'create_data.html',{'form': value})

def edit_data(request,id):
    value=back_mart.objects.get(pk=id)
    #print(value)
    form=back_martForm(instance=value)
    if request.method == 'POST':
        form=back_martForm(request.POST, instance=value)
        if form.is_valid():
            form.save()
            return redirect('find_data')
    return render(request,'update_data.html', {'form': form })

def delete_data(request,id):
    value=back_mart.objects.get(pk=id).delete()
    return redirect('find_data')

