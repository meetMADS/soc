from typing import Callable
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

def func(t, v, k):
    """ computes the function S(t) with constants v and k """
    
    # TODO: return the given function S(t)
    pass
    return (v*(t-((1-np.exp(-k*t))/k)))

    # END TODO


def find_constants(df: pd.DataFrame, func: Callable):
    """ returns the constants v and k """

    v = 0
    k = 0

    # TODO: fit a curve using SciPy to estimate v and k
    #extracting the data
    xdata=df.iloc[:,0]
    ydata=df.iloc[:,1]

    optimal_value,_ =curve_fit(func,xdata,ydata)
    v,k= optimal_value

    
    # END TODO

    return v, k


if __name__ == "__main__":
    df = pd.read_csv("data.csv")
    v, k = find_constants(df, func)
    v = v.round(4)
    k = k.round(4)
    print(v, k)

    # TODO: plot a histogram and save to fit_curve.png
    t_graph=np.linspace(0 , 0.370 , 100)
    S_graph=func(t_graph,v,k)
    xdata=df.iloc[:,0]
    ydata=df.iloc[:,1]
    plt.figure()
    plt.plot(xdata , ydata , 'b*' , label='data')
    plt.plot(t_graph,S_graph, 'r-' , label= f'fit: v={v:.4f},k={k:.4f}')
    plt.xlabel('t')
    plt.ylabel('S')
    plt.legend()

    plt.savefig('fit_curve.png')
    plt.show()

    # END TODO
