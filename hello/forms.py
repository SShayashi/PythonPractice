from django import forms

EMPTY_CHOICES = (
    ('', '-'*10),
)

GENDER_CHOICES = (
    ('man', '男'),
    ('woman', '女')
)

FOOD_CHOICES = (
    ('apple', 'りんご'),
    ('beef', '牛肉'),
    ('bread', 'パン'),

)


class HelloForm(forms.Form):
    your_name = forms.CharField(
        label='名前',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )
