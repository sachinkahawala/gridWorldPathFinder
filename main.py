import numpy as np
#["up","right","down","left"] as 0,1,2,3
class env:
    def __init__(self, x, y):
        self.A = [0,1,2,3]
        self.S = [(i,j) for i in range(x) for j in range(y)]
        self.Size=(x,y)
def bellman_update(env, V,pi, s, reward , gamma):
    x,y=s
    sumOfall=0
    mX,mY=env.Size
    for a in env.A:

        if a==0:
            s_=(x-1 if x>=1 else x, y)
        if a==1:
            s_=(x, y+1 if y<mY-1 else y)
        if a==2:
            s_=(x+1 if x<mX-1 else x, y)
        if a==3:
            s_=(x, y-1 if y>=1 else y)
        prob=pi[x,y,a]
        sumOfOthers = 1 * (reward[s_] + gamma * V[s_])
        sumOfall+=prob*sumOfOthers

    V[s]=sumOfall
def evaluate_policy(env, V,pi, gamma, theta,reward,targets):
    while True:
        delta = 0
        for s in env.S:
            if s not in targets:
                v = V[s]
                bellman_update(env, V,pi, s,reward, gamma)
                delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break
    return V
def q_greedify_policy(env, V, pi, s, gamma,reward):
    x,y=s
    mX,mY=env.Size
    G = [0 for i in range(len(env.A))]

    for a in env.A:
        if a==0:
            s_=(x-1 if x>=1 else x, y)
        if a==1:
            s_=(x, y+1 if y<mY-1 else y)
        if a==2:
            s_=(x+1 if x<mX-1 else x, y)
        if a==3:
            s_=(x, y-1 if y>=1 else y)
        G[a] +=1 * (reward[s_] + gamma * V[s_])

    greedyIndexes = np.argwhere(G ==np.amax(G))
    xs,ys=s
    for a in env.A:
        if a in greedyIndexes:
            pi[xs,ys,a]=1/float(len(greedyIndexes))
        else:
            pi[xs,ys,a]=0

def improve_policy(env, V, pi, gamma,reward):
    policy_stable = True
    for s in env.S:
        xs,ys=s
        old = pi[xs,ys].copy()
        q_greedify_policy(env, V, pi, s, gamma,reward)
        if not np.array_equal(pi[s], old):
            policy_stable = False
    return pi, policy_stable

def policy_iteration(env,V, pi, gamma, theta,reward,targets):

    policy_stable = False
    while not policy_stable:
        V = evaluate_policy(env, V, pi, gamma, theta,reward,targets)
        pi, policy_stable = improve_policy(env, V, pi, gamma,reward)

        #print(V)
    return V, pi
# x,y=4,4
# pi=np.full((x,y,4),0.25)
# obs=[(0,1),(0,2),(0,3),(2,0),(2,1),(2,2)]
# targets=set([(0,0)])
# reward=np.full((x,y),-1)
# for t in obs:reward[t]=-10
# values = np.zeros((x,y))
# theta=0.001
# gamma=1
# e=env(x,y)
# policy_iteration(e,values,pi, gamma, theta,reward)
