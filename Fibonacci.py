def nthFibonacci(nthTerm):
  ### Starting numbers
  number1 = 0
  number2 = 1

  if(nthTerm == number1):
    print("The first term in Fibonacci is: ", number1)
  elif(nthTerm == number2):
    print("The second term in Fibonacci is: ", number2)
  else:
    for counter in range(nthTerm):
      print("Term #", counter, ": ", number1)
      nthNumber = number1 + number2
      number1 = number2
      number2 = nthNumber

if __name__ == "__main__":
  ### Prompt user for input
  while True:
    try:
      nthNumber = int(input("What number n would you like to calculate?"))
      nthFibonacci(nthNumber)
      break
    except:
      print("Invalid input. Please try again.")
