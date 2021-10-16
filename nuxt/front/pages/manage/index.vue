<template>
    <div class="main">
        <Sidebar :position="$route.name.split('-')[0]" />

        <main class="content">
            <article class="wrapper manage">
                <div class="manage_section_title">
                    <h2>Book</h2>
                    <a href="/manage/post/book">Add New</a>
                </div>
                <div class="table">
                    <div class="table_header">
                        <div class="table_header_item table_item">
                            thumbnail
                        </div>
                        <div class="table_header_item table_item">title</div>
                        <div class="table_header_item table_item">
                            description
                        </div>
                        <div class="table_header_item table_item">article</div>
                        <div class="table_header_item table_item">
                            created_at
                        </div>
                        <div class="table_header_item table_item">
                            is_public
                        </div>
                    </div>
                    <nuxt-link
                        class="table_body"
                        :to="{
                            name: 'manage-update-book-id',
                            params: { id: book.id },
                        }"
                        v-for="book in books"
                        :key="book.id"
                    >
                        <div class="table_body_item table_item">
                            <img
                                class="thumbnail"
                                :src="book.thumbnail"
                                alt="thumbnail"
                            />
                        </div>
                        <div class="table_body_item table_item">
                            {{ book.title }}
                        </div>
                        <div class="table_body_item table_item">
                            {{ book.description }}
                        </div>
                        <div class="table_body_item table_item">
                            {{ book.article.length }}
                        </div>
                        <div class="table_body_item table_item">
                            {{ book.created_at }}
                        </div>
                        <div class="table_body_item table_item">
                            {{ book.is_public ? "⭕" : "❌" }}
                        </div>
                    </nuxt-link>
                </div>
                <div class="manage_section_title">
                    <h2>Article</h2>
                    <a href="manage/post/article">Add New</a>
                </div>
                <input type="checkbox" v-model="is_book_toggle" />
                <div class="table">
                    <div class="table_header">
                        <div class="table_header_item table_item">
                            thumbnail
                        </div>
                        <div class="table_header_item table_item">title</div>
                        <div class="table_header_item table_item">
                            description
                        </div>
                        <div class="table_header_item table_item">is_book</div>
                        <div class="table_header_item table_item">
                            created_at
                        </div>
                        <div class="table_header_item table_item">
                            is_public
                        </div>
                    </div>
                    <nuxt-link
                        class="table_body"
                        :to="{
                            name: 'manage-update-article-id',
                            params: { id: article.id },
                        }"
                        v-for="article in article_list(articles)"
                        :key="article.id"
                    >
                        <div class="table_body_item table_item">
                            <img
                                class="thumbnail"
                                :src="article.thumbnail"
                                alt="thumbnail"
                            />
                        </div>
                        <div class="table_body_item table_item">
                            {{ article.title }}
                        </div>
                        <div class="table_body_item table_item">
                            {{ article.description }}
                        </div>
                        <div class="table_body_item table_item">
                            {{ article.is_book ? "⭕" : "❌" }}
                        </div>
                        <div class="table_body_item table_item">
                            {{ article.created_at }}
                        </div>
                        <div class="table_body_item table_item">
                            {{ article.is_public ? "⭕" : "❌" }}
                        </div>
                    </nuxt-link>
                </div>
            </article>
        </main>
    </div>
</template>

<script>
export default {
    data() {
        return {
            books: [],
            articles: [],
            is_book_toggle: true,
        };
    },
    middleware: "auth",
    mounted() {
        this.$axios
            .get("get_book/")
            .then((response) => (this.books = response.data.book));
        this.$axios
            .get("get_article/")
            .then((response) => (this.articles = response.data.article));
    },
    methods: {
        article_list(articles) {
            var new_articles = [];
            if (this.is_book_toggle) {
                for (var i = 0; i < articles.length; i++) {
                    if (!articles[i].is_book) {
                        new_articles.push(articles[i]);
                    }
                }
            } else {
                for (var i = 0; i < articles.length; i++) {
                    new_articles.push(articles[i]);
                }
            }
            return new_articles;
        },
    },
};
</script>

<style lang="scss" scoped>
.manage {
    h2 {
        color: $font-strong;
    }
    .table {
        width: 100%;
        &_header {
            display: flex;
            width: inherit;
            color: $font-color;
            border-bottom: 1px $font-color solid;
        }
        &_body {
            text-decoration: none;
            color: black;
            display: flex;
            width: inherit;
            margin: 10px 0;
            transition: 0.3s ease;
            &:hover {
                transform: translateX(5px);
                transition: 0.3s ease;
            }
            &_item {
                height: 100px;
                font-weight: bold;
                .thumbnail {
                    width: 100px;
                    height: 100px;
                    object-fit: cover;
                    margin: 0;
                    border-radius: 10px;
                }
            }
        }
        &_item {
            margin-left: 10px;
            display: -webkit-box;
            -webkit-line-clamp: 4;
            -webkit-box-orient: vertical;
            overflow: hidden;
            &:nth-child(1) {
                width: 100px;
            }
            &:nth-child(2) {
                width: 200px;
            }
            &:nth-child(3) {
                width: 400px;
            }
            &:nth-child(4) {
                width: 100px;
            }
            &:nth-child(5) {
                width: 120px;
            }
            &:nth-child(6) {
                width: 100px;
            }
        }
    }
    &_section_title {
        display: flex;
        justify-content: space-between;
        a {
            font-weight: bold;
            padding: 10px;
            font-size: 20px;
            color: white;
            border-radius: 5px;
            text-decoration: none;
            vertical-align: bottom;
            height: min-content;
            margin: auto 0;
            background-color: $main-color;
            transition: 0.3s ease;
            border: 2px $main-color solid;
            &:hover {
                background: none;
                color: $main-color;
                transition: 0.3s ease;
                border: 2px $main-color solid;
            }
        }
    }
}
</style>