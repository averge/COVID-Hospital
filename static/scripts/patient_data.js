console.log()

dni_field = document.querySelector("#id_dni");
dni_field.addEventListener("change", function() {
    fetch(
        "/pacientes/api/patient_exists/" + dni_field.value
    ).then(function(response) {
        return response.json();
    }).then(function(json) {
        var data = json["data"];
        var nombre_y_apellido = document.querySelector("#id_nombre_y_apellido");
        var telefono = document.querySelector("#id_telefono");
        var mail = document.querySelector("#id_mail");
        var obra_social = document.querySelector("#id_obra_social");
        var domicilio = document.querySelector("#id_domicilio");
        var nombre_contacto =  document.querySelector("#id_nombre_contacto");
        var apellido_contacto = document.querySelector("#id_apellido_contacto");
        var telefono_contacto = document.querySelector("#id_telefono_contacto");
        var parentesco_contacto = document.querySelector("#id_parentesco_contacto");
        var antecedentes_personales = document.querySelector("#id_antecedentes_personales");
        var anio = data["fecha_nacimiento"];
        var anio_naci = anio.split("-")[0];
        var mes_naci = anio.split("-")[1];
        var dia_naci = anio.split("-")[2];
        var anio_nacimiento = document.querySelector("#id_fecha_nacimiento_year");
        var mes_nacimiento = document.querySelector("#id_fecha_nacimiento_month");
        var dia_nacimiento = document.querySelector("#id_fecha_nacimiento_day");

        if (mes_naci.startsWith("0")) {
            mes_naci = mes_naci.replace("0", "");
        }
        if (dia_naci.startsWith("0")) {
            dia_naci = dia_naci.replace("0", "");
        }

        var list_fecha_nacimiento = [anio_naci, mes_naci, dia_naci];

        option_anio = anio_nacimiento.querySelector("option[value='" + list_fecha_nacimiento[0] + "']");
        option_anio.selected = "selected";
        option_mes = mes_nacimiento.querySelector("option[value='" + list_fecha_nacimiento[1] + "']");
        option_mes.selected = "selected";
        option_dia = dia_nacimiento.querySelector("option[value='" + list_fecha_nacimiento[2] + "']");
        option_dia.selected = "selected";

        nombre_y_apellido.value = data["nombre_y_apellido"];
        nombre_y_apellido.readOnly = "readOnly";
        telefono.value = data["telefono"];
        mail.value = data["mail"];
        obra_social.value = data["obra_social"];
        domicilio.value = data["domicilio"];
        nombre_contacto.value = data["nombre_contacto"];
        apellido_contacto.value = data["apellido_contacto"];
        telefono_contacto.value = data["telefono_contacto"];
        parentesco_contacto.value = data["parentesco_contacto"];
        antecedentes_personales.value = data["antecedentes_personales"];

        var is_new_patient = document.querySelector("#new_patient");
        is_new_patient.setAttribute("value", "false");
    }).catch(function(err) {
        var nombre_y_apellido = document.querySelector("#id_nombre_y_apellido");
        nombre_y_apellido.value = "";
        nombre_y_apellido.readOnly = "";
        var telefono = document.querySelector("#id_telefono");
        telefono.value = "";
        var mail = document.querySelector("#id_mail");
        mail.value = "";
        var obra_social = document.querySelector("#id_obra_social");
        obra_social.value = "";
        var domicilio = document.querySelector("#id_domicilio");
        domicilio.value = "";
        var nombre_contacto =  document.querySelector("#id_nombre_contacto");
        nombre_contacto.value = "";
        var apellido_contacto = document.querySelector("#id_apellido_contacto");
        apellido_contacto.value = "";
        var telefono_contacto = document.querySelector("#id_telefono_contacto");
        telefono_contacto.value = "";
        var parentesco_contacto = document.querySelector("#id_parentesco_contacto");
        parentesco_contacto.value = "";
        var antecedentes_personales = document.querySelector("#id_antecedentes_personales");
        antecedentes_personales.value = "";
        var is_new_patient = document.querySelector("#new_patient");
        is_new_patient.setAttribute("value", "true");
    });
})