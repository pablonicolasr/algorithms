import os


def clearScreen():
    
    return os.system("cls" if os.name == "nt" else "clear")
    


class Horse:

    def __init__(self, n):
    
        self.n = n
    
        self.board = [
            [1, 2, 3], # 0 
            [4, 5, 6], # 1
            [7, 8, 9], # 2
            [None, 0, None] # 3
        ]

        self.movements = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
    
    
    def movs(self, i, j):
    
        movis = []
        
        for mov in self.movements:
            
            try:
            
                if self.board[i + mov[0]][j + mov[1]] is not None and i + mov[0] >= 0 and j + mov[1] >= 0:
                    
                    movis.append([i + mov[0],j + mov[1]])
                    
            except Exception as e:
                
                pass        
       
        return movis    
    
    def numMovs(self):
        
        lista_row = []
        
        for i in range(len(self.board)):
            
            lista_column = []
            
            for j in range(len(self.board[i])):
                
                if self.board[i][j] is not None:
                
                    lista_column.append(self.movs(i, j))
                
                else:
                    
                    lista_column.append([])
            
            lista_row.append(lista_column)
        
        return lista_row  
        
        
    def getMov(self, i, j):  
      
        
        return self.numMovs()[i][j]
       
        
    def totalMovs(self, n, i, j):
    
        #[[1, 6, 1], [1, 6, 7], [1, 6, 0], [1, 8, 1], [1, 8, 3]]
        #[[[0, 0], [1, 2], [0, 0]], [[0, 0], [1, 2], [2, 1]], [[0, 0], [1, 2], [3, 1]], [[0, 0], [2, 1], [3, 1]], [[0, 0], [2, 1], [0, 2]]]
        
        iteracion = 1
        
        lista = self.getMov(i, j)#[[1, 2], [2, 1]] --> [[[0, 0], [1, 2]], [[0, 0], [2, 1]]]       
        
        while iteracion < n:
        
            new_lista = list(lista)
            
            new_lista2 = []
            
            if len(lista) > 0:
            
                if iteracion == 1:       
                    
                    for u, value in enumerate(lista):
                        
                        new_lista[u] = [[i, j], value]
                
                new_lista2 = list(new_lista)
                        
                for x, value in enumerate(new_lista): #[[[0, 0], [1, 2]], [[0, 0], [2, 1]]]                 

                    n_movs = self.getMov(value[-1][0], value[-1][1]) # [[0, 0], [2, 0], [3, 1]]
                    
                    aux_list = []

                    for z in range(len(n_movs)):
                        
                        aux_list.append(new_lista[x])
                    
                    aw = []
                    
                    for u, value in enumerate(aux_list):
                        
                        au = list(aux_list[u])
                        
                        au.append(n_movs[u])     
                        
                        aw.append(au)                           
                        
                    new_lista2[x] = aw
            
            lista_aplanada = [item for sublista in new_lista2 for item in sublista]
            
            lista = list(lista_aplanada)
            
            iteracion += 1   
        
        return len(lista) if self.n == 1 else len(lista_aplanada)
                
            
    def countMovs(self):
        
        count = 0
    
        for i in range(len(self.board)):
            
            for j in range(len(self.board[i])):
                
                if self.board[i][j] is not None:
                    
                    count += self.totalMovs(self.n, i, j)
        
        return count       
                    
        
        
if __name__ == "__main__":
    
    band = False
    
    while not band:
        
        try:

            num_movements = int(input("Introduzca la cantidad de movimientos: "))
            
            if num_movements <= 0:
                
                print("Debe ingresar un número mayor que 0")
                
            else:
                
                band = True
                
                input(f"La cantidad de movimientos que se analizará es {num_movements}")
                
                clearScreen()
            
        except Exception as e:
            
            print("Usted debe introducir un número")
            
            
    print(f"La cantidad de posibilidades válidas con la cantidad de movimientos {num_movements} es: {Horse(num_movements).countMovs()}")