<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/documentation/article/editing-wp-config-php/
 *
 * @package WordPressection.blog-hdr{background:var(--color-primary);padding:10px 0 57px 0!important}.blog-hdr h1{color:#fff;margin-bottom:0;text-align:center}.breadcrumb.brdcrm-dark{padding:10px 0!important;margin-bottom:0;background:var(--color-primary);border-radius:0;border-bottom:1px solid var(--color-primary)}.brdcrm-dark .breadcrumb{background:var(--color-primary)}.brdcrm-dark a{color:#fff}.brdcrm-dark .breadcrumb-item+.breadcrumb-item::before{color:#fff}.blog-body{background:var(--color-light-primary)}.blogfilter .form-control,.result{background:0 0;border:1px solid #000;border-radius:10px;font-size:18px;color:#00000085;font-weight:500}.submit-srch img{width:19px;object-fit:cover;position:absolute;top:11px;right:30px}.blog-body .container{padding:0 150px}.blog-tabs{box-shadow:8px 8px 24px 0 #00000012;background:#fff;border-radius:35px;padding:25px;margin:2%;height:100%}.blog__posts .col-lg-4{margin-bottom:calc(2% + 30px)}img.img-fluid.blog__landing{height:200px;object-fit:cover;border-radius:25px;width:100%;margin:0}.title-blog{font-size:18px;font-weight:600;line-height:25px;margin:20px 0}.date-blog-posted{color:#000;position:absolute;bottom:10px}section.blog-article-content{margin-bottom:70px}.brdcrm-dark .breadcrumb-item+.breadcrumb-item::before{float:none}.posts-disp{background:#ebe2fb;padding:15px;margin-bottom:20px}.blog-botm-h3{margin-bottom:30px}.breadcrumb-item.active{color:#fff}.date-read-time{display:flex;justify-content:space-between;color:#fff}.stick-sidebar{position:sticky;top:100px}.tab-content{margin-bottom:10px}.table-contents ol{padding-left:16px}.table-contents ol li{padding-bottom:20px}.table-contents ol li a{font-weight:500;color:var(--color-primary);line-height:32px}.global-typograpgy h2,.global-typograpgy h3,.global-typograpgy h4{margin:30px 0}.global-typograpgy img{margin:40px 0}p{line-height:27px}.share-button-blog{background:var(--color-primary);border:1px solid var(--color-primary);width:100%;padding:5px 0;color:#fff;border-radius:5px}.share-width25{max-width:30px;margin-left:-10px}#divMsg{background-color:#fff;height:auto;width:100%;text-align:center;display:none;position:absolute;z-index:1;padding:20px;box-shadow:8px 8px 24px 0 #00000012;left:0;top:55px}.share-blogs{text-align:left;color:#000;font-weight:500;font-size:14px;margin:15px 0}.social-box-images{display:flex;align-items:center;justify-content:flex-start;margin:8px 0}span.ftr-logo1{background:url(https://www.keyideasinfotech.com/wp-content/themes/keyideas/imgnew/share-blogs-img.png);width:30px;height:30px;display:inline-block;background-size:160px;margin-right:6px}span.ftr-logo1.logo-face{background-position:164px 0}span.ftr-logo1.logo-pint{background-position:130px 0}span.ftr-logo1.logo-link{background-position:64px 0}span.ftr-logo1.logo-twitter{background-position:30px 0}.share-blogs{text-align:left;color:#000;font-weight:500;font-size:14px;margin:15px 0}.blog-social-s{box-shadow:0 0 0 rgb(0 0 0 / 16%)!important;margin:auto;max-width:100%;height:28px}.example{margin:auto;background:#fff;border-radius:5px;box-shadow:0 0 3px rgb(0 0 0 / 16%);display:flex}.gbl-btn-prim{border:none}form.blog-social-s input[type=text]{font-size:12px;border-left:1px solid grey;border-top:1px solid grey;border-bottom:1px solid grey;border-right:1px solid #ffff;float:left;width:80%;padding-bottom:10px!important;padding-top:10px!important;border-top-left-radius:5px;border-bottom-left-radius:5px;background:#fff url(https://www.keyideasinfotech.com/wp-content/themes/keyideas/imgnew/copy-icon.png) no-repeat center;appearance:none;background-size:12px;background-position:2%;padding-left:20px!important}form.example input[type=text]{padding:10px;font-size:17px;float:left;width:80%}form.blog-social-s a{float:left;width:20%;padding:0!important;background:var(--color-primary)!important;color:#fff;font-size:13px!important;border-left:none;cursor:pointer;height:28px!important;border-top-right-radius:5px!important;border-bottom-right-radius:5px!important;border-top-left-radius:0!important;border-bottom-left-radius:0!important;border:1px solid #50dec2!important;display:flex;align-items:center;justify-content:center}.content-details ul{padding-left:25px;margin:30px 0;font-size:18px}.content-details ul li{font-size:18px;line-height:30px}.content-details ul{margin-bottom:30px}.discuss-img img{margin:0}.global-typograpgy p{margin-bottom:20px}@media (min-width:1025px) and (max-width:1540px){.blogfilter .form-control,.result,.title-blog{font-size:16px}}@media (min-width:1180px) and (max-width:1280px){.blog-body .container{padding:0 15px}}@media (min-width:768px) and (max-width:1024px){.blogfilter .form-control,.result,.title-blog{font-size:16px}.blog-body .container{padding:0 15px}.search-blog-post{margin-top:30px}.pl-5{padding-left:15px!important}}@media (max-width:767px){.blogfilter .form-control,.result,.title-blog{font-size:16px}.blog-body .container{padding:0 15px}.pr-5{padding-right:15px!important}.pl-5{padding-left:15px!important}.row.mb-5{margin-bottom:15px!important;margin-top:20px}section.blog-hdr{background:var(--color-primary);padding:20px 0 35px 0!important}.global-typograpgy img{width:100%;height:auto;margin:20px 0}.global-typograpgy h2,.global-typograpgy h3,.global-typograpgy h4{margin:20px 0}.breadcrumb{width:100%;white-space:nowrap;overflow-x:auto;flex-wrap:nowrap;overflow-y:hidden;margin-bottom:10px}h1.text-left.py-5{padding:20px 0!important}.recent-posts{display:none}.Share-blog{text-align:center}}s
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'database_name_here' );

/** Database username */
define( 'DB_USER', 'username_here' );

/** Database password */
define( 'DB_PASSWORD', 'password_here' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'put your unique phrase here' );
define( 'SECURE_AUTH_KEY',  'put your unique phrase here' );
define( 'LOGGED_IN_KEY',    'put your unique phrase here' );
define( 'NONCE_KEY',        'put your unique phrase here' );
define( 'AUTH_SALT',        'put your unique phrase here' );
define( 'SECURE_AUTH_SALT', 'put your unique phrase here' );
define( 'LOGGED_IN_SALT',   'put your unique phrase here' );
define( 'NONCE_SALT',       'put your unique phrase here' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/documentation/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
