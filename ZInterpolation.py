import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import Point

# Input list of points
pts = IN[0]

# Start and end Z levels for interpolation
startZ = 208.70
endZ = 208.375

# Calculate the total length along the chain of points
total_length = 0
for i in range(len(pts) - 1):
    total_length += pts[i].DistanceTo(pts[i + 1])

# Create new points with interpolated Z coordinates
new_pts = []
cumulative = 0
for i in range(len(pts)):
    if i > 0:
        cumulative += pts[i - 1].DistanceTo(pts[i])
    ratio = cumulative / total_length
    new_z = startZ + ratio * (endZ - startZ)
    new_pt = Point.ByCoordinates(pts[i].X, pts[i].Y, new_z)
    new_pts.append(new_pt)

# Output the new points
OUT = new_pts
