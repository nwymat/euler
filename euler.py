import numpy as np

def Rx(a,d="deg"):
    if d == "deg":
        a = np.pi/180*a
    return np.matrix(
    [[1,0,0],
    [0,np.cos(a),np.sin(a)],
    [0,-np.sin(a),np.cos(a)]])


def Ry(a,d="deg"):
    if d == "deg":
        a = np.pi/180*a
    return np.matrix(
    [[np.cos(a),0,-np.sin(a)],
    [0,1,0],
    [np.sin(a),0,np.cos(a)]])


def Rz(a,d="deg"):
    if d == "deg":
        a = np.pi/180*a
    return np.matrix(
    [[np.cos(a),np.sin(a),0],
    [-np.sin(a),np.cos(a),0],
    [0,0,1]])

def PRV(C):
    phi = np.arccos(0.5*(float(C.trace())-1))
    e = 1/(2*np.sin(phi))*np.matrix([
        C[1,2]-C[2,1],
        C[2,0]-C[0,2],
        C[0,1]-C[1,0]
    ])
    return [phi,phi/np.pi*180,e]

def EP(b0,b1,b2,b3):
    return np.matrix([
    [b0**2+b1**2-b2**2-b3**2, 2*(b1*b2+b0*b3), 2*(b1*b3 - b0*b2)],
    [2*(b1*b2-b0*b3), b0**2-b1**2+b2**2-b3**2, 2*(b2*b3+b0*b1)],
    [2*(b1*b3+b0*b2), 2*(b2*b3-b0*b1), b0**2-b1**2-b2**2+b3**2]
    ]);

def sheppard(C):
    bs = np.zeros(4)
    bs[0] = 0.25*(1+C.trace())
    bs[1] = 0.25*(1+2*C[0,0]-C.trace())
    bs[2] = 0.25*(1+2*C[1,1]-C.trace())
    bs[3] = 0.25*(1+2*C[2,2]-C.trace())

    b0b1 = 0.25*(C[1,2]-C[2,1])
    b0b2 = 0.25*(C[2,0]-C[0,2])
    b0b3 = 0.25*(C[0,1]-C[1,0])
    b1b2 = 0.25*(C[0,1]+C[1,0])
    b3b1 = 0.25*(C[2,0]+C[0,2])
    b2b3 = 0.25*(C[1,2]+C[2,1])

    b = [[bs[0],b0b1,b0b2,b0b3],
         [b0b1,bs[1],b1b2,b3b1],
         [b0b2,b1b2,bs[2],b2b3],
         [b0b3,b3b1,b2b3,bs[3]]]

    maxbs = np.argmax(bs)

    return b[maxbs]/np.sqrt(bs[maxbs])

def addEPmatrix(b0,b1,b2,b3,b4):
# 
    return np.matrix([[b0,-b1,-b2,-b3],
                      [b1, b0, b3,-b2],
                      [b2,-b3, b0, b1],
                      [b3, b2,-b1, b0]])
