from django.shortcuts import render,redirect,get_object_or_404
from .models import producto
from .forms import ProductoForm

#crear
def producto_crear(request):
    if request.method =="POST":
        form= ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_lista')
    else:
        form=ProductoForm()
    return render(request,'app/producto_form.html',{'form':form})

#leer
def producto_lista(request):
    productos=producto.objects.all()
    return render(request, 'app/producto_lista.html',{'productos':productos})

#actualizar
def producto_editar(request,id):
    producto=get_object_or_404(producto,id=id)
    if request.method =='POST':
        form=ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_lista')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'app/producto_form.html',{'form':form})
#eliminar
def producto_eliminar(request,id):
    producto=get_object_or_404(producto,id=id)
    if request.method=='POST':
        producto.deleted()
        return redirect('producto_lista')
    return render(request,'app/producto_confirm_delete.html',{'producto':producto})