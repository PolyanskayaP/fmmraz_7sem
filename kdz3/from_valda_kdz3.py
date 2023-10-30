import pandas as pd

#Valda 
def valda_kr(df, WE_FIND):
    indices_valda = []
    if WE_FIND == "MAX":
        min_values_valda = df.min(axis=1)  #list(row.min() for index, row in df.iterrows())
        maximum_valda = max(min_values_valda)
        indices_valda = [i for i, v in enumerate(min_values_valda) if v == maximum_valda]
        
        print(df)
        print("Промежуточные вычисления.")
        print("min (Valda): \n", min_values_valda, "\n")
        print(maximum_valda) 
    elif WE_FIND == "MIN": #проверить
        max_values_valda = df.max(axis=1) #list(row.max() for index, row in df.iterrows())
        minimum_valda = min(max_values_valda)
        indices_valda = [i for i, v in enumerate(max_values_valda) if v == minimum_valda]
    else:
        pass
    return indices_valda #numeration from 0 



if __name__ == '__main__':
    WE_FIND = "MAX" #"MIN"
    #df = pd.read_csv('kdz2_1.csv', sep=';')  #header non или не non  
    df = pd.read_csv('fr3.csv', sep=';')   #и чем заполнять NaN в случае max и min ?
                        #КТО НА ПЕРВОМ КТО НА ВТОРОМ МЕСТЕ И Т Д 
    #отрицательные нельзя????
    valda_kr(df, WE_FIND)