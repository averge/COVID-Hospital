function setEventListeners() {
    var alert_box = document.querySelector(".messages");
    if(alert_box) {
        alert_box.addEventListener("click", function() {
            alert_box.remove();
        });
    }
}

window.onload = function() {
    setEventListeners();
};