from django.db import models
from django.contrib.auth.models import User


class Pet(model.Models):
    """ Model for Pets. """

    Types = [
        ('animal', 'Animal'),
        ('amphibian', 'Amphibian'),
        ('bird', 'Bird'),
        ('dog', 'Dog'),
        ('fish', 'Fish'),
        ('cat', 'Cat'),
        ('livestock', 'Livestock'),
        ('rabbit', 'rabbit'),
        ('reptile', 'Reptile'),
        ('rodent', 'Rodent')
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='pet', null=True)
    family = models.ForeignKey(
        Family, on_delete=models.CASCADE, related_name='pet', null=True)

    name = models.CharField(max_length=48)
    photo = models.ImageField(upload_to='images/pets')
    bio = models.CharField(max_length=255)

    animal_type = models.CharField(
        choices=TYPES, default='Animal', max_length=48)
    age = models.IntegerField()
    feeding_routine = models.CharField(max_length=500)
    daily_routine = models.CharField(max_length=500)
    medical_routine = models.CharField(max_length=500)
    other_notes = models.CharField(max_length=500)

    def __repr__(self):
        return f'<{self.name}, {self.animal_type}>'

    def __str__(self):
        return f'<{self.name}, {self.animal_type}>'


class Family(model.Models):
    """ Model for Families. """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='family', null=True)
    household = models.CharField(max_length=48)
    address = models.CharField(max_length=255)

    contact1 = models.CharField(max_length=48)
    contact1_phone = models.CharField(max_length=15)
    contact1_email = models.CharField(max_length=48)

    contact2 = models.CharField(max_length=48)
    contact2_phone = models.CharField(max_length=15)
    contact2_email = models.CharField(max_length=48)

    emergency1_contact = models.CharField(max_length=48)
    emergency1_phone = models.CharField(max_length=15)

    emergency2_contact = models.CharField(max_length=48)
    emergency2_phone = models.CharField(max_length=15)

    vet = models.CharField(max_length=48)
    vet_phone = models.CharField(max_length=15)
    vet_address = models.CharField(max_length=255)

    notes = models.CharField(max_length=500)

    def __repr__(self):
        return f'<Family: {self.family_name}>'

    def __str__(self):
        return f'<Family: {self.family_name}>'
