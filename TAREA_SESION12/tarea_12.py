
def main():
    sol={}
    doc=open('Alimentos.txt','rt')
    eat=doc.readlines()
    matrix = []
    doc.seek(0)
    for i in range(len(eat)):
        va=doc.readline().rstrip('\n').split(',')
       
        sol[va[1]]=float(va[2])
    return sol 
if __name__=='__main__':
    main()
    
  