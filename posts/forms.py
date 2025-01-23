from django import forms
from posts.models import Post
from posts.models import Category



class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image','title', 'description']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')

        if (title and description) and title.lower() == description.lower():
            raise forms.ValidationError('Название или описание должны быть разными.')
        return cleaned_data
    


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=False,
        widget = forms.TextInput(attrs={'placeholder':'Search'})
    )
    category = forms.ModelChoiceField(queryset= Category.objects.all(), required=False, widget = forms.Select())
    orderings = (
        ("created_at", "Дата создания"),
        ("-created_at", "Дата создания(По убыванию)"),
        ("updated_at", "Дата обновление"),
        ("-updated_at", "Дата обновление(По убыванию)"),
        ("rate" , "Рейтинг"),
        ("-rate" , "Рейтинг(По убыванию)"),
    )
    ordering = forms.ChoiceField(choices=orderings, required=False, widget=forms.Select())