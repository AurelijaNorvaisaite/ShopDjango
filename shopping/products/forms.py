from django import forms


class MyForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    city = forms.CharField(label='City', max_length=25)
    CHOICES = [('yes', 'Yes, I am happy!'),
               ('no', 'No, I am not happy.')]
    is_happy = forms.ChoiceField(label='Are you happy?', choices=CHOICES, widget=forms.RadioSelect)

    def clean(self):
        # Data from the form is fetched using super function.
        super(MyForm, self).clean()

        # Extract the username and text field from the data.
        name = self.cleaned_data.get('name')
        city = self.cleaned_data.get('city')

        # Conditions to be met for the name and city length.
        if len(name) > 30:
            self._errors['name'] = self.error_class([
                'Maximum 30 characters.'])
        if len(city) > 25:
            self._errors['city'] = self.error_class([
                'Maximum 25 characters.'])

            # Return any errors if found.
        return self.cleaned_data
