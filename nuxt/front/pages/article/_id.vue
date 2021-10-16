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
                <div class="toc"></div>
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
            topURL: process.env.topURL
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
    &_content {
        background-color: $card-background-color;
        border-radius: 5px;
        margin-top: 30px;
        padding: 40px;
        h2 {
            font-size: 1.8rem;
            position: relative;
            &:before {
                content: "";
                position: absolute;
                left: -15px;
                width: 5px;
                height: 100%;
                background-color: $main-color;
            }
        }
        h3 {
            border-bottom: 0.1rem $font-color solid;
            font-size: 1.5rem;
        }
        pre {
            font-size: 1.1rem;
        }
        code {
            font-family: "Source Code Pro", monospace;
            border-radius: 3px;
            padding: 1.1rem;
        }
        img {
            margin: 0 10%;
            width: 80%;
            object-fit: cover;
            border-radius: 10px;
        }
        strong {
            background: linear-gradient(
                transparent 70%,
                rgba($main-color, 0.6) 30%
            );
        }
        .embed-responsive {
            text-align: center;
        }
        .table-of-contents {
            border-radius: 5px;
            padding: 10px;
            background-color: $toc-background-color;
            a {
                text-decoration: none;
                color: $font-strong;
                font-size: 1.2rem;
                font-weight: bold;
            }
            ol {
                counter-reset: number; /*数字をリセット*/
                list-style-type: none !important; /*数字を一旦消す*/
                padding: 0.5em;
            }
            ol li {
                position: relative;
                padding-left: 50px;
                line-height: 1.5em;
                padding: 0.5em 0.5em 0.5em 50px;
            }

            ol li:before {
                position: absolute;
                counter-increment: number;
                content: counters(number, ".");
                display: inline-block;
                background: $main-color;
                color: $card-background-color;
                font-weight: bold;
                font-size: 15px;
                border-radius: 50%;
                left: 0;
                padding: 5px;
                width: 25px;
                height: 25px;
                line-height: 25px;
                text-align: center;
                top: 20px;
                -webkit-transform: translateY(-50%);
                transform: translateY(-50%);
            }
            li {
                color: $font-color;
                & > a {
                    color: inherit;
                }
            }
            & > ol {
                margin-bottom: 0;
                & > li {
                    color: $font-strong;
                    & > a {
                        color: inherit;
                    }
                }
            }
            .toc-container-header {
                font-size: 1.5rem;
                display: flex;
                padding-left: 1rem;
                color: $main-color;
                font-weight: bold;
                li {
                    list-style: upper-alpha;
                }
                &::before {
                    top: 0;
                    bottom: 0;
                    margin: auto 1rem auto 0;
                    display: block;
                    content: "";
                    width: 24px;
                    height: 24px;
                    background-image: url("~/assets/image/index.svg");
                }
            }
        }
    }
}
</style>