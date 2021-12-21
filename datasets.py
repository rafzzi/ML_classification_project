import csv

def load_accesses():
        
    data = []
    accesses = []
    
    with open('accesses.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # Skip first line
        
        for line in reader:
            data.append([int(i) for i in line[:-1]])
            accesses.append(int(line[-1]))
        
        
    return [data, accesses]

def load_searches():
    
    data = []
    accesses = []
    
    with open('searches.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            d = [int(line[0])]
            
            # Separando variável categórica
            if line[1] == 'algoritmos':
                d.extend([1,0,0])
            if line[1] == 'java':
                d.extend([0,1,0])
            if line[1] == 'ruby':
                d.extend([0,0,1])

            d.append(int(line[2]))
            
            accesses.append(int(line[-1]))
            data.append(d)
            
    return [data, accesses]

def load_searches_v2():
    
    import pandas as pd
    
    df = pd.read_csv('searches.csv')
    df = pd.get_dummies(df)
    
    # df['algoritmos'] = [1 if i == 'algoritmos' else 0 for i in df['busca']]
    # df['java'] = [1 if i == 'ruby' else 0 for i in df['busca']]
    # df['ruby'] = [1 if i == 'java' else 0 for i in df['busca']]
    
    return [
        df[['home','busca_algoritmos','busca_java','busca_ruby','logado']].values,
        df['comprou'].values
        ]