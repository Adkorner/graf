# 10. zadanie: do_sirky
# autor: Adam Lopaška
# datum: 26.5.2022

class Graph:
    def __init__(self, file_name):
        self.graph = {}
        def to_str(subor):         
            with open(subor, 'rb') as file:
                return ''.join(chr(x) if 32<=x<127 else ' ' for x in file.read())

        ret = to_str(file_name).split("  ")
        ret[0] = ret[0].split()
        vrcholy = ret[0]  #mena vrcholov
        ret[1] = ret[1].split() #postupnost hran
        dlz = len(ret[1])
        hrany = []  #dvojice hran v tvare (v1,v2)
        for i in range(0,dlz,2):
            hrany.append((ret[1][i],ret[1][i+1]))
        for v in vrcholy:
            if v not in self.graph:
                self.graph[v] = set()
        for v1,v2 in hrany:
            self.graph[v1].add(v2)
            self.graph[v2].add(v1)
        
        #print(self.graph)

    def in_distance(self, v1, start, end=None):
        urovne = []
        def dosirky(v1):
            visited = set()
            queue = [v1]
            uroven = 0
            while queue:
                #print(uroven, set(queue))
                urovne.append((uroven, set(queue)))
                dalsi_queue = []
                for v1 in queue:
                    if v1 not in visited:
                        visited.add(v1)
                        for v2 in self.graph[v1]:
                            if v2 not in visited and v2 not in urovne[uroven][1]:
                                dalsi_queue.append(v2)

                queue = dalsi_queue
                uroven += 1
        dosirky(v1)

        final = set()

        if end is not None:
            for level in urovne:
                if level[0] <= end and level[0] >= start:
                    for v in level[1]:
                        final.add(v)
        else:
            for level in urovne:
                if level[0] == start:
                    for v in level[1]:
                        final.add(v)
        return final
    
    def max(self, v1):
        urovne = []
        def dosirky(v1):
            visited = set()
            queue = [v1]
            uroven = 0
            while queue:
                #print(uroven, set(queue))
                urovne.append((uroven, set(queue)))
                dalsi_queue = []
                for v1 in queue:
                    if v1 not in visited:
                        visited.add(v1)
                        for v2 in self.graph[v1]:
                            if v2 not in visited and v2 not in urovne[uroven][1]:
                                dalsi_queue.append(v2)
                queue = dalsi_queue
                uroven += 1
        dosirky(v1) 
        if urovne:
            return urovne[-1][0], urovne[-1][1]    
        else:   
            return 0, set()

    def for_all(self, v1):
        urovne = []
        def dosirky(v1):
            visited = set()
            queue = [v1]
            uroven = 0
            while queue:
                #print(uroven, set(queue))
                urovne.append(set(queue))
                dalsi_queue = []
                for v1 in queue:
                    if v1 not in visited:
                        visited.add(v1)
                        for v2 in self.graph[v1]:
                            if v2 not in visited and v2 not in urovne[uroven]:
                                dalsi_queue.append(v2)
                queue = dalsi_queue
                uroven += 1
        dosirky(v1)
        return urovne

    def in_middle(self, v1, v2):
        level1 = self.for_all(v1)
        level2 = self.for_all(v2)
        dlz = min(len(level1),len(level2))
        middle = set()
        for i in range(dlz):
            prienik = level1[i].intersection(level2[i])
            if prienik:
                for v in prienik:
                    middle.add(v)
                prienik = set()
        return middle


if __name__ == '__main__':
    '''g = Graph('subor5.dat')
    print(g.in_distance('amam', 3, 3))
    print(g.max('mure'))'''
    g = Graph('subor1.dat')
   # print(g.in_distance("1",1))
    '''for v1, i, j in ('4', 1, 3), ('2', 4, 4), ('1', 5, 7), ('7', 1, 3):
        print(f'in_distance({v1!r}, {i}, {j}) =', g.in_distance(v1, i, j))'''
    #print("max('3') =", g.max('3'))
    print("for_all('5') = ", g.for_all('5'))
    '''for v1, v2 in ('6', '8'), ('3', '7'):
        print(f'in_middle({v1!r}, {v2!r}) =', g.in_middle(v1, v2))'''