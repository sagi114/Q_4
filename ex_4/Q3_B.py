class point:
    def __init__(self,data=0):
        self.data=data
        self.bool_val=[]
        for i in range(9):
            self.bool_val.append(True)
    def turn_data_to_false(self,val):
        self.bool_val[val-1]=False
        self.check_data()
    def get_val(self):
        return self.data
    def check_data(self):
        if self.data!=0: return
        count=0
        index_true=-1
        for i in range(9):
            if self.bool_val[i]==True:
                index_true=i+1
            else:
                count+=1
        if count==8:
            self.data=index_true

def take_sudoko_and_send_right_input(mat):
    s=[]
    for r in mat:
        l = ''
        for c in r:
            l+=f'{c}'
        s.append([int(l)])
    return s
def create_matrix():
    str="53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5","....8..79"
    matrix=[]
    s=len(str)
    #print(s)
    for s in str:
        a = []
        for c in s:
            if c=='.':
                a.append(0)
            else:
                a.append(int(c))
        matrix.append(a)
    return matrix
def print_mat(mat):
    for r in mat:
        l=""
        for c in r:
            l+=f'{c.get_val()}\t'
            #print('\t')
        l+='\n'
        #print(l)
def create_mat_from_other_matrix(matrix):
    mat=[]
    for r in matrix:
        tmp=[]
        for c in r:
            tmp.append(c.get_val())
        mat.append(tmp)
    return  mat
def solve_sudoko():
    first_sum = 0
    second_sum = 0
    matrix = []
    mat = create_matrix()
    square = []
    a = [[], [], [], [], [], [], [], [], []]
    for r in range(9):
        tmp = []
        for c in range(9):
            r_3 = int(r / 3)
            c_3 = int(c / 3)
            a[3 * r_3 + c_3].append([r, c])
            tmp.append(point(mat[r][c]))
        matrix.append(tmp)
    sum = 0
    for s in range(9):
        sum += 9 * (s + 1)
    # create matrix of squares
    i = 0
    while (True):

        # check rows and cols
        for r in range(9):
            for c in range(9):
                val = matrix[r][c].get_val()
                if val != 0:
                    for r_in in range(9):
                        (matrix[r_in][c]).turn_data_to_false(val)
                        # print(mat)
                        mat = create_mat_from_other_matrix(matrix)
                    for c_in in range(9):
                        (matrix[r][c_in]).turn_data_to_false(val)
                        # print(mat)
                        mat = create_mat_from_other_matrix(matrix)

        # check squares
        for s in a:
            for j in range(9):
                v = matrix[s[j][0]][s[j][1]].get_val()
                if v != 0:
                    for k in range(9):
                        matrix[s[k][0]][s[k][1]].turn_data_to_false(v)
                        # print(mat)
                        mat = create_mat_from_other_matrix(matrix)

        #print(mat)
        # check win
        count = 0
        for r in matrix:
            for c in r:
                count += c.get_val()

        if (i == 0):
            first_sum = count
            second_sum = 0
            i += 1
        else:
            second_sum = first_sum
            first_sum = count
        if first_sum == second_sum:
            i += 1
        else:
            i = 1
        if i == 4 or count == sum:
            break
    #print(f'sum is {sum}, in board there is {count}')
    #print_mat(matrix)
    # print(f'ma is {mat}')
    mat=take_sudoko_and_send_right_input(mat)
    return (mat)

"""""
if __name__ == '__main__':
    print(solve_sudoko())
    """""










