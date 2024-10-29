def consume(fraction):
  numerator, denominator = fraction.split("/")
  try:
    numerator, denominator = int(numerator), int(denominator)
    result = (numerator / denominator) * 100

    if result <= 1:
      return "E"
    elif result >= 99:
      return "F"
    else:
      return f"{int(result)}%"
    
  except (ValueError,ZeroDivisionError):
    return False


def main():
  error = False
  while not error:
    fraction = input("Fraction: ")
    result = consume(fraction)

    if result:
      print(result)
      error = True