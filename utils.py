import picar
import time
import numpy as np

def main():
    pose = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 1.57],
                     [2, 1, 0],
                     [2, 2, 1.57],
                     [1, 1, -.78], 
                     [0, 0, 0]])

    k_rho, k_alpha, k_beta = 3., 8., -2.5

    for i in xrange(pose.shape[0]-1):
        curr, target = pose[i, :], pose[i+1, :]
        rho = np.linalg.norm(target[:2] - curr[:2], 2)
        v = k_rho*rho

        alpha = np.arctan2(target[1]-curr[1], target[0]-curr[0]) - curr[2]
        beta = -curr[2] - alpha

        t = time.time()
        bw.speed = int(np.clip(v*20, 1, 100))
        bw.backward()
        while rho > 1e-1:
            omega = np.clip(k_alpha*alpha + k_beta*beta, -np.pi/6, np.pi/6)
            #print omega*180/np.pi
            fw.turn(90 - omega*180/np.pi)

            v_rho = -k_rho*rho*np.cos(alpha)
            v_alpha = k_rho*np.sin(alpha) - k_alpha*alpha - k_beta*beta
            v_beta = -k_rho*np.sin(alpha)

            dt = time.time() - t
            t = time.time()
            rho += v_rho*dt
            alpha += v_alpha*dt
            beta += v_beta*dt
            print rho

        #break
        #print rho
    fw.turn_straight
    bw.stop()

if __name__ == '__main__':
    fw = picar.front_wheels.Front_Wheels()
    bw = picar.back_wheels.Back_Wheels()
    try:
        main()
    except KeyboardInterrupt:
        fw.turn_straight()
        bw.stop()

