from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''Class to construct a custom user model'''

    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Administrator'
        SALES = "SALES", 'Agent Vanzari'
        WAREHOUSE_MANAGER = "WAREHOUSE MANAGER", 'Gestionar Depozit'
        WAREHOUSE_WORKER = "WAREHOUSE WORKER", 'Manipulator Depozit'

    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

class AgentVanzari(User):
    '''Class to create a model for sales users'''

    base_role = User.Role.SALES

    class Meta:
        proxy = True

class ManagerDepozit(User):
    '''Class to create a model for warehouse manager users'''

    base_role = User.Role.WAREHOUSE_MANAGER

    class Meta:
        proxy = True


class ManipulatorDepozit(User):
    '''Class to create a model for warehouse worker user'''

    base_role = User.Role.WAREHOUSE_WORKER

    class Meta:
        proxy = True





