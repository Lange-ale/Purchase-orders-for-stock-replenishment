# Purchase orders for stock replenishment

## Functional analysis

### Narrative

- As a shop seller
  I want to see the list of suppliers of a certain quantity of a product
  so that I can see for each supplier the total cost and shipping days
- As a shop seller
  I want the cheapest is highlighted
  so that I can see the min of all the costs
- As a shop seller
  I want the see all the actual and future offers for each article of the suppliers
  so that I can wait the period in witch the cost is lower
- As a shop seller
  I want update the data of a product in case of changes
  so that I can see always the actual data

### Acceptance criteria

- Given the main page
  When the shop seller fill the form with the product name and the quantity and click on the button "Search"
  Then the page show the list of suppliers with the total cost, shipping days, the list of offers and highlight the cheapest
- Given the page in which update the data of the products
  When the shop seller enter on this page
  Then the page show the list of all the products
- Given the page in which update the data of the products
  When the shop seller click on the button "Add supplier"
  Then the page show the form to add a new supplier
- Given the page in which update the data of the products
  When the shop seller click on the button "Add product"
  Then the page show the form to add a new product
- Given the page in which update the data of the products
  When the shop seller click on the button "Add offer"
  Then the page show the form to add a new offer
