from .models import *
from rest_framework.response import Response
from profileutility.models import Profile
from decimal import Decimal


def makeLoyalti(p_id, amount, type_of_transaction, redeem_val=None):
    paid_total = amount
    t_type = type_of_transaction

    try:
        old_bal = 0
        turnover = 0
        total_earned = 0
        profile_data = Profile.objects.filter(id=p_id).first()
        loyalti_data = Loyalti.objects.filter(profile_id=p_id).first()
        if loyalti_data:
            old_bal = loyalti_data.balance_points
            total_earned = loyalti_data.total_earned_points
            turnover = loyalti_data.business_turnover + amount

        membership = profile_data.membership
        points_for_plan = LoyaltiEntity.objects.get(category=membership)
        percentage = points_for_plan.points_add_per_100
        calc_value = percentage / 100

        points = amount * calc_value

        if type_of_transaction == 'Add':
            new_bal = old_bal + points
        elif type_of_transaction == 'Redeem':
            if old_bal >= redeem_val:
                new_bal = old_bal - redeem_val
                new_bal = new_bal + points
        
        try:
            if loyalti_data:
                loyalti_data.balance_points = new_bal
                loyalti_data.business_turnover = turnover
                loyalti_data.total_earned_points = total_earned + points
                loyalti_data.save()
            else:
                loyalti_data = Loyalti.objects.create(
                    profile_id=p_id,
                    balance_points=new_bal,
                    total_earned_points=new_bal,
                    business_turnover=paid_total
                )
            
            loy_transaction = LoyaltiTransaction.objects.create(
                profile=profile_data,
                amount=paid_total,
                transaction_type=t_type,
                status="Success",
                loyalti=loyalti_data
            )
            loy_transaction.save()
            
        except Exception as e:
            loy_transaction = LoyaltiTransaction.objects.create(
                profile=profile_data,
                amount=paid_total,
                transaction_type=t_type,
                status="Failed"
            )
            loy_transaction.save()

        check_loyalti_upgrade = LoyaltiEntity.objects.all()
        new_mebership = membership
        for upgrade in check_loyalti_upgrade:
            if loyalti_data.total_earned_points >  upgrade.points_upgrade:
                new_mebership = upgrade.category 

        if new_mebership != membership:
            profile_data.membership = new_mebership
            profile_data.save()


    except Exception as e:
        return Response({'status': 400, 'data': str(e)})
    

# def makeLoyalti(p_id, amount, type_of_transaction):
#     paid_total = amount
#     t_type = type_of_transaction

#     old_bal = 0
#     turnover = 0
#     total_earned = 0
#     profile_data = Profile.objects.filter(id=p_id).first()
#     loyalti_data = Loyalti.objects.filter(profile_id=p_id).first()
    
#     if loyalti_data:
#         old_bal = loyalti_data.balance_points
#         total_earned = loyalti_data.total_earned_points
#         turnover = loyalti_data.business_turnover + amount
#     print(" type is ",total_earned)
#     membership = profile_data.membership
#     points_for_plan = LoyaltiEntity.objects.get(category=membership)
#     percentage = points_for_plan.points_add_per_100
#     calc_value = percentage / 100

#     points = amount * calc_value

#     if type_of_transaction == 'Add':
#         new_bal = old_bal + points
#     elif type_of_transaction == 'Redeem':
#         new_bal = old_bal - points
    
#     if loyalti_data:
#         loyalti_data.balance_points = new_bal
#         loyalti_data.business_turnover = turnover
#         loyalti_data.total_earned_points = total_earned + points
#         loyalti_data.save()
#     else:
#         loyalti_data = Loyalti.objects.create(
#             profile_id=p_id,
#             balance_points=new_bal,
#             total_earned_points=new_bal,
#             business_turnover=paid_total
#         )
    
#     loy_transaction = LoyaltiTransaction.objects.create(
#         profile=profile_data,
#         amount=paid_total,
#         transaction_type=t_type,
#         status="Success",
#         loyalti=loyalti_data
#     )
#     loy_transaction.save()

#     check_loyalti_upgrade = LoyaltiEntity.objects.all()
#     new_membership = membership
#     for upgrade in check_loyalti_upgrade:
#         print(upgrade.points_upgrade)
#         if loyalti_data.total_earned_points > upgrade.points_upgrade:
#             new_membership = upgrade.category 

#     if new_membership != membership:
#         profile_data.membership = new_membership
#         profile_data.save()
