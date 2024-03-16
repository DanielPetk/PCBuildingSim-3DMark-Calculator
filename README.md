# PCBuildingSim-3DMark-Calculator
Program to calculate all of the CPU/GPU combinations that achieve a certain 3DMark score. Note that other hardware in your in-game computer can also _slightly_ boost your score.

First of all, please read ```ATTRIBUTIONS.txt``` to see the data I built this project off of.

**Project Overview**

The ```main.py``` file is the main source code for the program. You can just run it directly if you don't want to run the .exe file (found in releases). The two CSV files, ```GPUReal.csv``` and ```CPUReal.csv``` contain all of the 3DMark data for each GPU and CPU respectively, in (name),(cost),(score) format. These files are necessary for the program to function, and should be in the same directory as ```main.py```.

**How it Works**

The program first prompts you for a few filters to narrow down the results you get. It firsts ask for a minumum 3DMark score threshhold that you want to achieve. Note that other hardware in-game can also _slightly_ boost your 3DMark score, so it may be a good idea to shoot for a slightly lower score using this filter. It then asks for a certain GPU and certain CPU that you want to filter by. These filters are not case-sensitive but **are** whitespace-sensitive. They are also optional, and simply clicking enter and skipping by them will bypass the filter.

The program will then loop through every single CPU and GPU combination and find their combined 3DMark score using the formula ```1/((.85/gpu_score) + (.15/cpuscore))``` found in the original google doc (see ```ATTRIBUTIONS.txt```). Is this the best and most efficient way to do it? Maybe not, but it still takes only a fraction of a second to run, so it doesn't really matter. Why did I do alot of things for that matter? I _could_ have used python's ```with``` statements to make my code more bug free and make sure that the files close correctly, but I truthfully never intended to put this on github, and sometimes you have to live life with a little risk! Submit a pull request and fix it yourself!

After the program finishes, it creates a ```Results.txt``` in the same directory as ```main.py```. Here, it lists every CPU and GPU combination that fits the provided filters, including their combined score.

