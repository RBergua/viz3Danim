
## SubDyn modes visualization (legacy)

The latest version of SubDyn (part of [OpenFAST](https://github.com/openfast/openfast)) can generate the '.json' file with Craig-Bampton, Guyan and FEM mode shapes by setting the options `OutCBModes` and `OutFEMModes`, in the SubDyn input file (see [here](https://openfast.readthedocs.io/en/dev/source/user/subdyn/input_files.html#output-summary-and-outfile)). After running SubDyn, simply drag and drop the generated `.json` files into the browser. There is no need to follow the step below which are for older version of SubDyn.

### Generating a json file from a SubDyn summary file:
There are two steps for now:
1.	Convert the yaml file to a "json" file, using a standalone python script called `subDynModeViz` located in the `legacy` folder`
2.	Load the json file into the web-gui, which requires a web-server (more on that later). 
We can make that 1 step in the future if needed.

For convenience the python script can launch step 2 automatically. 

The python script and web-app are located in this repository (i.e. [here](https://github.com/ebranlard/viz3Danim))


### Step 1 (and 2): 
-	To generate a json file:

      python legacy/subDynModeViz  File.sum.yaml  

-	To generate a json file, launch a web server and open the json file directly:

      python legacy/subDynModeViz  --open File.sum.yaml  

### Step 2 :
-	Option 1: use the [internet demo version](https://ebranlard.github.io/viz3Danim/) and open the json file there
-	Option 2: use the python script with `--open` flag to launch a local server 
-	Option 3: create your own local server and open the json file manually: 
```bash
      python legacy/subdynModeViz --open  # launch a web server on port 1337
      # then open a browser and navigate to https://localhost:1337/
```

