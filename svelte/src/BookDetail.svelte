<script>
    import { onMount, getContext } from "svelte";

    let currentIndex = $state(0);
    let autoplay = $state(false);
    let width = $state(0);
    let height = $state(0);
    let colClass = $derived(width > height ? "flex-row" : "flex-col");
    const pages = JSON.parse(document.getElementById("pages-data").textContent);
    const audios = JSON.parse(
        document.getElementById("audios-data").textContent,
    );

    function onclick(event) {
        if (currentIndex > 0) {
            document.getElementById(`audio-${currentIndex}`).pause();
            document.getElementById(`audio-${currentIndex}`).currentTime = 0;
        }

        if (
            event.clientX > window.screen.width / 2 &&
            currentIndex < pages.length - 1
        ) {
            currentIndex++;
            document.getElementById(`audio-${currentIndex}`).play();
        } else if (
            event.clientX < window.screen.width / 2 &&
            currentIndex > 0
        ) {
            currentIndex--;
        }
    }
</script>

<svelte:window bind:innerWidth={width} bind:innerHeight={height} />
<main>
    <div
        role="link"
        tabindex={currentIndex}
        {onclick}
        onkeyup={(e) =>
            e.key === "ArrowLeft"
                ? onclick({ clientX: 0 })
                : onclick({ clientX: 10000 })}
        aria-label="Change Page"
        class={["h-screen flex", colClass]}
    >
        <img src={pages[currentIndex].image} alt="Illustration" />
        <div class="h-full w-full flex flex-col justify-center text-center">
            <div class="p-6">
                <p>{pages[currentIndex].text}</p>
                {#if currentIndex === 0}
                    <label class="flex justify-center cursor-pointer gap-2">
                        <span class="label-text">Lecture Auto</span>
                        <input
                            type="checkbox"
                            class="toggle"
                            bind:checked={autoplay}
                        />
                    </label>
                {/if}
            </div>
        </div>
    </div>
    {#each audios as audio}
        <audio
            id={audio.id}
            src={audio.url}
            preload="auto"
            onended={() => {
                autoplay && onclick({ clientX: 10000 });
            }}
        ></audio>
    {/each}
</main>
