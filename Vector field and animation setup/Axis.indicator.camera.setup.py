from vpython import *
#Web VPython 3.2

from vpython import *

#Axis indicator
#Opacity and visibility
op=0.7
visibility=True
indicator1=arrow(pos=vec(0,0,0), axis=vec(100,0,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.red)
indicator2=arrow(pos=vec(0,0,0), axis=vec(0,100,0), shaftwidth=0.1, visible=visibility, opacity=op, color=color.cyan)
indicator3=arrow(pos=vec(0,0,0), axis=vec(0,0,100), shaftwidth=0.1, visible=visibility, opacity=op, color=color.green)

#1: Defaults
#scene.userzoom = True User can zoom in and out of the scene. Default True
#scene.userspin = True User can rotate camera. Default True
#scene.userpan = True User can pan across the scene. Default True
#scene.autoscale = True Camera automatically zooms out to keep all objects in view. Default True

#2: 
#scene.center Location toward which the camera continually looks. Default <0,0,0>.
#scene.forward Vector pointing in the direction in which the camera points. Default <0,0,-1>. Magnitude of this vector is ignored. If scene.forward is changed, the camera is moved to a position from which scene.forward points at scene.center.
#scene.range Distance from scene.center to edge of canvas. For a rectangular canvas range is the shorter of the two possible distances (the y direction for a canvas that is wider than it is tall).
#scene.fov Field of view of the camera in radians. Changes automatically if scene.autoscale is True.
#scene.up A vector perpendicular to scene.forward. By default <0,1,0>. Changing scene.up rotates the camera around the z axis.

#3: You may need to manipulate the camera directly if, for example, you are doing a fly-through of the scene:

#scene.camera.pos The position of the camera. Changes automatically if scene.autoscale is True. Changing scene.camera.pos changes scene.center to scene.camera.pos + scene.camera.axis.
#scene.camera.axis The current direction in which the camera is pointing. scene.camera.axis = scene.center - scene.camera.pos. 
#Changing scene.camera.axis changes scene.forward and scene.center. NOTE: it is possible to point t
#scene.camera.rotate(angle=myangle, axis=myaxis, origin=myorigin)
#scene.camera.follow(myobject) Resets the center of the scene to the current position of myobject. To turn off following set: scene.camera.follow(None).

#See also


#camera position and axis (axis is the object of interest with DIRECTION, and position is the observer's position)
scene.camera.pos=vec(1,1,1)
scene.camera.axis=vec(-1,-1,-1)