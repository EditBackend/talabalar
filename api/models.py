from django.db import models


class Oqituvchi(models.Model):
    ism = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    balans = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    qoshilgan_sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ism






class Talaba(models.Model):
    ism = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='talabalar/', blank=True, null=True)

    miqdor = models.PositiveIntegerField(default=1)
    balans = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    oqituvchilar = models.ManyToManyField(Oqituvchi, blank=True)
    mashgulot_sanalari = models.TextField(blank=True, null=True)

    izoh = models.TextField(blank=True, null=True)
    qoshilgan_sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ism


class Izoh(models.Model):
    talaba = models.ForeignKey(
        Talaba,
        on_delete=models.CASCADE,
        related_name='izohlar'
    )
    matn = models.TextField()
    sana = models.DateTimeField(auto_now_add=True)





class Guruh(models.Model):
    nomi = models.CharField(max_length=100)
    holati = models.BooleanField(default=True)
    talaba_qoshilgan_sana = models.DateField(null=True, blank=True)
    faollashtirilgan = models.BooleanField(default=False)
    narx = models.DecimalField(max_digits=12, decimal_places=2)
    guruh_boyicha = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi

class TalabaGuruh(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.talaba} - {self.guruh}"


class Eslatma(models.Model):
    sarlavha = models.CharField(max_length=200)
    izoh = models.TextField(blank=True, null=True)
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    sana = models.DateTimeField()
    xodim = models.CharField(max_length=100)

    def __str__(self):
        return self.sarlavha






class QongiroqTarixi(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    sana = models.DateTimeField(auto_now_add=True)
    izoh = models.TextField(blank=True, null=True)




class SMS(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    matn = models.TextField()
    sana = models.DateTimeField(auto_now_add=True)



class LidTarixi(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    holat = models.CharField(max_length=100)
    sana = models.DateTimeField(auto_now_add=True)




class Tolov(models.Model):
    TURI = (
        ('naqd', 'Naqd pul'),
        ('plastik', 'Plastik karta'),
        ('bank', 'Bank hisobi'),
        ('payme', 'Payme'),
        ('click', 'Click'),
        ('uzum', 'Uzum'),
        ('humo', 'Humo'),
    )

    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    guruh = models.ForeignKey(Guruh, on_delete=models.SET_NULL, null=True)
    miqdor = models.DecimalField(max_digits=12, decimal_places=2)
    tolov_usuli = models.CharField(max_length=20, choices=TURI)
    sana = models.DateField()
    izoh = models.TextField(blank=True, null=True)



class TolovQaytarish(models.Model):
    tolov = models.ForeignKey(Tolov, on_delete=models.CASCADE)
    miqdor = models.DecimalField(max_digits=12, decimal_places=2)
    sana = models.DateTimeField(auto_now_add=True)







class MiqdorTahrirlash(models.Model):
    ism = models.CharField(max_length=100)
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    miqdor = models.DecimalField(max_digits=12, decimal_places=2)
    sana = models.DateField()
    izoh = models.TextField(blank=True, null=True)
