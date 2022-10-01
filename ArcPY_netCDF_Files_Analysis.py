import arcpy
import os
import sys
from arcpy import env

# Inputs

Xlist = [58.15, 58.95, 59.65]
Ylist = [23.55, 23.15, 22.35]
npts=len(Xlist)
Infolder=r"D:\educational\Masters_spring2022\CEI613_GIS2\ASIGN2DATA\PROB3DATA\a"
Outfolder=r"D:\educational\Masters_spring2022\CEI613_GIS2\Assignment2"
Workfolder=r"D:\educational\Masters_spring2022\CEI613_GIS2\Assignment2"

# Settings

env.overwriteOutput = True
env.Workspace = Workfolder
env.scratchWorkspace = Workfolder+"/TEMP"

# Nc files list

nc_flst = os.listdir(Infolder+"/GPM")
print("number of files is: "+ str(len(nc_flst)))

#Extract Data
c=1
for i in range(npts):
    outfname = Outfolder+"/point"+str(i+1)
    outf = open(outfname,"w")
    outf.write("time step 0.5hr,Date,Hour,Miniute,Intenisty mm/hr \n")
    X=Xlist[i]
    Y=Ylist[i]
    t=0
    for name in nc_flst:
        #getting raster for each file "timestep"
        arcpy.MakeNetCDFRasterLayer_md(Infolder+"/GPM/"+name,"precipitationCal","lon","lat","Iraster.tif")
        #getting values at X,Y from each raster
        value = arcpy.GetCellValue_management("Iraster.tif",str(X)+" "+str(Y))
        #extracting date and time from files name
        date= name.split(".")[4][:8]
        hour= name.split(".")[4].split("-")[2][1:3]
        minute= name.split(".")[4].split("-")[2][3:5]
        #writing output
        outf.write(str(t)+","+str(date)+","+str(hour)+","+str(minute)+","+str(value)+"\n")
        t+=1
        #setting progressor 
        c+=1
        percentage= 100*c/(npts*len(nc_flst))
        print ("\r Processing the Hyetographs at points...."+str(percentage)+"% completed"),
        sys.stdout.flush()
        
    outf.close()