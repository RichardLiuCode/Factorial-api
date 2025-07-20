def calculate(input):
  print("calculating factorial of " + input)
  input=float(input)
  input=round(input,0)
  input=int(input)
  result = 1
  while input > 1:
    result=result*input
    input=input-1
  return str(result)
  