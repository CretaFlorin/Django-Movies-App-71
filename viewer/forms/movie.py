from django.forms import Form, CharField, ModelChoiceField, IntegerField, DateField, Textarea, ModelForm
from viewer.validators import capitalized_validator
from viewer.models import Movie, Genre
from django.core.exceptions import ValidationError


# class MovieForm(Form):
#     title = CharField(max_length=64)
#     genre = ModelChoiceField(queryset=Genre.objects)
#     rating = IntegerField(min_value=1, max_value=10)
#     released = DateField()
#     description = CharField(widget=Textarea, required=False)


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        
    title = CharField(max_length=128, validators=[capitalized_validator])
    rating = IntegerField(min_value=1, max_value=10)
    
    # def clean_description(self):
    #     # Force each sentence of the description to be capitalized.
    #     initial = self.cleaned_data['description']
    #     sentences = re.sub(r's*.s*', '.', initial).split('.')
    #     return '. '.join(sentence.capitalize() for sentence in sentences)

    # def clean(self):
    #     result = super().clean()

    #     Daca avem nevoie de mai multe coloane ale modelului folosim functia clean
    #     # if result['genre'].name == 'Comedy' and result['rating'] > 5:
    #     #     self.add_error('genre', '')
    #     #     self.add_error('rating', '')
    #     #     raise ValidationError(
    #     #         "Commedies aren't so good to be rated over 5."
    #     #     )
    #     return result

    

