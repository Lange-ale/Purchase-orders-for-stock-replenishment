import { writable } from 'svelte/store'

// quantity of products selected
export const quantity_selected = writable(1) 
// date selected, default is today
export const date_selected = writable(new Date().toJSON().slice(0, 10)) 
// id in the database of the product selected
export const id_product_selected = writable(-1)
// description of the product selected
export const product_description = writable("")
// stocks of the product sold by the supplier
export const stocks = writable([])
// lowest total price among all the suppliers
export const lowest_price = writable(0)

