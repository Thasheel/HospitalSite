from django.db import models


# Create your models here.
class Departmets(models.Model):
    dep_name = models.CharField(max_length=220)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name


class Doctors(models.Model):
    do_name = models.CharField(max_length=50)
    do_spe = models.CharField(max_length=250)
    do_dep = models.ForeignKey(Departmets, on_delete=models.CASCADE)
    do_img = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr' +   self.do_name+ '(' +self.do_spe + ')'


class Booking(models.Model):
    p_name = models.CharField(max_length=50)
    p_phone = models.CharField(max_length=50)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

