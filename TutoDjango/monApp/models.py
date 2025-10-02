from django.db import models

class Categorie(models.Model):
    idCat = models.AutoField(primary_key=True)
    nomCat = models.CharField(max_length=100)

    def __str__(self):
        return self.nomCat

class Statut(models.Model):
    idStatus = models.AutoField(primary_key=True)
    libelleStatus = models.CharField(max_length=100)

    def __str__(self):
        return self.libelleStatus

class Rayon(models.Model):
    idRayon = models.AutoField(primary_key=True)
    nomRayon = models.CharField(max_length=100)
    produits = models.ManyToManyField('Produit', related_name='rayons')

    def __str__(self):
        return self.nomRayon

class Produit(models.Model):
    refProd = models.AutoField(primary_key=True)
    intituleProd = models.CharField(max_length=200)
    prixUnitaireProd = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="produits", null=True, blank=True)
    dateFabrication = models.DateField(null=True, blank=True)
    statut = models.ForeignKey(Statut, on_delete=models.SET_NULL, null=True, blank=True, related_name='produits')

    def __str__(self):
        return self.intituleProd

class Contenir(models.Model):
    rayons = models.ForeignKey(Rayon, on_delete=models.CASCADE, null=False, blank=False, default=0)
    produits = models.ForeignKey(Produit, on_delete=models.CASCADE, null=False, blank=False, default=0)
    qte = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.rayons} : {self.produits}"

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        #fields = '__all__'
        exclude = ('categorie', 'statut')