<template>
    <div class="main">
        <Sidebar :position="$route.name.split('-')[0]" />

        <main class="content">
            <article class="wrapper editor">
                <h1>新規本投稿</h1>
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
                            <div
                                id="upload_preview_dummy"
                                class="editor_thumbnail_book_dummy"
                            >
                                Preview
                            </div>
                            <img
                                class="editor_thumbnail_book"
                                :src="thumbnail"
                                id="upload_preview"
                                alt="thumbnail"
                            />
                        </div>
                    </div>
                    <div class="editor_flex_content">
                        <h2>タイトル</h2>
                        <p>
                            <input type="text" v-model="title" />
                        </p>
                        <h2>説明</h2>
                        <p>
                            <input type="text" v-model="description" />
                        </p>
                    </div>
                </div>
                <div>
                    <div class="editor_flex">
                        <div class="editor_flex_content">
                            <h2>記事選択</h2>
                            <div class="editor_selected_item_outer">
                                <button
                                    class="editor_selected_item"
                                    v-for="selected_article in article"
                                    :key="selected_article"
                                    v-on:click="
                                        remove_selected_article(
                                            selected_article
                                        )
                                    "
                                >
                                    {{
                                        articles.find(
                                            (element) =>
                                                element.id == selected_article
                                        ).title
                                    }}
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
                                <div
                                    :class="`select_article_list_item ${
                                        article_item.title.indexOf(search_text)
                                            ? 'visiable'
                                            : 'invisiable'
                                    }`"
                                    v-for="article_item in articles"
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
                </div>
                <div class="editor_flex">
                    <div class="editor_flex_content">
                        <h2 class="editor_section_title">公開設定</h2>
                        <label id="toggle">
                            <input type="checkbox" v-model="is_public" />
                            <i></i>
                        </label>
                    </div>
                    <div class="editor_flex_content">
                        <button id="post" v-on:click="post">投稿</button>
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
            thumbnail: "",
            title: "",
            description: "",
            article: [],
            is_public: false,
            search_text: "",
        };
    },
    async asyncData({ $axios, params }) {
        const response = await $axios.get(`get_article`);
        return { articles: response.data.article };
    },
    methods: {
        fileSelected(e) {
            var fileReader = new FileReader();
            fileReader.onload = function () {
                document.getElementById("upload_preview").src =
                    fileReader.result;
                document.getElementById("upload_preview").style.display =
                    "block";
                document.getElementById("upload_preview_dummy").style.display =
                    "none";
            };
            fileReader.readAsDataURL(e.target.files[0]);
            this.thumbnail = e.target.files[0];
        },
        post() {
            const url = "post_book/";
            const url2 = "update_article/";
            const formdata = new FormData();
            this.$axios.defaults.xsrfCookieName = "csrftoken";
            this.$axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            formdata.append("thumbnail", this.thumbnail);
            formdata.append("title", this.title);
            formdata.append("description", this.description);
            formdata.append("is_public", this.is_public);
            this.$axios
                .$post(url, formdata, {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                })
                .then((response) => {
                    for (var i = 0; i < this.article.length; i++) {
                        const formdata = new FormData();
                        formdata.append("is_book", response.book.id);
                        this.$axios.$patch(
                            `${url2 + this.article[i]}`,
                            formdata,
                            {
                                headers: {
                                    "Content-Type": "multipart/form-data",
                                },
                            }
                        );
                    }
                });
            this.$router.push("/manage");
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
</style>