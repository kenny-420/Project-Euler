from os import listdir, system

for file in sorted(listdir(".")):
    if file == "run_all.py":
        continue
    if file[-2:] == 'py':
        system(f"python {file} > /tmp/answer")
        print(file[:-3] + ":", open('/tmp/answer').read(), end="")
