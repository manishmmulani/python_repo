from mat import Mat
import math

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
    return Mat((labels, labels), {(t,t):1 for t in labels})

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    resultMat = identity()
    resultMat['x','u']=x
    resultMat['y','u']=y
    return resultMat

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    scaleMat = identity()
    scaleMat['x','x']=a
    scaleMat['y','y']=b
    return scaleMat

## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    rotateMat = identity()
    rotateMat['x','x']=math.cos(angle)
    rotateMat['x','y']=-math.sin(angle)
    rotateMat['y','x']=math.sin(angle)
    rotateMat['y','y']=math.cos(angle)
    return rotateMat

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    return translation(x,y)*rotation(angle)*translation(-x,-y)

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    reflectyMat = identity()
    reflectyMat['x','x']=-1
    return reflectyMat

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    reflectxMat = identity()
    reflectxMat['y','y']=-1
    return reflectxMat

## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    colMat = identity({'r','g','b'})
    colMat['r','r']=scale_r
    colMat['g','g']=scale_g
    colMat['b','b']=scale_b
    return colMat

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    labels = {'r', 'g', 'b'}
    return Mat((labels, labels), {(row, col):(77.0 if col=='r' else 151.0 if col=='g' else 28.0)/256.0 for row in labels for col in labels})

## Task 10cTWS4QeFc8
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    x1,y1=p1
    x2,y2=p2
    theta = math.atan(((x2-x1)*1.0)/(y2-y1)) if y2 != y1 else math.pi/2.0
    return rotate_about(x1,y1,-theta)*translation(x1,y1)*reflect_y()*translation(-x1,-y1)*rotate_about(x1,y1,theta)


