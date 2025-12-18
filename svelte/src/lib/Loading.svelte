<script>
    let { value, max } = $props();
</script>

<div class="h-screen w-full flex flex-col justify-center">
    <div class="w-full flex justify-center mb-4">
        <span class="loading loading-ring loading-xl"></span>
    </div>
    <div class="w-full flex justify-center">
        <progress class="progress progress-primary w-56" {value} {max}
        ></progress>
    </div>
</div>
