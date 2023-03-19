from utils import menu

def main():
  try:
    menu()
  except Exception as e:
    print(str(e))
  
if "__main__" == __name__:
  main()
