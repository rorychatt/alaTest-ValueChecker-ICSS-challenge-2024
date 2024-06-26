# alaTest-ValueChecker-ICSS-challenge-2024

# Before everything else...

I've been lately working a lot with ML algorhitms and thus decided to also use ipynb for convenience.
While there is definetly a better way to write more structured code in .py files, in this case .ipynb allows for better explanation of each block, running each block separately and hands more possibilities to manipulate variables. For production, this is definetly not the best choice, but I will format the code such that a user can basically copy all the code cells into a new .py file and get production ready code without extra comments. Really, the code should be self-explanatory with all the typings included.

# Telephone Routing

This project implements a telephone call routing system to determine the cheapest operator for a given phone number based on provided price lists.

## Description

The program handles multiple price lists from different operators and calculates which operator is the cheapest for a specific phone number. It uses the longest matching prefix to determine the price. If an operator's price list does not include a certain prefix, that operator cannot be used to dial numbers starting with that prefix.

Do not edit the `tests_dataset.py` file unless you want to edit tests in the `telephone_routing.ipynb` file.

## How to Use
   
1. **Run the Program:**
   Run the `telephone_routing.ipynb` Jupyter notebook to test and find the cheapest operator. You can also generate `telephone_routing.py` script if you have jupyter package installed and uncomment last block of code.

2. **Main Execution:**
   Use the `telephone_routing.py` script for command-line execution.

## Running Unit Tests

Unit tests are included in the `telephone_routing.ipynb` and `telephone_routing.py`. They verify the correctness of the `find_cheapest_operator` function.

## Important Notes

- **Do not copy the code:** This code is intended for educational purposes. Please do not copy it for production use without proper understanding / do not copy it for your own submissions
- **Author:** Mikael Rinne

## Other code / CV

Have a look at my other recent public repos, like:

- [Estomania](https://github.com/rorychatt/estomania)
- [Estomania Server](https://github.com/rorychatt/estomania-server)
- [SpaceCorps2](https://github.com/rorychatt/SpaceCorps2)
- [TensorFlow GPU Example](https://github.com/rorychatt/tensorflow-gpu-example)
- [RoryCraft](https://github.com/rorychatt/rorycraft)

In case CV is needed... 

- [CV - Mikael Rinne](https://docs.google.com/document/d/10pKjKs0SLbWi3wr7NJZ9vk5cpPOQL-SC/edit?usp=sharing&ouid=111974498764303832021&rtpof=true&sd=true)


## Contact

For any questions regarding this project, please contact Mikael Rinne pavel.rinne@gmail.com

