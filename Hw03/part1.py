'''
BFS için: “while queue:” satırı O(V) ve içindeki for döngüsü 
          O(V) zamanda çalıştığı için iki döngünün toplamı O(V^2)’dir. 
          Yani T(n) = O(V^2) olur.

DFS için: V tane vertex için V tane vertex’in visited node olup olmadığı kontrol edilir. 
          Dolayısıyla T(n) = O(V^2) olur.

'''

# XLS dosyasini okumak icin kuruldu.
!pip install xlrd
import xlrd
from collections import deque

# Verilen excel dosyasi okunur.
workbook = xlrd.open_workbook("Graph_data.XLS") 

class Graph:
    vNum = 0 # vertex sayisi
    vertexes = [] # matrix graph icin dizi

    # Matrix graph icin vertex sayisina bagli olarak
    # iki boyutlu bir dizi olusturur. 
    def __init__(self, vNum):
        self.vNum = vNum
        for i in range(vNum):
            row = []
            for j in range(vNum):
                row.append(0)
            self.vertexes.append(row)

    def print_matrix_graph(self):
        for i in range(self.vNum):
            for j in range(self.vNum):
                print(self.vertexes[i][j], end=' ')
            print()
    # Verilen edge'in bilgisini array'a kaydeder. 
    def add_edge(self, i, j):
        if i < self.vNum and j < self.vNum:
            self.vertexes[i][j] = 1
            
    # Verilen baslangic indeksi ile graph'in
    # tum vertex'leri print edilir.
    def breadth_first_search(self, start):
        # Ziyaret edilen node'ların kayit edilmesi
        # icin boolean bir array olusturulur.
        visited_nodes = self.vNum * [False]
        queue = deque()
        
        # Baslangic vertex'i queue'ye kaydedilir. 
        queue.append(start)
        visited_nodes[start] = True
        
        # Queue bos kalana kadar dongu devam eder.
        while queue:
            # Queue'nin basindaki vertex alinarak
            # onun komsu vertex'lerine bakilarak ziyaret
            # edilmeyen vertex'ler queue'ye atılır.
            start = queue.popleft()
            print(start, end=' ')
            for i in range(self.vNum):
                if self.vertexes[start][i] == 1 and visited_nodes[i] == False:
                    queue.append(i)
                    visited_nodes[i] = True
                    
    # Dfs icin recursive cagri yapan helper fonksiyondur.
    def dfs_helper(self, i, visited_nodes):
        # Ziyaret edilen vertex'i isaretler ve print eder.
        visited_nodes[i] = True
        print(i, end=' ')
        # Ziyaret edilen vertex'in komsusu varsa
        # ve ziyaret edilmemisse fonk recursive cagri yaparak
        # dfs ilerler.
        for j in range(self.vNum):
            if visited_nodes[j] == False and self.vertexes[i][j] == 1:
                self.dfs_helper(j, visited_nodes)
            
    # Verilen baslangic indeksi ile graph'in
    # tum vertex'leri print edilir.
    def depth_first_search(self, start):
        # Ziyaret edilen node'ların kayit edilmesi
        # icin boolean bir array olusturulur.
        visited_nodes = self.vNum * [False]
        self.dfs_helper(start, visited_nodes)


# Excel dosyasindaki graph bilgileri ile
# bir graph olusturulur.
current_sheet = workbook.sheet_by_index(0) 
current_sheet.cell_value(0, 0) 

# Root vertex baslangic noktasi olarak alinir.
root_vertex = int(current_sheet.cell_value(0, 1))
vNum = root_vertex

# Vertex sayisi en buyuk vertex degerine gore belirlenir.
for i in range(3,current_sheet.nrows): 
    source = int(current_sheet.cell_value(i, 0))
    target = int(current_sheet.cell_value(i, 1))
    if source > vNum:
        vNum = source
    if target > vNum:
        vNum = target

# Graph olusturulur.        
g = Graph(vNum+1)

# Excel dosyasindaki edge'ler graph'a eklenir.
for i in range(3,current_sheet.nrows): 
    source = current_sheet.cell_value(i, 0)
    target = current_sheet.cell_value(i, 1)
    g.add_edge(int(source), int(target))

print("// Matrix Graph Representation \\\\")
g.print_matrix_graph()
print()
print("Root Vertex: ", root_vertex)
print("--> Breadth First Search: ", end="")
g.breadth_first_search(root_vertex)
print()
print("--> Depth First Search: ", end="")
g.depth_first_search(root_vertex)
print()
