<template>
    <ul class="book_card">
        <a class="book_card_item" v-for="book in books" :key="book.id" href="">
            <li>
                <div class="image_wrapper">
                    <img :src="book.thumbnail" alt="thumbnail" />
                </div>
                <h3>{{ book.title }}</h3>
            </li>
        </a>
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
        width: calc(100% / 5 - 10px * 2);
        height: 430px;
        margin: 10px;
        position: relative;
        text-decoration: none;
        li {
            width: 100%;
            .image_wrapper {
                width: 100%;
                height: 300px;
                img {
                    width: 100%;
                    height: 360px;
                    transition: 0.3s ease;
                    width: inherit;
                    height: inherit;
                    object-fit: cover;
                    margin: 0;
                    border-radius: $book-card-radius;
                    box-shadow: 2px 2px 6px #bebebe, -2px -2px 6px #ffffff;
                }
                &:before {
                    content: "";
                    position: absolute;
                    width: 10px;
                    height: inherit;
                    left: 0;
                    background-color: rgba(0, 0, 0, 0.5);
                    border-radius: $book-card-radius 0 0 $book-card-radius;
                }
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
                color: $font-color;
            }
            .created_at {
                position: absolute;
                bottom: 0;
                right: 0;
                margin: 3px 5px;
                color: $font-color;
            }
        }
    }
}
</style>