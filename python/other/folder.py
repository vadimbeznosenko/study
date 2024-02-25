from pathlib import Path

print(Path.cwd())
mkdir_ = Path('.').absolute() / "mydir"


if not mkdir_.exists():
    print(mkdir_.mkdir())

with open(mkdir_/"firs.txt", "w") as first_file:
    first_file.write("First line in first file \n")
    
with open(mkdir_/"second.txt", "w") as second_file:
    second_file.write("First line in first file \n")
    
with open(mkdir_/"firs.txt", "a") as first_file:
    first_file.write("Second line in first file")    

with open(mkdir_/"second.txt", "a") as second_file:
    second_file.write("Second line in first file")

with open(mkdir_/"firs.txt") as first_file:
    print(first_file.read())


# построчное чтение
with open(mkdir_/"firs.txt") as first_file:
    while True:
        line = first_file.readline()
        if not line:
            break
        print(line)

if Path(mkdir_/"first.txt").exists and Path(mkdir_/"second.txt").exists:
    Path(mkdir_/"firs.txt").unlink()
    Path(mkdir_/"second.txt").unlink()
    
if Path(mkdir_).exists:
    Path(mkdir_).rmdir()