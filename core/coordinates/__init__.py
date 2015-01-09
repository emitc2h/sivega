#############################################
## ORIGIN & TRANSFORM CONVENTION:
##
## > All Origins are provided in absolute coordinates.
## > All Transforms are provided as Absolute/Given Transform
##
## > Example 1: from plot coordinates to absolute coordinates:
##     - Absolute Origin : (0,0)
##     - Plot Origin : (15,10)
##     - Absolute/Plot Transform: (10,5)
##     - Test Point is (1,1) in plot coordinates
##     - (1,1) x (10,5) + (15,10) = (25,15) in absolute coordinates
##     - Plot Point x Absolute/Plot Transform + Plot Origin
##
## > Example 2: what is the absolute origin in plot coordinates?
##     - Absolute Origin : (0,0)
##     - Plot Origin : (15,10)
##     - Absolute/Plot Transform: (10,5)
##     - ( (0,0) - (15,10) ) / (10,5) = (-1.5, -2)
##     - (Absolute Point - Plot Origin) / Absolute/Plot Transform
##
## > Example 3: going from one given Transform to another:
##     - Absolute Origin : (0,0)
##     - Origin 1 : (15,10)
##     - Absolute/1 Transform : (10,5)
##     - Origin 2 : (45,60)
##     - Absolute/2 Transform : (60,100)
##     - Test Point (in Coordinate System 1) : (1,1)
##     - Step 1: (1,1) x (10,5) + (15,10) = (25,15)
##     - Step 2: ( (25,15) - (45,60) ) / (60,100) = (-0.3333, -4.5)
##     - ( ( Test Point x Absolute/Origin 1 Transform + Origin 1 ) - Origin 2 ) / Absolute/Origin 2)
##
## > Example 4: Using a periodic coordinate system:
##     - 

## Define absolute system of coordinates

from origin    import Origin
from transform import Transform, linear

absolute_origin    = Origin()
absolute_transform = Transform()