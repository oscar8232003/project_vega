-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-07-2019 a las 20:28:18
-- Versión del servidor: 10.1.30-MariaDB
-- Versión de PHP: 7.2.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `django_sistema_valledor`
--
DROP DATABASE IF EXISTS `django_sistema_valledor`;
CREATE DATABASE IF NOT EXISTS `django_sistema_valledor` DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci;
USE `django_sistema_valledor`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add Tipo de Usuarios', 7, 'add_tipo_usuarios'),
(26, 'Can change Tipo de Usuarios', 7, 'change_tipo_usuarios'),
(27, 'Can delete Tipo de Usuarios', 7, 'delete_tipo_usuarios'),
(28, 'Can view Tipo de Usuarios', 7, 'view_tipo_usuarios'),
(29, 'Can add Unidad de Medida', 8, 'add_unidad_medida'),
(30, 'Can change Unidad de Medida', 8, 'change_unidad_medida'),
(31, 'Can delete Unidad de Medida', 8, 'delete_unidad_medida'),
(32, 'Can view Unidad de Medida', 8, 'view_unidad_medida'),
(33, 'Can add Puntos', 9, 'add_puntos'),
(34, 'Can change Puntos', 9, 'change_puntos'),
(35, 'Can delete Puntos', 9, 'delete_puntos'),
(36, 'Can view Puntos', 9, 'view_puntos'),
(37, 'Can add Oferta', 10, 'add_oferta'),
(38, 'Can change Oferta', 10, 'change_oferta'),
(39, 'Can delete Oferta', 10, 'delete_oferta'),
(40, 'Can view Oferta', 10, 'view_oferta'),
(41, 'Can add Categoria', 11, 'add_categoria_productos'),
(42, 'Can change Categoria', 11, 'change_categoria_productos'),
(43, 'Can delete Categoria', 11, 'delete_categoria_productos'),
(44, 'Can view Categoria', 11, 'view_categoria_productos'),
(45, 'Can add Local', 12, 'add_local'),
(46, 'Can change Local', 12, 'change_local'),
(47, 'Can delete Local', 12, 'delete_local'),
(48, 'Can view Local', 12, 'view_local'),
(49, 'Can add Producto', 13, 'add_productos'),
(50, 'Can change Producto', 13, 'change_productos'),
(51, 'Can delete Producto', 13, 'delete_productos'),
(52, 'Can view Producto', 13, 'view_productos'),
(53, 'Can add Producto de la lista', 14, 'add_productos_listas'),
(54, 'Can change Producto de la lista', 14, 'change_productos_listas'),
(55, 'Can delete Producto de la lista', 14, 'delete_productos_listas'),
(56, 'Can view Producto de la lista', 14, 'view_productos_listas'),
(57, 'Can add Listas', 15, 'add_listas'),
(58, 'Can change Listas', 15, 'change_listas'),
(59, 'Can delete Listas', 15, 'delete_listas'),
(60, 'Can view Listas', 15, 'view_listas'),
(61, 'Can add Auditoria de Listas', 16, 'add_registro_listas'),
(62, 'Can change Auditoria de Listas', 16, 'change_registro_listas'),
(63, 'Can delete Auditoria de Listas', 16, 'delete_registro_listas'),
(64, 'Can view Auditoria de Listas', 16, 'view_registro_listas'),
(65, 'Can add Auditoria de Premium', 17, 'add_registro_premium'),
(66, 'Can change Auditoria de Premium', 17, 'change_registro_premium'),
(67, 'Can delete Auditoria de Premium', 17, 'delete_registro_premium'),
(68, 'Can view Auditoria de Premium', 17, 'view_registro_premium'),
(69, 'Can add Registro de Productos', 18, 'add_registro_de_productos'),
(70, 'Can change Registro de Productos', 18, 'change_registro_de_productos'),
(71, 'Can delete Registro de Productos', 18, 'delete_registro_de_productos'),
(72, 'Can view Registro de Productos', 18, 'view_registro_de_productos'),
(73, 'Can add Reporte de Productos', 19, 'add_reporte_productos'),
(74, 'Can change Reporte de Productos', 19, 'change_reporte_productos'),
(75, 'Can delete Reporte de Productos', 19, 'delete_reporte_productos'),
(76, 'Can view Reporte de Productos', 19, 'view_reporte_productos'),
(77, 'Can add Auditoria de Productos', 20, 'add_registro_auditoria_productos'),
(78, 'Can change Auditoria de Productos', 20, 'change_registro_auditoria_productos'),
(79, 'Can delete Auditoria de Productos', 20, 'delete_registro_auditoria_productos'),
(80, 'Can view Auditoria de Productos', 20, 'view_registro_auditoria_productos'),
(81, 'Can add Valorizacion de Pedidos', 21, 'add_valorizacion_pedidos'),
(82, 'Can change Valorizacion de Pedidos', 21, 'change_valorizacion_pedidos'),
(83, 'Can delete Valorizacion de Pedidos', 21, 'delete_valorizacion_pedidos'),
(84, 'Can view Valorizacion de Pedidos', 21, 'view_valorizacion_pedidos'),
(85, 'Can add Reporte de Pedidos', 22, 'add_reporte_listas'),
(86, 'Can change Reporte de Pedidos', 22, 'change_reporte_listas'),
(87, 'Can delete Reporte de Pedidos', 22, 'delete_reporte_listas'),
(88, 'Can view Reporte de Pedidos', 22, 'view_reporte_listas'),
(89, 'Can add Log de Acceso', 23, 'add_log_acceso'),
(90, 'Can change Log de Acceso', 23, 'change_log_acceso'),
(91, 'Can delete Log de Acceso', 23, 'delete_log_acceso'),
(92, 'Can view Log de Acceso', 23, 'view_log_acceso'),
(93, 'Can add Preguntas secretas', 24, 'add_preguntas_secretas'),
(94, 'Can change Preguntas secretas', 24, 'change_preguntas_secretas'),
(95, 'Can delete Preguntas secretas', 24, 'delete_preguntas_secretas'),
(96, 'Can view Preguntas secretas', 24, 'view_preguntas_secretas'),
(97, 'Can add Tabla de Preguntas y Respuestas', 25, 'add_login_respuesta_secreta'),
(98, 'Can change Tabla de Preguntas y Respuestas', 25, 'change_login_respuesta_secreta'),
(99, 'Can delete Tabla de Preguntas y Respuestas', 25, 'delete_login_respuesta_secreta'),
(100, 'Can view Tabla de Preguntas y Respuestas', 25, 'view_login_respuesta_secreta');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) COLLATE utf8_spanish_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_spanish_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_spanish_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$120000$XhK1CpZyFyh1$+7GaT5/wMIpSF2Wc7nBqVaPwTCWAdZkoV/iAXuuI1wE=', '2019-06-29 20:55:02.782175', 1, 'root', 'Admin', '', 'nerd.16@hotmail.cl', 1, 1, '2019-03-22 00:49:11.000000'),
(11, 'pbkdf2_sha256$120000$oL1ldtiU64FF$u8E8L/xFmiriNECE3ovI9UKYi8MoyoRswolQr3z/D6w=', '2019-06-30 23:42:45.554681', 0, '19.169.969-6', 'Oscar', 'Valenzuela', 'nerd.16@hotmail.cl', 0, 1, '2019-03-27 21:47:59.000000'),
(12, 'pbkdf2_sha256$120000$aOBo7duktejv$6VzeZqXY8nk+VP1jdloWwQkyzA3QKU6ahXtAMeMburw=', '2019-06-29 22:38:36.681641', 0, '12.493.793-0', 'Lidia', 'Rojas', '', 0, 1, '2019-03-27 21:48:20.000000'),
(13, 'pbkdf2_sha256$120000$ljKSzUCD3jaj$q+CUtBxOE6xhsid0jVm8bHOVB+HZulb/0NQmAOs7vi0=', '2019-06-17 19:25:42.442930', 0, '19.036.216-7', 'Katherine', '', '', 0, 1, '2019-04-04 01:22:42.392909'),
(14, 'pbkdf2_sha256$120000$kNmI3pFAV6v8$c2TfcY64hgiyC8T7k62PcxtlODYdqZ/ttSiHDIFJK6Y=', '2019-06-27 22:15:56.211459', 0, '19.169.969-7', 'Maria', '', '', 0, 1, '2019-05-01 06:34:12.603680'),
(15, 'pbkdf2_sha256$120000$adiB9kBXzJ11$BfZIqihCGP4CRf8758Resc/v4p+RZsvAqCf4qcWTVFQ=', '2019-05-05 19:22:18.845965', 0, '11.111.111-1', 'prueba', '', '', 0, 1, '2019-05-04 05:10:35.000000'),
(17, 'pbkdf2_sha256$120000$uiTC8ImCE9XR$8BF5M1T/s9EJC9TtGDxrcSqpLrtCKFFCXEkBLmZAH2E=', NULL, 0, '12.493.793-1', '', '', '', 0, 1, '2019-06-06 21:32:43.294778'),
(18, 'pbkdf2_sha256$120000$Ldqwkr7hu8gf$gvhv4RPs7xcJWYbuvlHH3q25TNgob9i4g+uyN5cJAlU=', '2019-06-28 20:03:12.490104', 0, '19.184.388-6', 'Ronald', '', '', 0, 1, '2019-06-28 20:03:00.771334'),
(19, 'pbkdf2_sha256$120000$DFuMTe1s3irl$bVz+eQeYwdgFgEJBi3CZq0bz/vU5kmZAx5dw3HjmLMM=', NULL, 0, '19.036.216-9', 'Regina', '', '', 0, 1, '2019-06-29 02:18:02.719432'),
(20, 'pbkdf2_sha256$120000$rGmZ74fei2QR$P7NbGFoxp7MqcmllVHsuvLu0mFa5IvyuIxH3X5SiCF8=', NULL, 0, '11.123.456-8', 'Monica', '', '', 0, 1, '2019-06-29 06:22:52.907879'),
(21, 'pbkdf2_sha256$120000$pDtJSrDVO4NX$zXJh3CFY0GuX/mwRO46AOuyj3gGMbzdLPqS80V6pWZs=', NULL, 0, '22.123.123-1', 'Morticia', '', '', 0, 1, '2019-06-29 06:36:56.961067'),
(22, 'pbkdf2_sha256$120000$QfkM5SlzEFX1$SXWwxgqkdcPfcUkmYzyz+5cY880x6YEoPXYcwONza+I=', NULL, 0, '22.123.123-2', 'Morticia Valenzuela', '', '', 0, 1, '2019-06-29 06:38:01.947470'),
(23, 'pbkdf2_sha256$120000$SyzY7hQTXgLE$uRmg9Abo0ar+IBHqnLI2c03rx0BmdnhwteoOHE+ZSO0=', NULL, 0, '22.123.123-3', 'Juanita', '', '', 0, 1, '2019-06-29 06:43:31.699839');

