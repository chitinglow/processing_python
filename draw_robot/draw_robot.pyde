## Draw robot

size(720, 480)
strokeWeight(2)
# Blue background
background(0,153,204)
ellipseMode(RADIUS)

#NECK
stroke(255)
line(266, 257, 266, 162) #left
line(276, 257, 276, 162) #middle
line(286, 257, 286, 162) #right

# Antenna
line(276, 155, 246, 112) #small
line(276, 155, 306, 56) # tall
line(276, 155, 342, 170) #medium

#Body
noStroke() # Disable stroke
fill(255,204,0) # set fill to orange
ellipse(264,377,33,33) #antigravity orb
fill(0) #fill black
#main body
rect(219,257,90,120)
#gray color
fill(102)
#gray stripe
rect(219,274,90,6)

#Head
fill(0) #black
ellipse(276,155,45,45) #head
fill(255) #white color
ellipse(288,150,14,14) #large eye
#black
fill(0)
#pupil
ellipse(288,150,3,3)
#blue color
fill(153,104,255)
#small eye 1
ellipse(263,148,5,5)
#small eye 2
ellipse(296,130,4,4)
#small eye 3
ellipse(305,162,3,3)
