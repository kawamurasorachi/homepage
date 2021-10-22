<template>
    <ul class="work_wrapper">
        <li
            class="work_card"
            v-for="(work, index) in works"
            :key="work.id"
            @click="open_works(index)"
        >
            <img :src="work.thumbnail" alt="" />
            <div>
                <div class="tag_flex">
                    <div
                        class="tag_item"
                        v-for="tag in work.tag.split(',')"
                        :key="tag"
                    >
                        {{ tag }}
                    </div>
                </div>
                <h3>
                    {{ work.title }}
                </h3>
                <p>
                    {{ work.content }}
                </p>
            </div>
        </li>
        <div id="overwrap">
            <div id="overwrap_card">
                <div id="overwrap_left">
                    <img id="overwrap_thumbnail" />
                    <div class="close_btn" @click="close_works">
                        <div>
                            <span></span>
                            <span></span>
                        </div>
                    </div>
                </div>
                <div id="overwrap_right">
                    <h1 id="overwrap_meta_title"></h1>
                    <hr />
                    <div class="tag_flex">
                        <div
                            class="tag_item"
                            v-for="tag in tag_list"
                            :key="tag"
                        >
                            {{ tag }}
                        </div>
                    </div>
                    <p id="overwrap_meta_content"></p>
                    <a id="overwrap_site" href=""></a>
                    <iframe
                        id="overwrap_git"
                        width="500"
                        height="162"
                        scrolling="no"
                        frameborder="0"
                        src="https://matsubara0507.github.io/github-card/?target=kawamurasorachi/homepage"
                    ></iframe>
                </div>
            </div>
        </div>
    </ul>
</template>

<script>
export default {
    props: ["works"],
    data() {
        return {
            tag_list: [],
        };
    },
    methods: {
        open_works(num) {
            document.getElementById("overwrap").style.display = "block";
            console.log(`${window.pageYOffset}px`);
            document.getElementById(
                "overwrap"
            ).style.top = `${window.pageYOffset}px`;
            document.getElementById("overwrap_thumbnail").src =
                this.works[num].thumbnail;
            document.getElementById("overwrap_meta_title").innerHTML =
                this.works[num].title;
            document.getElementById("overwrap_meta_content").innerHTML =
                this.works[num].content;
            if (this.works[num].repo_url.length) {
                document.getElementById(
                    "overwrap_git"
                ).src = `https://matsubara0507.github.io/github-card/?target=${this.works[
                    num
                ].repo_url.substring(
                    this.works[num].repo_url.indexOf("github.com/") + 11,
                    this.works[num].repo_url.length
                )}`;
            }
            if (this.works[num].site_url.length) {
                document.getElementById("overwrap_site").href =
                    this.works[num].site_url;
                document.getElementById("overwrap_site").innerHTML =
                    this.works[num].site_url;
            }
            this.tag_list = this.works[num].tag.split(",");
            document.body.classList.add = "no-scroll";
        },
        close_works() {
            document.getElementById("overwrap").style.display = "none";
            document.body.classList.remove = "no-scroll";
        },
    },
};
</script>

<style lang="scss" scope>
.no-scroll {
    overflow: hidden;
}
#overwrap {
    position: absolute;
    display: none;
    left: 0;
    top: 0;
    min-width: 100vw;
    height: 100vh;
    z-index: 100;
    background-color: rgba(0, 0, 0, 0.5);
    &_card {
        position: absolute;
        left: 0;
        right: 0;
        top: 0;
        bottom: 0;
        margin: auto;
        width: 80vw;
        height: 60vh;
        background-color: $card-background-color;
        border-radius: 20px;
        display: flex;
        z-index: 101;
    }
    &_left {
        width: 60%;
        position: relative;
        margin-right: 20px;
        img {
            display: block;
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 20px 0 0 20px;
        }
        .close_btn {
            position: absolute;
            left: -120px;
            top: -120px;
            transition: 0.5s ease;
            div {
                width: 120px;
                height: 120px;
                position: relative;
                span {
                    position: absolute;
                    left: 0;
                    top: 0;
                    margin: auto;
                    display: block;
                    width: 100px;
                    height: 7px;
                    background-color: white;
                    border-radius: 5px;
                    &:nth-child(1) {
                        transform: rotate(45deg) translate(48px, 35px);
                    }
                    &:nth-child(2) {
                        transform: rotate(-45deg) translate(-35px, 48px);
                    }
                }
            }
            &:hover {
                transform: rotate(90deg);
                transition: 0.5s ease;
            }
        }
    }
    &_right {
        width: 40%;
        padding-right: 20px;
    }
}
.work {
    &_wrapper {
        width: 100%;
        list-style: none;
        padding: 0;
        display: flex;
        flex-wrap: wrap;
    }
    &_card {
        width: calc(100% / 2 - 22px);
        margin: 10px;
        background-color: $card-background-color;
        border-radius: 10px;
        overflow: hidden;
        border: 1px #ddd solid;
        display: flex;
        img {
            width: 200px;
            height: 100%;
            object-fit: cover;
        }
        h3 {
            padding: 0 20px;
            margin: 10px 0;
        }
        p {
            margin: 10px 0;
            padding: 0 20px;
            color: $font-color;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }
    }
}
.tag {
    &_flex {
        display: flex;
        flex-wrap: wrap;
        padding: 0 20px;
    }
    &_item {
        padding: 5px 10px;
        margin: 5px;
        border-radius: 5px;
        width: min-content;
        white-space: nowrap;
        color: white;
        background-color: $main-color;
    }
}
</style>