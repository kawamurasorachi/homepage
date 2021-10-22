<template>
    <ul class="article_card">
        <nuxt-link
            class="article_card_item"
            :to="{
                name: 'articles-id',
                params: { id: article.id },
            }"
            v-for="article in articles.filter((book) => book.is_public)"
            :key="article.id"
        >
            <li>
                <div class="image_wrapper">
                    <img :src="article.thumbnail" alt="thumbnail" />
                </div>
                <div class="tag_container">
                    <span
                        class="tag_item"
                        v-for="tag in article.tags"
                        :key="tag"
                    >
                        {{ tag }}
                    </span>
                </div>
                <h3>{{ article.title }}</h3>
                <p>{{ article.description }}</p>
                <span class="created_at">
                    {{ article.created_at.split("-")[1] }}/{{
                        article.created_at.split("-")[2]
                    }}
                </span>
            </li>
        </nuxt-link>
    </ul>
</template>

<script>
export default {
    props: ["articles"],
};
</script>

<style lang="scss" scope>
@import url("https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100;300&display=swap");
.article_card {
    padding: 0;
    display: flex;
    flex-wrap: wrap;
    &_item {
        display: block;
        list-style: none;
        background-color: $card-background-color;
        width: calc(100% / 4 - 10px * 2);
        height: 360px;
        margin: 10px;
        box-shadow: 2px 2px 6px #bebebe, -2px -2px 6px #ffffff;
        border-radius: $article-card-radius;
        position: relative;
        text-decoration: none;
        &:hover img {
            transform: scale(1.05, 1.05);
            transition: 0.3s ease;
        }
        .image_wrapper {
            width: 100%;
            height: 150px;
            overflow: hidden;
        }
        img {
            transition: 0.3s ease;
            width: 100%;
            height: 150px;
            object-fit: cover;
            margin: 0;
        }
        h3 {
            margin: 0.6rem 1.2rem 0;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
            color: $font-strong;
        }
        p {
            margin: 0.3rem 1.2rem 0;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
            color: $font-color;
        }
        .created_at {
            position: absolute;
            width: 65px;
            padding-right: 5px;
            height: 30px;
            transform: translateX(-10px);
            line-height: 30px;
            text-align: right;
            background-color: $main-color;
            top: 10px;
            left: 0;
            color: $card-background-color;
            font-weight: bold;
            font-family: "Roboto Mono", monospace;
            &:before {
                content: "";
                top: 30px;
                left: 0;
                position: absolute;
                width: 0;
                height: 0;
                border-style: solid;
                border-width: 0 10px 5px 0;
                border-color: transparent $main-color-strong transparent
                    transparent;
            }
        }
        .tag {
            &_item {
                color: $card-background-color;
                font-family: "Roboto Mono", monospace;
                background-color: $main-color;
                border-radius: 15px;
                padding: 2px 7px;
                margin: 0 3px;
            }
            &_container {
                display: flex;
                flex-wrap: wrap;
                margin: 0.3rem 0.3rem 0;
            }
        }
    }
}
</style>