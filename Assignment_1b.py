import copy
import math

# This class is to hold matrix data
class Matrix:
    def __init__(self, row: int, col: int, listOfList: list):
        self.n: int = row
        self.m: int = col
        self.data: list = listOfList


# This class has functions for different operations on a matrix
class MatrixOperations:
    def print_matrix(self, message:str, matrix:Matrix):
        '''Print Matrix
        Input:  message (A string to print before the matrix), matrix (A Matrix Object)
        Output: A multi line string of the Matrix data
        '''
        print()
        print(message)
        for row in matrix.data:
            line: str = ""
            for element in row:
                line += str(element) + "\t"
            print(line)
        print()

    #Gauss Elimination using Pivot
    def REF(self, matrix:Matrix, d):
        '''Calculate the Row Echelon Form for a Matrix thru' Gauss Elimination Method
        Input:  matrix (A Matrix Object)
        Output: REF (A Matrix Object holding the REF form for matrix)
        '''
        add = 0
        mul = 0
        div = 0
        
        REF:Matrix = Matrix(matrix.n, matrix.m, matrix.data)
        for i in range(REF.n):
            # Pivot the row when the pivot element is 0
            if (REF.data[i][i] == 0):
                for j in range(i, REF.n):
                    if abs(REF.data[j][i]) > abs(REF.data[i][i]):
                       REF.data[j], REF.data[i] = REF.data[i], REF.data[j]
                       break
            
            for j in range(i + 1, REF.n):
                # Getting Ratio to minimize no. of division operations performed
                ratio: float = REF.data[j][i] / REF.data[i][i]
                div = div + 1

                # Assign 0 hence reducing multiplication and addition by one for elements under the pivot
                REF.data[j][i] = 0
                for k in range(i + 1, REF.m):
                    #calculating the resultant value from elementary row operation
                    res_elem = REF.data[j][k] - ratio * REF.data[i][k]
                    add = add + 1
                    mul = mul + 1

                    #Rounding off to "d" significant digits
                    REF.data[j][k] = round(res_elem, d - int(math.floor(math.log10(abs(res_elem)))) - 1)
                    
        op_dict = {"Additions" : add, "Multiplications": mul, "Divisions": div}

        return REF, op_dict
    
    #Gauss Elimination without Pivot
    def REF_nopivot(self, matrix:Matrix, d):
        '''Calculate the Row Echelon Form for a Matrix thru' Gauss Elimination Method
        Input:  matrix (A Matrix Object)
        Output: REF (A Matrix Object holding the REF form for matrix)
        '''
        add = 0
        mul = 0
        div = 0
        
        REF_nopivot:Matrix = Matrix(matrix.n, matrix.m, matrix.data)
        for i in range(REF_nopivot.n):
            
            for j in range(i + 1, REF_nopivot.n):
                # Getting Ratio to minimize no. of division operations performed
                ratio: float = REF_nopivot.data[j][i] / REF_nopivot.data[i][i]
                div = div + 1

                # Assign 0 hence reducing multiplication and addition by one for elements under the pivot
                REF_nopivot.data[j][i] = 0
                for k in range(i + 1, REF_nopivot.m):
                    #calculating the resultant value from elementary row operation
                    res_elem = REF_nopivot.data[j][k] - ratio * REF_nopivot.data[i][k]
                    add = add + 1
                    mul = mul + 1

                    #Rounding off to "d" significant digits
                    REF_nopivot.data[j][k] = round(res_elem, d - int(math.floor(math.log10(abs(res_elem)))) - 1)
                    
        op_dict = {"Additions" : add, "Multiplications": mul, "Divisions": div}

        return REF_nopivot, op_dict

def main():
    print('-------------------------------------------------------------------------')
    print('Accepting entries for matrix: ')
    print('Enter number of rows: ')
    n: int = int(input())
    print('Enter number of columns: ')
    m: int = int(input())
    listOfList: list = []
    i: int = 0
    while(i < n):
        print('Enter ' + str(m) + ' elements for ' + str(i) +' row separated by white space')
        row: list = list(map(float, input().split()))
        if len(row) > m:
            print('number of elements in row greater than column count hence truncating')
        del row[m:]
        print(row)
        listOfList.append(row)
        i += 1
    matrixA: Matrix = Matrix(n, m, listOfList)
    print('-------------------------------------------------------------------------')
    
    print('Enter the number of significant digits for rounding in REF: ')
    d: int = int(input())
    print('-------------------------------------------------------------------------')
    
    operation: MatrixOperations = MatrixOperations()
    operation.print_matrix('Input Matrix is:', matrixA)
    print('-------------------------------------------------------------------------')

    res1_array = operation.REF(matrixA, d)
    operation.print_matrix('REF for Matrix obtained thru Gauss Elim with Pivot is:', res1_array[0])
    print('No. of Operations Performed:', res1_array[1])
    print('-------------------------------------------------------------------------')
    
    res2_array = operation.REF_nopivot(matrixA, d)
    operation.print_matrix('REF for Matrix obtained thru Gauss Elim without Pivot is:', res2_array[0])
    print('No. of Operations Performed:', res2_array[1])
    print('-------------------------------------------------------------------------')

if __name__ == '__main__':
    main()