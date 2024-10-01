# eci_to_ecef.py
#
# Usage: python3 eci_to_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km
#
# Parameters:
#  year 
# month 
# day
# hour
# minute
# second
# eci_x_km
# eci_y_km
# eci_z_km
#  ...
# Output:
#  A description of the script output
#
# Written by Alwaleed Alrashidi 
# Other contributors: Brad Denby
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math
import numpy as np

# "constants"

w = 7.292115 * 10**-5 # given in lecture 6

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
year = float('nan') # time in years
month = float('nan') # time in months
day = float('nan') # time in days
hour = float('nan') # time in hours
minute = float('nan') # time in minutes
second = float('nan') # time in seconds
eci_x_km = float('nan') # eci x component 
eci_y_km = float('nan') # eci y component 
eci_z_km = float('nan') # eci z component 

# parse script arguments
if len(sys.argv)==10:
    year = int(sys.argv[1]) # time in years
    month = int(sys.argv[2]) # time in months
    day = int(sys.argv[3]) # time in days
    hour = int(sys.argv[4]) # time in hours
    minute = int(sys.argv[5]) # time in minutes
    second = float(sys.argv[6]) # time in seconds
    eci_x_km = float(sys.argv[7]) # eci x component 
    eci_y_km = float(sys.argv[8]) # eci y component 
    eci_z_km = float(sys.argv[9]) # eci z component 
else:
    print(\
   'Usage: '\
   'python3 eci_to_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km'\
    )
    exit()

# write script below this line
A = math.floor(year / 100)
B = 2 - A + math.floor(A / 4) 
JD = math.floor(365.25 * (year + 4716)) + math.floor(30.6001 * (month + 1)) + day + B - 1524.5
# Add the fractional part of the day
d_frac = (hour + minute / 60 + second / 3600) / 24
JD_Frac=JD+d_frac
T = (JD_Frac - 2451545.0) / 36525.0
GMST_Angle = (67310.54841 + (876600 * 60*60 +8640184.812866)*T + 0.093104 * T**2 - 6.2e-6 * T**3)
GMST_Angle_Rad = math.fmod(GMST_Angle%86400 * w +2*math.pi, 2*math.pi)
#ecef_x_km=eci_x_km*(math.cos(GMST_Angle_Rad))-eci_y_km*(math.sin(GMST_Angle_Rad))
#ecef_y_km=eci_y_km*math.cos(GMST_Angle_Rad)+eci_x_km*math.sin(GMST_Angle_Rad)
#ecef_z_km=eci_z_km
eci_vec=np.array([eci_x_km, eci_y_km, eci_z_km])
rot_matrix= np.array([[math.cos(-GMST_Angle_Rad), -math.sin(-GMST_Angle_Rad), 0], 
                    [math.sin(-GMST_Angle_Rad), math.cos(-GMST_Angle_Rad), 0],
                    [0,0,1]])
r_ecef=np.dot(rot_matrix, eci_vec)
ecef_x_km=r_ecef[0]
ecef_y_km=r_ecef[1]
ecef_z_km=r_ecef[2]
print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)