
#STARTING ALLOWANCE
allowance =2000

#SPENT 400 ON BOOKS
allowance-=400

#FOUND 100 UNDER THE BED
print(f"remaining allowance{allowance}")
allowance+=100
print(allowance)

#BOUGHT SNACKS FOR 250
allowance-=250
print(f"allowance:{allowance}")

#GIVE 25% OF THE BALANCE TO SIBLINGS
print("discount:25%")
percent=25/100
percent*=allowance
allowance-=percent
print(f"allowance : {allowance}")

#USE ONE THIRD OF THE REMAINING BAL TO BUY DATA
one_third=1/3
one_third*=allowance
allowance-=one_third
print(f"allowance: {allowance}")

#Tithing ad savings use (floor division)
allowance  = allowance // 2
print(allowance)

allowance%=100

print(allowance)



