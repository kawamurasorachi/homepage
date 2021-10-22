<template>
    <div class="main">
        <Sidebar :position="$route.name.split('-')[0]" />
        <main class="content works">
            <article class="wrapper">
                <WorkCard :works="works" />
            </article>
        </main>
    </div>
</template>

<script>
export default {
    async asyncData({ $axios }) {
        const url = "get_work/";
        const response = await $axios.get(url);
        return { works: response.data.work };
    },
};
</script>

<style lang="scss" scoped>
</style>