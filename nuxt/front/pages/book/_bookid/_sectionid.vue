<template>
    <div class="main">
        <BookNavbar :nav_list="this.book.article" />
        <main class="content book">
            <article class="wrapper"></article>
        </main>
    </div>
</template>

<script>
export default {
    async asyncData({ $axios, params }) {
        const response = await $axios.get(`get_book/?id=${params.bookid}`);
        return { book: response.data.book[0] };
    },
};
</script>

<style lang="scss" scoped>
</style>