--
-- Disparadores `auth_user`
--
DROP TRIGGER IF EXISTS `delete_tipo`;
DELIMITER $$
CREATE TRIGGER `delete_tipo` BEFORE DELETE ON `auth_user` FOR EACH ROW delete from registration_tipo_usuarios where user_id_id = OLD.username
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `ingresar_tipo`;
DELIMITER $$
CREATE TRIGGER `ingresar_tipo` AFTER INSERT ON `auth_user` FOR EACH ROW INSERT INTO registration_tipo_usuarios (tipo_usuario, tipo_premium, fecha_caducidad, user_id_id, fecha_inicio) values("cliente", 0 , '2019-01-01',NEW.id, '2019-01-01')
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente_listas`
--

DROP TABLE IF EXISTS `cliente_listas`;
CREATE TABLE `cliente_listas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `total` int(10) UNSIGNED DEFAULT NULL,
  `fecha_enviado` date DEFAULT NULL,
  `fecha_expiracion` date DEFAULT NULL,
  `local_id` int(11) DEFAULT NULL,
  `comentario_cliente` longtext COLLATE utf8_spanish_ci,
  `comentario_vendedor` longtext COLLATE utf8_spanish_ci,
  `estado_lista` varchar(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `fecha_actualizacion` datetime(6) DEFAULT NULL,
  `cancelaciones` int(10) UNSIGNED,
  `total_marcado` int(10) UNSIGNED,
  `valorizacion` tinyint(1)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `cliente_listas`
--

INSERT INTO `cliente_listas` (`id`, `nombre`, `total`, `fecha_enviado`, `fecha_expiracion`, `local_id`, `comentario_cliente`, `comentario_vendedor`, `estado_lista`, `user_id`, `fecha_actualizacion`, `cancelaciones`, `total_marcado`, `valorizacion`) VALUES
(13, 'Prueba continua', 78000, '2019-06-26', NULL, 1, 'Fono +228232003', 'Armando pedido 24/05/2019', 'normal', 12, '2019-06-27 20:10:37.706200', 5, 0, 0),
(14, 'Prueba para borrar', 0, NULL, NULL, 1, '', NULL, 'normal', 12, '2019-06-27 20:17:40.786466', 5, 0, 0),
(15, 'Preba QA', 1800, '2019-06-27', NULL, 1, '', NULL, 'enviada', 12, '2019-06-27 19:27:38.034465', 5, 0, 0);

--
-- Disparadores `cliente_listas`
--
DROP TRIGGER IF EXISTS `ingresar_datos_pedidos`;
DELIMITER $$
CREATE TRIGGER `ingresar_datos_pedidos` AFTER UPDATE ON `cliente_listas` FOR EACH ROW BEGIN
declare cantidad_productos int;
declare items int;
set cantidad_productos = 0;
set items = 0;

select sum(cantidad)
into cantidad_productos
from cliente_productos_listas
where lista_id = new.id;

select count(*)
into items
from cliente_productos_listas
where lista_id = new.id;

if old.estado_lista = 'lista_retiro' or old.estado_lista = 'armando_pedido' then
if new.estado_lista = 'completada' or new.estado_lista = 'cancelada' or new.estado_lista = 'no_retirada' then

insert into cliente_reporte_listas(lista, local_id, nombre_lista, cliente_id, fecha_registro, total, cantidad_productos, estado, cantidad_items) values (new.id, new.local_id, new.nombre, new.user_id, now(), new.total, cantidad_productos, new.estado_lista, items);
end if;
end if;

END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente_productos_listas`
--

DROP TABLE IF EXISTS `cliente_productos_listas`;
CREATE TABLE `cliente_productos_listas` (
  `id` int(11) NOT NULL,
  `cantidad` int(10) UNSIGNED DEFAULT NULL,
  `comentarios` longtext COLLATE utf8_spanish_ci,
  `precio_producto` int(10) UNSIGNED DEFAULT NULL,
  `lista_id` int(11) DEFAULT NULL,
  `local_id` int(11) DEFAULT NULL,
  `productos_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `producto_marcado` tinyint(1),
  `oferta` tinyint(1)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `cliente_productos_listas`
--

INSERT INTO `cliente_productos_listas` (`id`, `cantidad`, `comentarios`, `precio_producto`, `lista_id`, `local_id`, `productos_id`, `user_id`, `producto_marcado`, `oferta`) VALUES
(12, 20, '', 1800, 13, 1, 17, 12, 0, 1),
(13, 50, '', 300, 13, 1, 4, 12, 0, 1),
(14, 30, '', 900, 13, 1, 23, 12, 0, 0),
(15, 1, '', 1800, 15, 1, 17, 12, 0, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente_registro_premium`
--

DROP TABLE IF EXISTS `cliente_registro_premium`;
CREATE TABLE `cliente_registro_premium` (
  `id` int(11) NOT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_caducidad` date DEFAULT NULL,
  `id_registro_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `premium` int(10) UNSIGNED
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `cliente_registro_premium`
--

INSERT INTO `cliente_registro_premium` (`id`, `fecha_inicio`, `fecha_caducidad`, `id_registro_id`, `user_id`, `premium`) VALUES
(3, '2019-06-07', '2019-07-07', 10, 15, 1),
(4, '2019-06-06', '2019-07-06', 10, 15, 1),
(5, '2019-06-06', '2019-07-06', 5, 11, 3),
(6, '2019-06-07', '2019-07-07', 8, 13, 1),
(7, '2019-06-05', '2019-07-05', 8, 13, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente_reporte_listas`
--

DROP TABLE IF EXISTS `cliente_reporte_listas`;
CREATE TABLE `cliente_reporte_listas` (
  `id` int(11) NOT NULL,
  `lista` int(10) UNSIGNED DEFAULT NULL,
  `nombre_lista` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  `total` int(10) UNSIGNED DEFAULT NULL,
  `cantidad_items` int(10) UNSIGNED DEFAULT NULL,
  `cantidad_productos` int(10) UNSIGNED DEFAULT NULL,
  `estado` varchar(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `cliente_id` int(11) DEFAULT NULL,
  `local_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `cliente_reporte_listas`
--

INSERT INTO `cliente_reporte_listas` (`id`, `lista`, `nombre_lista`, `fecha_registro`, `total`, `cantidad_items`, `cantidad_productos`, `estado`, `cliente_id`, `local_id`) VALUES
(1, 13, 'Prueba continua', '2019-06-21', 245000, 3, 300, 'completada', 12, 1),
(2, 13, 'Prueba continua', '2019-06-21', 101000, 3, 120, 'completada', 12, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente_reporte_productos`
--

DROP TABLE IF EXISTS `cliente_reporte_productos`;
CREATE TABLE `cliente_reporte_productos` (
  `id` int(11) NOT NULL,
  `lista` int(10) UNSIGNED DEFAULT NULL,
  `producto` int(10) UNSIGNED DEFAULT NULL,
  `nombre_producto` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `cantidad` int(10) UNSIGNED DEFAULT NULL,
  `oferta` tinyint(1) DEFAULT NULL,
  `Total` int(10) UNSIGNED DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  `cliente_id` int(11) DEFAULT NULL,
  `local_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `cliente_reporte_productos`
--

INSERT INTO `cliente_reporte_productos` (`id`, `lista`, `producto`, `nombre_producto`, `cantidad`, `oferta`, `Total`, `fecha_registro`, `cliente_id`, `local_id`) VALUES
(1, 13, 6, 'Arroz Marca Chancho', 50, 0, 15000, '2019-06-21', 12, 1),
(2, 13, 17, 'Aceitunas Jumbo', 20, 1, 36000, '2019-06-21', 12, 1),
(3, 13, 17, 'Aceitunas Jumbo', 20, 1, 36000, '2019-06-23', 12, 1),
(4, 13, 4, 'Pasta frola', 50, 1, 15000, '2019-06-23', 12, 1),
(5, 13, 23, 'Azucar Iansa de kilo', 30, 0, 27000, '2019-06-23', 12, 1),
(6, 13, 17, 'Aceitunas Jumbo', 20, 1, 36000, '2019-06-23', 12, 1),
(7, 13, 4, 'Pasta frola', 50, 1, 15000, '2019-06-23', 12, 1),
(8, 13, 23, 'Azucar Iansa de kilo', 30, 0, 27000, '2019-06-23', 12, 1),
(9, 13, 17, 'Aceitunas Jumbo', 20, 1, 36000, '2019-06-26', 12, 1),
(10, 13, 4, 'Pasta frola', 50, 1, 15000, '2019-06-26', 12, 1),
(11, 13, 23, 'Azucar Iansa de kilo', 30, 0, 27000, '2019-06-26', 12, 1),
(12, 13, 17, 'Aceitunas Jumbo', 20, 1, 36000, '2019-06-26', 12, 1),
(13, 13, 4, 'Pasta frola', 50, 1, 15000, '2019-06-26', 12, 1),
(14, 13, 23, 'Azucar Iansa de kilo', 30, 0, 27000, '2019-06-26', 12, 1),
(15, 13, 17, 'Aceitunas Jumbo', 20, 1, 36000, '2019-06-26', 12, 1),
(16, 13, 4, 'Pasta frola', 50, 1, 15000, '2019-06-26', 12, 1),
(17, 13, 23, 'Azucar Iansa de kilo', 30, 0, 27000, '2019-06-26', 12, 1),
(18, 13, 17, 'Aceitunas Jumbo', 20, 1, 36000, '2019-06-26', 12, 1),
(19, 13, 4, 'Pasta frola', 50, 1, 15000, '2019-06-26', 12, 1),
(20, 13, 23, 'Azucar Iansa de kilo', 30, 0, 27000, '2019-06-26', 12, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente_valorizacion_pedidos`
--

DROP TABLE IF EXISTS `cliente_valorizacion_pedidos`;
CREATE TABLE `cliente_valorizacion_pedidos` (
  `id` int(11) NOT NULL,
  `lista` int(10) UNSIGNED DEFAULT NULL,
  `puntuacion` int(10) UNSIGNED DEFAULT NULL,
  `comentarios` longtext COLLATE utf8_spanish_ci,
  `local_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `cliente_valorizacion_pedidos`
--

INSERT INTO `cliente_valorizacion_pedidos` (`id`, `lista`, `puntuacion`, `comentarios`, `local_id`, `user_id`, `fecha_registro`) VALUES
(1, 13, 5, 'Todo super bien', 1, 12, '2019-06-26'),
(3, 13, 4, 'Todo bien!', 1, 12, '2019-06-26');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_spanish_ci,
  `object_repr` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8_spanish_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2019-03-22 22:02:35.576096', '2', '19.169.969-6', 1, '[{\"added\": {}}]', 4, 1),
(2, '2019-03-24 18:16:53.429205', '2', '19.169.969-6', 2, '[{\"changed\": {\"fields\": [\"first_name\", \"last_name\"]}}]', 4, 1),
(3, '2019-03-25 21:15:11.186339', '5', '', 3, '', 4, 1),
(4, '2019-03-25 21:15:11.188339', '4', '20.000.314-4', 3, '', 4, 1),
(5, '2019-03-25 21:17:59.202197', '7', '12.123.345-6', 1, '[{\"added\": {}}]', 4, 1),
(6, '2019-03-25 21:18:07.735391', '7', '12.123.345-6', 2, '[{\"changed\": {\"fields\": [\"first_name\"]}}]', 4, 1),
(7, '2019-03-25 21:18:49.023991', '1', 'root', 2, '[{\"changed\": {\"fields\": [\"first_name\"]}}]', 4, 1),
(8, '2019-03-25 22:13:17.521089', '2', '11.123.456-7, prueba, tipo cliente, premium 0, caduce 2019-03-25', 2, '[{\"changed\": {\"fields\": [\"fecha_caducidad\"]}}]', 7, 1),
(9, '2019-03-25 22:13:23.336355', '2', '11.123.456-7, prueba, tipo cliente, premium 0, caduce 2019-03-25', 2, '[]', 7, 1),
(10, '2019-03-26 00:12:39.405580', '9', '13.123.123-6', 1, '[{\"added\": {}}]', 4, 1),
(11, '2019-03-26 02:19:54.370917', '10', '23.169.969-6', 1, '[{\"added\": {}}]', 4, 1),
(12, '2019-03-27 21:42:12.260691', '3', '12.493.793-0', 3, '', 4, 1),
(13, '2019-03-27 21:42:12.262683', '2', '19.169.969-6', 3, '', 4, 1),
(14, '2019-03-27 21:47:07.888601', '7', '12.123.345-6', 3, '', 4, 1),
(15, '2019-03-27 21:47:27.382606', '8', '11.123.456-7', 3, '', 4, 1),
(16, '2019-03-27 21:47:27.384607', '9', '13.123.123-6', 3, '', 4, 1),
(17, '2019-03-27 21:47:27.386608', '10', '23.169.969-6', 3, '', 4, 1),
(18, '2019-03-27 21:47:59.738750', '11', '19.169.969-6', 1, '[{\"added\": {}}]', 4, 1),
(19, '2019-03-27 21:48:08.410712', '11', '19.169.969-6', 2, '[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\"]}}]', 4, 1),
(20, '2019-03-27 21:48:20.740608', '12', '12.493.793-0', 1, '[{\"added\": {}}]', 4, 1),
(21, '2019-03-27 21:48:26.950186', '12', '12.493.793-0', 2, '[{\"changed\": {\"fields\": [\"first_name\", \"last_name\"]}}]', 4, 1),
(22, '2019-03-27 21:48:34.711821', '5', '19.169.969-6, Oscar, tipo vendedor, premium 0, caduce 2019-03-27', 2, '[{\"changed\": {\"fields\": [\"tipo_usuario\"]}}]', 7, 1),
(23, '2019-03-27 21:48:38.148085', '6', '12.493.793-0, Lidia, tipo cliente, premium 0, caduce 2019-03-27', 2, '[]', 7, 1),
(24, '2019-04-01 01:31:47.468203', '1', 'Kampito', 1, '[{\"added\": {}}]', 12, 1),
(25, '2019-04-01 18:53:02.878521', '3', 'sin nombre', 3, '', 12, 1),
(26, '2019-04-01 19:57:19.005877', '7', 'root, Admin, tipo administrador, premium 0, caduce None', 1, '[{\"added\": {}}]', 7, 1),
(27, '2019-04-01 20:22:20.900561', '1', 'abarrotes', 1, '[{\"added\": {}}]', 11, 1),
(28, '2019-04-01 20:23:33.335890', '3', 'Unidad', 1, '[{\"added\": {}}]', 8, 1),
(29, '2019-04-01 20:23:36.259206', '1', 'Arroz aruba 500gramos', 1, '[{\"added\": {}}]', 13, 1),
(30, '2019-04-01 22:28:48.462824', '1', 'Abarrotes', 2, '[{\"changed\": {\"fields\": [\"categoria\"]}}]', 11, 1),
(31, '2019-04-01 22:29:01.811050', '2', 'Lacteos', 1, '[{\"added\": {}}]', 11, 1),
(32, '2019-04-01 22:29:05.433121', '3', 'Condimentos', 1, '[{\"added\": {}}]', 11, 1),
(33, '2019-04-01 22:29:08.704779', '4', 'Remedios', 1, '[{\"added\": {}}]', 11, 1),
(34, '2019-04-01 22:29:11.936860', '5', 'Infusiones', 1, '[{\"added\": {}}]', 11, 1),
(35, '2019-04-01 22:29:13.929947', '6', 'Cafes', 1, '[{\"added\": {}}]', 11, 1),
(36, '2019-04-01 22:29:17.045459', '7', 'Bolsas', 1, '[{\"added\": {}}]', 11, 1),
(37, '2019-04-01 22:29:21.785710', '8', 'Conservas', 1, '[{\"added\": {}}]', 11, 1),
(38, '2019-04-07 22:36:49.784698', '4', 'Kilo', 1, '[{\"added\": {}}]', 8, 1),
(39, '2019-04-07 22:36:56.910022', '5', 'Gramo', 1, '[{\"added\": {}}]', 8, 1),
(40, '2019-04-07 22:37:01.682144', '6', 'Caja', 1, '[{\"added\": {}}]', 8, 1),
(41, '2019-04-07 22:37:13.384488', '7', 'Docena', 1, '[{\"added\": {}}]', 8, 1),
(42, '2019-04-07 22:37:26.594302', '8', 'Litro', 1, '[{\"added\": {}}]', 8, 1),
(43, '2019-04-07 23:07:33.971676', '8', '19.036.216-7, Katherine, tipo vendedor, premium 0, caduce 2019-04-03', 2, '[{\"changed\": {\"fields\": [\"tipo_usuario\"]}}]', 7, 1),
(44, '2019-04-07 23:10:03.675062', '2', 'Rancho', 1, '[{\"added\": {}}]', 12, 1),
(45, '2019-04-07 23:25:26.458975', '2', 'Rancho', 2, '[]', 12, 1),
(46, '2019-04-17 18:29:39.625785', '5', '19.169.969-6, Oscar, tipo vendedor, premium 3, caduce 2019-03-27', 2, '[{\"changed\": {\"fields\": [\"tipo_premium\"]}}]', 7, 1),
(47, '2019-04-18 00:13:04.063672', '2', 'Rancho', 2, '[{\"changed\": {\"fields\": [\"imagen_banner\"]}}]', 12, 1),
(48, '2019-04-18 00:13:12.785612', '1', 'Kampito', 2, '[{\"changed\": {\"fields\": [\"imagen_banner\"]}}]', 12, 1),
(49, '2019-04-19 04:57:33.675349', '1', 'Kampito', 2, '[{\"changed\": {\"fields\": [\"user\", \"ubicacion_local\"]}}]', 12, 1),
(50, '2019-04-26 00:51:51.047719', '2', 'Rancho', 2, '[{\"changed\": {\"fields\": [\"activado\"]}}]', 12, 1),
(51, '2019-04-26 01:39:15.834629', '2', 'Rancho', 2, '[{\"changed\": {\"fields\": [\"activado\"]}}]', 12, 1),
(52, '2019-04-27 19:57:35.454357', '1', '10% de descuento en conservas con compras arriba de 20000', 1, '[{\"added\": {}}]', 10, 1),
(53, '2019-04-30 17:42:42.278823', '2', 'Rancho', 2, '[{\"changed\": {\"fields\": [\"activado\"]}}]', 12, 1),
(54, '2019-04-30 17:55:46.221529', '2', 'Rancho', 2, '[{\"changed\": {\"fields\": [\"activado\"]}}]', 12, 1),
(55, '2019-05-01 06:34:51.331344', '9', '19.169.969-7, Maria, tipo vendedor, premium 2, caduce 2019-05-01', 2, '[{\"changed\": {\"fields\": [\"tipo_usuario\", \"tipo_premium\"]}}]', 7, 1),
(56, '2019-05-01 06:35:30.557266', '3', 'MegaMax', 1, '[{\"added\": {}}]', 12, 1),
(57, '2019-05-01 06:37:06.350120', '3', 'MegaMax', 2, '[{\"changed\": {\"fields\": [\"activado\"]}}]', 12, 1),
(58, '2019-05-04 04:57:40.135328', '8', '19.036.216-7, Katherine, tipo cliente, premium 0, caduce 2019-04-03', 2, '[{\"changed\": {\"fields\": [\"tipo_usuario\"]}}]', 7, 1),
(59, '2019-05-04 05:01:39.013142', '8', '19.036.216-7, Katherine, tipo vendedor, premium 0, caduce 2019-04-03', 2, '[{\"changed\": {\"fields\": [\"tipo_usuario\"]}}]', 7, 1),
(60, '2019-05-04 05:10:35.334311', '15', '11.111.111-1', 1, '[{\"added\": {}}]', 4, 1),
(61, '2019-05-04 05:10:42.214230', '15', '11.111.111-1', 2, '[{\"changed\": {\"fields\": [\"first_name\"]}}]', 4, 1),
(62, '2019-05-04 05:10:57.147809', '10', '11.111.111-1, prueba, tipo vendedor, premium 0, caduce 2019-05-04', 2, '[{\"changed\": {\"fields\": [\"tipo_usuario\"]}}]', 7, 1),
(63, '2019-05-04 05:11:40.054103', '10', '11.111.111-1, prueba, tipo cliente, premium 0, caduce 2019-05-04', 2, '[{\"changed\": {\"fields\": [\"tipo_usuario\"]}}]', 7, 1),
(64, '2019-05-05 18:51:08.513513', '4', 'Sin definir', 2, '[{\"changed\": {\"fields\": [\"activado\"]}}]', 12, 1),
(65, '2019-05-05 19:21:38.050138', '10', '11.111.111-1, prueba, tipo vendedor, premium 0, caduce 2019-05-04', 2, '[{\"changed\": {\"fields\": [\"tipo_usuario\"]}}]', 7, 1),
(66, '2019-05-05 19:21:50.278088', '4', 'Sin definir', 2, '[{\"changed\": {\"fields\": [\"activado\"]}}]', 12, 1),
(67, '2019-05-15 18:24:36.547547', '1', 'Lista 1', 1, '[{\"added\": {}}]', 15, 1),
(68, '2019-05-15 18:24:59.831770', '2', 'Lista 2', 1, '[{\"added\": {}}]', 15, 1),
(69, '2019-05-15 18:25:17.904615', '3', 'Lista cancelada', 1, '[{\"added\": {}}]', 15, 1),
(70, '2019-05-15 18:26:16.457344', '4', 'Lista armando pedido', 1, '[{\"added\": {}}]', 15, 1),
(71, '2019-05-15 18:26:44.845148', '5', 'Lista Para retirar', 1, '[{\"added\": {}}]', 15, 1),
(72, '2019-05-15 18:27:22.082173', '6', 'Lista Completada', 1, '[{\"added\": {}}]', 15, 1),
(73, '2019-05-15 18:27:54.588001', '7', 'Lista no retirada', 1, '[{\"added\": {}}]', 15, 1),
(74, '2019-05-17 04:10:03.623005', '11', 'Lista 6 de prueba', 2, '[{\"changed\": {\"fields\": [\"local\", \"nombre\", \"total\", \"comentario_cliente\", \"estado_lista\"]}}]', 15, 1),
(75, '2019-05-22 19:38:20.301819', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(76, '2019-05-22 20:00:21.649787', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(77, '2019-05-22 20:00:32.287121', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(78, '2019-05-22 20:06:16.004036', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(79, '2019-05-22 20:09:56.830507', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(80, '2019-05-22 20:10:07.108126', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(81, '2019-05-22 20:10:16.215619', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(82, '2019-05-22 20:17:12.882289', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(83, '2019-05-22 20:17:19.964141', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(84, '2019-05-22 20:17:27.350655', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(85, '2019-05-22 20:17:36.084146', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(86, '2019-05-22 20:17:42.908462', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(87, '2019-05-22 20:17:49.645139', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(88, '2019-05-22 20:18:02.123896', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(89, '2019-05-22 21:41:19.515091', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(90, '2019-05-22 21:46:58.331887', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(91, '2019-05-22 21:55:39.034935', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(92, '2019-05-22 21:58:22.718785', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(93, '2019-05-22 21:58:33.921418', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(94, '2019-05-22 22:01:18.672495', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(95, '2019-05-22 22:01:58.541117', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(96, '2019-05-22 22:04:30.056104', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(97, '2019-05-22 22:09:32.280226', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(98, '2019-05-22 22:09:45.555643', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(99, '2019-05-22 22:22:24.917043', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(100, '2019-05-24 21:56:53.964376', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(101, '2019-05-24 21:57:35.135635', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(102, '2019-05-24 23:29:29.384693', '12', 'Lista para el martes', 2, '[{\"changed\": {\"fields\": [\"estado_lista\"]}}]', 15, 1),
(103, '2019-05-29 18:17:14.556559', '13', 'Prueba continua', 2, '[{\"changed\": {\"fields\": [\"comentario_vendedor\", \"estado_lista\"]}}]', 15, 1),
(104, '2019-06-01 22:07:40.733386', '24', 'Azucar Acuenta', 2, '[{\"changed\": {\"fields\": [\"stock\"]}}]', 13, 1),
(105, '2019-06-01 22:11:13.865683', '24', 'Azucar Acuenta', 2, '[{\"changed\": {\"fields\": [\"stock\", \"maximo_prod_comprar\"]}}]', 13, 1),
(106, '2019-06-01 23:10:44.612553', '1', 'Arroz Tucapel 500gramos', 2, '[{\"changed\": {\"fields\": [\"precio\"]}}]', 13, 1),
(107, '2019-06-01 23:11:01.352174', '1', 'Arroz Tucapel 500gramos', 2, '[{\"changed\": {\"fields\": [\"precio\"]}}]', 13, 1),
(108, '2019-06-06 20:02:09.554337', '5', '19.169.969-6, Oscar, tipo vendedor, premium 3, caduce 2019-06-06', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\", \"fecha_caducidad\"]}}]', 7, 1),
(109, '2019-06-06 20:02:14.967641', '9', '19.169.969-7, Maria, tipo vendedor, premium 2, caduce 2019-05-01', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(110, '2019-06-06 20:25:46.892292', '9', '19.169.969-7, Maria, tipo vendedor, premium 3, caduce 2019-05-01', 2, '[{\"changed\": {\"fields\": [\"tipo_premium\"]}}]', 7, 1),
(111, '2019-06-06 20:27:10.897564', '10', '11.111.111-1, prueba, tipo vendedor, premium 1, caduce 2019-05-04', 2, '[{\"changed\": {\"fields\": [\"tipo_premium\", \"fecha_inicio\"]}}]', 7, 1),
(112, '2019-06-06 20:30:25.039482', '10', '11.111.111-1, prueba, tipo vendedor, premium 1, caduce 2019-05-04', 2, '[]', 7, 1),
(113, '2019-06-06 20:32:01.870328', '10', '11.111.111-1, prueba, tipo vendedor, premium 1, caduce 2019-05-04', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(114, '2019-06-06 20:38:11.689331', '10', '11.111.111-1, prueba, tipo vendedor, premium 1, caduce 2019-05-04', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(115, '2019-06-06 20:53:43.586983', '8', '19.036.216-7, Katherine, tipo vendedor, premium 0, caduce 2019-04-03', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(116, '2019-06-06 20:54:13.241091', '8', '19.036.216-7, Katherine, tipo vendedor, premium 0, caduce 2019-04-03', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(117, '2019-06-06 20:59:31.970904', '9', '19.169.969-7, Maria, tipo vendedor, premium 3, caduce 2019-05-01', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(118, '2019-06-06 21:00:50.916483', '9', '19.169.969-7, Maria, tipo vendedor, premium 3, caduce 2019-05-01', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(119, '2019-06-06 21:01:31.358199', '9', '19.169.969-7, Maria, tipo vendedor, premium 3, caduce 2019-05-01', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(120, '2019-06-06 21:02:36.253414', '9', '19.169.969-7, Maria, tipo vendedor, premium 3, caduce None', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(121, '2019-06-06 21:02:52.851707', '9', '19.169.969-7, Maria, tipo vendedor, premium 3, caduce None', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(122, '2019-06-06 21:02:57.977482', '9', '19.169.969-7, Maria, tipo vendedor, premium 3, caduce None', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(123, '2019-06-06 21:04:24.012394', '5', '19.169.969-6, Oscar, tipo vendedor, premium 3, caduce 2019-06-06', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(124, '2019-06-06 21:07:30.364697', '5', '19.169.969-6, Oscar, tipo vendedor, premium 3, caduce None', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(125, '2019-06-06 21:07:41.855097', '5', '19.169.969-6, Oscar, tipo vendedor, premium 3, caduce None', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(126, '2019-06-06 21:07:54.182383', '8', '19.036.216-7, Katherine, tipo vendedor, premium 1, caduce 2019-04-03', 2, '[{\"changed\": {\"fields\": [\"tipo_premium\", \"fecha_inicio\"]}}]', 7, 1),
(127, '2019-06-06 21:09:04.420128', '5', '19.169.969-6, Oscar, tipo vendedor, premium 3, caduce None', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(128, '2019-06-06 21:10:24.094670', '9', '19.169.969-7, Maria, tipo vendedor, premium 3, caduce None', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(129, '2019-06-06 21:10:44.576157', '9', '19.169.969-7, Maria, tipo vendedor, premium 3, caduce None', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(130, '2019-06-06 21:11:53.558272', '8', '19.036.216-7, Katherine, tipo vendedor, premium 1, caduce None', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(131, '2019-06-06 21:12:02.996164', '8', '19.036.216-7, Katherine, tipo vendedor, premium 1, caduce 2019-07-07', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(132, '2019-06-06 21:13:32.569948', '8', '19.036.216-7, Katherine, tipo vendedor, premium 1, caduce 2019-07-07', 2, '[]', 7, 1),
(133, '2019-06-06 21:13:43.518749', '8', '19.036.216-7, Katherine, tipo vendedor, premium 1, caduce None', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(134, '2019-06-06 21:16:48.034113', '8', '19.036.216-7, Katherine, tipo vendedor, premium 1, caduce None', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(135, '2019-06-06 21:16:55.273732', '8', '19.036.216-7, Katherine, tipo vendedor, premium 1, caduce None', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(136, '2019-06-06 21:19:55.670881', '8', '19.036.216-7, Katherine, tipo vendedor, premium 1, caduce None', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(137, '2019-06-06 21:30:48.051083', '16', '12.493.793-1', 1, '[{\"added\": {}}]', 4, 1),
(138, '2019-06-06 21:32:04.582337', '11', '12.493.793-1, , tipo cliente, premium 0, caduce None', 3, '', 7, 1),
(139, '2019-06-06 21:32:30.204780', '16', '12.493.793-1', 3, '', 4, 1),
(140, '2019-06-06 21:32:43.377787', '17', '12.493.793-1', 1, '[{\"added\": {}}]', 4, 1),
(141, '2019-06-06 21:33:01.567118', '12', '12.493.793-1, , tipo cliente, premium 0, caduce 2019-01-01', 2, '[{\"changed\": {\"fields\": [\"fecha_inicio\"]}}]', 7, 1),
(142, '2019-06-10 17:08:05.782225', '1', 'root', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 1),
(143, '2019-06-29 03:04:39.333088', '1', 'Cuantos hijos tienes?', 1, '[{\"added\": {}}]', 24, 1),
(144, '2019-06-29 03:05:04.719435', '2', 'Cuales son los ultimos 3 digitos de documento de su cedula de identidad?', 1, '[{\"added\": {}}]', 24, 1),
(145, '2019-06-29 06:11:56.605044', '1', 'Cuantos hijos tienes?', 3, '', 24, 1),
(146, '2019-06-29 06:13:57.721047', '3', 'Color favorito?', 1, '[{\"added\": {}}]', 24, 1),
(147, '2019-06-29 06:13:57.764066', '4', 'Color favorito?', 1, '[{\"added\": {}}]', 24, 1),
(148, '2019-06-29 06:14:08.480979', '5', 'Nombre de la primera mascota?', 1, '[{\"added\": {}}]', 24, 1),
(149, '2019-06-29 06:14:18.707117', '3', 'Color favorito?', 3, '', 24, 1),
(150, '2019-06-29 06:14:28.409723', '6', 'Nombre de la madre', 1, '[{\"added\": {}}]', 24, 1),
(151, '2019-06-29 06:14:35.428002', '7', 'Lugar de nacimiento', 1, '[{\"added\": {}}]', 24, 1),
(152, '2019-06-29 06:14:42.410796', '8', 'Lugar de nacimiento de la madre', 1, '[{\"added\": {}}]', 24, 1),
(153, '2019-06-29 06:14:50.775913', '9', 'Nombre de un familiar querido', 1, '[{\"added\": {}}]', 24, 1),
(154, '2019-06-29 06:14:56.455802', '10', 'Nombre de un hijo', 1, '[{\"added\": {}}]', 24, 1),
(155, '2019-06-29 06:15:07.343472', '11', 'Nombre de su primer amor', 1, '[{\"added\": {}}]', 24, 1),
(156, '2019-06-29 06:15:12.160449', '12', 'Nombre de su amor', 1, '[{\"added\": {}}]', 24, 1),
(157, '2019-06-29 06:15:21.216082', '13', 'Comida favorita', 1, '[{\"added\": {}}]', 24, 1),
(158, '2019-06-29 06:15:34.537045', '14', 'Color de pelo favorito', 1, '[{\"added\": {}}]', 24, 1),
(159, '2019-06-29 06:15:40.417151', '15', 'Banda preferida', 1, '[{\"added\": {}}]', 24, 1),
(160, '2019-06-29 06:15:58.105987', '16', 'Nombre de un MMORPG', 1, '[{\"added\": {}}]', 24, 1),
(161, '2019-06-29 06:21:52.889769', '1', 'Cuales son los ultimos 3 digitos de documento de su cedula de identidad? - 823', 1, '[{\"added\": {}}]', 25, 1),
(162, '2019-06-29 19:33:05.630691', '3', 'Nombre de un MMORPG - wow', 1, '[{\"added\": {}}]', 25, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(15, 'cliente', 'listas'),
(14, 'cliente', 'productos_listas'),
(18, 'cliente', 'registro_de_productos'),
(16, 'cliente', 'registro_listas'),
(17, 'cliente', 'registro_premium'),
(22, 'cliente', 'reporte_listas'),
(19, 'cliente', 'reporte_productos'),
(21, 'cliente', 'valorizacion_pedidos'),
(5, 'contenttypes', 'contenttype'),
(23, 'registration', 'log_acceso'),
(25, 'registration', 'login_respuesta_secreta'),
(24, 'registration', 'preguntas_secretas'),
(7, 'registration', 'tipo_usuarios'),
(6, 'sessions', 'session'),
(11, 'vendedor', 'categoria_productos'),
(12, 'vendedor', 'local'),
(10, 'vendedor', 'oferta'),
(13, 'vendedor', 'productos'),
(9, 'vendedor', 'puntos'),
(20, 'vendedor', 'registro_auditoria_productos'),
(8, 'vendedor', 'unidad_medida');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-03-13 20:35:40.419476'),
(2, 'auth', '0001_initial', '2019-03-13 20:35:40.826568'),
(3, 'admin', '0001_initial', '2019-03-13 20:35:40.916589'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-03-13 20:35:40.933592'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-03-13 20:35:40.946595'),
(6, 'contenttypes', '0002_remove_content_type_name', '2019-03-13 20:35:41.005609'),
(7, 'auth', '0002_alter_permission_name_max_length', '2019-03-13 20:35:41.049619'),
(8, 'auth', '0003_alter_user_email_max_length', '2019-03-13 20:35:41.094629'),
(9, 'auth', '0004_alter_user_username_opts', '2019-03-13 20:35:41.112633'),
(10, 'auth', '0005_alter_user_last_login_null', '2019-03-13 20:35:41.142640'),
(11, 'auth', '0006_require_contenttypes_0002', '2019-03-13 20:35:41.145640'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2019-03-13 20:35:41.153641'),
(13, 'auth', '0008_alter_user_username_max_length', '2019-03-13 20:35:41.191651'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2019-03-13 20:35:41.231660'),
(15, 'sessions', '0001_initial', '2019-03-13 20:35:41.254665'),
(16, 'registration', '0001_initial', '2019-03-25 20:33:00.897295'),
(17, 'registration', '0002_auto_20190325_1901', '2019-03-25 22:02:04.498945'),
(18, 'registration', '0003_auto_20190327_2348', '2019-03-28 02:49:01.136325'),
(19, 'vendedor', '0001_initial', '2019-03-29 02:43:20.082180'),
(20, 'vendedor', '0002_auto_20190330_1252', '2019-03-30 15:52:28.325333'),
(21, 'vendedor', '0003_productos_comentario', '2019-03-30 19:07:32.522773'),
(22, 'cliente', '0001_initial', '2019-04-01 15:33:33.178652'),
(23, 'vendedor', '0004_auto_20190401_2324', '2019-04-02 02:24:55.983458'),
(24, 'cliente', '0002_auto_20190401_2329', '2019-04-02 02:30:01.534765'),
(25, 'vendedor', '0005_auto_20190401_2329', '2019-04-02 02:30:01.613796'),
(26, 'vendedor', '0006_oferta_activado', '2019-04-05 21:37:25.414693'),
(27, 'vendedor', '0007_auto_20190407_2004', '2019-04-08 00:04:50.913266'),
(28, 'vendedor', '0008_auto_20190419_0053', '2019-04-19 04:54:02.414035'),
(29, 'vendedor', '0009_local_activado', '2019-04-25 20:32:00.868231'),
(30, 'vendedor', '0010_auto_20190427_0149', '2019-04-27 05:49:46.867783'),
(31, 'vendedor', '0011_auto_20190505_2247', '2019-05-06 02:47:32.030947'),
(32, 'vendedor', '0012_auto_20190514_1433', '2019-05-14 19:05:55.051511'),
(33, 'cliente', '0003_auto_20190514_1509', '2019-05-14 19:09:26.200841'),
(34, 'cliente', '0004_registro_listas_registro_premium', '2019-05-15 05:37:43.882168'),
(35, 'cliente', '0005_listas_fecha_creacion', '2019-05-15 17:19:07.104127'),
(36, 'cliente', '0006_auto_20190515_1355', '2019-05-15 17:55:31.894629'),
(37, 'cliente', '0007_auto_20190516_0121', '2019-05-16 05:21:28.141169'),
(38, 'cliente', '0008_auto_20190516_0124', '2019-05-16 05:24:31.082000'),
(39, 'cliente', '0009_auto_20190519_2343', '2019-05-20 03:43:19.103004'),
(40, 'vendedor', '0013_productos_maximo_prod_comprar', '2019-05-20 03:44:49.263593'),
(41, 'cliente', '0010_productos_listas_producto_marcado', '2019-05-22 17:48:07.531290'),
(42, 'cliente', '0011_listas_cancelaciones', '2019-06-02 00:37:31.881832'),
(43, 'cliente', '0012_auto_20190602_1445', '2019-06-02 18:45:59.424943'),
(44, 'cliente', '0013_auto_20190602_1514', '2019-06-02 19:14:46.202672'),
(45, 'cliente', '0014_listas_total_marcado', '2019-06-02 22:03:53.925414'),
(46, 'cliente', '0015_auto_20190606_1521', '2019-06-06 19:22:01.387881'),
(47, 'registration', '0004_tipo_usuarios_fecha_inicio', '2019-06-06 19:37:14.048769'),
(48, 'cliente', '0016_registro_premium', '2019-06-06 19:51:16.457009'),
(49, 'cliente', '0017_auto_20190606_1557', '2019-06-06 19:57:03.503946'),
(50, 'cliente', '0018_auto_20190616_2227', '2019-06-17 02:27:50.082464'),
(51, 'vendedor', '0014_remove_productos_cambios_restantes', '2019-06-17 02:28:45.249883'),
(52, 'vendedor', '0015_registro_auditoria_productos', '2019-06-17 20:07:16.888489'),
(53, 'cliente', '0019_listas_valorizacion', '2019-06-21 04:26:52.877515'),
(54, 'cliente', '0020_valorizacion_pedidos', '2019-06-21 04:43:50.944794'),
(55, 'cliente', '0021_auto_20190621_1730', '2019-06-21 21:30:46.238709'),
(56, 'cliente', '0022_productos_listas_oferta', '2019-06-21 22:09:12.088783'),
(57, 'cliente', '0023_valorizacion_pedidos_fecha_registro', '2019-06-26 07:01:47.397588'),
(58, 'registration', '0005_log_acceso', '2019-06-27 21:48:47.562134'),
(59, 'registration', '0006_preguntas_secretas', '2019-06-29 02:22:01.649026'),
(60, 'registration', '0007_login_respuesta_secreta', '2019-06-29 02:59:21.903058'),
(61, 'cliente', '0024_auto_20190630_2139', '2019-07-01 01:39:50.021212'),
(62, 'cliente', '0025_auto_20190630_2144', '2019-07-01 01:44:36.517245'),
(63, 'cliente', '0026_auto_20190701_1337', '2019-07-01 17:37:39.811236'),
(64, 'vendedor', '0016_auto_20190701_1341', '2019-07-01 17:41:39.212182'),
(65, 'registration', '0008_auto_20190701_1342', '2019-07-01 17:42:40.574604');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_spanish_ci NOT NULL,
  `session_data` longtext COLLATE utf8_spanish_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('05cepzb109uiq4ys9zr6gyzbpaqfhqda', 'MDFhNzhlMDg5MTIxYTMyZmVhNjA4MmM4OTY4OGQ5OWNjOGViMWRmNDp7InRpcG8iOiJ2ZW5kZWRvciIsInByZW1pdW0iOjMsIl9hdXRoX3VzZXJfaWQiOiIxMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzY1NWU0NGEyOTdlZWM4NjllMjg4MjZiM2VkYTJmZDU3MDcyYTg4YyJ9', '2019-06-25 04:07:37.357691'),
('16jtefushhshfryzc1b3gxwcxfdyd7wd', 'MDFhNzhlMDg5MTIxYTMyZmVhNjA4MmM4OTY4OGQ5OWNjOGViMWRmNDp7InRpcG8iOiJ2ZW5kZWRvciIsInByZW1pdW0iOjMsIl9hdXRoX3VzZXJfaWQiOiIxMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzY1NWU0NGEyOTdlZWM4NjllMjg4MjZiM2VkYTJmZDU3MDcyYTg4YyJ9', '2019-06-07 23:34:15.706395'),
('1vzwaovwjpvr90lczl20zju1bp05itfr', 'N2Q5ZTM2Mjc0YTk3YmIzOTIyNjlhMzQ2YTQ2NjBiYzdhYTcyZDkwOTp7InRpcG8iOiJjbGllbnRlIiwicHJlbWl1bSI6MCwiX2F1dGhfdXNlcl9pZCI6IjEyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0MWY3NWExM2VjNDA4YTEzM2ZjZDJlYWY4ZDNjOGFkM2E3MWU0NzBmIn0=', '2019-07-07 22:04:32.760411'),
('4ordgwyicevyfnb1alruiyj0gaigd74t', 'N2Q5ZTM2Mjc0YTk3YmIzOTIyNjlhMzQ2YTQ2NjBiYzdhYTcyZDkwOTp7InRpcG8iOiJjbGllbnRlIiwicHJlbWl1bSI6MCwiX2F1dGhfdXNlcl9pZCI6IjEyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0MWY3NWExM2VjNDA4YTEzM2ZjZDJlYWY4ZDNjOGFkM2E3MWU0NzBmIn0=', '2019-07-11 05:16:22.590784'),
('4v5iua9xn247kqv4p59ip1le3z5hs3ja', 'MDFhNzhlMDg5MTIxYTMyZmVhNjA4MmM4OTY4OGQ5OWNjOGViMWRmNDp7InRpcG8iOiJ2ZW5kZWRvciIsInByZW1pdW0iOjMsIl9hdXRoX3VzZXJfaWQiOiIxMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzY1NWU0NGEyOTdlZWM4NjllMjg4MjZiM2VkYTJmZDU3MDcyYTg4YyJ9', '2019-07-05 23:01:20.088314'),
('5w2qtc3dg9uzzs5s6bpbrylfb80ykvvw', 'OGUwODgzNWJkNTcxMTI3MzJlNGRiYzc4ZTQ0OGI0ZjUxM2E1ZjJmYzp7InRpcG8iOiJhZG1pbmlzdHJhZG9yIiwicHJlbWl1bSI6MCwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6Ijg2NzQ3NWI0YWU5MmRlZDc0ZGUwYmYxYzU5Y2QxZmE0ZGU2Nzk1MzAifQ==', '2019-06-15 22:45:23.725871'),
('81eld3kyw7jdp43uzdjfevasx010u05p', 'MDFhNzhlMDg5MTIxYTMyZmVhNjA4MmM4OTY4OGQ5OWNjOGViMWRmNDp7InRpcG8iOiJ2ZW5kZWRvciIsInByZW1pdW0iOjMsIl9hdXRoX3VzZXJfaWQiOiIxMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzY1NWU0NGEyOTdlZWM4NjllMjg4MjZiM2VkYTJmZDU3MDcyYTg4YyJ9', '2019-06-16 19:16:55.385709'),
('avwckdx5e5l8hnr6ttn8c1mhpna4z04q', 'OGUwODgzNWJkNTcxMTI3MzJlNGRiYzc4ZTQ0OGI0ZjUxM2E1ZjJmYzp7InRpcG8iOiJhZG1pbmlzdHJhZG9yIiwicHJlbWl1bSI6MCwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6Ijg2NzQ3NWI0YWU5MmRlZDc0ZGUwYmYxYzU5Y2QxZmE0ZGU2Nzk1MzAifQ==', '2019-06-07 21:56:37.274975'),
('l4o3w5t7ih9bwpew9mjko8z4alhrkkg6', 'MDFhNzhlMDg5MTIxYTMyZmVhNjA4MmM4OTY4OGQ5OWNjOGViMWRmNDp7InRpcG8iOiJ2ZW5kZWRvciIsInByZW1pdW0iOjMsIl9hdXRoX3VzZXJfaWQiOiIxMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzY1NWU0NGEyOTdlZWM4NjllMjg4MjZiM2VkYTJmZDU3MDcyYTg4YyJ9', '2019-06-20 01:01:03.444909'),
('lcf0tk8cbxu8tj62vcdvvk33pmvzexya', 'OGUwODgzNWJkNTcxMTI3MzJlNGRiYzc4ZTQ0OGI0ZjUxM2E1ZjJmYzp7InRpcG8iOiJhZG1pbmlzdHJhZG9yIiwicHJlbWl1bSI6MCwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6Ijg2NzQ3NWI0YWU5MmRlZDc0ZGUwYmYxYzU5Y2QxZmE0ZGU2Nzk1MzAifQ==', '2019-06-05 19:37:29.714530'),
('p1shzbjcodtmesdwik7nziyjekm09bhi', 'N2Q5ZTM2Mjc0YTk3YmIzOTIyNjlhMzQ2YTQ2NjBiYzdhYTcyZDkwOTp7InRpcG8iOiJjbGllbnRlIiwicHJlbWl1bSI6MCwiX2F1dGhfdXNlcl9pZCI6IjEyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0MWY3NWExM2VjNDA4YTEzM2ZjZDJlYWY4ZDNjOGFkM2E3MWU0NzBmIn0=', '2019-06-29 03:16:37.027843'),
('pqo0mccskbmr7ym003m24jig0ueelraj', 'OGUwODgzNWJkNTcxMTI3MzJlNGRiYzc4ZTQ0OGI0ZjUxM2E1ZjJmYzp7InRpcG8iOiJhZG1pbmlzdHJhZG9yIiwicHJlbWl1bSI6MCwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6Ijg2NzQ3NWI0YWU5MmRlZDc0ZGUwYmYxYzU5Y2QxZmE0ZGU2Nzk1MzAifQ==', '2019-06-12 18:16:32.038554'),
('prxrr9wwwpmwsax4crncyitkl779y1y7', 'YmMxMGZkMTcxZDBkOTI4NGVhYTUxOGM0ZTcwMmI3NTEyMjBlMDZjYjp7InRpcG8iOiJ2ZW5kZWRvciIsInByZW1pdW0iOjMsIl9hdXRoX3VzZXJfaWQiOiIxMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzY1NWU0NGEyOTdlZWM4NjllMjg4MjZiM2VkYTJmZDU3MDcyYTg4YyIsImlkX3BlcnNvbmEiOjExLCJmZWNoYSI6IjIwMTktMDYtMzAgMjA6Mzk6MjEuNDA5NjU1In0=', '2019-07-15 00:39:21.432660'),
('wbigc0kidrhjz2f3n2n02l488m92i48u', 'NGExZDllMjQ2M2FlZGY1MjE0MzM3OGM0Yjc4YjRhZmFhZWE1YWQ0Yzp7InRpcG8iOiJhZG1pbmlzdHJhZG9yIiwicHJlbWl1bSI6MCwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjE0NjZmNTlhODdhOTU0NDA1NzVkNGZhOWZkOTkxZjhmOGNiNTAxZDAifQ==', '2019-07-01 20:12:35.656307'),
('wly0b0tsglzq4oh8t61j6bifmgawmpwd', 'OGI1NTcwOTM0N2ZiYzNjYmZmNWYyNzBkNzg5ZDlhMzU3NjVhMzEyMzp7Il9hdXRoX3VzZXJfaWQiOiIxMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzY1NWU0NGEyOTdlZWM4NjllMjg4MjZiM2VkYTJmZDU3MDcyYTg4YyJ9', '2019-04-15 01:32:22.207073');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registration_login_respuesta_secreta`
--

DROP TABLE IF EXISTS `registration_login_respuesta_secreta`;
CREATE TABLE `registration_login_respuesta_secreta` (
  `id` int(11) NOT NULL,
  `respuesta` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `pregunta_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `registration_login_respuesta_secreta`
--

INSERT INTO `registration_login_respuesta_secreta` (`id`, `respuesta`, `pregunta_id`, `user_id`) VALUES
(1, '823', 2, 11),
(2, 'AC/DC', 15, 23),
(3, 'wow', 16, 12);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registration_log_acceso`
--

DROP TABLE IF EXISTS `registration_log_acceso`;
CREATE TABLE `registration_log_acceso` (
  `id` int(11) NOT NULL,
  `fecha_registro` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `tipo_cliente` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `registration_log_acceso`
--

INSERT INTO `registration_log_acceso` (`id`, `fecha_registro`, `tipo_cliente`, `user_id`) VALUES
(1, '2019-06-27 18:01:35.459829', 'cliente', 12),
(2, '2019-06-27 18:02:08.562671', 'administrador', 1),
(3, '2019-06-27 18:03:38.687678', 'vendedor', 11),
(4, '2019-06-27 18:06:33.374899', 'cliente', 12),
(5, '2019-06-27 18:14:58.388509', 'cliente', 12),
(6, '2019-06-27 18:15:56.230463', 'vendedor', 14),
(7, '2019-06-27 23:03:09.649849', 'vendedor', 11),
(8, '2019-06-28 16:03:12.508109', 'cliente', 18),
(9, '2019-06-28 23:04:22.794343', 'administrador', 1),
(10, '2019-06-29 02:52:20.355060', 'vendedor', 11),
(11, '2019-06-29 02:57:55.718245', 'administrador', 1),
(12, '2019-06-29 15:32:22.865614', 'administrador', 1),
(13, '2019-06-29 16:55:02.805180', 'administrador', 1),
(14, '2019-06-29 18:04:18.679247', 'cliente', 12),
(15, '2019-06-29 18:36:47.950623', 'cliente', 12),
(16, '2019-06-29 18:37:43.040322', 'cliente', 12),
(17, '2019-06-29 18:38:36.698645', 'cliente', 12),
(18, '2019-06-30 19:42:45.582687', 'vendedor', 11);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registration_preguntas_secretas`
--

DROP TABLE IF EXISTS `registration_preguntas_secretas`;
CREATE TABLE `registration_preguntas_secretas` (
  `id` int(11) NOT NULL,
  `pregunta` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `registration_preguntas_secretas`
--

INSERT INTO `registration_preguntas_secretas` (`id`, `pregunta`) VALUES
(2, 'Cuales son los ultimos 3 digitos de documento de su cedula de identidad?'),
(4, 'Color favorito?'),
(5, 'Nombre de la primera mascota?'),
(6, 'Nombre de la madre'),
(7, 'Lugar de nacimiento'),
(8, 'Lugar de nacimiento de la madre'),
(9, 'Nombre de un familiar querido'),
(10, 'Nombre de un hijo'),
(11, 'Nombre de su primer amor'),
(12, 'Nombre de su amor'),
(13, 'Comida favorita'),
(14, 'Color de pelo favorito'),
(15, 'Banda preferida'),
(16, 'Nombre de un MMORPG');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registration_tipo_usuarios`
--

DROP TABLE IF EXISTS `registration_tipo_usuarios`;
CREATE TABLE `registration_tipo_usuarios` (
  `id` int(11) NOT NULL,
  `tipo_usuario` varchar(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `tipo_premium` int(10) UNSIGNED DEFAULT NULL,
  `fecha_caducidad` date DEFAULT NULL,
  `user_id_id` int(11) NOT NULL,
  `fecha_inicio` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `registration_tipo_usuarios`
--

INSERT INTO `registration_tipo_usuarios` (`id`, `tipo_usuario`, `tipo_premium`, `fecha_caducidad`, `user_id_id`, `fecha_inicio`) VALUES
(5, 'vendedor', 3, '2019-07-06', 11, '2019-06-06'),
(6, 'cliente', 0, '2019-03-27', 12, NULL),
(7, 'administrador', 0, NULL, 1, NULL),
(8, 'vendedor', 1, '2019-07-05', 13, '2019-06-05'),
(9, 'vendedor', 3, NULL, 14, '2019-06-06'),
(10, 'vendedor', 1, '2019-07-06', 15, '2019-06-06'),
(12, 'cliente', 0, '0000-00-00', 17, '2019-06-05'),
(13, 'cliente', 0, '2019-01-01', 18, '2019-01-01'),
(14, 'cliente', 0, '2019-01-01', 19, '2019-01-01'),
(15, 'cliente', 0, '2019-01-01', 20, '2019-01-01'),
(16, 'cliente', 0, '2019-01-01', 21, '2019-01-01'),
(17, 'cliente', 0, '2019-01-01', 22, '2019-01-01'),
(18, 'cliente', 0, '2019-01-01', 23, '2019-01-01');

--
-- Disparadores `registration_tipo_usuarios`
--
DROP TRIGGER IF EXISTS `crear_actualizar_local`;
DELIMITER $$
CREATE TRIGGER `crear_actualizar_local` BEFORE UPDATE ON `registration_tipo_usuarios` FOR EACH ROW BEGIN
declare verificador int;
declare tipo_antiguo varchar(20) ;
declare tipo_nuevo varchar(20);
declare fecha_nueva date;
set verificador = 0;
set tipo_antiguo = old.tipo_usuario;
set tipo_nuevo = new.tipo_usuario;

select count(*)
into verificador
from vendedor_local
where user_id=new.user_id_id;

if tipo_antiguo != tipo_nuevo then
    IF tipo_antiguo = 'cliente' and tipo_nuevo = 'vendedor' THEN
    	if verificador = 0 then
    		insert into vendedor_local (nombre_local, ubicacion_local, imagen_muestra, imagen_banner, user_id, activado) values ("Sin definir", "Sin definir","core/sin_imagen.jpg", "core/sin_imagen.jpg",new.user_id_id, true);
    	else
            update vendedor_local
            set activado = true
            where user_id = new.user_id_id;
        end if;   
    else
        update vendedor_local
        set activado = false
        where user_id = new.user_id_id;

        update vendedor_productos
        set activado = false
        where user_id = new.user_id_id;
     end if;
end if;

#AQUI EMPIEZA EL TRIGGER DE AUDITORIA

if old.fecha_inicio != new.fecha_inicio and new.tipo_premium != 0 and  new.fecha_inicio != '' and new.tipo_usuario = 'vendedor' then

set fecha_nueva = ADDDATE(new.fecha_inicio, INTERVAL 30 DAY);

insert into cliente_registro_premium (premium, fecha_inicio, fecha_caducidad, id_registro_id, user_id) values (new.tipo_premium, new.fecha_inicio, fecha_nueva, new.id, new.user_id_id);

set new.fecha_caducidad = fecha_nueva;
else
set new.fecha_caducidad = '';
end if;

END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor_categoria_productos`
--

DROP TABLE IF EXISTS `vendedor_categoria_productos`;
CREATE TABLE `vendedor_categoria_productos` (
  `id` int(11) NOT NULL,
  `categoria` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `vendedor_categoria_productos`
--

INSERT INTO `vendedor_categoria_productos` (`id`, `categoria`) VALUES
(1, 'Abarrotes'),
(2, 'Lacteos'),
(3, 'Condimentos'),
(4, 'Remedios'),
(5, 'Infusiones'),
(6, 'Cafes'),
(7, 'Bolsas'),
(8, 'Conservas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor_local`
--

DROP TABLE IF EXISTS `vendedor_local`;
CREATE TABLE `vendedor_local` (
  `id` int(11) NOT NULL,
  `nombre_local` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `ubicacion_local` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `imagen_muestra` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `imagen_banner` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `activado` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `vendedor_local`
--

INSERT INTO `vendedor_local` (`id`, `nombre_local`, `ubicacion_local`, `imagen_muestra`, `imagen_banner`, `user_id`, `activado`) VALUES
(1, 'Kampito', 'Calle 48, local 56', 'vendedor/img_tiendas/48417047_768112653535527_9149281488766763008_n.png', 'vendedor/img_tiendas/Mi_Tienda_M8pMWTQ.png', 11, 1),
(2, 'Rancho', 'Calle 48, local 67', 'core/sin_imagen.jpg', 'vendedor/img_tiendas/Mi_Tienda.png', 13, 1),
(3, 'MegaMax', 'Calle 48, local 69', 'vendedor/img_tiendas/descarga.jpg', 'vendedor/Mi_Tienda.png', 14, 1),
(4, 'Sin definir', 'Sin definir', 'core/sin_imagen.jpg', 'core/sin_imagen.jpg', 15, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor_oferta`
--

DROP TABLE IF EXISTS `vendedor_oferta`;
CREATE TABLE `vendedor_oferta` (
  `id` int(11) NOT NULL,
  `oferta` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `tipo_oferta` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `local_id` int(11) DEFAULT NULL,
  `activado` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `vendedor_oferta`
--

INSERT INTO `vendedor_oferta` (`id`, `oferta`, `tipo_oferta`, `local_id`, `activado`) VALUES
(1, '10% de descuento en conservas con compras arriba de 20000', 'convencional', 1, 1),
(3, '10% de descuento en productos de limpieza', 'temporada', 1, 1),
(4, '5% al final de su compra solo por abril', 'general', 1, 1),
(5, '5% de descuento en especias', 'temporada', 1, 1),
(6, '3x2 en sopas instantaneas mercadito', 'rango_diamante', 1, 0),
(7, '10% de descuento en conservas con compras arriba de 20000', 'convencional', 2, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor_productos`
--

DROP TABLE IF EXISTS `vendedor_productos`;
CREATE TABLE `vendedor_productos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `precio` int(10) UNSIGNED DEFAULT NULL,
  `oferta` tinyint(1) DEFAULT NULL,
  `precio_oferta` int(10) UNSIGNED DEFAULT NULL,
  `stock` int(10) UNSIGNED DEFAULT NULL,
  `imagen` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `activado` tinyint(1) DEFAULT NULL,
  `categoria_id` int(11) DEFAULT NULL,
  `unidad_medida_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `comentario` longtext COLLATE utf8_spanish_ci,
  `maximo_prod_comprar` int(10) UNSIGNED
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `vendedor_productos`
--

INSERT INTO `vendedor_productos` (`id`, `nombre`, `precio`, `oferta`, `precio_oferta`, `stock`, `imagen`, `activado`, `categoria_id`, `unidad_medida_id`, `user_id`, `comentario`, `maximo_prod_comprar`) VALUES
(1, 'Arroz Tucapel 500gramos', 900, 0, 0, 2600, 'vendedor/img_productos/7801420220138.png', 1, 1, 3, 11, '', 500),
(4, 'Pasta frola', 600, 1, 300, 400, 'vendedor/img_productos/pastafrola-membrillo-batata-dulce-de-leche-tartas-dulces-D_NQ_NP__eBn8ND8.jpg', 1, 1, 3, 11, '', 60),
(6, 'Arroz Marca Chancho', 300, 0, 0, 0, 'vendedor/img_productos/wmtcl.jpg', 1, 1, 3, 11, '', 50),
(13, 'Pansito', 0, 0, 0, 0, 'core/sin_imagen.jpg', 0, 7, 3, 11, '', 0),
(14, 'Cloro clorinda litro', 990, 0, 0, 200, 'vendedor/img_productos/clorinda-1-lt.jpg', 1, 1, 3, 11, '', 20),
(15, 'Arroz aruba pregraneado 500gr', 540, 0, 0, 100, 'vendedor/img_productos/Arroz_Aruba_Pregraneado_medio_kilo.jpg', 1, 1, 3, 11, '', 10),
(16, 'Pan de molde grande', 1800, 1, 1750, 100, 'vendedor/img_productos/Ideal_Pan_de_Molde_Blanco_Ideal_580_g-500x500.jpg', 1, 1, 3, 11, '', 10),
(17, 'Aceitunas Jumbo', 2000, 1, 1800, 39, 'vendedor/img_productos/Aceituna-Negra.jpg', 1, 8, 4, 11, '', 30),
(18, 'Oregano kilo', 1150, 0, 0, 50, 'vendedor/img_productos/6593e88301bf4c-oregano-x-kilo-481618.jpg', 1, 3, 4, 11, '', 5),
(19, 'Cloro litro', 980, 0, 0, 300, 'core/sin_imagen.jpg', 1, 1, 3, 13, '', 30),
(21, 'Pan de molde', 1800, 1, 1710, 200, 'core/sin_imagen.jpg', 1, 1, 3, 13, '', 20),
(22, 'Aceitunas Jumbo', 2200, 1, 1750, 200, 'core/sin_imagen.jpg', 1, 8, 4, 13, '', 20),
(23, 'Azucar Iansa de kilo', 900, 0, 0, 180, 'vendedor/img_productos/wmtcl_1.jpg', 1, 1, 3, 11, '', 30),
(24, 'Azucar Acuenta', 650, 1, 550, 500, 'vendedor/img_productos/wmtcl_2.jpg', 1, 1, 3, 11, '', 50),
(25, 'Azucar Rubia', 1000, 0, 0, 0, 'vendedor/img_productos/wmtcl_3.jpg', 1, 1, 3, 11, '', 60),
(26, 'Duraznos en conserva wasil', 950, 0, 0, 100, 'vendedor/img_productos/wmtcl_4.jpg', 1, 8, 3, 13, '', 10),
(27, 'Lomito san jose en agua', 1250, 1, 1000, 500, 'vendedor/img_productos/wmtcl_5.jpg', 1, 8, 3, 13, '', 50),
(28, 'Palmitos enteros', 1890, 1, 1550, 180, 'vendedor/img_productos/wmtcl_6.jpg', 1, 8, 3, 13, '', 20),
(29, 'Jurel san jose', 1300, 0, 0, 300, 'vendedor/img_productos/wmtcl_7.jpg', 1, 8, 3, 13, '', 10),
(33, 'Aceite Barato', 5000, 0, 0, 500, 'core/sin_imagen.jpg', 1, 1, 3, 11, '', 50),
(34, 'Porotos burros', 800, 0, 0, 250, 'core/sin_imagen.jpg', 1, 1, 4, 13, '', 25),
(35, 'Lentejas', 1200, 0, 0, 500, 'core/sin_imagen.jpg', 1, 1, 4, 13, '', 50),
(36, 'Garbanzos', 1500, 0, 0, 500, 'core/sin_imagen.jpg', 1, 1, 4, 13, '', 0),
(37, 'Porotos negros', 2000, 0, 0, 100, 'core/sin_imagen.jpg', 1, 1, 4, 13, '', 0),
(38, 'Comida Gaty', 500, 0, 0, 500, 'core/sin_imagen.jpg', 1, 8, 3, 11, '', 50);

--
-- Disparadores `vendedor_productos`
--
DROP TRIGGER IF EXISTS `actualizar_max_productos_compra`;
DELIMITER $$
CREATE TRIGGER `actualizar_max_productos_compra` BEFORE INSERT ON `vendedor_productos` FOR EACH ROW BEGIN
SET new.maximo_prod_comprar=round(new.stock*0.1);
END
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `ingresar_auditoria_prod_actualizar`;
DELIMITER $$
CREATE TRIGGER `ingresar_auditoria_prod_actualizar` AFTER UPDATE ON `vendedor_productos` FOR EACH ROW begin
insert into vendedor_registro_auditoria_productos (producto, vendedor_id, nombre_producto, accion, fecha_registro) values(new.id, new.user_id, new.nombre, 'Update', now());
end
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `ingresar_auditoria_prod_eliminar`;
DELIMITER $$
CREATE TRIGGER `ingresar_auditoria_prod_eliminar` BEFORE DELETE ON `vendedor_productos` FOR EACH ROW begin
insert into vendedor_registro_auditoria_productos (producto, vendedor_id, nombre_producto, accion, fecha_registro) values(old.id, old.user_id, old.nombre, 'Delete', now());
end
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `ingresar_auditoria_productos`;
DELIMITER $$
CREATE TRIGGER `ingresar_auditoria_productos` AFTER INSERT ON `vendedor_productos` FOR EACH ROW BEGIN
insert into vendedor_registro_auditoria_productos (producto, vendedor_id, nombre_producto, accion, fecha_registro) values(new.id, new.user_id, new.nombre, 'Insert', now());

END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor_puntos`
--

DROP TABLE IF EXISTS `vendedor_puntos`;
CREATE TABLE `vendedor_puntos` (
  `id` int(11) NOT NULL,
  `puntos` int(10) UNSIGNED DEFAULT NULL,
  `tipo_cuenta` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `local_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `vendedor_puntos`
--

INSERT INTO `vendedor_puntos` (`id`, `puntos`, `tipo_cuenta`, `local_id`, `user_id`) VALUES
(1, 52, 'Plata', 1, 12);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor_registro_auditoria_productos`
--

DROP TABLE IF EXISTS `vendedor_registro_auditoria_productos`;
CREATE TABLE `vendedor_registro_auditoria_productos` (
  `id` int(11) NOT NULL,
  `producto` int(10) UNSIGNED DEFAULT NULL,
  `nombre_producto` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `accion` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  `vendedor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `vendedor_registro_auditoria_productos`
--

INSERT INTO `vendedor_registro_auditoria_productos` (`id`, `producto`, `nombre_producto`, `accion`, `fecha_registro`, `vendedor_id`) VALUES
(1, 0, 'Porotos burros', 'Insert', '2019-06-17', 13),
(2, 0, 'Lentejas', 'Insert', '2019-06-17', 13),
(3, 0, 'Garbanzos', 'Insert', '2019-06-17', 13),
(4, 37, 'Porotos negros', 'Insert', '2019-06-17', 13),
(5, 20, 'Arroz aruba pregraneado 500gr', 'Delete', '2019-06-17', 13),
(6, 29, 'Jurel san jose', 'Update', '2019-06-17', 13),
(7, 1, 'Arroz Tucapel 500gramos', 'Update', '2019-06-21', 11),
(8, 25, 'Azucar Rubia', 'Update', '2019-06-21', 11),
(9, 6, 'Arroz Marca Chancho', 'Update', '2019-06-21', 11),
(10, 25, 'Azucar Rubia', 'Update', '2019-06-21', 11),
(11, 6, 'Arroz Marca Chancho', 'Update', '2019-06-21', 11),
(12, 17, 'Aceitunas Jumbo', 'Update', '2019-06-21', 11),
(13, 25, 'Azucar Rubia', 'Update', '2019-06-21', 11),
(14, 6, 'Arroz Marca Chancho', 'Update', '2019-06-21', 11),
(15, 17, 'Aceitunas Jumbo', 'Update', '2019-06-21', 11),
(16, 25, 'Azucar Rubia', 'Update', '2019-06-21', 11),
(17, 6, 'Arroz Marca Chancho', 'Update', '2019-06-21', 11),
(18, 17, 'Aceitunas Jumbo', 'Update', '2019-06-21', 11),
(19, 25, 'Azucar Rubia', 'Update', '2019-06-21', 11),
(20, 6, 'Arroz Marca Chancho', 'Update', '2019-06-21', 11),
(21, 17, 'Aceitunas Jumbo', 'Update', '2019-06-21', 11),
(22, 25, 'Azucar Rubia', 'Update', '2019-06-21', 11),
(23, 6, 'Arroz Marca Chancho', 'Update', '2019-06-21', 11),
(24, 17, 'Aceitunas Jumbo', 'Update', '2019-06-21', 11),
(25, 25, 'Azucar Rubia', 'Update', '2019-06-21', 11),
(26, 6, 'Arroz Marca Chancho', 'Update', '2019-06-21', 11),
(27, 17, 'Aceitunas Jumbo', 'Update', '2019-06-21', 11),
(28, 6, 'Arroz Marca Chancho', 'Update', '2019-06-21', 11),
(29, 17, 'Aceitunas Jumbo', 'Update', '2019-06-21', 11),
(30, 6, 'Arroz Marca Chancho', 'Update', '2019-06-21', 11),
(31, 17, 'Aceitunas Jumbo', 'Update', '2019-06-21', 11),
(32, 6, 'Arroz Marca Chancho', 'Update', '2019-06-21', 11),
(33, 17, 'Aceitunas Jumbo', 'Update', '2019-06-21', 11),
(34, 6, 'Arroz Marca Chancho', 'Update', '2019-06-21', 11),
(35, 17, 'Aceitunas Jumbo', 'Update', '2019-06-21', 11),
(36, 6, 'Arroz Marca Chancho', 'Update', '2019-06-21', 11),
(37, 17, 'Aceitunas Jumbo', 'Update', '2019-06-21', 11),
(38, 17, 'Aceitunas Jumbo', 'Update', '2019-06-23', 11),
(39, 4, 'Pasta frola', 'Update', '2019-06-23', 11),
(40, 23, 'Azucar Iansa de kilo', 'Update', '2019-06-23', 11),
(41, 17, 'Aceitunas Jumbo', 'Update', '2019-06-23', 11),
(42, 4, 'Pasta frola', 'Update', '2019-06-23', 11),
(43, 23, 'Azucar Iansa de kilo', 'Update', '2019-06-23', 11),
(44, 17, 'Aceitunas Jumbo', 'Update', '2019-06-23', 11),
(45, 4, 'Pasta frola', 'Update', '2019-06-23', 11),
(46, 23, 'Azucar Iansa de kilo', 'Update', '2019-06-23', 11),
(47, 17, 'Aceitunas Jumbo', 'Update', '2019-06-26', 11),
(48, 4, 'Pasta frola', 'Update', '2019-06-26', 11),
(49, 23, 'Azucar Iansa de kilo', 'Update', '2019-06-26', 11),
(50, 17, 'Aceitunas Jumbo', 'Update', '2019-06-26', 11),
(51, 4, 'Pasta frola', 'Update', '2019-06-26', 11),
(52, 23, 'Azucar Iansa de kilo', 'Update', '2019-06-26', 11),
(53, 17, 'Aceitunas Jumbo', 'Update', '2019-06-26', 11),
(54, 4, 'Pasta frola', 'Update', '2019-06-26', 11),
(55, 23, 'Azucar Iansa de kilo', 'Update', '2019-06-26', 11),
(56, 17, 'Aceitunas Jumbo', 'Update', '2019-06-26', 11),
(57, 4, 'Pasta frola', 'Update', '2019-06-26', 11),
(58, 23, 'Azucar Iansa de kilo', 'Update', '2019-06-26', 11),
(59, 17, 'Aceitunas Jumbo', 'Update', '2019-06-26', 11),
(60, 4, 'Pasta frola', 'Update', '2019-06-26', 11),
(61, 23, 'Azucar Iansa de kilo', 'Update', '2019-06-26', 11),
(62, 17, 'Aceitunas Jumbo', 'Update', '2019-06-27', 11),
(63, 38, 'Comida Gaty', 'Insert', '2019-06-27', 11);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor_unidad_medida`
--

DROP TABLE IF EXISTS `vendedor_unidad_medida`;
CREATE TABLE `vendedor_unidad_medida` (
  `id` int(11) NOT NULL,
  `medida_plural` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `medida_unidad` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `vendedor_unidad_medida`
--

INSERT INTO `vendedor_unidad_medida` (`id`, `medida_plural`, `medida_unidad`) VALUES
(3, 'Unidades', 'Unidad'),
(4, 'Kilos', 'Kilo'),
(5, 'Gramos', 'Gramo'),
(6, 'Cajas', 'Caja'),
(7, 'Docenas', 'Docena'),
(8, 'Litros', 'Litro');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `cliente_listas`
--
ALTER TABLE `cliente_listas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cliente_listas_local_id_55802b9a_fk_vendedor_local_id` (`local_id`),
  ADD KEY `cliente_listas_user_id_a6189135_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `cliente_productos_listas`
--
ALTER TABLE `cliente_productos_listas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cliente_productos_listas_lista_id_f21a9bdf_fk_cliente_listas_id` (`lista_id`),
  ADD KEY `cliente_productos_listas_local_id_4c790852_fk_vendedor_local_id` (`local_id`),
  ADD KEY `cliente_productos_li_productos_id_0ee07e7d_fk_vendedor_` (`productos_id`),
  ADD KEY `cliente_productos_listas_user_id_53abd657_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `cliente_registro_premium`
--
ALTER TABLE `cliente_registro_premium`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cliente_registro_pre_id_registro_id_d1309675_fk_registrat` (`id_registro_id`),
  ADD KEY `cliente_registro_premium_user_id_73bb43e3_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `cliente_reporte_listas`
--
ALTER TABLE `cliente_reporte_listas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cliente_reporte_listas_cliente_id_132a24a5_fk_auth_user_id` (`cliente_id`),
  ADD KEY `cliente_reporte_listas_local_id_a68885d9_fk_vendedor_local_id` (`local_id`);

--
-- Indices de la tabla `cliente_reporte_productos`
--
ALTER TABLE `cliente_reporte_productos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cliente_reporte_productos_cliente_id_09032704_fk_auth_user_id` (`cliente_id`),
  ADD KEY `cliente_reporte_productos_local_id_78037625_fk_vendedor_local_id` (`local_id`);

--
-- Indices de la tabla `cliente_valorizacion_pedidos`
--
ALTER TABLE `cliente_valorizacion_pedidos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cliente_valorizacion_local_id_100241c5_fk_vendedor_` (`local_id`),
  ADD KEY `cliente_valorizacion_pedidos_user_id_6865b9a3_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `registration_login_respuesta_secreta`
--
ALTER TABLE `registration_login_respuesta_secreta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `registration_login_r_pregunta_id_77b62eb0_fk_registrat` (`pregunta_id`),
  ADD KEY `registration_login_r_user_id_3746c3ed_fk_auth_user` (`user_id`);

--
-- Indices de la tabla `registration_log_acceso`
--
ALTER TABLE `registration_log_acceso`
  ADD PRIMARY KEY (`id`),
  ADD KEY `registration_log_acceso_user_id_f84455f5_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `registration_preguntas_secretas`
--
ALTER TABLE `registration_preguntas_secretas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `registration_tipo_usuarios`
--
ALTER TABLE `registration_tipo_usuarios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `registration_tipo_usuarios_user_id_id_f9b8660f_fk_auth_user_id` (`user_id_id`);

--
-- Indices de la tabla `vendedor_categoria_productos`
--
ALTER TABLE `vendedor_categoria_productos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `vendedor_local`
--
ALTER TABLE `vendedor_local`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vendedor_local_user_id_2e7dd27e_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `vendedor_oferta`
--
ALTER TABLE `vendedor_oferta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vendedor_oferta_local_id_c52e67af_fk_vendedor_local_id` (`local_id`);

--
-- Indices de la tabla `vendedor_productos`
--
ALTER TABLE `vendedor_productos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vendedor_productos_categoria_id_26f2a807_fk_vendedor_` (`categoria_id`),
  ADD KEY `vendedor_productos_unidad_medida_id_5c598be4_fk_vendedor_` (`unidad_medida_id`),
  ADD KEY `vendedor_productos_user_id_37c2acd7_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `vendedor_puntos`
--
ALTER TABLE `vendedor_puntos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vendedor_puntos_local_id_f9c09d2b_fk_vendedor_local_id` (`local_id`),
  ADD KEY `vendedor_puntos_user_id_685f2908_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `vendedor_registro_auditoria_productos`
--
ALTER TABLE `vendedor_registro_auditoria_productos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vendedor_registro_au_vendedor_id_d57a4c81_fk_auth_user` (`vendedor_id`);

--
-- Indices de la tabla `vendedor_unidad_medida`
--
ALTER TABLE `vendedor_unidad_medida`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cliente_listas`
--
ALTER TABLE `cliente_listas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `cliente_productos_listas`
--
ALTER TABLE `cliente_productos_listas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `cliente_registro_premium`
--
ALTER TABLE `cliente_registro_premium`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `cliente_reporte_listas`
--
ALTER TABLE `cliente_reporte_listas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `cliente_reporte_productos`
--
ALTER TABLE `cliente_reporte_productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `cliente_valorizacion_pedidos`
--
ALTER TABLE `cliente_valorizacion_pedidos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=163;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT de la tabla `registration_login_respuesta_secreta`
--
ALTER TABLE `registration_login_respuesta_secreta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `registration_log_acceso`
--
ALTER TABLE `registration_log_acceso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `registration_preguntas_secretas`
--
ALTER TABLE `registration_preguntas_secretas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `registration_tipo_usuarios`
--
ALTER TABLE `registration_tipo_usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `vendedor_categoria_productos`
--
ALTER TABLE `vendedor_categoria_productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `vendedor_local`
--
ALTER TABLE `vendedor_local`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `vendedor_oferta`
--
ALTER TABLE `vendedor_oferta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `vendedor_productos`
--
ALTER TABLE `vendedor_productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT de la tabla `vendedor_puntos`
--
ALTER TABLE `vendedor_puntos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `vendedor_registro_auditoria_productos`
--
ALTER TABLE `vendedor_registro_auditoria_productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- AUTO_INCREMENT de la tabla `vendedor_unidad_medida`
--
ALTER TABLE `vendedor_unidad_medida`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `cliente_listas`
--
ALTER TABLE `cliente_listas`
  ADD CONSTRAINT `cliente_listas_local_id_55802b9a_fk_vendedor_local_id` FOREIGN KEY (`local_id`) REFERENCES `vendedor_local` (`id`),
  ADD CONSTRAINT `cliente_listas_user_id_a6189135_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `cliente_productos_listas`
--
ALTER TABLE `cliente_productos_listas`
  ADD CONSTRAINT `cliente_productos_li_productos_id_0ee07e7d_fk_vendedor_` FOREIGN KEY (`productos_id`) REFERENCES `vendedor_productos` (`id`),
  ADD CONSTRAINT `cliente_productos_listas_lista_id_f21a9bdf_fk_cliente_listas_id` FOREIGN KEY (`lista_id`) REFERENCES `cliente_listas` (`id`),
  ADD CONSTRAINT `cliente_productos_listas_local_id_4c790852_fk_vendedor_local_id` FOREIGN KEY (`local_id`) REFERENCES `vendedor_local` (`id`),
  ADD CONSTRAINT `cliente_productos_listas_user_id_53abd657_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `cliente_registro_premium`
--
ALTER TABLE `cliente_registro_premium`
  ADD CONSTRAINT `cliente_registro_pre_id_registro_id_d1309675_fk_registrat` FOREIGN KEY (`id_registro_id`) REFERENCES `registration_tipo_usuarios` (`id`),
  ADD CONSTRAINT `cliente_registro_premium_user_id_73bb43e3_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `cliente_reporte_listas`
--
ALTER TABLE `cliente_reporte_listas`
  ADD CONSTRAINT `cliente_reporte_listas_cliente_id_132a24a5_fk_auth_user_id` FOREIGN KEY (`cliente_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `cliente_reporte_listas_local_id_a68885d9_fk_vendedor_local_id` FOREIGN KEY (`local_id`) REFERENCES `vendedor_local` (`id`);

--
-- Filtros para la tabla `cliente_reporte_productos`
--
ALTER TABLE `cliente_reporte_productos`
  ADD CONSTRAINT `cliente_reporte_productos_cliente_id_09032704_fk_auth_user_id` FOREIGN KEY (`cliente_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `cliente_reporte_productos_local_id_78037625_fk_vendedor_local_id` FOREIGN KEY (`local_id`) REFERENCES `vendedor_local` (`id`);

--
-- Filtros para la tabla `cliente_valorizacion_pedidos`
--
ALTER TABLE `cliente_valorizacion_pedidos`
  ADD CONSTRAINT `cliente_valorizacion_local_id_100241c5_fk_vendedor_` FOREIGN KEY (`local_id`) REFERENCES `vendedor_local` (`id`),
  ADD CONSTRAINT `cliente_valorizacion_pedidos_user_id_6865b9a3_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `registration_login_respuesta_secreta`
--
ALTER TABLE `registration_login_respuesta_secreta`
  ADD CONSTRAINT `registration_login_r_pregunta_id_77b62eb0_fk_registrat` FOREIGN KEY (`pregunta_id`) REFERENCES `registration_preguntas_secretas` (`id`),
  ADD CONSTRAINT `registration_login_r_user_id_3746c3ed_fk_auth_user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `registration_log_acceso`
--
ALTER TABLE `registration_log_acceso`
  ADD CONSTRAINT `registration_log_acceso_user_id_f84455f5_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `registration_tipo_usuarios`
--
ALTER TABLE `registration_tipo_usuarios`
  ADD CONSTRAINT `registration_tipo_usuarios_user_id_id_f9b8660f_fk_auth_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `vendedor_local`
--
ALTER TABLE `vendedor_local`
  ADD CONSTRAINT `vendedor_local_user_id_2e7dd27e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `vendedor_oferta`
--
ALTER TABLE `vendedor_oferta`
  ADD CONSTRAINT `vendedor_oferta_local_id_c52e67af_fk_vendedor_local_id` FOREIGN KEY (`local_id`) REFERENCES `vendedor_local` (`id`);

--
-- Filtros para la tabla `vendedor_productos`
--
ALTER TABLE `vendedor_productos`
  ADD CONSTRAINT `vendedor_productos_categoria_id_26f2a807_fk_vendedor_` FOREIGN KEY (`categoria_id`) REFERENCES `vendedor_categoria_productos` (`id`),
  ADD CONSTRAINT `vendedor_productos_unidad_medida_id_5c598be4_fk_vendedor_` FOREIGN KEY (`unidad_medida_id`) REFERENCES `vendedor_unidad_medida` (`id`),
  ADD CONSTRAINT `vendedor_productos_user_id_37c2acd7_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `vendedor_puntos`
--
ALTER TABLE `vendedor_puntos`
  ADD CONSTRAINT `vendedor_puntos_local_id_f9c09d2b_fk_vendedor_local_id` FOREIGN KEY (`local_id`) REFERENCES `vendedor_local` (`id`),
  ADD CONSTRAINT `vendedor_puntos_user_id_685f2908_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `vendedor_registro_auditoria_productos`
--
ALTER TABLE `vendedor_registro_auditoria_productos`
  ADD CONSTRAINT `vendedor_registro_au_vendedor_id_d57a4c81_fk_auth_user` FOREIGN KEY (`vendedor_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
