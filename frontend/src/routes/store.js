import { writable } from 'svelte/store'

export const quantity_selected = writable(1)
export const date_selected = writable(new Date().toJSON().slice(0, 10))
export const id_product_selected = writable(-1)
export const product_description = writable("")
export const stocks = writable([])
export const lowest_price = writable(0)

