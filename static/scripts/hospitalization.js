var all = document.querySelector("#button-all");
var cambios = document.querySelector("#button-changes");
var evoluciones = document.querySelector("#button-evolutions");

var container_all = document.querySelector("#all");
var container_changes = document.querySelector("#only-changes");
var container_evoluciones = document.querySelector("#only-evoluciones");

if(all) {
    all.addEventListener("click", function() {
        if(container_changes)
            container_changes.style.display = "none";
        if(container_evoluciones)
            container_evoluciones.style.display = "none";
        if(container_all)
            container_all.style.display = "block";
        all.classList.remove("no-activo");
        if(cambios)
            if(!cambios.classList.contains("no-activo"))
                cambios.classList.add("no-activo");
        if(evoluciones)
            if(!evoluciones.classList.contains("no-activo"))
                evoluciones.classList.add("no-activo");
    });
}

if(cambios) {
    cambios.addEventListener("click", function() {
        if(container_all)
            container_all.style.display = "none";
        if(container_evoluciones)
            container_evoluciones.style.display = "none";
        if(container_changes)
            container_changes.style.display = "block";
        cambios.classList.remove("no-activo");
        if(all)
            if(!all.classList.contains("no-activo"))
                all.classList.add("no-activo");
        if(evoluciones)
            if(!evoluciones.classList.contains("no-activo"))
                evoluciones.classList.add("no-activo");
    });
}

if(evoluciones) {
    evoluciones.addEventListener("click", function() {
        if(container_changes)
            container_changes.style.display = "none";
        if(container_all)
            container_all.style.display = "none";
        if(container_evoluciones)
            container_evoluciones.style.display = "block";
        evoluciones.classList.remove("no-activo");
        if(cambios)
            if(!cambios.classList.contains("no-activo"))
                cambios.classList.add("no-activo");
        if(all)
            if(!all.classList.contains("no-activo"))
                all.classList.add("no-activo");
    });
}