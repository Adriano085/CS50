def playback(msg):
  return msg.replace(" ", "...")

def main():
  msg = input("> ")
  print(playback(msg))


if __name__ == "__main__":
    main()