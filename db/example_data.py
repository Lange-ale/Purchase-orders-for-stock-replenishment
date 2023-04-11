example_product_id_1 = { 
    "name": "Philips monitor 17”", 
    "description": "A monitor with a 17” screen, this product is the example given by the problem text"
}
    
example_data = [
    # Supplier 1 has 8pcs in stock at 120€ each, and offers 5% discount 
    # for purchases of minimum 1000€. Min. days to ship order is 5
    {
        "supplier" : {
            "name": "Supplier1",
            "address": "Corso Magenta 1",
            "phone": "+39 1234567890",
            "email": "Supplier1@gmail.com"
        },
        "stock": {
            "quantity": 8,
            "price": 120,
            "shipping_time": 5
        },
        "discount_tot_cost_based": [ {
            "min_tot_cost": 1000,
            "discount_percentage": 5
        } ]
    },
    # Supplier 2 has 15pcs in stock at 128€ each, and offers a 3% discount if you 
    # order >5pcs and 5% discount if you order >10pcs. Min. days to ship order is 7
    {
        "supplier" : {
            "name": "Supplier2",
            "address": "Corso Magenta 2",
            "phone": "+39 1234567891",
            "email": "Supplier2@gmail.com"
        },
        "stock": {
            "quantity": 15,
            "price": 128,
            "shipping_time": 7
        },
        "discount_n_pcs_based": [
            {
                "min_quantity": 5,
                "discount_percentage": 3
            }, 
            {
                "min_quantity": 10,
                "discount_percentage": 5
            }   
        ]
    },
    # Supplier 3 has 23pcs in stock at 129€ each, and offers a discount 
    # of 5% for orders over 1000€. It also offers an additional discount 
    # of 2% for orders placed in september. Min. days to ship order is 4
    {
        "supplier" : {
            "name": "Supplier3",
            "address": "Corso Magenta 3",
            "phone": "+39 1234567892",
            "email": "Supplier3@gmail.com"
        },
        "stock": {
            "quantity": 23,
            "price": 129,
            "shipping_time": 4
        },  
        "discount_tot_cost_based": [ {
            "min_tot_cost": 1000,
            "discount_percentage": 5
        } ],
        "discount_time_based": [ {
            "date_start": "2023-09-01",
            "date_end": "2023-09-30",
            "discount_percentage": 2
        } ]
    }
]