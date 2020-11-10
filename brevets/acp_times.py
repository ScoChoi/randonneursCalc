"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args: 
      control_dist_km:  number, the control distance in kilometers
      brevet_dist_km: number, the nominal distance of the brevet    
         in kilometers, which must be one of 200, 300, 400, 600,
         or 1000 (the only official ACP brevet distances)
      brevet_start_time:  An ISO 8601 format date-time string indicating
         the official start time of the brevet
   Returns:
      An ISO 8601 format date string indicating the control open time.
      This will be in the same time zone as the brevet start time.
   """
   speedMax = {200: 200/34, 300: 200/34 + 100/32, 400: 200/34 + 200/32, 600: 200/34 + 200/32 + 200/30, 1000: 200/34 + 200/32 + 200/30 + 400/28} # speed table
   startT = arrow.get(brevet_start_time)
   if control_dist_km >= brevet_dist_km:  # when controls >= brevet
      shiftM = round(speedMax[brevet_dist_km] * 60)
      return startT.shift(minutes=+shiftM).isoformat()
   else:
      if control_dist_km <= 200:
         shiftM = round(control_dist_km / 34 * 60)
         return startT.shift(minutes=+shiftM).isoformat()
      elif control_dist_km <= 400:
         shiftM = round((speedMax[200] + (control_dist_km-200)/32) * 60)
         return startT.shift(minutes=+shiftM).isoformat()
      elif control_dist_km <= 600:
         shiftM = round((speedMax[400] + (control_dist_km-400)/30) * 60)
         return startT.shift(minutes=+shiftM).isoformat()
      elif control_dist_km < 1000:
         shiftM = round((speedMax[600] + (control_dist_km-600)/28) * 60)
         return startT.shift(minutes=+shiftM).isoformat()

def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
      control_dist_km:  number, the control distance in kilometers
      brevet_dist_km: number, the nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600, or 1000
         (the only official ACP brevet distances)
      brevet_start_time:  An ISO 8601 format date-time string indicating
         the official start time of the brevet
   Returns:
      An ISO 8601 format date string indicating the control close time.
      This will be in the same time zone as the brevet start time.
   """
   
   frenchSpeedMin= {200: 13.5, 300: 300/15, 400: 27, 600: 600/15, 1000: 600/15 + 400/11.428}   # speed table special cases for 200 and 400
   startT = arrow.get(brevet_start_time)
   if control_dist_km >= brevet_dist_km:  # when controls >= brevet 
      shiftM = round(frenchSpeedMin[brevet_dist_km] * 60)
      return startT.shift(minutes=+shiftM).isoformat()
   elif control_dist_km <=  60:  # special case when control distance is less than 60
      shiftM = round((control_dist_km/20 + 1) * 60)
      return startT.shift(minutes=+shiftM).isoformat()
   else:
      if control_dist_km <= 600:
         shiftM = round(control_dist_km / 15 * 60)
         return startT.shift(minutes=+shiftM).isoformat()
      elif control_dist_km < 1000:
         shiftM = round((frenchSpeedMin[600] + (control_dist_km-600)/11.428) * 60)
         return startT.shift(minutes=+shiftM).isoformat()
