import requests
import re

url = "http://books.toscrape.com/index.html"
response = requests.get(url)
text0 = response.text
result = re.findall(r'<div class="side_categories">(.*?)</div>', text0, re.M | re.DOTALL)
# print(result)
category_pat = re.compile(r'<li>\s*<a href="(.*?)">\s*(\w+[\s\w]+\w)\s*?<', re.M | re.DOTALL)
result = re.findall(category_pat, text0)
result.pop(0)
result.pop(0)
# for i in range(len(result)):
#     print(result[i])


url_cat = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
resp = requests.get(url_cat)
text1 = resp.text
text1 = text1.replace("\n", " ")
book_pat = re.compile(r'<h3><a href="(.*?)" title="(.*?)">')
result1 = re.findall(book_pat, text1)
# for i in range(len(result1)):
#     print(result1[i])

# next_page = re.findall(r'<li class="next"><a href="(.*?)">next</a></li>', text1)
# print(next_page)
# i = url_cat.rfind("/")
# url_cat = url_cat[0:i+1] + next_page[0]
# print(url_cat)

book_url = "http://books.toscrape.com/catalogue/sharp-objects_997/index.html"


def book_details(link):
    res = requests.get(link)
    text = res.text
    text = text.replace("\n", " ")
    book_img_link = re.compile(r'<div class="item active">\s*<img src="(.*?)"')
    book_img_link = re.findall(book_img_link, text)
    # print(book_img_link)

    book_description = re.compile(
        r'<div id="product_description" class="sub-header">\s*<h2>Product Description</h2>\s*</div>\s*<p>(.*?)</p>')
    book_description = re.findall(book_description, text)
    # print(book_description)

    book_UPC = re.compile(r'<th>UPC</th><td>(.*?)</td>')
    book_UPC = re.findall(book_UPC, text)
    # print(book_UPC)

    book_price = re.compile(r'<tr>\s*<th>Price (incl. tax)</th><td>(.+?)</td>\s*</tr>')
    book_price = re.findall(book_price, text)
    # print(book_price)

    book_count = re.compile(r'<td>In stock (.*?)</td>')
    book_count = re.findall(book_count, text)
    # print(book_count[0])


book_details(book_url)
