<?php
session_start();
require_once('config.php');




$cast = $_POST['cast'];



$sql = "SELECT   C.Name as Name, MC.Role as role From NMovies M, Cast C, moviecast MC  where M.id = MC.MovieID AND C.id = MC.CastID AND  M.Name= '$cast'";

$result = $conn->query($sql);



echo "<table border='1'>
<tr>

<th>Cast member</th>
<th>Role</th>

</tr>";

while ($row = $result->fetch_assoc()) {
echo "<tr>";

echo "<td>" . $row['Name'] . "</td>";
echo "<td>" . $row['role'] . "</td>";

echo "</tr>"; 
}
echo "</table>";