#-------------------------------------------------------------
# ArgosSelectionTool.py
#
# Description: Reads in an Argos tracking data file and allows
#   the user to identify the tracked sitings found within a 
#   specified bounding box.
#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2026
#--------------------------------------------------------------

# Create the geographic selection box
the_box = {
    'x_min' : 34.00,
    'y_min' : -76.00,
    'x_max' : 34.50,
    'y_max' : -75.00
}