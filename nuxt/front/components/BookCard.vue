<template>
    <ul class="book_card">
        <p v-if="!books.length">本はまだありません。</p>
        <nuxt-link
            class="book_card_item"
            v-for="book in books.filter((book) => book.is_public)"
            :key="book.id"
            :to="{
                name: 'book-bookid',
                params: { bookid: book.id },
            }"
        >
            <li>
                <div
                    class="caption"
                    :style="`background-image:url(${book.thumbnail})`"
                >
                    <div class="caption_wrapper">
                        <div class="caption_title">
                            {{ book.title }}
                        </div>
                        <div class="caption_description">
                            {{ book.description }}
                        </div>
                    </div>
                </div>
            </li>
        </nuxt-link>
    </ul>
</template>

<script>
export default {
    props: ["books"],
};
</script>

<style lang="scss" scope>
.book_card {
    padding: 0;
    display: flex;
    flex-wrap: wrap;
    &_item {
        display: block;
        list-style: none;
        width: calc(100% / 4 - 20px * 2);
        margin: 20px;
        position: relative;
        text-decoration: none;
        &:hover {
            .caption_wrapper {
                top: 0;
                background-color: rgba(0, 0, 0, 0.4);
                transition: 0.5s ease;
            }
        }
        li {
            width: 100%;
            .caption {
                position: relative;
                width: 100%;
                height: 370px;
                background-size: cover;
                background-position: center;
                border-radius: 5px;
                overflow: hidden;
                display: flex;
                align-items: center;
                justify-content: center;
                &_wrapper {
                    position: absolute;
                    top: 60%;
                    width: calc(100% - 10px * 2);
                    height: calc(100% - 10px * 2);
                    background-color: rgba(0, 0, 0, 0);
                    padding: 10px;
                    color: $card-background-color;
                    transition: 0.5s ease;
                }
                &_title {
                    width: 100%;
                    height: 150px;
                    font-size: 24px;
                    text-align: center;
                    font-weight: bold;
                    display: -webkit-flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    -webkit-line-clamp: 2;
                    -webkit-box-orient: vertical;
                    overflow: hidden;
                    text-shadow: 0px 0px 5px rgb(0, 0, 0);
                }
                &_description {
                    width: inherit;
                    height: 100px;
                    display: -webkit-box;
                    align-items: center;
                    -webkit-line-clamp: 4;
                    -webkit-box-orient: vertical;
                    overflow: hidden;
                }
            }
        }
    }
}
</style>