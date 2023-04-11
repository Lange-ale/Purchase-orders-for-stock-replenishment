<script>
    import { quantity_selected, date_selected, id_product_selected, 
             product_description, stocks, lowest_price } from "../store.js"
    import { SERVER_IP } from "../conf.js"
    import { onMount } from "svelte"
    
    function set_quantity_selected() { // set the quantity selected when the user changes it in the text bar
        let q = parseInt($quantity_selected) // convert the quantity to an integer
        if (isNaN(q) || q < 1) // if the quantity is not a number or is less than 1 set it to 1
          q = 1
        quantity_selected.set(q) 
        update_stocks()
    }

    function increment_quantity_selected() {
        quantity_selected.update(n => n + 1) // increment the quantity selected
        update_stocks()
    }

    function decrement_quantity_selected() {
        if ($quantity_selected > 1) {
            quantity_selected.update(n => n - 1) // decrement the quantity selected
            update_stocks()
        }
    }

    function update_stocks() { // update the stocks when something changes
        if ($id_product_selected == -1) return // if no product is selected do nothing
        // fetch the stocks from the server
        fetch( SERVER_IP + "/stocks/" + $id_product_selected + "/" + $quantity_selected)
            .then(response => response.json()) // convert the response to json
            .then(data => {
                // set the description of the product in the part above the table
                product_description.set(data[0][1].product_description)

                stocks.set(data) // set the data received in stocks
                let actual_lowest_price = null // the actual lowest price
                $stocks.forEach((stock_id_and_values) => { // for each stock calculate the final price
                    let stock = stock_id_and_values[1] 
                    let price = stock.price * $quantity_selected // the final price 
                    let max_discount = 0 // the max discount that can be applied to the price
                    let d_n_pcs = stock.discount_n_pcs_based 
                    let d_tot_cost = stock.discount_tot_cost_based
                    let d_time = stock.discount_time_based
                    if (d_n_pcs.length > 0){ // if there are discounts based on the quantity
                      for (let i = 0; i < d_n_pcs.length; i++) { // for each discount based on the quantity
                          if ($quantity_selected >= d_n_pcs[i].min_quantity &&  // if the quantity is enough
                              d_n_pcs[i].discount_percentage > max_discount)    // and the discount is the max
                              max_discount = d_n_pcs[i].discount_percentage     // then set the max discount
                      }
                      price = price - price * max_discount / 100 // apply the discount
                    }
                    if (d_tot_cost.length > 0){ // if there are discounts based on the total cost
                      max_discount = 0  
                      for (let i = 0; i < d_tot_cost.length; i++) { // for each discount based on the total cost
                          if (price >= d_tot_cost[i].min_tot_cost &&            // if the total cost is enough
                              d_tot_cost[i].discount_percentage > max_discount) // and the discount is the max
                              max_discount = d_tot_cost[i].discount_percentage // then set the max discount
                      }
                      price = price - price * max_discount / 100 // apply the discount
                    }
                    if (d_time.length > 0){ // if there are discounts based on the time
                      max_discount = 0
                      for (let i = 0; i < d_time.length; i++) { // for each discount based on the time
                          if (d_time[i].date_start <= $date_selected &&     
                              $date_selected <= d_time[i].date_end &&       // if the date selected is in the range
                              d_time[i].discount_percentage > max_discount) // and the discount is the max
                              max_discount = d_time[i].discount_percentage  // then set the max discount
                      }
                      price = price - price * max_discount / 100 // apply the discount
                    }
                    price = price.toFixed(2) // round the price to cents
                    stock.final_price = price // set the final price
                    if (actual_lowest_price == null || price < actual_lowest_price) // if the price is the lowest
                        actual_lowest_price = price // set it as the lowest price
                })
                lowest_price.set(actual_lowest_price) // set the lowest price
            })
    }

    let product_search = "" // the text inserted in the search bar
    let product_selected = "Select a product" // the name of the product selected
    let products = [] // the list of the products names

    onMount(async () => { // when the page is loaded
        await fetch( SERVER_IP + "/products_names") // fetch the products names from the server
            .then(response_products_names => response_products_names.json()) // convert the response to json
            .then(data_product_names => { products = data_product_names }) // set the data received in products
    })
</script>

<main class="p-4 flex items-center">
  <div class="flex-auto input-group max-w-max p-2">
      <button class="btn btn-primary" on:click="{decrement_quantity_selected}">-</button>
      <input type="text" class="text-center" bind:value={$quantity_selected} on:change="{set_quantity_selected}" />
      <button class="btn btn-primary" on:click="{increment_quantity_selected}">+</button>
  </div>

  <div>
    <input type="date" class="input input-bordered" bind:value={$date_selected} on:change="{update_stocks}" />
  </div>

  <div class="flex-auto dropdown dropdown-bottom dropdown-start">
    <label tabindex="0" class="btn btn-primary m-1 gap-2"> 
      {product_selected}
    </label>
    <ul tabindex="0" class="dropdown-content menu p-2 shadow bg-base-300 rounded-box">
      <input type="search" class="input input-bordered" placeholder="Search..." bind:value={product_search} />
      <div class="overflow-y-scroll h-64">
        {#each products as product}
          {#if product_search.toLowerCase().split(" ")
                .every(word => product[1].toLowerCase().includes(word))}
            <li>
              <a class="" 
                 on:click="{ () =>
                    { 
                      product_selected = product[1]
                      id_product_selected.set(product[0])
                      update_stocks()
                    }
                  }">
                  {product[1]} 
              </a>
            </li>
          {/if}
        {/each}
      </div>
    </ul>
  </div>

</main>