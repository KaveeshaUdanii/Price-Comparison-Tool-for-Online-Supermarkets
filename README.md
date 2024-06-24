### Price Comparison Tool for Online Supermarkets

This Python script allows users to compare prices of specific products between two online supermarkets, LaughSuper and Glomark. The script fetches and extracts the current prices from the respective websites and determines which option offers the better price at the time of execution.

#### Usage:
1. Specify the products from LaughSuper and Glomark that you want to compare.
2. Run the script to fetch the latest prices and get a recommendation on which option is more economical.

#### Requirements:
- Python 3.x
- Beautiful Soup (for web scraping)
- Requests (for HTTP requests)

#### Example:
```python
from compare_prices import compare_prices

product_laughs = 'coconut'
product_glomark = 'coconut'

cheaper_option = compare_prices(product_laughs, product_glomark)
print(f"For {product_laughs}, {cheaper_option} offers a better price currently.")
```
