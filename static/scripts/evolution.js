var o2_suplementario = document.querySelector("#id_requiere_o2_suplementario");
o2_suplementario.addEventListener("change", function() {
    var o2_hidden = document.querySelector("#o2-hidden-fields");
    var o2_subcategory = document.querySelector("#o2-subcategory");
    if (o2_suplementario.checked) {
        o2_hidden.style.display = "flex";
        o2_subcategory.classList.add("multiple-category");
    } else {
        o2_hidden.style.display = "none";
        o2_subcategory.classList.remove("multiple-category");
    }
});

var canula_checkbox = document.querySelector("#canula-checkbox");
var mascara_checkbox = document.querySelector("#mascara-checkbox");
canula_checkbox.addEventListener("change", function() {
    var canula_hidden_fields = document.querySelector("#canula-hidden-fields");
    var mascara_hidden_fields = document.querySelector("#mascara-hidden-fields");
    if (canula_checkbox.checked) {
        canula_hidden_fields.style.display = "flex";
        mascara_hidden_fields.style.display = "none"
    }
});
mascara_checkbox.addEventListener("change", function() {
    var canula_hidden_fields = document.querySelector("#canula-hidden-fields");
    var mascara_hidden_fields = document.querySelector("#mascara-hidden-fields");
    if (mascara_checkbox.checked) {
        mascara_hidden_fields.style.display = "flex";
        canula_hidden_fields.style.display = "none"
    }
});

var pafi_checkbox = document.querySelector("#id_pafi");
pafi_checkbox.addEventListener("change", function() {
    var pafi_valor_hidden_fields = document.querySelector("#pafi-valor-hidden-fields");
    if (pafi_checkbox.checked) {
        pafi_valor_hidden_fields.style.display = "flex";
    } else {
        pafi_valor_hidden_fields.style.display = "none";
    }
});

var rx_tx_checkbox = document.querySelector("#id_rx_tx");
var rx_tx_normal = document.querySelector("#id_tipo_rx_tx_0");
var rx_tx_patologico = document.querySelector("#id_tipo_rx_tx_1");
var rx_tx_type_hidden_fields = document.querySelector("#rx-tx-type-hidden-fields");
var rx_tx_descripcion_hidden_fields = document.querySelector("#rx-tx-descripcion-hidden-fields");
rx_tx_checkbox.addEventListener("change", function() {
    var rx_tx_subcategory = document.querySelector("#rx-tx-subcategory");
    if (rx_tx_checkbox.checked) {
        rx_tx_type_hidden_fields.style.display = "flex";
        rx_tx_subcategory.classList.add("multiple-category");
    } else {
        rx_tx_type_hidden_fields.style.display = "none";
        rx_tx_subcategory.classList.remove("multiple-category");
        rx_tx_descripcion_hidden_fields.style.display = "none";
        rx_tx_normal.checked = false;
        rx_tx_patologico.checked = false;
    }
});
rx_tx_normal.addEventListener("change", function() {
    rx_tx_descripcion_hidden_fields.style.display = "none";
});
rx_tx_patologico.addEventListener("change", function() {
    rx_tx_descripcion_hidden_fields.style.display = "flex";
});

var tac_torax_checkbox = document.querySelector("#id_tac_torax");
var tac_torax_normal = document.querySelector("#id_tipo_tac_torax_0");
var tac_torax_patologico = document.querySelector("#id_tipo_tac_torax_1");
var tac_torax_type_hidden_fields = document.querySelector("#tac-torax-type-hidden-fields");
var tac_torax_descripcion_hidden_fields = document.querySelector("#tac-torax-descripcion-hidden-fields");
tac_torax_checkbox.addEventListener("change", function() {
    var tac_torax_subcategory = document.querySelector("#tac-torax-subcategory");
    if (tac_torax_checkbox.checked) {
        tac_torax_type_hidden_fields.style.display = "flex";
        tac_torax_subcategory.classList.add("multiple-category");
    } else {
        tac_torax_type_hidden_fields.style.display = "none";
        tac_torax_subcategory.classList.remove("multiple-category");
        tac_torax_descripcion_hidden_fields.style.display = "none";
        tac_torax_normal.checked = false;
        tac_torax_patologico.checked = false;
    }
});
tac_torax_normal.addEventListener("change", function() {
    tac_torax_descripcion_hidden_fields.style.display = "none";
});
tac_torax_patologico.addEventListener("change", function() {
    tac_torax_descripcion_hidden_fields.style.display = "flex";
});

