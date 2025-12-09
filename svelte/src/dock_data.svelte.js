let autoplay = localStorage.getItem("autoplay") === "true" ? true : false;
let sound = localStorage.getItem("sound") === "false" ? false : true;

export const dockData = $state({
    autoplay: autoplay,
    sound: sound,
    currentIndex: 0
})