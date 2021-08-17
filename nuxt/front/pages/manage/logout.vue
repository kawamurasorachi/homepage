<template>
    <div class="main">
        <Sidebar :position="$route.name.split('-')[0]" />

        <main class="content">
            <article class="wrapper">
                <button type="primary" v-on:click="logout">ログアウト</button>
            </article>
        </main>
    </div>
</template>

<script>
export default {
    middleware({ store, redirect }) {
        if (!store.$auth.loggedIn) {
            redirect("/login");
        }
    },
    computed: {
        user() {
            return this.$auth.user;
        },
    },
    methods: {
        logout() {
            this.$auth.logout();
        },
    },
};
</script>