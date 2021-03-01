# apple_num = pear_num * 2
# every group needs 3 pear + 4 apple
# after pears are gone and now apple = 16

"""
x = group
total_fruit = x * ( 3 + 4) + 16

"""


# for group in range(1, 100):
#     apple = 4 * group + 16
#     pear = 3 * group
#     if apple == pear * 2:
#         print("Total group number is ", group)
#         break


# Note:
"""hat of pears.
So we need to give 6-4=2 apples more for each group. We have total 16 apples left.
Then we know the group number will be 16 / 2 = 8.

"""

# import numpy

# 2 * x = x + 1
# for x in numpy.arange(0, 100, 0.1):
#     if x * 2 == x + 0.5:
#         print("result is ", x)
#         break




# 2/20/21
#16_3

# def get_grp(a_num, b_num, a_b_ratio, a_left):
#     a_wh_perfect_num_per_day = b_num * a_b_ratio
#     diff_perfect_num_a = a_wh_perfect_num_per_day - a_num
#     days_total = a_left / diff_perfect_num_a

#     return days_total

# 1. 
# apple = orange * 3
# if everyone has 2 oranges and 4 apples
# oranges are perfectly gone
# and then there are 14 apples left

"""
because apple = 3 * orange apples should be 6 so they both will be perfectly gone at the same time
so 6-4=2 and the 2 is how many apples more needed per group to perfectly split them both 
and 14 / 2 = 7 so there are 7 groups
"""
# apples_left = 14
# oranges_per_grp = 2
# apple_to_orange_ratio = 3
# apples_per_grp = 4
# perfect_apple_num = apple_to_orange_ratio * oranges_per_grp
# diff_perfect_num = perfect_apple_num - apples_per_grp
# grp_num = apples_left / diff_perfect_num
# print(f"The total group number: {grp_num}")

# 2. a warehouse and b warehouse 
# a wh = b wh * 2 
# a wh everyday - 40 tons of food
# b wh everyday - 30 tons of food
# after some days b wh is empty but a wh still has 80 tons of food

# print("Total students: ", get_grp(4, 2, 3, 14))

"""
because a wh = b wh * 2 and b wh moves 30 tons everyday
a wh should move 60 tons everyday but instead they move 40 tons everyday
so it should be 60 - 40 = 20 so if a wh moved 20 tons more everyday b wh and a wh would be empty at the same time
and a wh still has 80 tons of food left so it should be 80 / 20 = 4 days
"""
# print("Total days: ", get_grp(40, 30, 2, 80))
# a_wh_left = 80
# a_wh_ratio_b_wh = 2
# a_wh_num_per_day = 40
# b_wh_num_per_day = 30
# a_wh_perfect_num_per_day = b_wh_num_per_day * a_wh_ratio_b_wh
# diff_perfect_num_a_wh = a_wh_perfect_num_per_day - a_wh_num_per_day
# days_total = a_wh_left / diff_perfect_num_a_wh
# print(f"total number of days is {int(days_total)}")
# a_wh_total_num = days_total * a_wh_num_per_day + a_wh_left
# print(f"A warehouse total tons of food is {int(a_wh_total_num)} tons")
# b_wh_total_num = days_total * b_wh_num_per_day
# print(f"B warehouse total tons of food is {int(b_wh_total_num)} tons")



# 3. 
# everygroup has 7 student to plant trees
# yang tree = shan tree * 2
# if every group gets 6 shan tree and 8 yang tree
# perfectly shan tree is gone
# there are still 20 yang tree left
# how many students are planting trees

# students_per_grp = 7
# yang_tree_per_grp = 8
# shan_tree_per_grp = 6
# yang_to_shan_ratio = 2
# yang_trees_left = 20
# perfect_yang_num = shan_tree_per_grp * yang_to_shan_ratio
# perfect_yang_diff = perfect_yang_num - yang_tree_per_grp
# num_of_grps = yang_trees_left / perfect_yang_diff
# num_of_students = num_of_grps * students_per_grp
# print(f"Total number of students is {int(num_of_students)}")


# for grp in range(1, 100):
#     total_shan = grp * shan_tree_per_grp
#     total_yang = grp * yang_tree_per_grp + yang_trees_left
#     if total_yang / total_shan == 2:
#         print("total group: ", grp)
#         print("Total students: ", grp * 7)
#         break

# print("group: ", get_grp(8, 6, 2, 20))



# 2/27/21
#16_4
# 0.
# abasket A and bbasket B
# if move 8 oranges from A to B and the oranges now in A and B are equal
# if move 13 oranges from B to A, the oranges in basket A is now 2 times that in basket B.
# A basket has how many oranges? B basket has how many oranges?

# Because the oranges in A and B are equal when move 8 oranges from A to B, we know that oranges in A is 16 (8X2) more than that in B.
#  
# because A can move 8 oranges to B and be eqaul A is 16 more than B
# and then B can move 13 oranges to A so that means B will be 26+16=42 less than A
# 42 is now the number of oranges in B currently
# 26+16=42 so 42 is when B gives 13 oranges to A and A is 84 when B gives it the oranges.
# and to find A and B when they started, 84-13 is A and 42+13 is B


# 1.
# A warehouse and B warehouse 
# if move 31 tons from A to B, they are the same amount of goods
# if move 14 tons from B to A, then A=Bx4
# A and B have how many tons of goods?

# A is 62 (31 * 2) tons more than B because A can move 31 tons to B and be equal to B
# and if B moved 14 tons to A, A would be 90 (62 + 14 * 2) tons heavier than B
# so that means 90 = B * (4-1). And to find the oringinal B and A, 30 + 14 = B and (4 * 30)120 - 14 = A

"""
B
(31 * 2 + 14 * 2) / (4 - 1) + 14

A
(31 * 2 + 14 * 2) / (4 - 1) * 4 - 14
"""

# 2.
# stanley and sherwin
# they have the same amount of money
# sh bought 5 books and every book cost him 8.4 dollars
# st bought 3 pens and every pen cost him 1.2 dollars
# now st = sh * 3

# sherwin spent 5 * 8.4 = 42 dollars
# stanley spent 3 * 1.2 = 3.6 dollars
# sherwin spent 38.4 (42 - 3.6) dollars more than stanley
# 38.4 is sherwins after money times two
# 38.4 / 2 = 19.2, 19.2 * 3 is stanleys money after he spent some
# so we need to add 57.6 (19.2 * 3) to the money he spent to find the amount of money that they started with
# 57.6 + 3.6 = 61.2 dollars 

"""
[(5 * 8.4 - 3 * 1.2) / (3 - 1)] * 3 + 3 * 1.2

[(5 * 8.4 - 3 * 1.2) / (3 - 1)] + 5 * 8.4
"""

# 3. 
# if 5 girls dont come and give their places to boys 
# now the number of boys and girls are the same
# if 4 boys dont come and give their places to girls
# now the number of girls is twice of the number of boys


# there will be 10 (2 * 5) more girls than boys 
# 10 + 8 (4 * 2) = 18 so 18 is the boys curent number
# 18 + 4 = boys
# (18 * 2) 36 - 4 = girls

"""
Girls
(2 * 5 + 4 * 2) * 2 - 4

Boys
(2 * 5 + 4 * 2) + 
"""