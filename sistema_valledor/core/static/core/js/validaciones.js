////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////Productos/////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function validar_nombre(){
	var nombre = document.getElementById("id_nombre");
    var regex_nombre = /^\w{1,20}(\s\w{1,20})*$/;
	var span_nombre = document.getElementById("id_nombre-invalid");
	nombre.classList.remove("is-valid");
	nombre.classList.remove("is-invalid");
	if(nombre.value.trim().length != 0){
		if(nombre.value.match(regex_nombre)){
			nombre.classList.add("is-valid");
			return true;
		}else{
			span_nombre.innerHTML="Ingrese un nombre valido, sin espacios al principio/final";
			nombre.classList.add("is-invalid");
			nombre.focus();
			return false;
		}
	}else{
		span_nombre.innerHTML="Por favor rellene el campo vacio";
		nombre.classList.add("is-invalid");
		nombre.focus();
		return false;
	}
}

function validar_categoria(){
	var categoria = document.getElementById("id_categoria");
	var span_categoria = document.getElementById("id_categoria-invalid");
	categoria.classList.remove("is-valid");
	categoria.classList.remove("is-invalid");
	if(!categoria.value ==""){
			categoria.classList.add("is-valid");
			return true;
	}else{
		span_categoria.innerHTML="Seleccione una categoria";
		categoria.classList.add("is-invalid");
		categoria.focus();
		return false;
	}
}

function validar_unidad_medida(){
	var unidad_medida = document.getElementById("id_unidad_medida");
	var span_unidad_medida = document.getElementById("id_unidad_medida-invalid");
	unidad_medida.classList.remove("is-valid");
	unidad_medida.classList.remove("is-invalid");
	if(!unidad_medida.value ==""){
			unidad_medida.classList.add("is-valid");
			return true;
	}else{
		span_unidad_medida.innerHTML="Seleccione una opcion";
		unidad_medida.classList.add("is-invalid");
		unidad_medida.focus();
		return false;
	}
}

function validar_precio_venta(){
	var precio_venta = document.getElementById("id_precio");
	var span_precio_venta = document.getElementById("id_precio-invalid");
	var revisar_precio = false;
	precio_venta.classList.remove("is-valid");
	precio_venta.classList.remove("is-invalid");
	    if (precio_venta.value.trim().length != 0){
            if(precio_venta.value.trim()%10 == 0){
               revisar_precio = true;
            }
            if(revisar_precio){
                precio_venta.classList.add("is-valid");
                return true;
            }else{
                span_precio_venta.innerHTML="Redondee la cifra a base 10";
                precio_venta.classList.add("is-invalid");
                precio_venta.focus();
                return false;
            }
        }else{
            span_precio_venta.innerHTML="Rellene el campo correctamente";
            precio_venta.classList.add("is-invalid");
            precio_venta.focus();
            return false;
        }
}

function validar_stock(){
    var stock = document.getElementById("id_stock");
    var span_stock = document.getElementById("id_stock-invalid");
    stock.classList.remove("is-valid");
	stock.classList.remove("is-invalid");
	if(stock.value.trim().length != 0 && stock.value >=0){
	    stock.classList.add("is-valid");
	    return true;
	}else{
	    span_stock.innerHTML="Por favor ingrese un stock valido"
	    stock.classList.add("is-invalid");
	    stock.focus()
	    return false;
	}
}

