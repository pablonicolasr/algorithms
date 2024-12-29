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
    
    def possibleMovs(self, i, j):
    
        num_list = []
        
        pos_list = []
        
        for mov in self.movements:
            
            try:
            
                if self.board[i + mov[0]][j + mov[1]] is not None and i + mov[0] >= 0 and j + mov[1] >= 0:
                    
                    num_list.append(self.board[i + mov[0]][j + mov[1]])
                    
                    pos_list.append([i + mov[0], j + mov[1]])
                    
            except Exception as e:
                
                pass
        
        return pos_list, num_list            
            
            
    def countMovements(self):

        lista = []

        for i in range(len(self.board)):
            
            lista_row = []
            
            for j in range(len(self.board[i])):
                
                if self.board[i][j] is not None:
                
                    lista_row.append(self.possibleMovs(i, j)[0])
                    
                else:
                    
                    lista_row.append([])            
            
            lista.append(lista_row)
        
        print(lista)
          
                
        return lista
        
        
    def treeOrig(self):
        
        lista = self.countMovements() # Lista de movimientos de cada            
        
        a = 1
    
        while a < self.n:        
        
            for i, value in enumerate(lista):
                
                for j, val in enumerate(value):    
                    
                    if len(lista[i][j]) > 0:

                        aux_list = []
                            
                        for x, y in enumerate(lista[i][j]):           
                                
                            aux_list += self.possibleMovs(y[0], y[1])[0]                            
                        
                        lista[i][j] = aux_list
                                            
            a += 1
        
        suma = 0
    
        print(f"lista {lista}")
        
        for u, value in enumerate(lista):
            
            for v, val in enumerate(value):
               
                suma += len(val)                
                                
        return suma
        
        
if __name__ == "__main__":
    
    band = False
    
    while not band:
        
        try:

            num_movements = int(input("Introduzca la cantidad de movimientos: "))
            
            if num_movements <= 0:
                
                print("Debe ingreasar un número mayor que 0")
                
            else:
                
                band = True
                
                input(f"La cantidad de movimientos que se analizará es {num_movements}")
                
                clearScreen()
            
        except Exception as e:
            
            print("Usted debe introducir un número")
            
            
    print(f"La cantidad de posibilidades válidas con la cantidad de movimientos {num_movements} es: {Horse(num_movements).treeOrig()}")
        
        