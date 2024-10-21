import xlrd
import xlwt
import numpy as np
import sys

### Inputs

start = input("""Hi, My name is Kami
              How Can I Help You?
              1. Calculate a matrix system
              2. Calculate a matrix inverse
              
              Problem: """)
if start == "1":
    qq = input("""
               OK! in this case you should enter the matrix of {A|B}n*m
               which A is Coefficient Matrix an B is Fixed Matrix
               
               1. I have an excel sheet
               2. I enter matrix number by myself :D
              
               which one do you prefer: """)
    if qq == "1":
        ss = input("""
                   enter the full path of your excel sheet
                   like: C:\\Users\\abc\\Documents\\test1.xlsx
                   path: """)
        
        wkb = xlrd.open_workbook(ss)
        sheet = wkb.sheet_by_index(0)
        mtx_A=[]
        for row in range (sheet.nrows):
            _row = []
            for col in range (sheet.ncols):
                _row.append(sheet.cell_value(row,col))
            mtx_A.append(_row)
            
        n = len(mtx_A)
        m = len(mtx_A[0])
    elif qq == "2":
        print("""
              NOTE!
              split numbers in each row by SPACE and each row by ENTER
              """)
        n = int(input("""
                  How many rows {A|B} matrix have
                  n: """))
        m = int(input("""
                  How many culmns {A|B} matrix have
                  m: """))
        
        mtx_A = []
        for i in range(n):
            nmm = input("%s row: "%i)
            nmm = nmm.split()
            nmm = list(map(lambda x:float(x), nmm))
            mtx_A.append(nmm)
        
        else:
            print("""Opps I guess you made a mistake
                  Now restart the program""")
                  
if start == "2":
    pp = input("""
               OK! in this case you should enter the matrix of An*n
               
               1. I have an excel sheet
               2. I enter matrix number by myself :D
               
               which one do you prefer: """)
    
    if pp == "1":
        ss = input("""
                   enter the full path of your excel sheet
                   like: C:\\Users\\abc\\Documents\\test1.xlsx
                   path: """)
        wkb = xlrd.open_workbook(ss)
        sheet = wkb.sheet_by_index(0)
        mtx_A=[]
        for row in range (sheet.nrows):
            _row = []
            
            for col in range (sheet.ncols):
                _row.append(sheet.cell_value(row,col))
            mtx_A.append(_row)
        
        n = len(mtx_A)
        m = 2*n
        print(mtx_A)
        for i in range(n):
            abc = [0 for x in range(n)]
            nmm = mtx_A[i]
            abc[i] = 1
            nmm.extend(abc)
            mtx_A.append(nmm)
    elif pp == "2":
        print("""
              NOTE!
              split numbers in each row by SPACE and each row by ENTER
              """)
        n = int(input("""
                  How many rows A matrix have
                  n: """))
        m = n*2
        
        mtx_A = []
        for i in range(n):
            abc = [0 for x in range(n)]
            nmm = input("%s row: "%i)
            nmm = nmm.split()
            nmm = list(map(lambda x:float(x), nmm))
            abc[i] = 1
            nmm.extend(abc)
            mtx_A.append(nmm)
    
    else:
        print("""Opps I guess you made a mistake
                  Now restart the program""")

### Check det(A)
mtx_B = []
for i in range(n):
    yio = []
    for j in range(n):
        
        yio.append(mtx_A[i][j])
    mtx_B.append(yio)
mtx = np.array(mtx_B)
det = np.linalg.det(mtx)
if det == 0:
    print("""Opps, it seems that det(A) is zero!
          """)
    sys.exit()
    
    
for i in range(n):
    
    
    ### Pivoting
    if abs(mtx_A[i][i]) < 0.00000001:
        mx = 0
        ro = 0
        for o in range(i, n):
            if abs(mtx_A[o][i]) > mx:
                mx = mtx_A[o][i]
                ro = o
        re = mtx_A[ro]
        mtx_A[ro] = mtx_A[i]
        mtx_A[i] = re
        
    ### Algorihtm
    a = mtx_A[i][i]
    b = mtx_A[i]
    r = list(map(lambda x:x/a, b))
    mtx_A[i] = r
    for j in range(i):
        c = mtx_A[j][i]
        rr = list(map(lambda x, y: x - c*y, mtx_A[j], mtx_A[i]))
        mtx_A[j] = rr
    
    for j in range(i+1, n):
        c = mtx_A[j][i]
        rr = list(map(lambda x, y: x - c*y, mtx_A[j], mtx_A[i]))
        mtx_A[j] = rr
    
    ### Print mtx_A in each step
    for p in range(n):
        print()
        for q in range(m):
            print(mtx_A[p][q], end = "\t")
    
    print("\n\n NEXT STEP \n\n")
    
print(" IS FINAL ANSWER")
arb = int(input("""Number of significant digits
                (type "16" if you want maximum NSDs)
                NSDs: """))

print("""
      
      THE FINAL ANSWER IS:
      
      """)
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Sheet")
for i in range(n):
    print()
    for j in range(n, m):
        sheet.write(i, j, mtx_A[i][j])         
        print(round(mtx_A[i][j], arb), end = "\t")
workbook.save("test.xls")

        



        


    
            
    
    
    
    
        
    