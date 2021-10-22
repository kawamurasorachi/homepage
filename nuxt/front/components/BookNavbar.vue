<template>
    <div class="navbar">
        <ul class="navbar_list">
            <nuxt-link
                class="navbar_item"
                :href="`/book/${$route.params.bookid}`"
                :to="{
                    name: 'book-bookid',
                    params: {
                        bookid: $route.params.bookid,
                    },
                }"
            >
                <li>TOP</li>
            </nuxt-link>
            <nuxt-link
                :class="
                    `navbar_item ` +
                    (index + 1 == $route.params.sectionid ? `position` : ``)
                "
                v-for="(nav, index) in nav_list"
                :to="{
                    name: 'books-bookid-sectionid',
                    params: {
                        bookid: $route.params.bookid,
                        sectionid: index + 1,
                    },
                }"
                :key="nav.pk"
            >
                <li>
                    {{ nav.title }}
                </li>
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
    min-width: $navbar-width;
    max-width: $navbar-width;
    height: 100vh;
    overflow-y: scroll;
    padding: 0 10px;
    z-index: 1;
    &_list {
        list-style: none;
        padding: 0;
    }
    &_item {
        width: calc(100% - 10px * 2);
        font-size: 22px;
        height: 40px;
        line-height: 40px;
        padding: 5px;
        margin: 10px 0;
        display: -webkit-box;
        -webkit-line-clamp: 1;
        -webkit-box-orient: vertical;
        overflow: hidden;
        color: $font-color;
        text-decoration: none;
        &[aria-current="page"] {
            background-color: rgba(165, 165, 165, 0.7);
            color: $card-background-color;
            border-radius: 5px;
        }
    }
}
</style>
