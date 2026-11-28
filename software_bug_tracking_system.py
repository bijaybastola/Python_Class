# software bug tracking system!

project_name = input("Enter the project Name : ")
bug_id = int(input("Enter the bug id : "))
bug_description = input("Enter the bug description : ")

#ask the user for  bug severity score (1–5)
bss = float(input("Enter the bug severity score (1-5) : "))
if bss <= 0 and bss >= 0 : 
    print("The bug severity score should be in the range of (1 - 5) ")

estimated_hours_to_fix = int(input("Enter the estimated hours to fix the bugg : "))
developer_hourly_rate = float(input("Enter the developers hourly rate : "))

#ask the user if the bug is reproducible or not.
reproducible = bool(input("Is the bug  reproducible (yes or no) : "))

# calculating the estimated  fixing cost
estimated_fixing_cost = estimated_hours_to_fix * developer_hourly_rate

# calculationg testing time
testing_time = 0.25 * estimated_hours_to_fix

# calculating the total estimated development time and cost + testing
estimated_development_time = estimated_fixing_cost + testing_time

# checking wheather the bug critical, fixing time, total estmated cost > than 8 ans if it requires urgent attention
if bss >= 4 and estimated_hours_to_fix > 8 and estimated_fixing_cost > 1000:
    print("The bug requires urgent attention  (critical and reproducible).") 

#printing the output 
print(f"Project name:: {project_name}")
print(f"Project bug_id:: {bug_id}")
print(f"Project bug_description:: {bug_description}")
print(f"bug_severity_score::  {bss}")
print(f"estimated_hours_to_fix::  {estimated_hours_to_fix}")
print(f"developer_hourly_rate::  {developer_hourly_rate}")
print(f"estimated_fixing_cost::  {estimated_fixing_cost}")
print(f"total_estimated_development_t&c_with_testing::  {estimated_development_time}")