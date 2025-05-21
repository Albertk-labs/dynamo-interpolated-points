# Dynamo Z-Coordinate Interpolation

This Python script is designed to work within Dynamo for Autodesk Revit.  
It takes a list of points and calculates new points along the same path with interpolated Z values based on distance along the curve.  
Perfect for modeling slopes, terrain profiles, or elevation-adjusted geometry.

---

##  Features

- Calculates total distance along a polyline made of input points.
- Interpolates Z values smoothly between a start and end elevation.
- Outputs new 3D points that maintain X and Y but adjust Z linearly.

---

##  How It Works

###  Inputs
- `IN[0]`: List of Dynamo points (Point objects)
- `startZ`: Starting elevation
- `endZ`: Ending elevation

###  Output
- `OUT`: List of new Point objects with adjusted Z values

---

##  Technologies Used

- Python for Dynamo
- Autodesk DesignScript Geometry (ProtoGeometry)

---

##  Use Cases

- Terrain modeling
- Creating sloped geometry
- Pipe/cable routes with elevation drop
- Generating topographic features

---

##  File

- `ZInterpolation.py` — script to interpolate Z along input points in Dynamo

---

##  Author

**Albert Kłoczewiak**  
GitHub: [@albertk-labs](https://github.com/albertk-labs)  
Email: akkloczewiak@gmail.com
