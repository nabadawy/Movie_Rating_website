<?php 

$db_user = "sql3408738";
$db_pass = "GIAGcE6KUA";
$db_name = "sql3408738";

$db = new PDO('mysql:host=sql3.freesqldatabase.com;dbname=' . $db_name . ';charset=utf8', $db_user, $db_pass);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$conn = new mysqli("sql3.freesqldatabase.com", $db_user, $db_pass, $db_name);