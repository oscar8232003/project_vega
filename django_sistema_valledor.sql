-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-04-2019 a las 02:23:45
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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

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
(60, 'Can view Listas', 15, 'view_listas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

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
(1, 'pbkdf2_sha256$120000$0C8ZHBxllSGb$tjUdwZjGYRgtfdG54LsjO62448oDR1vvM4E2Z0oHAL4=', '2019-04-07 23:24:35.469220', 1, 'root', 'Admin', '', 'nerd.16@hotmail.cl', 1, 1, '2019-03-22 00:49:11.000000'),
(11, 'pbkdf2_sha256$120000$oL1ldtiU64FF$u8E8L/xFmiriNECE3ovI9UKYi8MoyoRswolQr3z/D6w=', '2019-04-08 00:11:45.494827', 0, '19.169.969-6', 'Oscar', 'Valenzuela', 'nerd.16@hotmail.cl', 0, 1, '2019-03-27 21:47:59.000000'),
(12, 'pbkdf2_sha256$120000$aOBo7duktejv$6VzeZqXY8nk+VP1jdloWwQkyzA3QKU6ahXtAMeMburw=', '2019-04-07 18:33:32.740666', 0, '12.493.793-0', 'Lidia', 'Rojas', '', 0, 1, '2019-03-27 21:48:20.000000'),
(13, 'pbkdf2_sha256$120000$ljKSzUCD3jaj$q+CUtBxOE6xhsid0jVm8bHOVB+HZulb/0NQmAOs7vi0=', '2019-04-08 00:12:31.988729', 0, '19.036.216-7', 'Katherine', '', '', 0, 1, '2019-04-04 01:22:42.392909');

--
-- Disparadores `auth_user`
--
DELIMITER $$
CREATE TRIGGER `delete_tipo` BEFORE DELETE ON `auth_user` FOR EACH ROW delete from registration_tipo_usuarios where user_id_id = OLD.username
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `insertar_tipo` AFTER INSERT ON `auth_user` FOR EACH ROW insert into registration_tipo_usuarios (tipo_usuario, tipo_premium, fecha_caducidad, user_id_id) values ("cliente", 0, now(), new.id)
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente_listas`
--

CREATE TABLE `cliente_listas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `total` int(10) UNSIGNED DEFAULT NULL,
  `fecha_enviado` date DEFAULT NULL,
  `fecha_expiracion` date DEFAULT NULL,
  `comentarios` longtext COLLATE utf8_spanish_ci,
  `estado` tinyint(1) DEFAULT NULL,
  `local_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente_productos_listas`
--

CREATE TABLE `cliente_productos_listas` (
  `id` int(11) NOT NULL,
  `cantidad` int(10) UNSIGNED DEFAULT NULL,
  `comentarios` longtext COLLATE utf8_spanish_ci,
  `precio_producto` int(10) UNSIGNED DEFAULT NULL,
  `lista_id` int(11) DEFAULT NULL,
  `local_id` int(11) DEFAULT NULL,
  `productos_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

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
(45, '2019-04-07 23:25:26.458975', '2', 'Rancho', 2, '[]', 12, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

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
(5, 'contenttypes', 'contenttype'),
(7, 'registration', 'tipo_usuarios'),
(6, 'sessions', 'session'),
(11, 'vendedor', 'categoria_productos'),
(12, 'vendedor', 'local'),
(10, 'vendedor', 'oferta'),
(13, 'vendedor', 'productos'),
(9, 'vendedor', 'puntos'),
(8, 'vendedor', 'unidad_medida');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

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
(27, 'vendedor', '0007_auto_20190407_2004', '2019-04-08 00:04:50.913266');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_spanish_ci NOT NULL,
  `session_data` longtext COLLATE utf8_spanish_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('9docuovavoa5x920pw6dx3gx82pdanyr', 'NTNiZmEyNmE0NWI5ODk5MzQ5NTVmZjdmMWJmZGMzMzZiNTE5MmYzMjp7InRpcG8iOm51bGwsInByZW1pdW0iOjB9', '2019-04-22 00:12:54.152741'),
('wly0b0tsglzq4oh8t61j6bifmgawmpwd', 'OGI1NTcwOTM0N2ZiYzNjYmZmNWYyNzBkNzg5ZDlhMzU3NjVhMzEyMzp7Il9hdXRoX3VzZXJfaWQiOiIxMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzY1NWU0NGEyOTdlZWM4NjllMjg4MjZiM2VkYTJmZDU3MDcyYTg4YyJ9', '2019-04-15 01:32:22.207073');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registration_tipo_usuarios`
--

CREATE TABLE `registration_tipo_usuarios` (
  `id` int(11) NOT NULL,
  `tipo_usuario` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `tipo_premium` int(10) UNSIGNED DEFAULT NULL,
  `fecha_caducidad` date DEFAULT NULL,
  `user_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `registration_tipo_usuarios`
--

INSERT INTO `registration_tipo_usuarios` (`id`, `tipo_usuario`, `tipo_premium`, `fecha_caducidad`, `user_id_id`) VALUES
(5, 'vendedor', 0, '2019-03-27', 11),
(6, 'cliente', 0, '2019-03-27', 12),
(7, 'administrador', 0, NULL, 1),
(8, 'vendedor', 0, '2019-04-03', 13);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor_categoria_productos`
--

CREATE TABLE `vendedor_categoria_productos` (
  `id` int(11) NOT NULL,
  `categoria` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL
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

CREATE TABLE `vendedor_local` (
  `id` int(11) NOT NULL,
  `nombre_local` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `ubicacion_local` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `imagen_muestra` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `imagen_banner` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `vendedor_local`
--

INSERT INTO `vendedor_local` (`id`, `nombre_local`, `ubicacion_local`, `imagen_muestra`, `imagen_banner`, `user_id`) VALUES
(1, 'Kampito', 'Calle 48, local 56', 'vendedor/img_tiendas/sin_imagen.jpg', 'vendedor/img_tiendas/sin_imagen_kjompAj.jpg', 11),
(2, 'Rancho', 'Calle 48, local 67', 'core/sin_imagen.jpg', 'core/sin_imagen.jpg', 13);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor_oferta`
--

CREATE TABLE `vendedor_oferta` (
  `id` int(11) NOT NULL,
  `oferta` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `tipo_oferta` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `local_id` int(11) DEFAULT NULL,
  `activado` tinyint(1)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor_productos`
--

CREATE TABLE `vendedor_productos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `precio` int(10) UNSIGNED DEFAULT NULL,
  `oferta` tinyint(1) DEFAULT NULL,
  `precio_oferta` int(10) UNSIGNED DEFAULT NULL,
  `stock` int(10) UNSIGNED DEFAULT NULL,
  `imagen` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `cambios_restantes` int(10) UNSIGNED DEFAULT NULL,
  `activado` tinyint(1) DEFAULT NULL,
  `categoria_id` int(11) DEFAULT NULL,
  `unidad_medida_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `comentario` longtext COLLATE utf8_spanish_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `vendedor_productos`
--

INSERT INTO `vendedor_productos` (`id`, `nombre`, `precio`, `oferta`, `precio_oferta`, `stock`, `imagen`, `cambios_restantes`, `activado`, `categoria_id`, `unidad_medida_id`, `user_id`, `comentario`) VALUES
(1, 'Arroz Tucapel 500gramos', 900, 0, 0, 50, 'vendedor/img_productos/7801420220138.png', 3, 1, 1, 3, 11, ''),
(3, 'Pan de Molde', 1800, 0, 0, 250, 'core/sin_imagen.jpg', 3, 1, 1, 3, 11, ''),
(4, 'Pasta frola', 600, 1, 300, 600, 'core/sin_imagen.jpg', 3, 1, 1, 3, 11, ''),
(6, 'Arroz Marca Chancho', 300, 0, 0, 500, 'core/sin_imagen.jpg', 3, 1, 1, 3, 11, ''),
(13, 'Pansito', 0, 0, 0, 0, 'core/sin_imagen.jpg', 3, 0, 7, 3, 11, ''),
(14, 'Cloro clorinda litro', 990, 0, 0, 200, 'vendedor/img_productos/clorinda-1-lt.jpg', 3, 1, 1, 3, 11, ''),
(15, 'Arroz aruba pregraneado 500gr', 540, 0, 0, 100, 'vendedor/img_productos/Arroz_Aruba_Pregraneado_medio_kilo.jpg', 3, 1, 1, 3, 11, ''),
(16, 'Pan de molde grande', 1800, 1, 1750, 100, 'vendedor/img_productos/Ideal_Pan_de_Molde_Blanco_Ideal_580_g-500x500.jpg', 3, 1, 1, 3, 11, ''),
(17, 'Aceitunas Jumbo', 2000, 1, 1800, 300, 'vendedor/img_productos/Aceituna-Negra.jpg', 3, 1, 8, 4, 11, ''),
(18, 'Oregano kilo', 1150, 0, 0, 50, 'vendedor/img_productos/6593e88301bf4c-oregano-x-kilo-481618.jpg', 3, 1, 3, 4, 11, ''),
(19, 'Cloro litro', 980, 0, 0, 300, 'core/sin_imagen.jpg', 3, 1, 1, 3, 13, ''),
(20, 'Arroz aruba pregraneado 500gr', 550, 0, 0, 100, 'core/sin_imagen.jpg', 3, 1, 1, 3, 13, ''),
(21, 'Pan de molde', 1800, 1, 1750, 200, 'core/sin_imagen.jpg', 3, 1, 1, 3, 13, ''),
(22, 'Aceitunas Jumbo', 2200, 1, 1750, 200, 'core/sin_imagen.jpg', 3, 1, 8, 4, 13, '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor_puntos`
--

CREATE TABLE `vendedor_puntos` (
  `id` int(11) NOT NULL,
  `puntos` int(10) UNSIGNED DEFAULT NULL,
  `tipo_cuenta` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `local_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor_unidad_medida`
--

CREATE TABLE `vendedor_unidad_medida` (
  `id` int(11) NOT NULL,
  `medida_plural` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `medida_unidad` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL
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
  ADD KEY `cliente_listas_local_id_55802b9a_fk_vendedor_local_id` (`local_id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cliente_productos_listas`
--
ALTER TABLE `cliente_productos_listas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `registration_tipo_usuarios`
--
ALTER TABLE `registration_tipo_usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `vendedor_categoria_productos`
--
ALTER TABLE `vendedor_categoria_productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `vendedor_local`
--
ALTER TABLE `vendedor_local`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `vendedor_oferta`
--
ALTER TABLE `vendedor_oferta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `vendedor_productos`
--
ALTER TABLE `vendedor_productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT de la tabla `vendedor_puntos`
--
ALTER TABLE `vendedor_puntos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

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
  ADD CONSTRAINT `cliente_listas_local_id_55802b9a_fk_vendedor_local_id` FOREIGN KEY (`local_id`) REFERENCES `vendedor_local` (`id`);

--
-- Filtros para la tabla `cliente_productos_listas`
--
ALTER TABLE `cliente_productos_listas`
  ADD CONSTRAINT `cliente_productos_li_productos_id_0ee07e7d_fk_vendedor_` FOREIGN KEY (`productos_id`) REFERENCES `vendedor_productos` (`id`),
  ADD CONSTRAINT `cliente_productos_listas_lista_id_f21a9bdf_fk_cliente_listas_id` FOREIGN KEY (`lista_id`) REFERENCES `cliente_listas` (`id`),
  ADD CONSTRAINT `cliente_productos_listas_local_id_4c790852_fk_vendedor_local_id` FOREIGN KEY (`local_id`) REFERENCES `vendedor_local` (`id`),
  ADD CONSTRAINT `cliente_productos_listas_user_id_53abd657_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

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
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
