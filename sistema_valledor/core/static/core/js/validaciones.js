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
	precio_venta.classList.remove("is-valid");
	precio_venta.classList.remove("is-invalid");
	    if (precio_venta.value.trim().length != 0 && precio_venta.value >=0){
            precio_venta.classList.add("is-valid");
            return true;
        }else{
            span_precio_venta.innerHTML="Rellene el campo correctamente, el precio no puede ser 0";
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
	precio_oferta.classList.remove("is-valid");
	precio_oferta.classList.remove("is-invalid");
	    if (precio_oferta.value.trim().length != 0 && precio_oferta.value >= 0){
            if(precio_venta.value.trim() >= precio_oferta.value.trim()){
                precio_oferta.classList.add("is-valid");
                return true;
            }else{
            span_precio_oferta.innerHTML="El precio de oferta no puede ser mayor al precio normal";
            precio_oferta.classList.add("is-invalid");
            precio_oferta.focus();
            return false;
            }
        }else{
            span_precio_oferta.innerHTML="Rellene el campo correctamente";
            precio_oferta.classList.add("is-invalid");
            precio_oferta.focus();
            return false;
        }
}

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
///////////////////////////////////////////////BUSCAR/////////////////////////////////////////////////////////////////////////////////////////
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

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////LDC///////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function validar_local(){
	var local = document.getElementById("id_local");
	var span_local = document.getElementById("id_local-invalid");
	local.classList.remove("is-valid");
	local.classList.remove("is-invalid");
	if(!local.value ==""){
			local.classList.add("is-valid");
			return true;
	}else{
		span_local.innerHTML="Seleccione un local";
		local.classList.add("is-invalid");
		local.focus();
		return false;
	}
}


function validar_ldc(){

	if(validar_nombre() && validar_local()){
		return true;
	}else{
		return false;
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////PRODUCTOS A COMPRAR///////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function validar_producto(){
	var producto = document.getElementById("id_cod_productos");
	var span_producto = document.getElementById("id_cod_productos-invalid");
	producto.classList.remove("is-valid");
	producto.classList.remove("is-invalid");
	if(!producto.value ==""){
			producto.classList.add("is-valid");
			return true;
	}else{
		span_producto.innerHTML="Seleccione un Producto";
		producto.classList.add("is-invalid");
		producto.focus();
		return false;
	}
}

function validar_cantidad(){
	var cantidad = document.getElementById("id_cantidad");
	var span_cantidad = document.getElementById("id_cantidad-invalid");
	cantidad.classList.remove("is-valid");
	cantidad.classList.remove("is-invalid");
	    if (cantidad.value.trim().length != 0 && cantidad.value >= 0){
            cantidad.classList.add("is-valid");
            return true;
        }else{
            span_cantidad.innerHTML="Rellene el campo correctamente";
            cantidad.classList.add("is-invalid");
            cantidad.focus();
            return false;
        }
}

function validar_productos_comprar(){

	if(validar_producto() && validar_cantidad()){
		return true;
	}else{
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
            if(usuario.value.match(regex_usuario)){
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
/////////////////////////////////////////////Registro///////////////////////////////////////////////////////////////////////////////////////////
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


function validar_registro(){

	if(validar_nombre_registro()&& validar_usuario() && validar_password_registro() && validar_password2_registro()){
		return true;
	}else{
		return false;
	}
}