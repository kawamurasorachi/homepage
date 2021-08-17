<template>
    <div class="main">
        <Sidebar :position="$route.name.split('-')[0]" />

        <main class="content">
            <article class="wrapper editor">
                <h1>本を編集</h1>
                <div class="editor_flex">
                    <div class="editor_flex_content">
                        <h2>サムネイル</h2>
                        <div class="editor_thumbnail">
                            <input
                                type="file"
                                v-on:change="fileSelected"
                                id="upload"
                                hidden
                            />
                            <label for="upload">
                                <img
                                    src="~/assets/image/upload_file.svg"
                                    alt="upload_file"
                                />
                                <br />
                                Choose a Thumbnail
                            </label>
                            <img
                                class="editor_thumbnail_book"
                                :src="book.thumbnail"
                                id="upload_preview"
                                alt="thumbnail"
                            />
                        </div>
                    </div>
                    <div class="editor_flex_content">
                        <h2>タイトル</h2>
                        <p>
                            <input type="text" v-model="book.title" />
                        </p>
                        <h2>説明</h2>
                        <p>
                            <input type="text" v-model="book.description" />
                        </p>
                    </div>
                </div>
                <div class="editor_flex">
                    <div class="editor_flex_content">
                        <h2>記事選択</h2>
                        <div class="editor_selected_item_outer">
                            <button
                                class="editor_selected_item"
                                v-for="selected_article in article"
                                :key="selected_article"
                                v-on:click="
                                    remove_selected_article(selected_article)
                                "
                            >
                                {{ get_article_title(selected_article) }}
                            </button>
                        </div>
                    </div>
                    <div class="editor_flex_content">
                        <div class="editor_flex_content_flex">
                            <h2>記事を検索</h2>
                            <a href="/manage/post/article" target="_blank"
                                >記事を書く</a
                            >
                        </div>
                        <input type="text" v-model="search_text" />
                        <div class="select_article_list">
                            {{ search_text }}
                            <div
                                v-for="article_item in articles"
                                :class="`select_article_list_item ${
                                    article_item.title.indexOf(search_text) !==
                                    -1
                                        ? 'visiable'
                                        : 'invisiable'
                                }`"
                                :key="article_item.id"
                                :value="article_item.id"
                                v-on:click="
                                    add_selected_article(article_item.id)
                                "
                            >
                                <p>{{ article_item.id }}</p>
                                <p>{{ article_item.title }}</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="editor_flex">
                    <div class="editor_flex_content">
                        <h2 class="editor_section_title">公開設定</h2>
                        <label id="toggle">
                            <input type="checkbox" v-model="book.is_public" />
                            <i></i>
                        </label>
                    </div>
                    <div class="editor_flex_content">
                        <button id="post" v-on:click="patch">投稿</button>
                    </div>
                </div>
            </article>
        </main>
    </div>
</template>

<script>
export default {
    middleware: "auth",
    data() {
        return {
            book: {},
            article: [],
            articles: [],
            search_text: "",
            is_file_changed: false,
        };
    },
    mounted() {
        this.$axios
            .get(`get_book/?id=${this.$route.params.id}`)
            .then((response) => {
                this.book = response.data.book[0];
                for (
                    let index = 0;
                    index < response.data.book.length;
                    index++
                ) {
                    const element = response.data.book[index];
                    element.article.forEach((elm) => this.article.push(elm.pk));
                }
            });
        this.$axios
            .get(`get_article`)
            .then((response) => (this.articles = response.data.article));
    },
    methods: {
        fileSelected(e) {
            var fileReader = new FileReader();
            fileReader.onload = function () {
                document.getElementById("upload_preview").src =
                    fileReader.result;
            };
            fileReader.readAsDataURL(e.target.files[0]);
            this.book.thumbnail = e.target.files[0];
            this.is_file_changed = true;
        },
        patch() {
            const book_id = this.$route.params.id;
            const url = `update_book/${this.$route.params.id}`;
            const url2 = `update_article/`;
            const formdata = new FormData();
            this.$axios.defaults.xsrfCookieName = "csrftoken";
            this.$axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            if (this.is_file_changed) {
                formdata.append("thumbnail", this.book.thumbnail);
            }
            formdata.append("title", this.book.title);
            formdata.append("description", this.book.description);
            formdata.append("is_public", this.book.is_public);
            this.$axios
                .$patch(url, formdata, {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                })
                .then((response) => {
                    const after_article = this.article;
                    var before_article = [];
                    this.book.article.forEach((elm) =>
                        before_article.push(elm.pk)
                    );
                    for (let i = 0; i < this.articles.length; i++) {
                        const search_id = this.articles[i].id;
                        if (
                            before_article.includes(search_id) &&
                            !after_article.includes(search_id)
                        ) {
                            const formdata = new FormData();
                            formdata.append("is_book", "");
                            this.$axios.$patch(
                                `${url2 + search_id}`,
                                formdata,
                                {
                                    headers: {
                                        "Content-Type": "multipart/form-data",
                                    },
                                }
                            );
                        }
                        if (
                            !before_article.includes(search_id) &&
                            after_article.includes(search_id)
                        ) {
                            const formdata = new FormData();
                            formdata.append("is_book", book_id);
                            this.$axios.$patch(
                                `${url2 + search_id}`,
                                formdata,
                                {
                                    headers: {
                                        "Content-Type": "multipart/form-data",
                                    },
                                }
                            );
                        }
                    }
                });
            this.$router.push("/manage");
        },
        get_article_title(num) {
            const array = this.articles;
            for (let index = 0; index < array.length; index++) {
                const element = array[index];
                if (element.id == num) {
                    return element.title;
                }
            }
        },
        add_selected_article(article_num) {
            if (!this.article.includes(article_num)) {
                this.article.push(article_num);
            }
        },
        remove_selected_article(article_num) {
            this.article.splice(this.article.indexOf(article_num), 1);
        },
    },
};
</script>

<style lang="scss" scoped>
#upload_preview {
    display: block;
}
</style>