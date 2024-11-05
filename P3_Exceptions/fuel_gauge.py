def consume(fuel):
  if "/" not in fuel or fuel.count("/") != 1:
    return False

  numerator, denominator = fuel.split("/")
  try:
    numerator, denominator = int(numerator), int(denominator)
    result = (numerator / denominator) * 100

    if numerator > denominator:
      return False

    if result <= 1:
      return "E"
    elif result >= 99:
      return "F"
    else:
      return f"{round(result)}%"

  except (ValueError,ZeroDivisionError):
    return False


def main():
  while True:
    fuel = input("Fraction: ")
    result = consume(fuel)

    if result:
      print(result)
      break

if __name__ == "__main__":
  main()