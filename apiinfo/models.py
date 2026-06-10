from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User, AbstractUser
from .crypto import encrypt_value, decrypt_value
from django.contrib.auth.hashers import make_password, check_password


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

'''
class User2model(models.Model):
    name = models.CharField(max_length=100, unique=True)
    #name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=100)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


'''

class User2Manager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class User2model(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    #dessativar linha is superusse se der erro
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = User2Manager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email



class AlunoModel(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=30)
    classe = models.CharField(max_length=10)
    birth_date = models.DateField()
    registration_number = models.CharField(max_length=20)
    guardian_contact = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User2model,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Aluno'
        db_table = 'Usuario_Aluno'

    def __str__(self):
        return self.name


class AdaptationsModel(models.Model):
    student = models.ForeignKey(AlunoModel,on_delete=models.CASCADE, related_name='adaptations')
    description = models.TextField()
    justification = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User2model,on_delete=models.CASCADE,related_name='created_adaptations')

    class Meta:
        verbose_name = 'Adaptação'
        db_table = 'Adaptacao_aluno'
    def __str__(self):
        return self.student.name


class ReportsModel(models.Model):
    student = models.ForeignKey(AlunoModel,on_delete=models.CASCADE)
    teacher = models.ForeignKey(User2model,on_delete=models.CASCADE)
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
    