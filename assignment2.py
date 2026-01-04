import numpy as np

def stat ():
    data = np.loadtxt('populations.txt')
    
    hare = data[:,1]
    min_index = np.argmin(hare)
    min_year_hare = data[min_index, 0]
    lynx_avg = np.mean(data[:, 2])
    total = np.sum(data[:, 1:], axis=1)
    new_data = np.column_stack((data, total))
    new_data[new_data[:, 3] < 4000, 3] = 0
    
    
    print("Data:\n", data)
    print("Hare column:\n", hare)
    print("Year with miniumum hare population:", min_year_hare)
    print("Average lynx population:", lynx_avg)
    print("New data with total column:\n", new_data)
    
    return data, hare, min_year_hare, lynx_avg, new_data

stat()