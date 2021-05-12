// flash messages for 6 seconds
setTimeout(()=> {
    flash_message = document.getElementsByClassName("flash-message");
    for (let i = 0; i < flash_message.length; i++) {
        flash_message[i].style.display="none";
    }
}, 6000);