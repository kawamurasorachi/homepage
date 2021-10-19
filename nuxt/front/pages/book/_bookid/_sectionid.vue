<template>
    <div class="main">
        <Sidebar :position="$route.name.split('-')[0]" />
        <main class="content book">
            <article class="wrapper section">
                <div class="section_meta">
                    <div class="section_meta_left">
                        <img :src="article.thumbnail" alt="" />
                    </div>
                    <div class="section_meta_right">
                        <div class="section_meta_right_content">
                            <h2>{{ book.title }}</h2>
                            <h1>
                                第{{ $route.params.sectionid }}章　{{
                                    article.title
                                }}
                            </h1>
                            <p>{{ article.description }}</p>
                        </div>
                    </div>
                </div>
                <div
                    class="article_content"
                    v-html="$md.render(article.content)"
                ></div>
            </article>
        </main>
        <BookNavbar :nav_list="book.article" />
    </div>
</template>

<script>
export default {
    async asyncData({ $axios, params }) {
        const response = await $axios.get(`get_book/?id=${params.bookid}`);
        return {
            book: response.data.book[0],
            article: response.data.book[0].article[params.sectionid - 1],
        };
    },
};
</script>

<style lang="scss">
.section {
    &_meta {
        display: flex;
        margin-top: 10vh;
        &_left {
            width: 40%;
            position: relative;
            img {
                display: block;
                width: 80%;
                margin: auto;
                border-radius: 10px;
                z-index: 1;
            }
        }
        &_right {
            width: 60%;
            position: relative;
            h2 {
                color: $font-color;
                font-size: 20px;
                margin: 0;
            }
            h1 {
                margin: 5px 0;
            }
            &_content {
                position: absolute;
                height: min-content;
                top: 0;
                bottom: 0;
                margin: auto;
            }
        }
    }
}
</style>