<script>
    import { stocks, lowest_price } from "../store.js"
</script>

<main> 
    <div class="overflow-x-auto">
        <table class="table w-full">
            <thead>
                <tr>
                    <th>Supplier</th>
                    <th>Price</th>
                    <th>Availability</th>
                    <th>Shipping Time</th>
                    <th>Discounts on quantity</th>
                    <th>Discount on total</th>
                    <th>Discount in period</th>
                    <th>Final Price</th>
                </tr>
            </thead>
            <tbody>
                {#each $stocks as [id, stock] }
                    <tr class="{stock.final_price == $lowest_price ? 'active' : ''}">
                        <td> {stock.supplier.name} <br> {stock.supplier.email} <br> 
                          {stock.supplier.phone} <br> {stock.supplier.address} 
                      </td>
                        <td> {stock.price} </td>
                        <td> {stock.quantity} </td>
                        <td> {stock.shipping_time} </td>
                        <td> 
                          <ul class="list-disc">
                              {#each stock.discount_n_pcs_based as discount}
                                  <li> {discount.discount_percentage}% if bought {discount.min_quantity} </li>
                              {/each}
                          </ul>
                      </td>
                        <td> 
                        <ul class="list-disc">
                          {#each stock.discount_tot_cost_based as discount}
                              <li> {discount.discount_percentage}% on total with {discount.min_tot_cost}€ </li>
                          {/each}
                        </ul>
                      </td>
                        <td> 
                          <ul class="list-disc">
                              {#each stock.discount_time_based as discount}
                                  <li> {discount.discount_percentage}% from {discount.date_start} to {discount.date_end} </li>
                              {/each}
                          </ul>
                      </td>
                        <td> {stock.final_price} </td>
                  </tr>
              {/each}
          </tbody>
        </table>
    </div>
</main>