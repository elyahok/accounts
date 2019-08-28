from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from accounts.models import Balance


@receiver(pre_save, sender=Balance)
def update_account_usd_total_value_on_creating_or_updating_balance(sender, instance, **kwargs):
    # used when Balance has been updated
    if instance.id:
        saved_obj = sender.objects.get(id=instance.id)
        if saved_obj.quantity > instance.quantity:
            diff = saved_obj.quantity - instance.quantity
            instance.account_id.usd_total_value += diff * instance.asset_id.usd_value
        else:
            diff = instance.quantity - saved_obj.quantity
            instance.account_id.usd_total_value -= diff * instance.asset_id.usd_value
    # used when balance has been created
    else:
        instance.account_id.usd_total_value -= instance.quantity * instance.asset_id.usd_value
    instance.account_id.save()


@receiver(post_delete, sender=Balance)
def update_account_usd_total_value_on_deleting_balance(sender, instance, **kwargs):
    instance.account_id.usd_total_value += instance.quantity * instance.asset_id.usd_value
    instance.account_id.save()
