from django.db import models
from django.db import transaction
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Add the user to the group
class UserManager(BaseUserManager):
    def create_user(self, email,location, phone,name, password=None, password2=None, role=0):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            location=location,
            phone = phone
        )

        user.role = role
        user.set_password(password)
        user.save(using=self._db)
        
        with transaction.atomic():
            Farmergroup, created = Group.objects.get_or_create(name='Farmer')
            Donorsgroup, created = Group.objects.get_or_create(name='Donors')

            if role == 0:  # Donors
                Donors.objects.create(user=user)
                user.groups.add(Donorsgroup)
            elif role == 1:  # Farmer
                Farmer.objects.create(user=user)
                user.groups.add(Farmergroup)
            elif role == 2:  # Admin
                # Do nothing for admin users
                pass

        return user
    def create_superuser(self, email,location, name,phone=0, password=None):
        user = self.create_user(
            email,
            location=location,
            phone = phone,
            password=password,
            name=name,
            role=2  # Assuming 2 is the role for superusers
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user    
class User(AbstractBaseUser, PermissionsMixin):
    Donors = 0
    Farmer = 1
    ADMIN = 2  
    ROLE_CHOICES = (
        (Donors, 'Donors'),
        (Farmer, 'Farmer'),
        (ADMIN, 'Admin'), 
    )    
    role = models.IntegerField(default=Donors, choices=ROLE_CHOICES)


    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200,default ="kathmandu")
    phone = models.IntegerField(default=9841383906)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        if self.is_admin:
            return True
        if self.role == User.Farmer:
            # Define Farmer specific permissions
            return perm in ['some_Farmer_permission']
        return False

    def has_module_perms(self, app_label):
        if self.is_admin:
            return True
        if self.role == User.Farmer:
            # Define which app labels a Farmer has access to
            return app_label in ['app_label_for_Farmers']
        return False

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @is_staff.setter
    def is_staff(self, value):
        "Set the is_staff value"
        # Simplest possible answer: All staff are admins
        self.is_admin = value


class Donors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Donors')
    donation_balance = models.IntegerField(default=0)
    def __str__(self):
        return self.user.name
    
class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Farmer')
    latitude = models.TextField(default="")
    interest = models.TextField(default="")
    wallet_amount = models.IntegerField(default=0)
    def __str__(self):
        return self.user.name