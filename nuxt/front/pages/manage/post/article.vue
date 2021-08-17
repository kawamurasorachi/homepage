<template>
    <div class="main">
        <Sidebar :position="$route.name.split('-')[0]" />

        <main class="content">
            <article class="wrapper editor">
                <h1>新規記事投稿</h1>
                <div class="editor_flex">
                    <div class="editor_flex_content">
                        <h2 class="editor_section_title">サムネイル</h2>
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
                                class="editor_thumbnail_article_dummy"
                            >
                                Preview
                            </div>
                            <img
                                class="editor_thumbnail_article"
                                :src="thumbnail"
                                id="upload_preview"
                                alt="thumbnail"
                            />
                        </div>
                    </div>
                    <div class="editor_flex_content">
                        <h2 class="editor_section_title">タイトル</h2>
                        <p>
                            <input type="text" v-model="title" />
                        </p>
                        <h2 class="editor_section_title">説明</h2>
                        <p>
                            <input type="text" v-model="description" />
                        </p>
                    </div>
                </div>
                <h2 class="editor_section_title">本文</h2>
                <p>
                    <no-ssr>
                        <mavon-editor
                            ref="md"
                            :toolbars="markdownOption"
                            :language="'ja'"
                            placeholder="Markdown記法"
                            @imgAdd="$imgAdd"
                            v-model="content"
                        />
                    </no-ssr>
                </p>
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
            content: "",
            is_public: "",
            markdownOption: {
                bold: true,
                italic: true,
                header: true,
                underline: true,
                strikethrough: true,
                mark: true,
                superscript: true,
                subscript: true,
                quote: true,
                ol: true,
                ul: true,
                link: true,
                imagelink: true,
                code: true,
                table: true,
                fullscreen: true,
                readmodel: true,
                htmlcode: true,
                help: true,
            },
        };
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
            const url = "post_article/";
            const formdata = new FormData();
            this.$axios.defaults.xsrfCookieName = "csrftoken";
            this.$axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            formdata.append("thumbnail", this.thumbnail);
            formdata.append("title", this.title);
            formdata.append("description", this.description);
            formdata.append("content", this.content);
            formdata.append("is_public", this.is_public);
            this.$axios.$post(url, formdata, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            });
            this.$router.push("/manage");
        },
        $imgAdd(pos, $file) {
            var formdata = new FormData();
            formdata.append("image", $file);
            this.$axios({
                url: "post_article_image/",
                method: "post",
                data: formdata,
                headers: { "Content-Type": "multipart/form-data" },
            }).then((url) => {
                this.$refs.md.$img2Url(
                    pos,
                    `/django-media/article_image/${$file.name}`
                );
            });
        },
    },
};
</script>

<style lang="scss" scoped>
</style>