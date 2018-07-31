from django import forms

class ExpenseForm(forms.Form):
    title = forms.CharField()
    amount = forms.DecimalField()
    category = forms.CharField()
