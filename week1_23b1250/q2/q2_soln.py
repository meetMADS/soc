import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def PCA(init_array: pd.DataFrame):

    sorted_eigenvalues = None
    final_data = None
    dimensions = 2

    # TODO: transform init_array to final_data using PCA
    #normaliztion
    minimum = init_array.min()
    maximum = init_array.max()
    normal_array = (init_array-minimum)/(maximum-minimum)

    #finding covariance variance and then make a matrix out of it
    var1=normal_array[0].var()
    var2=normal_array[1].var()
    var3=normal_array[2].var()
    var4=normal_array[3].var()

    cvar12=normal_array[0].cov(normal_array[1])
    cvar13=normal_array[0].cov(normal_array[2])
    cvar14=normal_array[0].cov(normal_array[3])
    cvar23=normal_array[1].cov(normal_array[2])
    cvar24=normal_array[1].cov(normal_array[3])
    cvar34=normal_array[2].cov(normal_array[3])

    covariance ={
        'f1' : [ var1 , cvar12 , cvar13 , cvar14],
        'f2' : [ cvar12 , var2 , cvar23 , cvar24],
        'f3' : [ cvar13 , cvar23 , var3 , cvar34],
        'f4' : [ cvar14 , cvar24 , cvar34 , var4]
        }
    covariance_matrix = pd.DataFrame(covariance , index=['f1','f2','f3','f4'])
    
    #finding eigenctors and eigenvalues from the coavriance matrix
    eigenvalue,eigenvector = np.linalg.eig(covariance_matrix)
    eigenvalue = np.round(eigenvalue,decimals=4)
    
    eigenvector_matrix = pd.DataFrame(eigenvector)

    #arranging the matrix according to the eigenvalues
    indices = np.argsort(eigenvalue)[::-1]
    #the line below this has no relevance to pca return sorted_eigenvalues is asked thats why generated
    sorted_eigenvalues = np.sort(eigenvalue)[::-1]
    
    
    sorted_eigenvector = eigenvector_matrix.iloc[:,indices]
    #selecting top 2 columns
    transformation_vector = sorted_eigenvector.iloc[:,[0,1]]
    #final_data
    final_data = np.dot( normal_array , transformation_vector )
    final_data = pd.DataFrame(final_data)
        
    # END TODO

    return sorted_eigenvalues, final_data


if __name__ == '__main__':
    init_array = pd.read_csv("pca_data.csv", header = None)
    sorted_eigenvalues, final_data = PCA(init_array)
    np.savetxt("transform.csv", final_data, delimiter = ',')
    for eig in sorted_eigenvalues:
        print(eig)

    # TODO: plot and save a scatter plot of final_data to out.png
    plt.scatter(final_data.iloc[:,0],final_data.iloc[:,1])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Scatter Plot')

    plt.xlim(-15,15)
    plt.ylim(-15,15)

    plt.savefig('out.png')

    plt.show()
    

    # END TODO
