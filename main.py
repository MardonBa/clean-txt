
class Parser():
  def __init__(self, file_name):
    self.file_name = file_name
    self.lines = []
  
  def get_lines(self):
    with open(f"{self.file_name}.txt", "r") as file:
      self.lines = file.readlines()
      print(self.lines)
      for (i, line) in enumerate(self.lines):
        self.lines[i] = line.strip()
    return self.lines
  
  def write_to_file(self):
    with open(f"{file_name}.txt", "w") as file:
      file.truncate(0)
      for line in self.lines:
        if line == '':
          continue
        file.write(line + "\n")


if __name__ == "__main__":
  file_name = input("Please enter the name of the file you want to clean (path only, no extension): ")
  parser = Parser(file_name)
  print(parser.get_lines())
  print(parser.write_to_file())