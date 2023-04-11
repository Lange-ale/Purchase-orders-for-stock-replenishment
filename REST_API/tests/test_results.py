right_ans_test_api_get_products_names = [[1, "Philips monitor 17”"]]
right_ans_test_repositoory_get_products_names = [(1, "Philips monitor 17”")]


right_ans_test_get_product_description = {"product_description": "A monitor with a 17” screen, this product is the example given by the problem text"}

right_ans_test_get_quantity_not_available = [
  [ "-1", {
    "product_description": "A monitor with a 17” screen, this product is the example given by the problem text",
  } ]
]

right_ans_test_get_1_product_discounts = [
  [
    "1",
    {
      "discount_n_pcs_based": [],
      "discount_time_based": [],
      "discount_tot_cost_based": [
        {
          "discount_percentage": 5,
          "min_tot_cost": 1000
        }
      ],
      "price": 120,
      "product_description": "A monitor with a 17” screen, this product is the example given by the problem text",
      "quantity": 8,
      "shipping_time": 5,
      "supplier": {
        "address": "Corso Magenta 1",
        "email": "Supplier1@gmail.com",
        "name": "Supplier1",
        "phone": "+39 1234567890"
      }
    }
  ],
  [
    "2",
    {
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
      "product_description": "A monitor with a 17” screen, this product is the example given by the problem text",
      "quantity": 15,
      "shipping_time": 7,
      "supplier": {
        "address": "Corso Magenta 2",
        "email": "Supplier2@gmail.com",
        "name": "Supplier2",
        "phone": "+39 1234567891"
      }
    }
  ],
  [
    "3",
    {
      "discount_n_pcs_based": [],
      "discount_time_based": [
        {
          "date_end": "2023-09-30",
          "date_start": "2023-09-01",
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
      "product_description": "A monitor with a 17” screen, this product is the example given by the problem text",
      "quantity": 23,
      "shipping_time": 4,
      "supplier": {
        "address": "Corso Magenta 3",
        "email": "Supplier3@gmail.com",
        "name": "Supplier3",
        "phone": "+39 1234567892"
      }
    }
  ]
]