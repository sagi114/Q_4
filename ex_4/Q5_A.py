import random
class point:
    def __init__(self,end_start):
        self.data=random.randint(0,1)
        self.have_bean_visit=False
        self.end_start=end_start
        if(end_start):
            self.data=1
    def can_visit(self):
        if self.data==0 or self.have_bean_visit==True:
            return False
        else:
            return True
    def get_val(self):
        return self.data
    def visit(self):
        self.have_bean_visit=True
def create_maze(N,M,S,E):
    arr = []
    for n in range(N):
        tmp = []
        for m in range(M):
            if n==S[0] and m==S[1] or n==E[0] and m==E[1]:
                tmp.append(point(True))
            else:
                tmp.append(point(False))
        arr.append(tmp)
    return arr
def solve(maze,M,N,S,E):
    #print(S)
    if S==E:
        return True
    if maze[S[0]][S[1]].can_visit()==False:
        return False
    maze[S[0]][S[1]].visit()
    up = [S[0] - 1, S[1]]
    down = [S[0] + 1, S[1]]
    right = [S[0] , S[1]+1]
    left = [S[0] , S[1]-1]
    b1=b2=b3=b4=-1
    if(0<=(S[0] - 1)): b1=solve(maze,M,N,up,E)
    if (N > (S[0] + 1)):b2=solve(maze, M, N, down, E)
    if (0 <= (S[1]-1)):b3=solve(maze, M, N, left, E)
    if (M > (S[1]+1)):b4=solve(maze, M, N, right, E)
    if(b1 is True or b2 is True or b3 is True or b4 is True):
        return True
    else: return False

def maze_generate(N,M):
    S = [random.randint(0, N-1), random.randint(0, M-1)]
    # print(S)
    E = [random.randint(0, N-1), random.randint(0, M-1)]
    while True:
        arr=create_maze(N,M,S,E)
        if solve(arr,M,N,S,E) is True:
            return arr,S,E
def print_mat(mat):
    for r in mat:
        l=""
        for c in r:
            l+=f'{c.get_val()}\t'
            #print('\t')
        l+='\n'
        print(l)
"""""
if __name__ == '__main__':
    print_mat(maze_generate(9,10))
    """""

