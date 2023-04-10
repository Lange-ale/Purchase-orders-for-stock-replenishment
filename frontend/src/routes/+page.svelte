<script>
  import Input from "./Home/Input.svelte";
  import ProductDescription from "./Home/ProductDescription.svelte";
  //import Table from "./Home/Table.svelte";
  import { id_product_selected, quantity_selected } from "./store.js";
</script>

<main>
  <Input />
  {#if $id_product_selected > -1}
    <ProductDescription />
    <!-- <Table /> -->
  {/if}
</main>