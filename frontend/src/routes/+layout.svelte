<script>
    // Import our global CSS
    import "$lib/global.css"
    import { onMount } from 'svelte'
    import { themeChange } from 'theme-change'
    import Themes from "./Themes.svelte"

    // NOTE: the element that is using one of the theme attributes must be in the DOM on mount
    onMount(() => {
      themeChange(false)
      // 👆 false parameter is required for svelte
    })
</script>

<div class="navbar bg-base-200">
    <div class="flex-1">
        <a href="/" class="btn btn-ghost normal-case  text-xl"> Stock Replenishment </a>
    </div>
    <div class="flex-none">
        <ul class="menu menu-horizontal p-0">
            <li><a href="/suppliers">Suppliers</a></li>
            <li><a href="/products">Products</a></li>
            <li><a href="/discounts">Discounts</a></li>
            <li> <Themes /> </li>
        </ul>
    </div>
</div>

<slot></slot>