import json
import numpy as np
import matplotlib.pyplot as plt

def inv_transform(distribution: str, num_samples: int, lamda:float,**kwargs) -> list:
    """ populate the 'samples' list from the desired distribution """

    samples = []
    # TODO: first generate random numbers from the uniform distribution
    for i in range(num_samples):
        random_number = np.random.rand()
        inverted_number=((-1.0/lamda)*(np.log(1-random_number)))
        rounded_number=round(inverted_number,4)
        samples.append(rounded_number)
   
    # END TODO
    return samples


if __name__ == "__main__":
    np.random.seed(42)

    distribution="exponential"
    file_name = "q1_" + distribution + ".json"
    args = json.load(open(file_name, "r"))
    samples = inv_transform(**args)
        
    with open("q1_output_" + distribution + ".json", "w") as file:
        json.dump(samples, file)

    # TODO: plot and save the histogram to "q1_" + distribution + ".png"
    plt.hist(samples, bins=250)
    plt.title('Inverse Transform Sampling - Exponential Distribution')
    plt.xlabel('Samples')
    plt.ylabel('Frequency')
    plt.savefig("q1_" + distribution + ".png")
    plt.show()

    # END TODO
