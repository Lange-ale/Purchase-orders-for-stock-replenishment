<script>
    import { product_description } from "../store.js"
</script>

<main>
    <div class="flex text-xl">
        <p class="flex-none p-2">
            Description: 
        </p>
        <p class="flex-1 p-2">
          {$product_description}
        </p>
    </div>
</main>