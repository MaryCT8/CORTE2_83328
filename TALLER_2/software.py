def data(numb):
    t_paises= []
    f=open("organization_data.csv","r")
    f.readline()
    l=f.readlines()
    for i in l:
        index_country=i.replace("\n","").split(",") 
        if index_country[4] not in t_paises:
            t_paises.append(index_country[4])      
    alpha_country=sorted(t_paises)
    x=alpha_country[numb-1]
    f.seek(0)
    t_company=[]
    t_web=[]
    description=[]
    t_fundation=[]
    t_industry=[]
    t_employyes=[]
    for i in l:
        index_company=i.replace("\n","").split(",") 
        if index_company[4] == x:
            t_company.append(index_company[2])
            t_web.append(index_company[3])
            description.append(index_company[5])
            t_fundation.append(index_company[6])
            t_industry.append(index_company[7])
            t_employyes.append(int(index_company[8]))
    f.close
    max_employyes = max(t_employyes)
    index_employys_max= t_employyes.index(max_employyes)
    print(f'Pais:{x}')
    print(f'Empresa con mayor # de empleados: ')
    print(f'-Empresa: {t_company[index_employys_max]}')
    print(f'-Website:{t_web[index_employys_max]} ') 
    print(f'-Description: {description[index_employys_max]}')  
    print(f'-Fundación: {t_fundation[index_employys_max]}')
    print(f'-Industria: {t_industry[index_employys_max]}')
    print(f'- #Empleados {t_employyes[index_employys_max]}')
    min_employys= min(t_employyes)
    index_employys_min=t_employyes.index(min_employys)
    print(f'Empresa con menor # de empleados: ')
    print(f'-Empresa: {t_company[index_employys_min]}')
    print(f'-Website:{t_web[index_employys_min]} ') 
    print(f'-Description: {description[index_employys_min]}')  
    print(f'-Fundación: {t_fundation[index_employys_min]}')
    print(f'-Industria: {t_industry[index_employys_min]}')
    print(f'- #Empleados {t_employyes[index_employys_min]}')
    num_company = len(t_company)
    prom_employyes = round(sum (t_employyes)/num_company,2)
    print(f'Promedio empleados: {prom_employyes}')
    print(f'Cantidad de empresas: {num_company}')

    

























#formatear ','
#ordenar los paises en orden alfabetico
#generar el programa
