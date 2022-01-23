from django.db import models


class Compozitori(models.Model):
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=100)
    stil = models.CharField(max_length=45)
    tara_origine = models.CharField(max_length=45)
    data_nasterii = models.DateField()
    data_mortii = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.prenume} {self.nume}"


class Compozitii(models.Model):
    titlu = models.CharField(max_length=150)
    an_aparitie = models.SmallIntegerField()
    gen = models.CharField(max_length=45)
    gama = models.CharField(max_length=15, null=True, default=None, blank=True)
    nr_instrumente = models.SmallIntegerField(null=True, default=None,
                                              blank=True)

    def __str__(self):
        return str(self.titlu)


class Cataloage(models.Model):
    simbol = models.CharField(max_length=15)
    compozitor = models.ForeignKey(Compozitori, on_delete=models.CASCADE)
    compozitie = models.ForeignKey(Compozitii, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.simbol)

