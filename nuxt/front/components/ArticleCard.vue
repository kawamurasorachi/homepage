<template>
    <ul class="article_card">
        <a
            class="article_card_item"
            v-for="article in articles"
            :key="article.id"
            href=""
        >
            <li>
                <div class="image_wrapper">
                    <img :src="article.thumbnail" alt="thumbnail" />
                </div>
                <h3>{{ article.title }}</h3>
                <p>{{ article.description }}</p>
                <span class="created_at">
                    {{ article.created_at.split("-")[0] }}<br />
                    {{ article.created_at.split("-")[1] }}/{{
                        article.created_at.split("-")[2]
                    }}<br />
                </span>
            </li>
        </a>
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
        overflow: hidden;
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
            width: 60px;
            line-height: 30px;
            text-align: center;
            height: 60px;
            background-color: $main-color;
            top: 0;
            left: 0;
            color: $card-background-color;
            border-top-left-radius: $article-card-radius;
            font-weight: bold;
        }
    }
}
</style>