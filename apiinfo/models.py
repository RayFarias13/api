from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .crypto import encrypt_value, decrypt_value


'''
class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Usuário'
        db_table = 'Usuario1'

    def __str__(self):
        return self.user.username
'''
class User2model(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def set_password(self, raw_password):
        self.password = encrypt_value(raw_password)

    def check_password(self, raw_password):
        decrypted_password = decrypt_value(self.password)
        return decrypted_password == raw_password
    
    def get_password(self):
        return decrypt_value(self.password)

class User3model(AbstractUser):
    role = models.CharField(max_length=100, null=True, blank=True)





class AlunoModel(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=30)
    classe = models.CharField(max_length=10)
    birth_date = models.DateField()
    registration_number = models.CharField(max_length=20)
    guardian_contact = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    #created_by = models.ForeignKey(UserModel,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Aluno'
        db_table = 'Usuario_Aluno'

    def __str__(self):
        return self.name


class AdaptationsModel(models.Model):
    student = models.ForeignKey(AlunoModel,on_delete=models.CASCADE)
    description = models.TextField()
    justification = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    #created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Adaptação'
        db_table = 'Adaptacao_aluno'
    def __str__(self):
        return self.student.name


class ReportsModel(models.Model):
    student = models.ForeignKey(AlunoModel,on_delete=models.CASCADE)
    #teacher = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    date = models.DateField()
    result = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Relatório'
        db_table = 'Relatorio_aluno'

    def __str__(self):
        return self.student.name