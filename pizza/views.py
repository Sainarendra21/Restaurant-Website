from django.shortcuts import render
from .forms import PizzaForm,MultiplePizzasForm
from django.forms import formset_factory
from .models import Pizza
# Create your views here.
def home(request):
	return render(request,'pizza/home.html')



def order(request):
	multiple_form=MultiplePizzasForm()
	if request.method=='POST':
		filled_form=PizzaForm(request.POST)
		if filled_form.is_valid():
			created_pizza=filled_form.save()
			created_pizza_pk=created_pizza.id
			note='thanks for ordering your %s %s and %s pizza is on its way!'%(filled_form.cleaned_data['size'],
			filled_form.cleaned_data['topping1'],
			filled_form.cleaned_data['topping2'],)
			filled_form=PizzaForm()
		else:
			created_pizza_pk=None
			note='pizza order has failed !try again'

		return render(request,'pizza/order.html',{'created_pizza_pk':created_pizza_pk,'Pizzaform':filled_form,'note':note,'multiple_form':multiple_form})
	else:
		form=PizzaForm()
		return render(request,'pizza/order.html',{'Pizzaform':form,'multiple_form':multiple_form})



def pizzas(request):
	number_of_pizzas=2
	filled_multiple_pizza_form=MultiplePizzasForm(request.GET)
	if filled_multiple_pizza_form.is_valid():
		number_of_pizzas=filled_multiple_pizza_form.cleaned_data['number']
	PizzaFormSet=formset_factory(PizzaForm,extra=number_of_pizzas)
	formset=PizzaFormSet()
	if request.method=="POST":
		filled_formset=PizzaFormSet(request.POST)
		if filled_formset.is_valid():
			for form in filled_formset:
				print(form.cleaned_data['topping1'])
			notes="pizzas have been ordered"
		else:
			notes="order cannot be created please try again"
		return render(request,'pizza/pizzas.html',{'notes':notes,'formset':formset})
	else:
		return render(request,'pizza/pizzas.html',{'formset':formset})

def edit_order(request,pk):
	pizza=Pizza.objects.get(pk=pk)
	form=PizzaForm(instance=pizza)
	if request.method=='POST':
		filled_form=PizzaForm(request.POST,instance=pizza)
		if filled_form.is_valid():
			filled_form.save()
			form=filled_form
			note='Order has been updated'
			return render(request,'pizza/edit_order.html',{'note':note,'Pizzaform':form,'pizza':pizza})

	return render(request,'pizza/edit_order.html',{'Pizzaform':form,'pizza':pizza})