function validar_precio_oferta(){
	var precio_oferta = document.getElementById("id_precio_oferta");
	var precio_venta = document.getElementById("id_precio");
	var span_precio_oferta = document.getElementById("id_precio_oferta-invalid");
	var revisar = false;
	var oferta = document.getElementById('id_oferta');
	var activado = document.getElementById('id_activado');

	precio_oferta.classList.remove("is-valid");
	precio_oferta.classList.remove("is-invalid");
	    if(oferta.checked && activado.checked){
            if (precio_oferta.value.trim().length != 0 && precio_oferta.value.trim()>0){
                    if(precio_oferta.value.trim()%10 == 0){
                        revisar = true;
                    }
                    if(revisar){
                        if(parseInt(precio_venta.value.trim())>parseInt(precio_oferta.value.trim())){
                            var precio_oferta_descuento = parseInt(precio_venta.value.trim()*0.95);
                            var precio_oferta_descuento_string = precio_oferta_descuento.toString();
                            var eleccion = parseInt(precio_oferta_descuento_string[precio_oferta_descuento_string.length-1]);
                            if(eleccion>=0 && eleccion<=5){
                                precio_oferta_descuento = precio_oferta_descuento-eleccion;
                            }else{
                                precio_oferta_descuento = precio_oferta_descuento+(10-eleccion);
                            }
                            if(precio_oferta.value.trim() <= precio_oferta_descuento){
                                precio_oferta.classList.add("is-valid");
                                return true;
                            }else{
                            span_precio_oferta.innerHTML="La oferta tiene como minimo un 5% de descuento, el precio de oferta como maximo tiene que ser "+precio_oferta_descuento;
                            precio_oferta.classList.add("is-invalid");
                            precio_oferta.focus();
                            return false;
                            }
                        }else{
                            span_precio_oferta.innerHTML="La oferta debe ser menor al precio normal";
                            precio_oferta.classList.add("is-invalid");
                            precio_oferta.focus();
                            return false;
                        }
                    }else{
                    span_precio_oferta.innerHTML="El valor debe ser redondeado";
                    precio_oferta.classList.add("is-invalid");
                    precio_oferta.focus();
                    return false;
                    }
            }else{
                span_precio_oferta.innerHTML="Rellene el campo correctamente, no puede ser 0";
                precio_oferta.classList.add("is-invalid");
                precio_oferta.focus();
                return false;
            }
        }else{
            if (precio_oferta.value.trim().length != 0){
                precio_oferta.classList.add("is-valid");
                return true;
            }else{
                span_precio_oferta.innerHTML="Rellene el campo correctamente";
                precio_oferta.classList.add("is-invalid");
                precio_oferta.focus();
                return false;
            }
        }
}

function validar_stock_activado_y_precio(){
    var stock_validacion = document.getElementById('id_stock');
    var activado = document.getElementById('id_activado');
    var precio_venta = document.getElementById("id_precio");
    var alerta_activado = document.getElementById('alert_activado');
    var div_activado = document.getElementById('div_activado');
    div_activado.hidden = true;
    alerta_activado.innerHTML="";
        if(stock_validacion.value == 0 && activado.checked){
            alerta_activado.innerHTML="El producto no puede estar activado si el stock es 0, desactive el producto.";
            div_activado.hidden = false;
            return false;
        }else if(precio_venta.value == 0 && activado.checked){
            alerta_activado.innerHTML="El producto no puede estar activado si el precio es 0, desactive el producto.";
            div_activado.hidden = false;
            return false;
        }else{
            div_activado.hidden = true;
            alerta_activado.innerHTML="";
            return true;
        }
}

function validar_oferta_activado(){
    var oferta = document.getElementById('id_oferta');
    var activado = document.getElementById('id_activado');
    var precio_oferta = document.getElementById("id_precio_oferta");
    var alert_oferta = document.getElementById('alert_oferta');
    var div_oferta = document.getElementById('div_oferta');
    div_oferta.hidden = true;
    alert_oferta.innerHTML="";
        if(precio_oferta.value == 0 && activado.checked && oferta.checked){
            div_oferta.hidden=false;
            alert_oferta.innerHTML="El producto no puede estar activado si el precio de oferta es 0, desactive la oferta o cambie el precio oferta.";
            return false;
        }else{
            div_oferta.hidden=true;
            alert_oferta.innerHTML="";
            return true;
        }
}


function validar(){

	if(validar_nombre() && validar_precio_venta() && validar_categoria() && validar_unidad_medida() &&
	validar_stock() && validar_precio_oferta() && validar_oferta_activado() && validar_stock_activado_y_precio()){
		return true ;
	}else{
		return false;
	}
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////ACTUALIZAR LOCAL/////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function validar_nombre_local(){
	var nombre_local = document.getElementById("id_nombre_local");
	var span_nombre_local = document.getElementById("id_nombre_local-invalid");
	nombre_local.classList.remove("is-valid");
	nombre_local.classList.remove("is-invalid");
	if(nombre_local.value.trim().length != 0){
        nombre_local.classList.add("is-valid");
        return true;
	}else{
		span_buscar.innerHTML="Por favor rellene el campo";
		span_nombre_local.classList.add("is-invalid");
		span_nombre_local.focus();
		return false;
	}
}

