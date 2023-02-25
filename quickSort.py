def swap(arr, i1, i2): 
    temp = arr[i1] 
    arr[i1] = arr[i2] 
    arr[i2] = temp 

def getIndexFromLeft(arr, start, pivotIndex): 
    if start == pivotIndex: 
        return pivotIndex       #oppure return start è lo stesso 
    else: 
        if arr[start] > arr[pivotIndex]: 
            return start 
    return getIndexFromLeft(arr, start+1, pivotIndex) 

def sort(arr, start, pivotIndex): 
    if arr[pivotIndex-1] < arr[pivotIndex]:         #se è minore cerco un valore che vada bene 
        possibleIndexForSwap = getIndexFromLeft(arr, start, pivotIndex) 
        if possibleIndexForSwap == pivotIndex-1:      #se è minore e il valore che va bene è ormai di fianco al pivot ho finito 
            return (arr, pivotIndex)              #arr                  #HO BISOGNO DI RETURNARE ANCHE L'INDICE DEL PIVOT DOPO CHE è STATO SPOSTATO,++ RETURN DI UNA TUPLA?  
        else:                                           #altrimenti il valore che va bene viene spostato dove avverrebbe normalmente lo scambio 
            swap(arr, possibleIndexForSwap, pivotIndex-1) 
    swap(arr, pivotIndex-1, pivotIndex)                 #viene fatto lo scambio, sia se il valore andava già bene sia se è stato scambiato con quello che andava bene 
    return sort(arr, start, pivotIndex-1)               #viene richiamata la funzione diminuendo la posizione del pivot 
    # elif arr[iPivot-1] < arr[iPivot]:         dovrebbe essere verificato ancora prima di scambiare in caso ci sia un maggiore pivot alla sua sinistra 
    #     swap(arr, getIndexFromLeft(arr, start, iPivot), iPivot-1) 
        
    
def quickSort(arr, start, stop): 
    if start == stop:       
        return arr 
    else: 
        sort(arr, start, stop) 
    #quickSort(quickSort(arr, 0, iPivot-1), iPivot+1, len(arr-1))       NON SO COME FARGLI ARRIVARE L'INDICE DEL PIVOT 

input = [3, 5, 8, 4, 1, 9, 2] 
print(quickSort(input, 0, len(input)-1))