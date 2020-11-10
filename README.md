# Randonneurs Calculator (For the Hardcore Cyclists)

Author: Scott Choi, ascottychoi@gmail.com

# ACP Controle Times
From control location 0 - 200km: Minimum Speed is 15km/hr, Maximum Speed is 34km/hr 
From control location 200 - 400km: Minimum Speed is 15km/hr, Maximum Speed is 32km/hr 
From control location 400 - 600km: Minimum Speed is 15km/hr, Maximum Speed is 30km/hr 
From control location 600 - 1000km: Minimum Speed is 11.428km/hr, Maximum Speed is 28km/hr 
When control location is greater than the brevet distance, open and close times are the same as if the control location equalled the brevet distance.

# ACP Controle Times Special Cases
From control location 0 - 60km use the following algorithm: control_location/20km/hr + 1hr = closing time in hours
When brevet distance is 200km, closing time for controls greater than or equal to 200km is 13hrs 30min
When brevet distance is 400km, closing time for controls greater than or equal to 400km is 27hrs

# Notes
Be advised that control distances should be at most 120% of the brevet distance
The only selectable brevet distances are 200, 300, 400, 600, and 1000

# How to Run on Local Machine
Download docker and use the run.sh script inside the brevets directory
Using a browser, go to the address http://127.0.0.1:5000/
