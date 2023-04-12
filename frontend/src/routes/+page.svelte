<script>
    import Input from "./Home/Input.svelte"
    import ProductDescription from "./Home/ProductDescription.svelte"
    import Table from "./Home/Table.svelte"
    import { id_product_selected, stocks } from "./store.js"
</script>

<main>
    <Input />
    {#if $id_product_selected != -1} <!-- if a product is selected -->
        <ProductDescription />
        {#if $stocks.length > 0 && $stocks[0][0] == -1} <!-- if this quantity of this product is not available -->
            <div class="alert alert-error">
                <div class="flex-1">
                    <label class="cursor-pointer select-none"> 
                        <span class="text-xl font-bold">Error</span>
                        <span class="text-gray-600 text-xl">No stock available for this quantity</span>
                    </label>
                </div>
            </div>
        {:else} <!-- if this quantity of this product is available display the table -->
            <Table />
        {/if}
    {/if}

</main>