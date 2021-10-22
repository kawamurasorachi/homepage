<template>
    <div class="main">
        <Sidebar :position="$route.name.split('-')[0]" />
        <main class="content">
            <div
                class="article_top"
                :style="`background-image:url(${article.thumbnail});`"
            ></div>
            <article class="article">
                <div
                    class="article_thumbnail"
                    :style="`background-image:url(${article.thumbnail});`"
                ></div>
                <h1>
                    {{ article.title }}
                </h1>
                <div class="meta_container">
                    <p class="date_container">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            height="24px"
                            viewBox="0 0 24 24"
                            width="24px"
                        >
                            <path d="M0 0h24v24H0V0z" fill="none" />
                            <path
                                d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zm0-12H5V6h14v2zm-7 5h5v5h-5z"
                            />
                        </svg>
                        <span>
                            {{ article.created_at }}
                        </span>
                    </p>
                    <div class="tag_container">
                        <span
                            class="tag_item"
                            v-for="tag in article.tags"
                            :key="tag"
                        >
                            {{ tag }}
                        </span>
                    </div>
                </div>
                <div
                    class="article_content"
                    v-html="$md.render(article.content)"
                ></div>
            </article>
        </main>
    </div>
</template>

<script>
export default {
    data() {
        return {
            is_sidebar: false,
            topURL: process.env.topURL,
        };
    },
    head() {
        return {
            title: this.article.title,
            meta: [
                {
                    hid: "description",
                    name: "description",
                    content: this.article.description,
                },
                {
                    hid: "keywords",
                    name: "keywords",
                    content: this.article.tags,
                },
                {
                    hid: "og:description",
                    property: "og:description",
                    content: this.article.description,
                },
                {
                    hid: "og:title",
                    property: "og:title",
                    content: this.article.title,
                },
                {
                    hid: "og:image",
                    property: "og:image",
                    content: this.topURL + this.article.thumbnail,
                },
            ],
        };
    },
    async asyncData({ $axios, params }) {
        const response = await $axios.get(`get_article/?id=${params.id}`);
        return { article: response.data.article[0] };
    },
};
</script>


<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Source+Code+Pro&display=swap");
.article {
    transform: translateY(-15vh);
    width: calc(720px + 40px * 2);
    margin: 0 calc((100% - (720px + 40px * 2)) / 2);
    &_top {
        width: 100%;
        height: 20vh;
        background-size: cover;
        background-position: center;
        position: relative;
        z-index: 0;
        overflow: hidden;
        &:before {
            content: "";
            background: inherit;
            -webkit-filter: blur(5px);
            -moz-filter: blur(5px);
            -o-filter: blur(5px);
            -ms-filter: blur(5px);
            filter: blur(5px);
            position: absolute;
            top: -5px;
            left: -5px;
            right: -5px;
            bottom: -5px;
            z-index: -1;
        }
    }
    &_thumbnail {
        width: 100%;
        height: 300px;
        background-size: cover;
        background-position: center;
        position: relative;
        z-index: 0;
        overflow: hidden;
        border-radius: 20px;
        box-shadow: 2px 2px 6px #bebebe, -2px -2px 6px #ffffff;
    }
    h1 {
        font-size: 30px;
    }
    .meta_container {
        display: flex;
        justify-content: space-between;
        .date_container {
            display: flex;
            color: $font-color;
            margin: 0;
            svg {
                fill: $font-color;
                margin-top: auto;
            }
            span {
                height: min-content;
                margin-left: 5px;
                margin-top: auto;
            }
        }
        .tag {
            &_item {
                color: $card-background-color;
                background-color: $main-color;
                border-radius: 15px;
                padding: 5px 10px;
                margin: 0 3px;
                font-family: "Roboto Mono", monospace;
            }
            &_container {
                display: flex;
                flex-wrap: wrap;
                margin: 0 0.3rem;
            }
        }
    }
}
</style>