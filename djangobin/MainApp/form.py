from django import forms


BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (
    ('public', 'public'),
    ('private', 'private'),
)

class NewPaste(forms.Form):
    title = forms.CharField(label='Title',max_length=1000)
    content = forms.CharField(label='Content', widget=forms.Textarea)
    forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    visibility = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=FAVORITE_COLORS_CHOICES,
    )