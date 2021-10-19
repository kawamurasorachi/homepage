<template>
    <div class="main">
        <BookNavbar :nav_list="book.article" />
        <main class="content book">
            <article class="wrapper">
                <div class="book_meta">
                    <div class="book_meta_left">
                        <span></span>
                        <img :src="book.thumbnail" alt="" />
                    </div>
                    <div class="book_meta_right">
                        <div class="book_meta_right_content">
                            <h1>{{ book.title }}</h1>
                            <p>{{ book.description }}</p>
                            <p>{{ book.created_at }}</p>
                        </div>
                    </div>
                </div>
                <div class="book_section_list">
                    <!-- {{book.article}} -->
                    <nuxt-link
                        class="book_section_item"
                        v-for="(section, index) in book.article"
                        :key="index"
                        :to="{
                            name: 'book-bookid-sectionid',
                            params: {
                                bookid: $route.params.bookid,
                                sectionid: index + 1,
                            },
                        }"
                    >
                        <img :src="section.fields.thumbnail" alt="" />
                        <div class="book_section_item_caption">
                            <h3>
                                第{{ index + 1 }}章　{{ section.fields.title }}
                            </h3>
                            <p>{{ section.fields.description }}</p>
                            <p>{{ section.fields.created_at }}</p>
                        </div>
                    </nuxt-link>
                </div>
            </article>
        </main>
    </div>
</template>

<script>
export default {
    async asyncData({ $axios, params }) {
        const response = await $axios.get(`get_book/?id=${params.bookid}`);
        return { book: response.data.book[0] };
    },
};
</script>

<style lang="scss" scoped>
.book {
    &_meta {
        display: flex;
        margin-top: 10vh;
        &_left {
            width: 40%;
            position: relative;
            img {
                display: block;
                width: 60%;
                margin: auto;
                border-radius: 10px;
                z-index: 1;
            }
            span {
                position: absolute;
                bottom: -12%;
                left: 0;
                right: 0;
                margin: auto;
                width: 70%;
                height: 20%;
                background-color: rgb(110, 110, 110);
                z-index: -1;
                border-radius: 100%;
                -webkit-filter: blur(10px);
                -moz-filter: blur(10px);
                -o-filter: blur(10px);
                -ms-filter: blur(10px);
                filter: blur(10px);
            }
        }
        &_right {
            width: 60%;
            position: relative;
            &_content {
                position: absolute;
                height: min-content;
                top: 0;
                bottom: 0;
                margin: auto;
            }
        }
    }
    &_section {
        &_list {
            margin-top: 10vh;
            width: 100%;
        }
        &_item {
            width: 100%;
            display: flex;
            height: 150px;
            text-decoration: none;
            color: $font-strong;
            img {
                display: block;
                height: 80%;
                margin: auto;
                border-radius: 5px;
                object-fit: cover;
            }
            &_caption {
                width: 80%;
                h3 {
                    font-size: 22px;
                    display: -webkit-box;
                    -webkit-line-clamp: 1;
                    -webkit-box-orient: vertical;
                    overflow: hidden;
                    margin: 20px 0 0 0;
                }
                p {
                    display: -webkit-box;
                    -webkit-line-clamp: 1;
                    -webkit-box-orient: vertical;
                    overflow: hidden;
                }
            }
        }
    }
}
</style>