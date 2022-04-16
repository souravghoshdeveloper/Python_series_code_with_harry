# Lambda Functions or Anonymos Functions

# two no add function
def add(a, b):
    return a + b


#####################################
minus = lambda x, y: x - y      # this is lambda function

# We comment this two line because we uncomment this line --> minus = lambda x, y: x - y
# minus = lambda x, y: x - y  --> This line and next two line (function) are same

# def minus(x, y):
#     return x - y

print(minus(9, 4))

# Note :

# minus = lambda x, y: x - y    and  def minus(x, y):          both are same
#                                       return x - y





###############################################################################
def a_first(a):
    return a[1]
a = [[1, 14], [5, 6], [8, 23]]
a.sort(key=a_first)
print(a)    # Output [[5, 6], [1, 14], [8, 23]]


# if we want to do this by using lambda function then
a = [[1, 14], [5, 6], [8, 23]]
a.sort(key=lambda x:x[1])
print(a)    # Output [[5, 6], [1, 14], [8, 23]]