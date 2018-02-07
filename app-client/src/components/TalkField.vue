<template>
    <div class="talk-field">
        <div class="avator-picture">
            <img class="avator-default" src="favicon/default.png">
        </div>
        <div class="talk-main">
            <div class="talk-username">{{ role }}</div>
            <div class="talk-content">{{ word }}</div>
        </div>
        <div class="talk-time">
            <span></span>
        </div>
    </div>
</template>

<script>
    export default {
        props:['role','word']
    }
</script>

<style>
    .talk-field {
        display: flex;
        margin-bottom: 1rem;
    }

    .avator-default {
        width: 2.5rem;
        border-radius: 0.5rem;
        margin-right: 1.5rem;
    }

</style>