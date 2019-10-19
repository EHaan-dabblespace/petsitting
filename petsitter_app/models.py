from django.db import models
from django.contrib.auth.models import User

# TODO: set default avatars using:
# models.ImageField(upload_to='avatars/', null=True, blank=True, default='/static/img/default-user.png')


class Family(models.Model):
    """ Model for Families. """

    # TODO: Address why user shows up in the html form

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='family', null=True)
    household = models.CharField(max_length=48)
    address = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images/family', blank=True, null=True)

    contact1 = models.CharField(max_length=48)
    contact1_phone = models.CharField(max_length=15)
    contact1_email = models.CharField(max_length=48)

    contact2 = models.CharField(max_length=48, blank=True)
    contact2_phone = models.CharField(max_length=15, blank=True)
    contact2_email = models.CharField(max_length=48, blank=True)

    emergency1_contact = models.CharField(max_length=48, blank=True)
    emergency1_phone = models.CharField(max_length=15, blank=True)

    emergency2_contact = models.CharField(max_length=48, blank=True)
    emergency2_phone = models.CharField(max_length=15, blank=True)

    vet = models.CharField(max_length=48, blank=True)
    vet_phone = models.CharField(max_length=15, blank=True)
    vet_address = models.CharField(max_length=255, blank=True)

    notes = models.CharField(max_length=500, blank=True)

    def __repr__(self):
        return f'<self.household>'

    def __str__(self):
        return f'Family: {self.household}'


class Pet(models.Model):
    """ Model for Pets. """

    TYPES = [
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

    SEX = [
        ('male', 'Male'),
        ('female', 'Female')
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='pet', null=True)
    family = models.ForeignKey(
        Family, on_delete=models.CASCADE, related_name='pet', null=True)

    name = models.CharField(max_length=48)
    photo = models.ImageField(upload_to='images/pets', blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True)

    animal_type = models.CharField(
        choices=TYPES, default='Animal', max_length=48)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(choices=SEX, max_length=48, blank=True)
    feeding_routine = models.CharField(max_length=500, blank=True)
    daily_routine = models.CharField(max_length=500, blank=True)
    medical_routine = models.CharField(max_length=500, blank=True)
    other_notes = models.CharField(max_length=500, blank=True)

    def __repr__(self):
        return f'<{self.name}, {self.animal_type}>'

    def __str__(self):
        return f'{self.name}, {self.animal_type}'
