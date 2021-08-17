<template>
    <div class="main">
        <Sidebar :position="$route.name.split('-')[0]" />
        <main class="content">
            <article class="wrapper article">
                <ArticleCard :articles="articles" />
            </article>
        </main>
    </div>
</template>

<script>
export default {
    data() {
        return {
            articles: [],
        };
    },
    mounted() {
        this.$axios
            .get("get_article/")
            .then((response) => (this.articles = response.data.article));
    },
};
</script>

<style lang="scss" scoped>
.article {
}
</style>