#
# Complete the 'subscription_summary' function below.
#

def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):
    """
    Parameters:
      months_subscribed: How many months each account purchased.
      ad_free_months: How many months each account paid for ad free viewing.
      video_on_demand_purchases: How many Videos on Demand each account purchased.
    """
    print("Welcome to the Ada+ Account Dashboard\n")
    # print(months_subscribed)
    # print(ad_free_months)
    # print(video_on_demand_purchases)
   
    month_fee=0
    all_account_fees=[]
    monthly_fee_only=[]
    add_free_fees=[]
    vod_fees=[]
    max_earned = 0
    index_of_account_with_max = ""
    for i in range(len(months_subscribed)):
        #calculates base month fees
        if months_subscribed[i] >= 3:
            month_fee = (months_subscribed[i] // 3)*18 + (months_subscribed[i] % 3)*7
        else:
          month_fee=7*months_subscribed[i]
        monthly_fee_only.append(month_fee)
        #calculates additional month fee for add free viewing
        month_fee=month_fee+(ad_free_months[i]*2)
        #calculates additional month fee for video on demand_purchases
        month_fee=month_fee+(video_on_demand_purchases[i]*27.99)
        all_account_fees.append(month_fee)
        add_free_fees.append(ad_free_months[i]*2)
        vod_fees.append(video_on_demand_purchases[i]*27.99)
        #determines max earned of all account's month fees
        if max_earned < month_fee:
            max_earned = month_fee
            index_of_account_with_max_string = f"#{i+1}"
        elif max_earned == month_fee:
            index_of_account_with_max_string +=f", #{i+1}"
    # print (index_of_account_with_max)
    # print (all_account_fees)
    # print (monthly_fee_only)
    # print (add_free_fees)
    # print (vod_fees)
    
    total_earnings=0
    for i in range(len(all_account_fees)):
        total_earnings+=all_account_fees[i]
    # print (total_earnings)
    
    premium_content=0
    for i in range(len(add_free_fees)):
        premium_content+=add_free_fees[i]+vod_fees[i]
    # print (premium_content)
    
    for i in range(len(all_account_fees)):
        print(f"Account {i+1} made ${all_account_fees[i]:.2f} total\n>>> ${monthly_fee_only[i]:.2f} from monthly subscription fees\n>>> ${add_free_fees[i]:.2f} from Ad-free upgrades\n>>> ${vod_fees[i]:.2f} from Video on Demand purchases\n")
        
    print (f"Combined all accounts made ${sum(all_account_fees):.2f} total\nPremium content (Ad-free watching and Video on Demand) made ${sum(add_free_fees)+sum(vod_fees):.2f} total\n\n${max_earned:.2f} was the most earned by any single account\nThe accounts that earned the most were: {index_of_account_with_max_string}")
    
if __name__ == '__main__':    
    months_subscribed = []
    ad_free_months = []
    video_on_demand_purchases = []
    
    header = input().strip()

    while header == "months_subscribed:":
        line = input().strip()
        try:
            months_subscribed.append(int(line))
        except ValueError:
            header = line

    while header == "ad_free_months:":
        line = input().strip()
        try:
            ad_free_months.append(int(line))
        except ValueError:
            header = line

    while header == "video_on_demand_purchases:":
        try:
            line = input().strip()

            video_on_demand_purchases.append(int(line))
        except EOFError:
            header = None
            
    subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases)