<template>
    <ul class="article_card">
        <li
            class="article_card_item"
            v-for="article in articles"
            :key="article.id"
        >
            <a href="">
                <img :src="article.thumbnail" alt="thumbnail" />
                <h3>{{ article.title }}</h3>
                <p>{{ article.description }}</p>
            </a>
        </li>
    </ul>
</template>

<script>
export default {
    props: ["articles"],
};
</script>

<style lang="scss" scope>
.article_card {
    padding: 0;
    display: flex;
    flex-wrap: wrap;
    &_item {
        list-style: none;
        background-color: $card-background-color;
        width: calc(100% / 4 - 10px * 2);
        height: 350px;
        margin: 10px;
        box-shadow: 2px 2px 6px #bebebe, -2px -2px 6px #ffffff;
        border-radius: $article-card-radius 0;
        img {
            width: 100%;
            height: calc(100% - 200px);
            margin: 0;
            border-top-left-radius: $article-card-radius;
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
            margin: 0.6rem 1.2rem 0;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
            color: $font-color;
        }
        a {
            text-decoration: none;
            display: block;
            width: 100%;
            height: 100%;
        }
    }
}
</style>