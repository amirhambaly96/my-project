from django.db import models


class RIG(models.Model):
	rig_name = models.CharField(max_length=200)
	rig_sname = models.CharField(max_length=50)
	def __str__(self):
		return self.rig_sname


class Lecturer(models.Model):
	rig = models.ForeignKey(RIG, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=200)
	def __str__(self):
		return self.full_name

class Publication(models.Model):
	rig = models.ForeignKey(RIG, on_delete=models.CASCADE)
	lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
	ind_jour = models.TextField(blank=True)
	tot_ind_jour = models.IntegerField()
	nind_jour = models.TextField(blank=True)
	tot_nind_jour = models.IntegerField()
	oth_pub = models.TextField(blank=True)
	tot_oth_pub = models.IntegerField()
	def __str__(self):
		return self.lecturer.full_name
	

class ResearchGrant(models.Model):
	rig = models.ForeignKey(RIG, on_delete=models.CASCADE)
	lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
	name_grant = models.TextField(blank=True)
	no_grant = models.IntegerField()
	rm_grant = models.IntegerField()
	def __str__(self):
		return self.lecturer.full_name

class Performance(models.Model):
	rig = models.ForeignKey(RIG, on_delete=models.CASCADE)
	lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
	performance = models.DecimalField(max_digits=10, decimal_places=4)
	def __str__(self):
		return self.lecturer.full_name





