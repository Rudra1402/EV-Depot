from django import forms
from .models import ReviewRating


class ReviewRatingForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['rating', 'review']
        widgets = {
            'rating': forms.NumberInput(attrs={'placeholder': 'Rate between 1 and 5', 'min': 1, 'max': 5}),
            'review': forms.Textarea(attrs={'placeholder': 'Write your review here...', 'rows': 4}),
        }
        error_messages = {
            'rating': {
                'required': 'Please provide a rating between 1 and 5.',
                'min_value': 'Rating cannot be less than 1.',
                'max_value': 'Rating cannot be more than 5.',
            },
            'review': {
                'required': 'Please write your review.',
            },
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating is None or rating < 1 or rating > 5:
            raise forms.ValidationError('Rating must be between 1 and 5.')
        return rating
