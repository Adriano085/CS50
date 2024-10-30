def faces(msg):
  return msg.replace(":(" , "🙁").replace(":)", "🙂").strip("")

def main():
  msg = input().strip()
  print(faces(msg))

if __name__ == "__main__":
  main()