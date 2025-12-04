<script>
    let currentIndex = $state(0);
    let autoplay = $state(false);
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
    >
        <img src={pages[currentIndex].image} alt="Illustration" />
        <p>{pages[currentIndex].text}</p>
        {#if currentIndex === 0}
            <input
                type="checkbox"
                role="switch"
                id="autoplaySwitch"
                bind:checked={autoplay}
            />
        {/if}
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
