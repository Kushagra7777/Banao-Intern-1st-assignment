import csv
import requests
from bs4 import BeautifulSoup

# Set the URL of the page to scrape
url = "https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar"

listings = []
while len(listings) == 0:
    # Send a GET request to the URL and store the response
    response = requests.get(url)
    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the product listings on the page
    listings = soup.find_all('div', {'data-component-type': 's-search-result'})

# # Create a new CSV file to store the product details
with open('products.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    # Define the column names for the CSV file
    # fieldnames = ['Product Name', 'Price', 'Rating', 'Seller Name']
    fieldnames = ['Product Name', 'Price', 'Rating']

    # Create a CSV writer object
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the column names to the CSV file
    writer.writeheader()

    # Loop through each listing and extract the product details
    for listing in listings:
        # Check if the listing is not out of stock
        if not listing.find('span', {'class': 'a-size-base', 'aria-label': 'Currently unavailable'}):
            # Extract the product name
            product_name = listing.find('span', {'class': 'a-size-base-plus'}).text.strip()

            # Extract the product price
            product_price = listing.find('span', {'class': 'a-price-whole'}).text.strip()

            # Extract the product rating
            product_rating = listing.find('span', {'class': 'a-icon-alt'}).text.strip()

            # Extract the seller name
            # product_seller = listing.find('span', {'class': 'a-size-base', 'aria-label': 'by'}).text.strip()

            # Write the product details to the CSV file
            writer.writerow({
                'Product Name': product_name,
                'Price': product_price,
                'Rating': product_rating,
                # 'Seller Name': product_seller
            })
