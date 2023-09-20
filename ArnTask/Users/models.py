from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


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


class AgentVanzariManager(BaseUserManager):
    '''Class to construct a custom queryset manager for sale users'''

    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.SALES)

class AgentVanzari(User):
    '''Class to create a model for sales users'''

    base_role = User.Role.SALES
    objects = AgentVanzariManager()

    class Meta:
        proxy = True


class MangerDepozitManager(BaseUserManager):
    '''Class to construct a custom queryset manager for warehouse manager users'''

    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.WAREHOUSE_MANAGER)


class ManagerDepozit(User):
    '''Class to create a model for warehouse manager users'''

    base_role = User.Role.WAREHOUSE_MANAGER
    objects = MangerDepozitManager()

    class Meta:
        proxy = True


class ManipulatorDepozitManager(BaseUserManager):
    '''Class to construct a custom queryset manager for warehouse worker users'''

    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.WAREHOUSE_WORKER)


class ManipulatorDepozit(User):
    '''Class to create a model for warehouse worker user'''

    base_role = User.Role.WAREHOUSE_WORKER
    objects = ManipulatorDepozitManager()

    class Meta:
        proxy = True





