right_ans_test_api_get_products_names = [[1, "Philips monitor 17”"]]
right_ans_test_repositoory_get_products_names = [(1, "Philips monitor 17”")]


right_ans_test_get_product_description = {"description": "A monitor with a 17” screen"}

right_ans_test_get_product_discounts = {
  "1": {
    "discount_n_pcs_based": [],
    "discount_time_based": [],
    "discount_tot_cost_based": [
      {
        "discount_percentage": 5,
        "min_tot_cost": 1000
      }
    ],
    "price": 120,
    "quantity": 8,
    "shipping_time": 5,
    "supplier": {
      "address": "Corso Magenta 1",
      "email": "Supplier1@gmail.com",
      "name": "Supplier1",
      "phone": "+39 1234567890"
    }
  },
  "2": {
    "discount_n_pcs_based": [
      {
        "discount_percentage": 5,
        "min_quantity": 10
      },
      {
        "discount_percentage": 3,
        "min_quantity": 5
      }
    ],
    "discount_time_based": [],
    "discount_tot_cost_based": [],
    "price": 128,
    "quantity": 15,
    "shipping_time": 7,
    "supplier": {
      "address": "Corso Magenta 2",
      "email": "Supplier2@gmail.com",
      "name": "Supplier2",
      "phone": "+39 1234567891"
    }
  },
  "3": {
    "discount_n_pcs_based": [],
    "discount_time_based": [
      {
        "date_end": "2020-09-30",
        "date_start": "2020-09-01",
        "discount_percentage": 2
      }
    ],
    "discount_tot_cost_based": [
      {
        "discount_percentage": 5,
        "min_tot_cost": 1000
      }
    ],
    "price": 129,
    "quantity": 23,
    "shipping_time": 4,
    "supplier": {
      "address": "Corso Magenta 3",
      "email": "Supplier3@gmail.com",
      "name": "Supplier3",
      "phone": "+39 1234567892"
    }
  }
}