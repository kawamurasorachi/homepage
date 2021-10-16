<template>
    <div class="main">
        <Sidebar :position="$route.name.split('-')[0]" />
        <main class="content books">
            <article class="wrapper">
                <div class="books_search">
                    <img src="~/assets/image/search.svg" alt="" />
                    <input
                        name="search"
                        type="text"
                        placeholder="記事を検索"
                        v-model="search_text"
                    />
                </div>
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
            search_text: "",
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
.books {
    margin-top: 10vh;
    &_search {
        display: flex;
        position: relative;
        img {
            position: absolute;
            left: calc(10% + 10px);
            top: 0;
            bottom: 0;
            width: 40px;
            height: 40px;
            margin: auto;
        }
        input[type="text"] {
            margin: auto 10%;
            height: 30px;
            border: none;
            background: none;
            border: 2px $font-color solid;
            width: calc(100% - 20% - 20px);
            color: $font-strong;
            font-size: 20px;
            padding: 10px;
            padding-left: calc(10px + 40px + 10px);
            border-radius: 10px;
            font-family: "Roboto Mono", monospace;
            outline: none;
            position: relative;
        }
    }
}
</style>