import inflect

def main():
     p = inflect.engine()
     names = []

     while True:
          try:
               name = input("Name: " )
          except EOFError:
               break 
          names.append(name)
     joined = p.join(names)
     print(f"Adieu, adieu, to {joined}")

if __name__ == "__main__":
     main() 