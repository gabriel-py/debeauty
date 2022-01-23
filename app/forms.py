from django import forms

class NovoPedido(forms.Form):
    data_realizacao_desejada = forms.DateField()
    horario_inicio = forms.TimeField(required=False)
    horario_fim = forms.TimeField(required=False)