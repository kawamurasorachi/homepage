<template>
    <div class="navbar">
        <ul class="navbar_list">
            <a class="navbar_item" :href="`/book/${$route.params.bookid}`">
                <li>TOP</li>
            </a>
            <nuxt-link
                class="navbar_item"
                v-for="(nav, index) in nav_list"
                :to="{
                    name: 'book-bookid-sectionid',
                    params: {
                        bookid: $route.params.bookid,
                        sectionid: index + 1,
                    },
                }"
                :key="nav.pk"
            >
                <li>{{ nav.fields.title }}</li>
            </nuxt-link>
        </ul>
    </div>
</template>

<script>
export default {
    props: ["nav_list"],
};
</script>

<style lang="scss" scope>
.navbar {
    position: sticky;
    top: 0;
    width: $navbar-width;
    height: 100vh;
    padding: 0 20px;
    background-color: white;
    font-family: "Roboto Mono", monospace;
    &_list {
        list-style: none;
        padding: 0;
    }
    &_item {
        width: 100%;
        font-size: 22px;
        height: 40px;
        line-height: 40px;
        display: -webkit-box;
        -webkit-line-clamp: 1;
        -webkit-box-orient: vertical;
        overflow: hidden;
        color: $font-strong;
        text-decoration: none;
    }
}
</style>
