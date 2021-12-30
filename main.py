
import numpy as np
import pandas as pd
#import torch

ROWS = 3510 # 17 years * 252 trading days (3528)

'''
Autoregression model - on volatility

Calculating autocorrelation of previous 30 day, 5 day volatility 


'''

def variance(array,mean):
    for i in range(len(array)):
        abs(mean-array[i])
    #average
    return

def mean(array):
    mean = np.mean(array)
    print("Average,", np.mean(array))
    return mean

# Edit: sub array and array must be of equal length
# Backshifted array and t=0 array to be autocorrelated
# PROBLEM: covariance (within corrcoeff) is taking the covariance
# of the matrices, ie. is returning cov 1 bc they appear to be the same set.
# May need to do this manually as we do not have a good solution for autocorrelation.
# Solution - pandas df

# takes array, period integer
# returns volatilies in array for those respective periods
# result len = (len array) / period
def period_vol(array, period):

    n = 0
    std_arr = []
    while (n+period) < (len(array)):
        sub_array = np.array(array[n:(n+period)])
        period_std = round(np.std(sub_array),3)
        std_arr.append(period_std) # do not append on final loop -

        n += period
        #
    print(std_arr[0:3])
    return 0
    #return(np.corrcoef(backshift_std_arr,array))



def main():

    file = 'SPY.csv'  
    df = pd.read_csv(file, nrows = ROWS, usecols=[0,1,2,3,4])
    i = 0
    stop = False
    print(ROWS)
    arr_alpha = []
    arr_beta = []
    arr_gamma = []
    while i < (ROWS - 10) and stop == False:

        j = i + 1
        k = i + 5
        m = i + 30
        if (m+30 > ROWS): # prevent the next iteration
            stop = True

        diff_alpha = round((df.iloc[j,4] - df.iloc[i,4])/df.iloc[i,4],3)   #close - close % chg
        diff_beta  = round((df.iloc[k,4] - df.iloc[i,4])/df.iloc[i,4],3)   #close - close % chg
        diff_gamma = round((df.iloc[m,4] - df.iloc[i,4])/df.iloc[i,4],3)   #close - close % chg

        arr_alpha.append(diff_alpha)
        arr_beta.append(diff_beta)
        arr_gamma.append(diff_gamma)
        
        i += 1 # iterate

        #end while

    # 1, 5, 30 day periods
    #df_result = pd.DataFrame(arr_alpha, arr_beta, arr_gamma, columns=['1day','5day','30day']) 
    series_alpha = pd.Series(arr_alpha)
    series_beta = pd.Series(arr_beta)
    series_gamma = pd.Series(arr_gamma)

    print(series_alpha.head(n=3))
    #print(series_beta.head(n=3))
    #print(series_gamma.head(n=3))
    
    print("###")

    print(series_alpha.corr(series_beta))
    print(series_beta.corr(series_gamma))
    print(series_gamma.corr(series_alpha))

    # autocorrelation of vol, 30 day per

    #ac = autocorr(arr_alpha,30)
    print("$$$")
    ac = series_beta.autocorr(2)
    ac_2 = series_gamma.autocorr(2)
    print(ac)
    print(ac_2)

    '''
    mean_alpha = mean(arr_alpha)
    mean_beta = mean(arr_beta)
    variance(arr_alpha, mean_alpha)
    variance(arr_beta, mean_beta)
    '''
    return 




if __name__ == '__main__':
    print('working...')
    main()