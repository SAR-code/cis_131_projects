#cis_131_investment_return.py
'''
script: cis_131_investment_return
action: Calculates the rate of return for given principle, return, years
author: Dylan McCallum
date: 29AUG24

'''

# establish variables

principle_amt = 1000
return_rate = .07

# variables for return for 10, 20, 30 years

amt_10 = 0.0
amt_20 = 0.0
amt_30 = 0.0


# calculates returns

# return on 10 years
amt_10 = principle_amt * (1 + return_rate)**10

# return on 20 years
amt_20 = principle_amt * (1 + return_rate)**20

# return on 30 years
amt_30 = principle_amt * (1 + return_rate)**30


# display returns
print(f"${amt_10:.2f} \n${amt_20:.2f} \n${amt_30:.2f}")
