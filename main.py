import csv

cpufile = open("CPUReal.csv", "r")
cpu_reader = csv.reader(cpufile)

gpufile = open("GPUReal.csv", "r")
gpu_reader = csv.reader(gpufile)

newfile = open("Results.txt", "w")

while True:
    try:
        min = int(input("What is the minimum score you need? "))
        break
    except:
        print("Invalid score, try again")

cpufilter = input("Enter CPU Keyword to Filter By (Enter to skip)").strip("\n").strip()
gpufilter = input("Enter GPU Keyword to Filter By (Enter to skip)").strip("\n").strip()


for i in cpu_reader:

    if cpufilter and cpufilter.lower() not in i[0].lower():
        continue

    cpuscore = int(i[2])

    for j in gpu_reader:

        if gpufilter and gpufilter.lower() not in j[0].lower():
            continue

        gpu_score = int(j[2])

        totalscore = (1/((.85/gpu_score) + (.15/cpuscore)))

        if totalscore >= min:
            newfile.write(f"{i[0]}, {j[0]}, {totalscore}\n")

    gpufile.seek(0)

cpufile.close()
gpufile.close()
newfile.close()



