# Existing list of 10 employees(strings)
employees = ["Scorpion", "Sub-Zero", "Kabal", "Sonya", "Johnny", "Kitana", "Jax", "Kano", "Raiden", "Mileena"]

# Splitting the list into two sub-lists using slicing
subList1 = employees[:5]
subList2 = employees[5:]

# Adding a new employee to subList2 using the append method
subList2.append("Kriti Brown")

# Removing the second employee's name from subList1 using the del statement
# Why did it have to be Sub-Zero ):
del subList1[1]

# Merging both lists using concatenation
mergedList = subList1 + subList2

# List of salaries
salaryList = [50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000]

# Increasing salaries by 4% using list comprehension.
salaryList = [salary * (1.04) for salary in salaryList]

# Sorting the SalaryList using the sort method.
salaryList.sort(reverse=True)

# Showing top 3 salaries using slicing
top3Salaries = salaryList[:3]

# Output
print("List of Employees:", employees)
print("Merged List of Employees:", mergedList)
print("Salary List:", salaryList)
print("Updated Salary List:", salaryList)
print("Top 3 Salaries:", top3Salaries)