function validar_ubicacion(){
	var ubicacion_local = document.getElementById("id_ubicacion_local");
	var span_ubicacion_local = document.getElementById("id_ubicacion_local-invalid");
	ubicacion_local.classList.remove("is-valid");
	ubicacion_local.classList.remove("is-invalid");
	if(ubicacion_local.value.trim().length != 0){
        ubicacion_local.classList.add("is-valid");
        return true;
	}else{
		span_ubicacion_local.innerHTML="Por favor rellene el campo";
		ubicacion_local.classList.add("is-invalid");
		ubicacion_local.focus();
		return false;
	}
}


function validar_actualizacion_local(){
	if(validar_nombre_local() && validar_ubicacion()){
		return true ;
	}else{
		return false;
	}
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////BARRA BUSCADOR/////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function validar_buscar(){
	var buscar = document.getElementById("buscar_producto");
	var span_buscar = document.getElementById("buscar_producto-invalid");
	buscar.classList.remove("is-valid");
	buscar.classList.remove("is-invalid");
	if(buscar.value.trim().length != 0){
        buscar.classList.add("is-valid");
        return true;
	}else{
		span_buscar.innerHTML="Por favor rellene el campo";
		buscar.classList.add("is-invalid");
		buscar.focus();
		return false;
	}
}

