from django import forms
from .models import Identitee, Card


class CreateNewIdentity(forms.ModelForm):

    class Meta:
        model = Identitee
        fields = ['nom', 'prenom', 'email', 'tel', 'ville', 'code_postal', 'adresse']

    def __init__(self, *args, **kwargs):
        super(CreateNewIdentity, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    nom = forms.CharField(label="Nom", max_length=150, required=True, error_messages={
        'required': 'Entrez votre nom!'
    })
    prenom = forms.CharField(label="prenom", max_length=150, error_messages={
        'required': 'Entrez votre prenom!'
    })
    email = forms.EmailField(label="email", error_messages={
        'required': 'Entrez votre adresse email!',
        'invalid': 'Votre Email est invalid!',
        'unique': "cet email est dejà inseré"
    })
    tel = forms.IntegerField(label="telephone", error_messages={
        'required': 'Entrez votre numéro de telephone!'
    })
    ville = forms.CharField(label="ville", max_length=150, error_messages={
        'required': 'Entrez votre ville!'
    })
    code_postal = forms.IntegerField(label="code postal", error_messages={
        'required': 'Entrez votre code postal!'
    })
    adresse = forms.CharField(label="adresse", max_length=150, error_messages={
        'required': 'Entrez votre adresse!'
    })

    def clean_tel(self, *args, **kwargs):
        telephone = self.cleaned_data.get("tel")
        tel = str(telephone)
        if not len(tel) in [8, 9]:
            raise forms.ValidationError("numero de telephone invalide!")
        return telephone
    # def _clean_fields(self, *args, **kwargs):
    #     nom = self.cleaned_data.get("telephone")
    #     prenom = self.cleaned_data.get("telephone")
    #     email = self.cleaned_data.get("telephone")
    #     ville = self.cleaned_data.get("telephone")
    #     adresse = self.cleaned_data.get("telephone")
    #
    #     list = [nom, prenom, email, ville, adresse]
    #
    #     for item in list:
    #         if item == "":
    #             raise forms.ValidationError(f"ce champ doit être rempli!")
    #
    #     code_postal = self.cleaned_data.get("telephone")
    #     telephone = self.cleaned_data.get("telephone")


class CreateNewCard(forms.ModelForm):

    class Meta:
        model = Card
        fields = ['titulaire', 'numero', 'montant', 'cryptogramme', 'expiration', 'identitee_id']

    def __init__(self, *args, **kwargs):
        super(CreateNewCard, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    titulaire = forms.CharField(label="Titulaire", max_length=150, required=True, error_messages={
        'required': 'Entrez le titulaire de votre carte!'
    })
    numero = forms.IntegerField(label="Numero", required=True, error_messages={
        'required': 'Entrez le numero de votre carte!',
        'invalid': 'Le numero est invalide!'
    })
    montant = forms.CharField(label="Montant", max_length=150, required=True, error_messages={
        'required': 'Entrez le montant que vous voulez payer!'
    })
    cryptogramme = forms.CharField(label="Cryptogramme", max_length=150, required=True, error_messages={
        'required': 'Entrez le cryptogramme!'
    })
    # expiration = forms.CharField(label="Date d\'expiration", max_length=150, required=False)

    def clean_numero(self, *args, **kwargs):
        numero = str(self.cleaned_data.get("numero"))
        if len(numero) != 16:
            raise forms.ValidationError('Le numero est invalide (16 chiffres)!')
        elif numero[0] not in ["4", "5"]:
            raise forms.ValidationError('Le numero est invalide (le 1er chiffre soit 4 ou 5)!')
        return numero