from django import forms
from haystack.forms import SearchForm

class DateRangeSearchForm(SearchForm):
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)

    def search(self):
        sqs = super(DateRangeSearchForm, self).search()

        if self.cleaned_data['start_date']:
        sqs = sqs.filter(pub_date__gte=self.cleaned_data['start_date'])

        if self.cleaned_data['end_date']:
        sqs = sqs.filter(pub_date__lte=self.cleaned_data['end_date'])

        return sqs

