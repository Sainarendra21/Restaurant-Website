from django import forms
from .models import Pizza,Size

# class PizzaForm(forms.Form):
# 	toppings=forms.MultipleChoiceField(choices=[('pep','Peprone'),('cheese','Cheese'),('olives','Olives')],widget=forms.CheckboxSelectMultiple)
# 	# topping1=forms.CharField(label="Topping1",max_length=100,widget=forms.PasswordInput)
# 	# topping2=forms.CharField(label="Topping2",max_length=100)
# 	size=forms.ChoiceField(label='Size',choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])


#model forms
class PizzaForm(forms.ModelForm):

	# image=forms.ImageField()
	 # size=forms.ModelChoiceField(queryset=Size.objects,empty_label=None,widget=forms.RadioSelect)

	class Meta:
		model=Pizza
		fields=['topping1','topping2','size']
		labels={'topping1':'Topping 1','topping2':'Topping 2'}



class MultiplePizzasForm(forms.Form):
	number=forms.IntegerField(min_value=2,max_value=6)