<template>
    <div class="main">
        <Sidebar :position="$route.name.split('-')[0]" />
        <main class="content articles">
            <article class="wrapper">
                <div class="articles_search">
                    <img src="~/assets/image/search.svg" alt="" />
                    <input
                        name="search"
                        type="text"
                        placeholder="記事を検索"
                        v-model="search_text"
                    />
                </div>
                <div class="tags">
                    <a
                        class="tag"
                        :href="`?tags=${tag.slug}`"
                        v-for="tag in tags"
                        :key="tag.id"
                    >
                        {{ tag.name }}
                    </a>
                </div>
                <ArticleCard :articles="get_articles(search_text)" />
            </article>
        </main>
    </div>
</template>

<script>
export default {
    data() {
        return {
            articles: [],
            tags: [],
            search_text: "",
        };
    },
    mounted() {
        this.$axios
            .get(
                `get_article_not_book/?tags=${
                    this.$route.query.tags ? this.$route.query.tags : ""
                }`
            )
            .then((response) => (this.articles = response.data.article));
        this.$axios
            .get("get_tags/")
            .then((response) => (this.tags = response.data.tags));
    },
    methods: {
        get_articles(search_text) {
            var new_articles = this.articles.filter(function (item, index) {
                if (
                    item.tags.find(
                        (element) => element.indexOf(search_text) >= 0
                    ) ||
                    item.title.indexOf(search_text) >= 0 ||
                    item.description.indexOf(search_text) >= 0 ||
                    item.content.indexOf(search_text) >= 0
                )
                    return true;
            });
            return new_articles;
        },
    },
};
</script>

<style lang="scss" scoped>
.articles {
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
    .tags {
        display: flex;
        flex-wrap: wrap;
        margin: 30px 0;
        .tag {
            text-decoration: none;
            display: block;
            margin: 5px;
            padding: 5px 15px;
            color: $card-background-color;
            background-color: $main-color;
            border-radius: 30px;
            border: 2px $main-color solid;
            font-weight: bold;
            &:hover {
                background-color: $card-background-color;
                color: $main-color;
            }
        }
    }
}
</style>