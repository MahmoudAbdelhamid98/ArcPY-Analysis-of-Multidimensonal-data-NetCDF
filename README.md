# ArcPY-Analysis-of-Multidimensonal-data-NetCDF
Using ArcPY packages to analyze Multidimensional climate data in NetCDF format

## The code was intended to solve the following problem:
Given a serious of GPM rainfall data (previously downloaded from the
Global Precipitation Measurement mission website) in NetCDF single
dimension raster files. The data covers the period 06-07 June 2007
with time interval of 30 minutes. This data set captures the famous
Gonu Hurrican that affected Oman during this period. It is required to
write a standalone program that makes use of the arcpy and sa libraries
to extract the rainfall hyetographs at the following three geographic
locations:
- Xlist = [58.15, 58.95, 59.65]
- Ylist = [23.55, 23.15, 22.35]

## Files naming scheme:
3B-HHR-E.MS.MRG.3IMERG.20070606-S023000-E025959.0150.V06B.HDF5.nc4
