<script>
    import { quantity_selected, id_product_selected} from "../store.js"
    import { SERVER_IP } from "../conf.js"
    import { onMount } from "svelte"
    
    function increment_quantity_selected() {
        quantity_selected.update(q => q + 1)
    }

    function decrement_quantity_selected() {
        quantity_selected.update(q => q > 1 ? q - 1 : 1)
    }

    let product_search = ""
    let product_selected = "Select a product"
    let products = []

    onMount(async () => {
        await fetch( SERVER_IP + "/products_names") 
            .then(response => response.json())
            .then(data => { products = data })
    })
</script>

<main class="p-4 flex items-center">

  <div class="flex-auto max-w-max">
    <button class="btn btn-primary"> Search </button>
  </div>

  <div class="flex-auto input-group max-w-max p-2">
      <button class="btn btn-primary" on:click="{decrement_quantity_selected}">-</button>
      <input type="text" class="text-center" bind:value={$quantity_selected} />
      <button class="btn btn-primary" on:click="{increment_quantity_selected}">+</button>
  </div>


  <div class="flex-auto dropdown dropdown-bottom dropdown-start w-1/2">
    <label tabindex="0" class="btn btn-primary m-1 gap-2"> 
      {product_selected}
    </label>
    <ul tabindex="0" class="dropdown-content menu p-2 shadow bg-base-100 rounded-box">
      <input type="search" class="input input-bordered" placeholder="Search..." bind:value={product_search} />
      <div class="overflow-y-scroll h-64">
        {#each products as product}
          {#if product_search.toLowerCase().split(" ")
                .every(word => product[1].toLowerCase().includes(word))}
            <li>
              <a class="" on:click="{ () => { product_selected = product[1]
                                              id_product_selected.set(product[0]) } 
                                    }"> {product[1]} </a>
            </li>
          {/if}
        {/each}
      </div>
    </ul>
  </div>

</main>