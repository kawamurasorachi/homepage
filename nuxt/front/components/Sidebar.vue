<template>
    <div class="sidebar">
        <div class="sidebar_nav">
            <a
                :class="`sidebar_nav_link ${
                    position == 'article' ? 'sidebar_nav_is_here' : ''
                }`"
                href="/article"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    enable-background="new 0 0 24 24"
                    height="24px"
                    viewBox="0 0 24 24"
                    width="24px"
                >
                    <g>
                        <rect fill="none" height="24" width="24" />
                        <g>
                            <path
                                d="M19,5v14H5V5H19 M19,3H5C3.9,3,3,3.9,3,5v14c0,1.1,0.9,2,2,2h14c1.1,0,2-0.9,2-2V5C21,3.9,20.1,3,19,3L19,3z"
                            />
                        </g>
                        <path
                            d="M14,17H7v-2h7V17z M17,13H7v-2h10V13z M17,9H7V7h10V9z"
                        />
                    </g>
                </svg>
                Article
            </a>
            <a
                :class="`sidebar_nav_link ${
                    position == 'book' ? 'sidebar_nav_is_here' : ''
                }`"
                href="/book"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    height="24px"
                    viewBox="0 0 24 24"
                    width="24px"
                >
                    <path d="M0 0h24v24H0V0z" fill="none" />
                    <path
                        d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM9 4h2v5l-1-.75L9 9V4zm9 16H6V4h1v9l3-2.25L13 13V4h5v16z"
                    />
                </svg>
                Book
            </a>
            <a
                :class="`sidebar_nav_link ${
                    position == 'works' ? 'sidebar_nav_is_here' : ''
                }`"
                href=""
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    height="24px"
                    viewBox="0 0 24 24"
                    width="24px"
                >
                    <path d="M0 0h24v24H0V0z" fill="none" />
                    <path
                        d="M20 6h-4V4c0-1.11-.89-2-2-2h-4c-1.11 0-2 .89-2 2v2H4c-1.11 0-1.99.89-1.99 2L2 19c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-6 0h-4V4h4v2z"
                    />
                </svg>
                Works
            </a>
            <a
                :class="`sidebar_nav_link ${
                    position == 'profile' ? 'sidebar_nav_is_here' : ''
                }`"
                href="/"
                ><svg
                    xmlns="http://www.w3.org/2000/svg"
                    height="24px"
                    viewBox="0 0 24 24"
                    width="24px"
                >
                    <path d="M0 0h24v24H0V0z" fill="none" />
                    <path
                        d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zM7.07 18.28c.43-.9 3.05-1.78 4.93-1.78s4.51.88 4.93 1.78C15.57 19.36 13.86 20 12 20s-3.57-.64-4.93-1.72zm11.29-1.45c-1.43-1.74-4.9-2.33-6.36-2.33s-4.93.59-6.36 2.33C4.62 15.49 4 13.82 4 12c0-4.41 3.59-8 8-8s8 3.59 8 8c0 1.82-.62 3.49-1.64 4.83zM12 6c-1.94 0-3.5 1.56-3.5 3.5S10.06 13 12 13s3.5-1.56 3.5-3.5S13.94 6 12 6zm0 5c-.83 0-1.5-.67-1.5-1.5S11.17 8 12 8s1.5.67 1.5 1.5S12.83 11 12 11z"
                    />
                </svg>
                Profile
            </a>
            <a
                :class="`sidebar_nav_link ${
                    position == 'manage' ? 'sidebar_nav_is_here' : ''
                }`"
                href="/manage"
                v-if="auth.loggedIn"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    enable-background="new 0 0 24 24"
                    height="24px"
                    viewBox="0 0 24 24"
                    width="24px"
                >
                    <g>
                        <path d="M0,0h24v24H0V0z" fill="none" />
                    </g>
                    <g>
                        <g>
                            <path
                                d="M4,18v-0.65c0-0.34,0.16-0.66,0.41-0.81C6.1,15.53,8.03,15,10,15c0.03,0,0.05,0,0.08,0.01c0.1-0.7,0.3-1.37,0.59-1.98 C10.45,13.01,10.23,13,10,13c-2.42,0-4.68,0.67-6.61,1.82C2.51,15.34,2,16.32,2,17.35V20h9.26c-0.42-0.6-0.75-1.28-0.97-2H4z"
                            />
                            <path
                                d="M10,12c2.21,0,4-1.79,4-4s-1.79-4-4-4C7.79,4,6,5.79,6,8S7.79,12,10,12z M10,6c1.1,0,2,0.9,2,2s-0.9,2-2,2 c-1.1,0-2-0.9-2-2S8.9,6,10,6z"
                            />
                            <path
                                d="M20.75,16c0-0.22-0.03-0.42-0.06-0.63l1.14-1.01l-1-1.73l-1.45,0.49c-0.32-0.27-0.68-0.48-1.08-0.63L18,11h-2l-0.3,1.49 c-0.4,0.15-0.76,0.36-1.08,0.63l-1.45-0.49l-1,1.73l1.14,1.01c-0.03,0.21-0.06,0.41-0.06,0.63s0.03,0.42,0.06,0.63l-1.14,1.01 l1,1.73l1.45-0.49c0.32,0.27,0.68,0.48,1.08,0.63L16,21h2l0.3-1.49c0.4-0.15,0.76-0.36,1.08-0.63l1.45,0.49l1-1.73l-1.14-1.01 C20.72,16.42,20.75,16.22,20.75,16z M17,18c-1.1,0-2-0.9-2-2s0.9-2,2-2s2,0.9,2,2S18.1,18,17,18z"
                            />
                        </g>
                    </g>
                </svg>
                Manage
            </a>
        </div>
        <div class="sidebar_person">
            <img src="~/assets/image/icon.JPG" alt="icon" />
            <div class="sidebar_person_text">
                <h3>Sora</h3>
                <p>Web Developper</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ["position"],
    computed: {
        auth() {
            return this.$auth;
        },
    },
    methods: {
        logout() {
            this.$auth.logout();
        },
    },
};
</script>

<style lang="scss" scope>
@import url("https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100;300&display=swap");
// * {
//     outline: 2px red solid;
// }
.sidebar {
    position: relative;
    width: $sidebar-width;
    height: 100vh;
    background-color: white;
    font-family: "Roboto Mono", monospace;
    &_nav {
        width: 100%;
        position: absolute;
        top: 0;
        bottom: 15vh;
        margin: auto;
        height: min-content;
        &_link {
            width: calc(100% - 50px);
            text-decoration: none;
            color: $font-color;
            font-size: 25px;
            line-height: 70px;
            height: 70px;
            display: flex;
            font-weight: bold;
            transition: 0.3s;
            padding-left: 50px;
            position: relative;
            &:hover {
                transform: translateX(10px);
                transition: 0.3s;
            }
            svg {
                height: 30px;
                width: 30px;
                margin: calc((70px - 30px) / 2) 10px;
                fill: $font-color;
            }
            &:before {
                content: "";
                display: block;
                width: 20px;
                height: 80%;
                background-color: white;
                position: absolute;
                top: 0;
                bottom: 0;
                left: -10px;
                margin: auto;
                border-radius: 0 7px 7px 0;
            }
        }
        &_is_here {
            color: $main-color;
            svg {
                fill: $main-color;
            }
            &:before {
                content: "";
                display: block;
                width: 20px;
                height: 80%;
                background-color: $main-color;
                position: absolute;
                top: 0;
                bottom: 0;
                left: -10px;
                margin: auto;
                border-radius: 0 7px 7px 0;
            }
        }
    }
    &_person {
        background-color: $main-color-weak;
        margin: 15px;
        border-radius: 15px;
        position: absolute;
        display: flex;
        bottom: 0;
        width: calc(100% - 30px);
        height: 100px;
        img {
            width: 60px;
            height: 60px;
            object-fit: cover;
            border-radius: 100%;
            margin: 20px;
        }
        &_text {
            width: calc(100% - 100px);
            height: 100%;
            position: relative;
            h3 {
                position: absolute;
                font-size: 20px;
                font-weight: bold;
                top: 0;
                color: $font-strong;
            }
            p {
                position: absolute;
                bottom: 0;
                color: $font-color;
            }
        }
    }
}
</style>
