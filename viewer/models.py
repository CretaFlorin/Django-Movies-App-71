from django.db.models import Model, CharField, IntegerField, IntegerField, TextField, DateTimeField, ForeignKey, DO_NOTHING, DateField

class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return f"Genre(name={self.name})"

class Movie(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    comment = TextField(null=True)
    created = DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Movie(title={self.title})"
    
    