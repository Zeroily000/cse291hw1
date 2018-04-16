import picar
import time
import numpy as np

if __name__ == '__main__':
    bw = picar.back_wheels.Back_Wheels()
    fw = picar.front_wheels.Front_Wheels()
    pose = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 1.57],
                     [2, 1, 0],
                     [2, 2, 1.57],
                     [1, 1, -.78], 
                     [0, 0, 0]])

    k_rho, k_alpha, k_beta = 70, 0.1, 0.1
   
    for i in xrange(pose.shape[0]-1):
        start, end = pose[i, :2], pose[i+1, 0:2]
        rho = np.linalg.norm(end-start, 2)
        bw.speed = int(k_rho * rho)
        bw.backward()
    
        beta = np.arccos((pose[i+1, 0] - pose[i, 0])/rho)
        alpha = beta - pose[i, 2]
        gamma = k_alpha*alpha + k_beta*beta
        fw.turn(90 - gamma*180/np.pi)
        time.sleep(1)
    fw.turn_straight()
    bw.stop()
