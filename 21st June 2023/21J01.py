my_list = [1,2,3,4,5]

# Can we have way to iterate over the each element and run a function
# map() - built
# def doubleMe(a) ->  a*2
# 2,4, 6, 8, 10

def double_me(a):
   return a*2

#map(func, list or tuple , string) -->MapObjet -->


result = list(map(double_me,my_list))
print(result)

# for i in result:
#     print(i)

