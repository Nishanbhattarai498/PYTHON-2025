import os

source = 'test.txt'  # file to be moved
destination = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test.txt')  # move to parent directory

try:
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist")
        
    if os.path.exists(destination):
        print("Destination file already exists. Overwriting...")
    
    os.replace(source, destination)
    print(source + " has been moved to " + destination)

except FileNotFoundError as e:
    print(e)
    print("Error: Source file does not exist.")
