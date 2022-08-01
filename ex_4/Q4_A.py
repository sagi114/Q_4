class stack:
    def __init__(self):
        self.arr=[]
        self.count=0
    def push(self,var):
        var.check_in()
        self.arr.append(var)
        self.count+=1
    def pop(self):
        l=len(self.arr)
        if l==0:
            return None
        v=self.arr[-1]
        self.arr.pop()
        return v
    def watch(self):
        return self.arr[-1]
    def get_count(self):
        return self.count
    def return_arr(self):
        arr_real=[]
        for a in self.arr:
            arr_real.append(a.get_cord())
        return arr_real
class point:
    def __init__(self,cord):
        self.visit=False
        self.cord=cord
    def get_cord(self):
        return self.cord
    def check_visit(self):
        return self.visit
    def check_in(self):
        self.visit=True
def put_in_stack(stk,g,arr):
    if g.check_visit():return None
    stk.push(g)
    for i in g.get_cord():
        tmp=put_in_stack(stk,arr[i],arr)
        if tmp!=None:
            stk=tmp
    return stk

def connected_comp(G):
    num_of_comp=len(G)
    arr=[]
    real_arr=[]
    graph=[]
    max_comp=-1

    for g in G:
        graph.append(point(g))
    for g in graph:
        if g.check_visit() is False:
            stk=stack()
            arr.append(put_in_stack(stk,g,graph))
    count=0
    for a in arr:
        if a.get_count()>max_comp:
            max_comp=a.get_count()
            #real_arr=a.return_arr()
        tmp=[]
        for i in range(a.get_count()):
            tmp.append(count)
            count += 1
        real_arr.append(tmp)



    return real_arr,max_comp




    #stk=stack()
    #stk.push(G[0])


if __name__ == '__main__':
    g=[[1,3],[0],[3],[2,0],[]]
    print(connected_comp(g))
