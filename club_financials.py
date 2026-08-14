from import_data import *
from dataset import ClubFinancials

data = ClubFinancials(import_data('Datasets'), club_name='Manchester City')

#data.plot_revenue('revenue_eur_m', 'operating_profit_eur_m', 'net_transfer_spend_eur_m', 'wages_to_revenue_pct', 'wage_bill_eur_m')
#data.plot_tendancy('wages_to_revenue_pct')

#print(data.correff('net_transfer_spend_eur_m', 'operating_profit_eur_m'))
#print(data.correff('operating_profit_eur_m', 'wages_to_revenue_pct'))
#print(data.correff('operating_profit_eur_m', 'wage_bill_eur_m'))
#print(data.correff('operating_profit_eur_m', 'revenue_eur_m'))

"""
correlation coefficient between operating profit and net transfer spend equal to -0.65.
We can conclude that there is a moderate negative correlation between operating profit and net transfer spend.
This means that as the net transfer spend increases, the operating profit tends to decrease, and vice versa. 
The negative correlation coefficient suggests that these two variables are inversely related, 
and changes in one variable may have an impact on the other. 
However, the correlation is not strong enough to suggest a direct causal relationship between the two variables.
"""

#data.double_ax('revenue_eur_m', 'wages_to_revenue_pct')
print(data.correff('revenue_eur_m', 'wages_to_revenue_pct'))

plt.show()
