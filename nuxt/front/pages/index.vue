<template>
    <div class="main">
        <Sidebar :position="$route.name.split('-')[0]" />
    </div>
</template>

<script>
export default {
    data() {
        return {
            books: [],
        };
    },
    async asyncData({ $axios }) {
        const url = "get_book/";
        const response = await $axios.get(url);
        return { books: response.data };
    },
};
</script>

<style lang="scss" scoped>
</style>