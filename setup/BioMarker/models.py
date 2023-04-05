from django.db import models

# Categories = []
# Hormones = []
# Glycemic = []
# Diabetes_and_Metabolism = []
# Minerals_and_Vitamins = []

class Allergies(models.Model):
    pass

class Family_History(models.Model):
    pass

class Diagnoses(models.Model):
    pass

class Medication_and_Supplements(models.Model):
    pass

class Symptoms(models.Model):
    pass

class Lab_Test(models.Model):
    pass

class DNA_Test(models.Model):
    pass

class Medical_Visits(models.Model):
    pass

class Immunisations(models.Model):
    pass

class Surgeries(models.Model):
    pass

class Injuries_and_Hospitalisations(models.Model):
    pass

class Physicians(models.Model):
    pass

class Categories(models.Model):
    # Allgrgies = models.ForeignKey(Allergies, on_delete=models.CASCADE)
    # Family_History = models.ForeignKey(Family_History, on_delete=models.CASCADE)

    @property
    def Allergies(self):
        return Allergies.objects.all().count()

    @property
    def Family_History(self):
        return Family_History.objects.all().count()

    @property
    def Diagnoses(self):
        return Diagnoses.objects.all().count()

    @property
    def Medication_and_Supplements(self):
        return Medication_and_Supplements.objects.all().count()

    @property
    def Symptoms(self):
        return Symptoms.objects.all().count()

    @property
    def Lab_Test(self):
        return Lab_Test.objects.all().count()

    @property
    def DNA_Test(self):
        return DNA_Test.objects.all().count()

    @property
    def Medical_Visits(self):
        return Medical_Visits.objects.all().count()

    @property
    def Immunisations(self):
        return Immunisations.objects.all().count()

    @property
    def Surgeries(self):
        return Surgeries.objects.all().count()

    @property
    def Injuries_and_Hospitalisations(self):
        return Injuries_and_Hospitalisations.objects.all().count()

    @property
    def Physicians(self):
        return Physicians.objects.all().count()


class Health_Test_Result(models.Model):
    category = models.CharField(max_length=225)
    date_of_test = models.DateField()
    time_of_test = models.TimeField()
    date_of_cycle = models.DateField()
    provider = models.CharField(max_length=225)
    health_record_file = models.FileField()



class Hormone_Test_Result(models.Model):
    pass


class Biomarker_Result(models.Model):
    pass