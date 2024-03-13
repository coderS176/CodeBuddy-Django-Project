import codeforces, codechef, leetcode
from selenium_driver import driversetup


'''
codeforces_username = 'guptajirock176'
# create a selenium driver
driver = driversetup()
problems = codeforces.get_problems_solved(driver, codeforces_username)
print(problems)'''

'''
leetcode_username = 'shivambedar'
# create a selenium driver
driver = driversetup()
problems = leetcode.get_problems_solved(driver, leetcode_username)
print(problems)
'''

codechef_username = 'coder_s_176'
# create a selenium driver
driver = driversetup()
problems = codechef.get_problems_solved(driver, codechef_username)
print(problems)