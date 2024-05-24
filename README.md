# alaTest-ValueChecker-ICSS-challenge-2024

# Telephone Routing

This project implements a telephone call routing system to determine the cheapest operator for a given phone number based on provided price lists.

## Description

The program handles multiple price lists from different operators and calculates which operator is the cheapest for a specific phone number. It uses the longest matching prefix to determine the price. If an operator's price list does not include a certain prefix, that operator cannot be used to dial numbers starting with that prefix.

## How to Use

1. **Add Price Lists:**
   Define the price lists in the `sample_data.py` file.
   
2. **Run the Program:**
   Run the `telephone_routing.ipynb` Jupyter notebook to test and find the cheapest operator.

3. **Main Execution:**
   Use the `telephone_routing.py` script for command-line execution.

## Running Unit Tests

Unit tests are included in the `telephone_routing.ipynb` and `telephone_routing.py`. They verify the correctness of the `find_cheapest_operator` function.

## Important Notes

- **Do not copy the code:** This code is intended for educational purposes. Please do not copy it for production use without proper understanding / do not copy it for your own submissions
- **Author:** Mikael Rinne

## Contact

For any questions regarding this project, please contact Mikael Rinne.

