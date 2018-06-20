from bs4 import BeautifulSoup
import requests
import csv



def scrape():
    global all_product, product_name, product_link, product_price, product_review, list1
    list1 = []
    for page in range(0, 2):
        page = page + 1
        url = 'https://www.etsy.com/in-en/c/clothing/womens-clothing/dresses' + '?explicit=1&min=&max=25&price_bucket=' + str(page)
        print("URL:")
        print(url)

    #request url and html parser
    req = requests.get(url)

    print("REQUEST WAS SUCCESSFUL")
    print(req.status_code)

    soup = BeautifulSoup(req.text, "html.parser")
    print(soup.prettify())

    #getting list of all the products on the page
    all_product = soup.find_all('div', attrs={'class': 'col-xs-12 pl-xs-1 pl-md-3'})
    print("All Products")
    print(all_product)


    for item in all_product:
            d = {}

            # name & link
            product_name = item.findAll("a", {"class": "title"})
            d['product_name'] = product_name
            print('product_name')
            print(product_name)

            product_link = item.findAll("a", {"class": "href"})
            #product_link = 'https://www.etsy.com' + str(product_name.get('href'))
            d['product_link'] = product_link
            print('product_link')
            print(product_link)

            #price
            product_price = item.findAll("span", {"class": "currency-value"})
            #product_price = product_price.text.replace('\n', "").strip()
            d['product_price'] = product_price
            print('product_price')
            print(product_price)
            #d['Product_Price'] = 'Rp' + product_price

            #review
            product_review = item.findAll("div", {"class": "value"})

            d['product_review'] = product_review
            print('product_review')
            print(product_review)

            try:
                product_review = product_review.text
                d['product_review'] = int(product_review)
                print('product_review')
                print(product_review)

            except:
                d['product_review'] = 0


            print("Length of dictionary:")
            print(len(d))
            print("Appended List:")
            list1.append(d)

            filename = 'etsy_products.csv'
            with open(filename, "w", newline='') as f:
                w = csv.DictWriter(f, ['Product_Name', 'Product_Link', 'Product_Price', 'Product_Review'])
                w.writeheader()
                for d in list1:
                    w.writerow(d)



    return list1

if __name__ == "__main__":
    print(scrape())














