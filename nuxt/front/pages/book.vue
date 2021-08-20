<template>
    <div class="main">
        <Sidebar :position="$route.name.split('-')[0]" />
        <main class="content">
            <article class="wrapper book">
                <BookCard :books="books" />
            </article>
        </main>
    </div>
</template>

<script>
export default {
    data() {
        return {
            books: [],
        };
    },
    mounted() {
        this.$axios
            .get("get_book/")
            .then((response) => (this.books = response.data.book));
    },
};
</script>

<style lang="scss" scoped>
.book {
}
</style>