function validar_buscar_local(){
	var id_local = document.getElementById("id_local");
	var span_id_local = document.getElementById("id_local-invalid");
	id_local.classList.remove("is-valid");
	id_local.classList.remove("is-invalid");
	if(!id_local.value ==""){
			id_local.classList.add("is-valid");
			return true;
	}else{
		span_id_local.innerHTML="Seleccione un local";
		id_local.classList.add("is-invalid");
		id_local.focus();
		return false;
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////LOGIN///////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function validar_usuario(){
	var usuario = document.getElementById("id_username");
	var regex_usuario = /^(\d{1,3}(?:\.\d{3}){2}-[\dkK])$/;
	var span_usuario = document.getElementById("id_username-invalid");
	usuario.classList.remove("is-valid");
	usuario.classList.remove("is-invalid");
	    if (usuario.value.trim().length != 0){
            if(usuario.value.match(regex_usuario) || usuario.value == "root"){
                usuario.classList.add("is-valid");
                return true;
            }else{
                span_usuario.innerHTML="Ingrese un rut valido";
                usuario.classList.add("is-invalid");
                usuario.focus();
                return false;
            }
        }else{
            span_usuario.innerHTML="Rellene el campo vacio";
            usuario.classList.add("is-invalid");
            usuario.focus();
            return false;
        }
}

function validar_password(){
	var password = document.getElementById("id_password");
	var span_password = document.getElementById("id_password-invalid");
	password.classList.remove("is-valid");
	password.classList.remove("is-invalid");
	    if (password.value.trim().length != 0){
            password.classList.add("is-valid");
            return true;
        }else{
            span_password.innerHTML="Rellene el campo vacio";
            password.classList.add("is-invalid");
            password.focus();
            return false;
        }
}

function validar_login(){

	if(validar_usuario() && validar_password()){
		return true;
	}else{
		return false;
	}
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////REGISTRO///////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function validar_nombre_registro(){
	var nombre_registro = document.getElementById("id_first_name");
    var regex_nombre = /^[a-zzñáéíóúA-ZÁÉÍÓÚ]{1,20}(\s[a-zzñáéíóúA-ZÁÉÍÓÚ]{1,20})*$/;
	var span_nombre_registro = document.getElementById("id_first_name-invalid");
	nombre_registro.classList.remove("is-valid");
	nombre_registro.classList.remove("is-invalid");
	if(nombre_registro.value.trim().length != 0){
		if(nombre_registro.value.match(regex_nombre)){
			nombre_registro.classList.add("is-valid");
			return true;
		}else{
			span_nombre_registro.innerHTML="Ingrese un nombre valido, sin espacios al principio/final";
			nombre_registro.classList.add("is-invalid");
			nombre_registro.focus();
			return false;
		}
	}else{
		span_nombre_registro.innerHTML="Por favor rellene el campo vacio";
		nombre_registro.classList.add("is-invalid");
		nombre_registro.focus();
		return false;
	}
}

function validar_password_registro(){
	var password_registro = document.getElementById("id_password1");
	var span_password_registro = document.getElementById("id_password1-invalid");
	password_registro.classList.remove("is-valid");
	password_registro.classList.remove("is-invalid");
	validador = 0;
	/*
	var lista_error = document.getElementById("id_password1-invalid");

        if(lista_error.childElementCount > 0){
            var e =lista_error.childElementCount;
            for(var i = 0; i<e;i++){
                lista_error.removeChild(lista_error.children[i]);
            }
        }
        //Errores
	    if(password_registro.value.trim().length == 0){
	    validador=validador+1;
        var error1=document.createElement("li");
        error1.innerHTML="Rellene los campos vacios";
        lista_error.appendChild(error1);
	    }
	 */

	    if (password_registro.value.trim().length != 0){
	        if(password_registro.value.trim().length >=8){
	            if(password_registro.value.trim() >=0 || password_registro.value.trim() <=0 ){
                    span_password_registro.innerHTML="Su contraseña no puede ser completamente numerica";
                    password_registro.classList.add("is-invalid");
                    password_registro.focus();
                    return false;
                }else{
                    password_registro.classList.add("is-valid");
                    return true;
                }
	        }else{
	            span_password_registro.innerHTML="Su contraseña debe tener al menos 8 caracteres";
                password_registro.classList.add("is-invalid");
                password_registro.focus();
                return false;
	        }
        }else{
            span_password_registro.innerHTML="No puede dejar este campo en blanco";
            password_registro.classList.add("is-invalid");
            password_registro.focus();
            return false;
        }
}

function validar_password2_registro(){
	var password2_registro = document.getElementById("id_password2");
	var password_registro = document.getElementById("id_password1");
	var span_password2_registro = document.getElementById("id_password2-invalid");
	password2_registro.classList.remove("is-valid");
	password2_registro.classList.remove("is-invalid");

	    if (password_registro.value.trim() == password2_registro.value.trim()){
            password2_registro.classList.add("is-valid");
            return true;
        }else{
            span_password2_registro.innerHTML="Las contraseñas no coinciden, reviselas por favor";
            password2_registro.classList.add("is-invalid");
            password2_registro.focus();
            return false;
        }
}

function validar_pregunta_secreta(){
	var pregunta_secreta = document.getElementById("id_pregunta_secreta");
	var span_pregunta_secreta = document.getElementById("id_pregunta_secreta-invalid");
	pregunta_secreta.classList.remove("is-valid");
	pregunta_secreta.classList.remove("is-invalid");
	if(!pregunta_secreta.value ==""){
			pregunta_secreta.classList.add("is-valid");
			return true;
	}else{
		span_pregunta_secreta.innerHTML="Seleccione una opcion";
		pregunta_secreta.classList.add("is-invalid");
		pregunta_secreta.focus();
		return false;
	}
}

function validar_respuesta_secreta(){
	var respuesta_secreta = document.getElementById("id_respuesta_secreta");
	var span_respuesta_secreta = document.getElementById("id_respuesta_secreta-invalid");
	respuesta_secreta.classList.remove("is-valid");
	respuesta_secreta.classList.remove("is-invalid");
	    if (respuesta_secreta.value.trim().length != 0){
            respuesta_secreta.classList.add("is-valid");
            return true;
        }else{
            span_respuesta_secreta.innerHTML="Rellene el campo vacio";
            respuesta_secreta.classList.add("is-invalid");
            respuesta_secreta.focus();
            return false;
        }
}

function validar_registro(){

	if(validar_nombre_registro()&& validar_usuario() && validar_password_registro() && validar_password2_registro() && validar_pregunta_secreta() && validar_respuesta_secreta()){
		return true;
	}else{
		return false;
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////AGREGAR OFERTAS///////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function validar_oferta_mostrar(){
	var oferta = document.getElementById("id_oferta");
	var oferta_span = document.getElementById("id_oferta-invalid");
	oferta.classList.remove("is-valid");
	oferta.classList.remove("is-invalid");
	if(oferta.value.trim().length != 0){
        oferta.classList.add("is-valid");
        return true;
	}else{
		oferta_span.innerHTML="Por favor rellene el campo";
		oferta.classList.add("is-invalid");
		oferta.focus();
		return false;
	}
}

function validar_tipo_oferta(){
	var tipo_oferta = document.getElementById("id_tipo_oferta");
	var tipo_oferta_span = document.getElementById("id_tipo_oferta-invalid");
	tipo_oferta.classList.remove("is-valid");
	tipo_oferta.classList.remove("is-invalid");
	if(!tipo_oferta.value ==""){
			tipo_oferta.classList.add("is-valid");
			return true;
	}else{
		tipo_oferta_span.innerHTML="Seleccione una categoria";
		tipo_oferta.classList.add("is-invalid");
		tipo_oferta.focus();
		return false;
	}
}

function validar_agregar_ofertas(){
	if(validar_oferta_mostrar() && validar_tipo_oferta()){
		return true;
	}else{
		return false;
	}
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////AGREGAR LISTAS///////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function validar_nombre_lista(){
	var id_nombre = document.getElementById("id_nombre");
	var span_id_nombre = document.getElementById("id_nombre-invalid");
	id_nombre.classList.remove("is-valid");
	id_nombre.classList.remove("is-invalid");
	if(id_nombre.value.trim().length != 0){
			id_nombre.classList.add("is-valid");
			return true;
	}else{
		span_id_nombre.innerHTML="Por favor rellene el campo vacio";
		id_nombre.classList.add("is-invalid");
		id_nombre.focus();
		return false;
	}
}

function validar_nombre_local_listas(){
	var id_local = document.getElementById("id_local");
	var span_id_local = document.getElementById("id_local-invalid");
	id_local.classList.remove("is-valid");
	id_local.classList.remove("is-invalid");
	if(!id_local.value ==""){
			id_local.classList.add("is-valid");
			return true;
	}else{
		span_id_local.innerHTML="Seleccione un local";
		id_local.classList.add("is-invalid");
		id_local.focus();
		return false;
	}
}

function validar_lista_agregar(){

	if(validar_nombre_lista() && validar_nombre_local_listas()){
		return true;
	}else{
		return false;
	}
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////AGREGAR PRODUCTOS A LAS LISTAS///////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function validar_seleccion_lista(){
	var id_lista = document.getElementById("id_lista");
	if(id_lista != null){
        var span_id_lista = document.getElementById("id_lista-invalid");
        id_lista.classList.remove("is-valid");
        id_lista.classList.remove("is-invalid");
        if(id_lista.value != ""){
                id_lista.classList.add("is-valid");
                return true;
        }else{
            span_id_lista.innerHTML="Seleccione o agregue una lista";
            id_lista.classList.add("is-invalid");
            id_lista.focus();
            return false;
        }
	}else{
	var texto_emergencia = document.getElementById("id_texto_emergencia");
    texto_emergencia.removeAttribute("hidden");
    return false;
	}
}

function validar_cantidad_lista(){
	var id_cantidad = document.getElementById("id_cantidad");
	var span_id_cantidad = document.getElementById("id_cantidad-invalid");
	id_cantidad.classList.remove("is-valid");
	id_cantidad.classList.remove("is-invalid");
	if(parseInt(id_cantidad.value.trim())>0){
			id_cantidad.classList.add("is-valid");
			return true;
	}else{
		span_id_cantidad.innerHTML="Por favor selecciones un valor valido";
		id_cantidad.classList.add("is-invalid");
		id_cantidad.focus();
		return false;
	}
}

function validar_agregar_listas(){

	if(validar_seleccion_lista() && validar_cantidad_lista()){
		return true;
	}else{
		return false;
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////MODIFICAR PRODUCTOS A LAS LISTAS///////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function validar_stock_modificar_productos_de_lista(){
    var stock = document.getElementById("id_cantidad_pedido");
    var span_stock = document.getElementById("id_cantidad_pedido-invalid");
    stock.classList.remove("is-valid");
	stock.classList.remove("is-invalid");
	if(stock.value.trim().length != 0 && stock.value > 0){
	    stock.classList.add("is-valid");
	    return true;
	}else{
	    span_stock.innerHTML="Por favor ingrese un stock valido";
	    stock.classList.add("is-invalid");
	    stock.focus()
	    return false;
	}
}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////REGISTRO DE CLIENTES PREMIUM///////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function validar_buscar_cliente(){
    var cliente = document.getElementById("id_cliente");
    var span_cliente = document.getElementById("id_cliente-invalid");
    cliente.classList.remove("is-valid");
	cliente.classList.remove("is-invalid");
	if(cliente.value.trim().length != 0){
	    cliente.classList.add("is-valid");
	    return true;
	}else{
	    span_cliente.innerHTML="El campo no puede estar en blanco";
	    cliente.classList.add("is-invalid");
	    cliente.focus()
	    return false;
	}
}

function validar_premium(){
    var premium = document.getElementById("id_premium");
    var span_premium = document.getElementById("id_premium-invalid");
    premium.classList.remove("is-valid");
	premium.classList.remove("is-invalid");
	if(premium.value != ""){
	    premium.classList.add("is-valid");
	    return true;
	}else{
	    span_premium.innerHTML="Por favor seleccione una opcion";
	    premium.classList.add("is-invalid");
	    premium.focus()
	    return false;
	}
}

function validar_fecha_inicio(){
    var fecha_inicio = document.getElementById("fecha_inicio");
    var span_fecha_inicio = document.getElementById("fecha_inicio-invalid");
    fecha_inicio.classList.remove("is-valid");
	fecha_inicio.classList.remove("is-invalid");
	if(fecha_inicio.value != ""){
	    fecha_inicio.classList.add("is-valid");
	    return true;
	}else{
	    span_fecha_inicio.innerHTML="Por favor seleccione una fecha valida";
	    fecha_inicio.classList.add("is-invalid");
	    fecha_inicio.focus()
	    return false;
	}
}

function validar_fecha_fin(){
    var fecha_fin = document.getElementById("fecha_fin");
    var span_fecha_fin = document.getElementById("fecha_fin-invalid");
    fecha_fin.classList.remove("is-valid");
	fecha_fin.classList.remove("is-invalid");
	if(fecha_fin.value != ""){
	    fecha_fin.classList.add("is-valid");
	    return true;
	}else{
	    span_fecha_fin.innerHTML="Por favor seleccione una fecha valida";
	    fecha_fin.classList.add("is-invalid");
	    fecha_fin.focus()
	    return false;
	}
}

function validar_fechas(){

	if(validar_fecha_inicio() && validar_fecha_fin()){
		return true;
	}else{
		return false;
	}
}

function validar_estado(){
    var estado = document.getElementById("id_estado");
    var span_estado = document.getElementById("id_estado-invalid");
    estado.classList.remove("is-valid");
	estado.classList.remove("is-invalid");
	if(estado.value != ""){
	    estado.classList.add("is-valid");
	    return true;
	}else{
	    span_estado.innerHTML="Por favor seleccione una opcion";
	    estado.classList.add("is-invalid");
	    estado.focus()
	    return false;
	}
}

function validar_tienda(){
    var tienda = document.getElementById("id_tienda");
    var span_tienda = document.getElementById("id_tienda-invalid");
    tienda.classList.remove("is-valid");
	tienda.classList.remove("is-invalid");
	if(tienda.value != ""){
	    tienda.classList.add("is-valid");
	    return true;
	}else{
	    span_tienda.innerHTML="Por favor seleccione una opcion";
	    tienda.classList.add("is-invalid");
	    tienda.focus()
	    return false;
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////validaciones extras/////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function validar_email(){
	var email = document.getElementById("email");
	var regex_email = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/;
	var span_email = document.getElementById("email-invalid");
	email.classList.remove("is-valid");
	email.classList.remove("is-invalid");
	if(!email.value ==""){
		if(email.value.match(regex_email)){
			email.classList.add("is-valid");
			return true;
		}else{
			span_email.innerHTML="Por favor ingrese un email valido";
			email.classList.add("is-invalid");
			return false;
		}
	}else{
		span_email.innerHTML="Por favor rellene el campo en blanco.";
		email.classList.add("is-invalid");
		return false;
	}
}


function validar_condiciones(){
	var condiciones = document.getElementById("condiciones");
	condiciones.classList.remove("is-valid");
	condiciones.classList.remove("is-invalid");
	if(condiciones.checked){
		condiciones.classList.add("is-valid");
			return true;
	}else{
		condiciones.classList.add("is-invalid");
			return false;
	}
}