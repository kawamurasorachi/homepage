<template>
    <div class="main">
        <Sidebar :position="$route.name.split('-')[0]" />

        <main class="content login">
            <article class="wrapper">
                <form class="login_container" @submit.prevent="login">
                    <div>
                        <p>Usermane</p>
                        <input v-model="form.username" type="text" />
                    </div>
                    <div>
                        <p>Password</p>
                        <input v-model="form.password" type="password" />
                    </div>
                    <div>
                        <button type="submit">LOGIN</button>
                    </div>
                </form>
            </article>
        </main>
    </div>
</template>

<script>
export default {
    middleware({ store, redirect }) {
        if (store.$auth.loggedIn) {
            redirect("/manage");
        }
    },
    data() {
        return {
            form: {
                username: "",
                password: "",
            },
            message: "",
        };
    },
    methods: {
        async login() {
            const response = await this.$auth
                .loginWith("local", { data: this.form })
                .catch((err) => {
                    return err.response;
                });
            if (response.status !== 200) {
                this.message = "ログインに失敗しました";
            }
        },
    },
};
</script>

<style lang="scss">
.login {
    position: relative;
    background-image: url("~/assets/image/001.jpeg");
    background-size: cover;
    &_container {
        width: 760px;
        height: 340px;
        background: rgba(255, 255, 255, 0.25);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        margin: auto;
        padding: 30px;
        div {
            position: relative;
            width: 80%;
            height: calc(100% / 3);
            padding: 0 10%;
            input {
                position: absolute;
                top: 0;
                bottom: 0;
                margin: auto;
                height: 30px;
                border-radius: 3px;
                border: 1px rgba(255, 255, 255, 0.5) solid;
                background: rgba(66, 66, 66, 0.157);
                width: calc(80% - 20px - 2px);
                color: white;
                font-size: 20px;
                padding: 10px;
                font-family: "Roboto Mono", monospace;
                outline: none;
            }
            p {
                position: absolute;
                top: 0;
                margin: 0;
                color: white;
                font-size: 16px;
                padding: 0 10px;
                font-family: "Roboto Mono", monospace;
            }
            button {
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                display: block;
                margin: auto;
                border: none;
                border-radius: 50px;
                height: 50px;
                width: 160px;
                font-size: 20px;
                font-weight: bold;
                background-color: #ddd;
                color: #666;
                transition: 0.3s ease;
                border: 2px #ddd solid;
                &:hover {
                    background-color: rgba(0, 0, 0, 0);
                    border: 2px #ddd solid;
                    color: #ddd;
                    transition: 0.3s ease;
                }
            }
        }
    }
}
</style>