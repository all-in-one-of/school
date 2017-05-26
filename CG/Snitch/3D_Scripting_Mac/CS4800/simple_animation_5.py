import maya.cmds as cmdsimport random'''Simple animation script that moves persp camerascales, rotates and translates and shades.'''#erases anything on stage creates a new filenewfile = cmds.file(f=True, new=True)sec=33#sets playback timecmds.playbackOptions( minTime='0sec', maxTime='200sec', ast=0, ps=1.8)#sets the angle of the cameracmds.setAttr('persp.translateX', 15)cmds.setAttr('persp.translateY', 30)cmds.setAttr('persp.translateZ', -15)#sets the rotation of the cameracmds.setAttr('persp.rotateX', 360)cmds.setAttr('persp.rotateY', 90.000)cmds.setAttr('persp.rotateZ', 60.000)#a function to apply color to objects def applyColor(objectName, colorR, colorG, colorB):    myShader = cmds.shadingNode('blinn', n='myShader', asShader=True)    cmds.select(objectName)    cmds.setAttr( myShader +'.color',colorR, colorG, colorB, type='double3')    shaderSet = cmds.sets(renderable=True, noSurfaceShader=True, empty=True)    cmds.connectAttr(myShader +".outColor", shaderSet+".surfaceShader")    cmds.sets(forceElement=shaderSet, e=True)	#my list of ballsballs = ["Star1", "Star2", "Star3", "Star4", "Star5", "Star6", "Star7", "Star8", "Star9"]dbz=[]for ball in balls:   #This will be used for  the balls radius as well as the balls initial starting y   r = (random.random())-10   #creates the ball   x = (5*random.random())-5   y = (6*random.random())-10   z = (7*random.random())-30     n=cmds.polySphere(r=(30*random.random()*5r))    cmds.move(x,y,z,n[0], absolute=True )   dbz.append(n[0])      applyColor(n[0],random.random(),random.random(),random.random())rotation={}for ball in dbz:  rotation[ball]=(180*random.random())for ti in range(0,sec):  for ball in dbz:    ty=cmds.getAttr(ball+'.translateY')    print ty      ty=2*ty-1.0    cmds.setAttr(ball+'.translateY', ty)    tx=cmds.getAttr(ball+'.translateX')    tx=tx+(2*random.random()-10)    cmds.setAttr(ball+'.translateX', tx)    tz=cmds.getAttr(ball+'.translateZ')    tz=tz+(.5*random.random()-0.5)    cmds.setAttr(ball+'.translateZ', tz)	    print tx,' ', ty,' ', tz    sz=1.33-(0.6*random.random())    cmds.scale(sz,sz,sz,ball)    cmds.rotate(rotation[ball],(10-(30*random.random())),(20-(50*random.random())),ball,pivot=(tx,ty,tz),relative=True)  s=str(ti)+'sec'  cmds.setKeyframe(dbz,t=s)cmds.play()