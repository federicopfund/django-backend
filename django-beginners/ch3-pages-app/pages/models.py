from django.db import models


class Publicacion(models.Model): # new class Publicacion
    text = models.TextField("Hola mundo") # new var name text and type TextField

    def __str__(self):  # new methods string representation of the object
        return self.text[:50] # max 50 characters
