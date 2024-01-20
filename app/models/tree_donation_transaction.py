from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models.user import Donors, Farmer 
import random
import os

class TreeDonationTransaction(models.Model):
    donar_id = models.ForeignKey(Donors, on_delete=models.CASCADE)
    donation_name = models.CharField(max_length=255)
    donation_description = models.TextField()
    tree_count = models.IntegerField(default=1)
    donation_amount = models.IntegerField()
    status = models.CharField(max_length=255,default="false")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.donation_name

    def save(self, *args, **kwargs):
        # Set the donation_amount based on the tree_count
        self.donation_amount = self.tree_count * 100
        super().save(*args, **kwargs)

class TreeAcceptTransaction(models.Model):
    tree_trans_id = models.OneToOneField(TreeDonationTransaction,on_delete=models.CASCADE)
    farmer_id = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    status = models.CharField(max_length=255,default="true")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at)


def get_random_name(instance, filename):
    base_filename, file_extension= os.path.splitext(filename)
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    random_str = ''.join((random.choice(chars) for _ in range(10)))
    return '{random_str}{ext}'.format(random_str=random_str, ext=file_extension)

class TreeDonationStatus(models.Model):
    tree_accept_id = models.ForeignKey(TreeAcceptTransaction,on_delete=models.CASCADE) 
    status = models.CharField(max_length=255,default="started")
    comments = models.TextField(default="")
    image_path = models.ImageField(upload_to=get_random_name, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.created_at)

@receiver(post_save, sender=TreeAcceptTransaction)
def create_tree_donation_status(sender, instance, created, **kwargs):
    if created:
        TreeDonationStatus.objects.create(tree_accept_id=instance, status="started", comments="", image_path="")

        # Set the status of the corresponding TreeDonationTransaction instance to "true"
        tree_donation_transaction = instance.tree_trans_id
        tree_donation_transaction.status = "true"
        tree_donation_transaction.save()