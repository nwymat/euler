# euler
Collection of kinematics functions in Python (with numpy matrix)

The code is based on the Coursera lecture ["Kinematics: Describing the Motions of Spacecraft"](https://www.coursera.org/learn/spacecraft-dynamics-kinematics/) of Professor Hansperter Schaub.

All the functions are using right-handed orientation. The DCM is the direction cosine matrix.

Function | Description
---------|------------
Rx,Ry,Rz|Intrinsic rotation about x,y or z axis
PRV | Calculates the principal rotation vector and angel of a DCM
EP | Takes the Euler Parameters (Quaternions) and calculates the DCM
sheppard | Applies Sheppard's method to calculate the Euler Parameters of a DCM
addEPmatrix | Creates the quaternion rotation matrix: b3 = B2\*b1
addEPmatrix2 | Creates the quaternion rotation matrix: b3 = B1\*b2







