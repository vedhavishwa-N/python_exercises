# Write a function to compute simple interest when principal, 
# number of years and annual rate of interest is given

def compute_simple_interest (principal_amount, number_of_years, annual_rate_of_interest):
    #simple interest= principal amount*(1+rate of interest*years)
    simple_interest = principal_amount * (1+ annual_rate_of_interest * number_of_years)
    return simple_interest

#test case

print ("the simple interest is ", compute_simple_interest (1000, 5, 5))
