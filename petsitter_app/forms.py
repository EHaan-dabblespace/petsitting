from django.forms import ModelForm
from .models import Pet, Family


class PetForm(ModelForm):

    class Meta:
        model = Pet
        fields = [
            'user',
            'family',
            'name',
            'photo',
            'bio',
            'animal_type',
            'age',
            'sex',
            'feeding_routine',
            'daily_routine',
            'medical_routine',
            'other_notes',
        ]


class FamilyForm(ModelForm):

    class Meta:
        model = Family
        fields = [
            'user',
            'household',
            'address',
            'photo',
            'contact1',
            'contact1_phone',
            'contact1_email',
            'contact2',
            'contact2_phone',
            'contact2_email',
            'emergency1_contact',
            'emergency1_phone',
            'emergency2_contact',
            'emergency2_phone',
            'vet',
            'vet_phone',
            'vet_address',
            'notes',
        ]
