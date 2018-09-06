import math
pressh =52.85379

psh = 26.26848
qsh = 154.1493
lsh = 170.8741
ssh = math.sqrt(pressh**2 + 400)
sth = 99.63802
pth = 39.23936
qth = 195.3119
lth = 138.6887
alpharsipr=90
VHRShsipr = 20*math.sin(math.pi/2 - alpharsipr*math.pi/180)
print(VHRShsipr)
VHRSvsipr = 20- 20*math.cos(math.pi/2-alpharsipr*math.pi/180)
print(VHRSvsipr)
VHRShysipr = math.sqrt(VHRShsipr**2 + VHRSvsipr**2)
print(VHRShysipr)
angleVHcossipr = math.acos(VHRShsipr/VHRShysipr)
print(angleVHcossipr)
angleVHsinsipr = math.asin(VHRShsipr/VHRShysipr)
print(angleVHsinsipr)
anglesVHhysipr = math.pi-angleVHcossipr
print(anglesVHhysipr)
sshsipr = math.sqrt(pressh**2+VHRShysipr**2-2*VHRShysipr*pressh*math.cos(anglesVHhysipr))
alphacrsiprex=math.acos((sshsipr**2+pressh**2-VHRShysipr**2)/(2*sshsipr*pressh))
Drsipr=math.sqrt(sshsipr**2+lsh**2-2*sshsipr*lsh*math.cos(alphacrsiprex+alpharsipr*math.pi/180))
alphacrsipr=(math.acos((Drsipr**2+psh**2-qsh**2)/(2*Drsipr*psh))+math.acos((Drsipr**2+sshsipr**2-lsh**2)/(2*Drsipr*sshsipr)))*180/math.pi
thetarersipr=3*(alphacrsipr+alphacrsiprex*180/math.pi)
print(thetarersipr)
