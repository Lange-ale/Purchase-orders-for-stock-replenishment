<script>
    import { onMount } from "svelte";
    import { id_product_selected } from "../store.js";
    import { SERVER_IP } from "../conf.js";

    let product_description = "";

    $: if ($id_product_selected > -1) {
        fetch(SERVER_IP + "/product_description/" + $id_product_selected)
            .then(response => response.json())
            .then(data => {
                product_description = data["description"];
            });
    }
    
</script>

<main>
    <div class="flex text-xl
    ">
        <p class="flex-none p-2">
            Description: 
        </p>
        <p class="flex-1 p-2">
          {product_description}
        </p>
    </div>
</main>