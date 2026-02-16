def hollow_square(n):
    if n <= 0:
      return ""
    if n == 1:
      return "*"
    
    result = ""

    for i in range(n):
        if i == 0 or i == n - 1:
            result += "*" * n
        else:
         result += "*" + " " * (n-2) + "*"
        result += "\n"
    
    return result

# Plugging in n = 5
print(hollow_square(5))

def number_pattern(n):
   result = ""
   i = 1

   while i <= n:
      j = 1
      while j <= i:
         result += str(j)
         j += 1

      if i != n:
        result += "\n"

      i += 1
    
   return result
   
# Plugging in n = 4
print(number_pattern(4))


def sum_of_natural_numbers(n):
   total = 0
   counter = 1

   while counter <= n:
      total += counter
      counter += 1

   return total

#Plugging in n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
print(sum_of_natural_numbers(5))

def centered_star_pyramid(n):
   result = ""
   i = 1

   while i <= n:
      spaces = n - i
      stars = 2 * i - 1

      result += " " * spaces
      result += "*" * stars

      if i != n:
         result += "\n"

      i += 1
   
   return result

#Plugging in n = 4
print(centered_star_pyramid(4))