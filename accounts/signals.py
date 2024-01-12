# from django.contrib.auth.models import User
# from django.db.models.signals import post_save, pre_delete, post_delete
# from django.dispatch import receiver
# from admin_app.models import UserProfile

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         profile, _ = UserProfile.objects.get_or_create(user=instance)
        # You can add additional logic here if needed

# @receiver(pre_delete, sender=UserProfile)
# def delete_user_with_user_profile(sender, instance, **kwargs):
#     # Disconnect the post_delete signal for User
#     post_delete.disconnect(delete_user_with_user_profile, sender=UserProfile)
#     try:
#         instance.user.delete()
#     except UserProfile.DoesNotExist:
#         pass
#     # Reconnect the post_delete signal for User after the deletion
#     post_delete.connect(delete_user_with_user_profile, sender=UserProfile)