var ecg_checkbox = document.querySelector("#id_ecg");
var ecg_normal = document.querySelector("#id_tipo_ecg_0");
var ecg_patologico = document.querySelector("#id_tipo_ecg_1");
var ecg_descripcion_hidden_fields = document.querySelector("#ecg-descripcion-hidden-fields");
var ecg_type_hidden_fields = document.querySelector("#ecg-type-hidden-fields");
ecg_checkbox.addEventListener("change", function() {
    var ecg_subcategory = document.querySelector("#ecg-subcategory");
    if (ecg_checkbox.checked) {
        ecg_type_hidden_fields.style.display = "flex";
        ecg_subcategory.classList.add("multiple-category");
    } else {
        ecg_type_hidden_fields.style.display = "none";
        ecg_subcategory.classList.remove("multiple-category");
        ecg_descripcion_hidden_fields.style.display = "none";
        ecg_normal.checked = false;
        ecg_patologico.checked = false;
    }
});
ecg_normal.addEventListener("change", function() {
    ecg_descripcion_hidden_fields.style.display = "none";
});
ecg_patologico.addEventListener("change", function() {
    ecg_descripcion_hidden_fields.style.display = "flex";
});

var pcr_checkbox = document.querySelector("#id_pcr_covid");
var pcr_normal = document.querySelector("#id_tipo_pcr_covid_0");
var pcr_patologico = document.querySelector("#id_tipo_pcr_covid_1");
var pcr_descripcion_hidden_fields = document.querySelector("#pcr-descripcion-hidden-fields");
var pcr_type_hidden_fields = document.querySelector("#pcr-type-hidden-fields");
pcr_checkbox.addEventListener("change", function() {
    var pcr_subcategory = document.querySelector("#pcr-subcategory");
    if (pcr_checkbox.checked) {
        pcr_type_hidden_fields.style.display = "flex";
        pcr_subcategory.classList.add("multiple-category");
    } else {
        pcr_type_hidden_fields.style.display = "none";
        pcr_subcategory.classList.remove("multiple-category");
        pcr_descripcion_hidden_fields.style.display = "none";
        pcr_normal.checked = false;
        pcr_patologico.checked = false;
    }
});
pcr_normal.addEventListener("change", function() {
    pcr_descripcion_hidden_fields.style.display = "none";
});
pcr_patologico.addEventListener("change", function() {
    pcr_descripcion_hidden_fields.style.display = "flex";
});

var arm_checkbox = document.querySelector("#id_arm");
arm_checkbox.addEventListener("change", function() {
    var arm_descripcion_hidden_fields = document.querySelector("#arm-descripcion-hidden-fields");
    var arm_subcategory = document.querySelector("#arm-subcategory");
    if (arm_checkbox.checked) {
        arm_subcategory.classList.add("multiple-category");
        arm_descripcion_hidden_fields.style.display = "flex";
    } else {
        arm_subcategory.classList.remove("multiple-category");
        arm_descripcion_hidden_fields.style.display = "none";
    }
});

var vasopresores_checkbox = document.querySelector("#id_vasopresores");
vasopresores_checkbox.addEventListener("change", function() {
    var vasopresores_descripcion_hidden_fields = document.querySelector("#vasopresores-descripcion-hidden-fields");
    var vasopresores_subcategory = document.querySelector("#vasopresores-subcategory");
    if (vasopresores_checkbox.checked) {
        vasopresores_subcategory.classList.add("multiple-category");
        vasopresores_descripcion_hidden_fields.style.display = "flex";
    } else {
        vasopresores_subcategory.classList.remove("multiple-category");
        vasopresores_descripcion_hidden_fields.style.display = "none";
    }
});