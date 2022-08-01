class point:
    def __init__(self,data):
        self.data=data
        self.have_been=False
    def check_could_visit(self):
        if self.data==0 or self.have_been==True:return False
        else:return True
    def check_out(self):
        self.have_been=True
class val_and_bool:
    def __init__(self,val=-1):
        self.val=val
        self.bool=False
    def change_to_false(self):
        self.bool=False
    def change_to_True(self):
        self.bool=True
    def get_bool(self):
        return self.bool
    def add_one_to_data(self):
        if(self.val==-1):
            self.val=0
        self.val+=1
    def get_val(self):
        return self.val
    def change_bool(self,bool):
        self.bool=bool
    def get_bool(self):
        return self.bool
    def swap(self,var):
        self.val=var.get_val()
        self.bool=var.get_bool()
def solve(maze,N,M,S,E,K,l,K_g):
    b=[]
    for i in range(4):
        b.append(val_and_bool())
    if (S == E):
        v = val_and_bool(0)
        v.change_to_True()
        return v
    K-=1
    if(K!=0):
        if(l=='u'):
            if S[0]<0 or maze[S[0]][S[1]].check_could_visit() is False:return val_and_bool()
            maze[S[0]][S[1]].check_out()
            b[0].swap(solve(maze,M,N,[S[0]-1,S[1]],E,K,l,K_g))
        elif (l == 'd'):
            if S[0]>=N or maze[S[0]][S[1]].check_could_visit() is False:return val_and_bool()
            maze[S[0]][S[1]].check_out()
            b[1].swap(solve(maze,M,N,[S[0]+1,S[1]],E,K,l,K_g))
        elif (l == 'r'):
            if S[1]>=M or maze[S[0]][S[1]].check_could_visit() is False:return val_and_bool()
            maze[S[0]][S[1]].check_out()
            b[2].swap(solve(maze,M,N,[S[0],S[1]+1],E,K,l,K_g))
        elif (l == 'l'):
            if S[1]<0 or maze[S[0]][S[1]].check_could_visit() is False:return val_and_bool()
            maze[S[0]][S[1]].check_out()
            b[3].swap(solve(maze,M,N,[S[0],S[1]-1],E,K,l,K_g))
        min = 100000000000000000000000000000000000000000000000
        for i in b:
            if i.get_bool() == False:
                continue
            else:
                if i.get_val() < min and i.get_val() != -1:
                    min = i.get_val()
        v=val_and_bool(min+1)
        v.change_to_True()
        return v

    else:
        return maze_solver_1(maze,M,N,S,E,K_g)
def maze_solver_1(maze,M,N,S,E,K):
    b=[]
    for i in range(4):
        b.append(val_and_bool())
    up=[S[0]-1,S[1]]
    down = [S[0] +1, S[1]]
    left = [S[0], S[1]-1]
    right= [S[0] , S[1]+1]
    if (0 <= (up[0])and maze[up[0]][up[1]].check_could_visit()):
        b[0].swap(solve(maze, M, N, up, E,K,'u',K))
    if (N > down[0] and maze[down[0]][down[1]].check_could_visit()):
        b[1].swap(solve(maze, M, N, down, E,K,'d',K))
    if (0 <= left[1] and maze[left[0]][left[1]].check_could_visit()):
        b[2].swap(solve(maze, M, N, left, E,K,'l',K))
    if (M > right[1] and maze[right[0]][right[1]].check_could_visit()):
        b[3].swap(solve(maze, M, N, right,E, K,'r',K))
    if (b[0].get_bool() is not True) and (b[1].get_bool() is not True) and (b[2].get_bool() is not True) and (b[3].get_bool() is not True):
        return val_and_bool()
    min=100000000000000000000000000000000000000000000000
    for i in b:
        if i.get_bool()==False:
            continue
        else:
            if i.get_val()<min and i.get_val()!=-1:
                min=i.get_val()
    v=val_and_bool(min+1)
    v.change_to_True()
    return v
def maze_solver(mat,S,E,K):
    S=list(S)
    E=list(E)
    if len(S)==1:
        S.append(S[0])
    if len(E)==1:
        E.append(E[0])
    N = M = 0
    matrix = []
    for r in mat:
        N += 1
        tmp = []
        for c in r:
            M += 1
            tmp.append(point(c))
        matrix.append(tmp)
    v=maze_solver_1(matrix,M,N,S,E,K).get_val()
    if v>=100000000000000000000000000000000000000000000000:
        return -1
    else:
        return v
"""""
if __name__ == '__main__':
    mat = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
           [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
           [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
           [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
           [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
           [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]]
    s_1={0,0}
    e_1={2,4}
    print(maze_solver(mat,s_1,e_1,2))
"""""

