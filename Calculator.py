def add(numbers):
  return sum(numbers)


def subtract(numbers):
  result = numbers[0]
  for num in numbers[1:]:
    result -= num
  return result


def multiply(numbers):
  result = 1
  for num in numbers:
    result *= num
  return result


def divide(numbers):
  result = numbers[0]
  for num in numbers[1:]:
    if num != 0:
      result /= num
    else:
      return "Error: Division by zero"
  return result


def calculator():
  print("Welcome to the calculator!")
  print("Available operations:")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")

  operation = input("Enter operation (1/2/3/4): ")
  numbers = input("Enter numbers separated by space: ").split()
  numbers = [float(num) for num in numbers]

  if operation == '1':
    print("Result:", add(numbers))
  elif operation == '2':
    print("Result:", subtract(numbers))
  elif operation == '3':
    print("Result:", multiply(numbers))
  elif operation == '4':
    print("Result:", divide(numbers))
  else:
    print("Invalid operation")


if __name__ == "__main__":
  calculator()
