<?php
session_start();

require_once('config.php');



$sql = "SELECT DISTINCT Name, Rating From NMovies M, MovieGenre G where M.id = G.mov_id AND G.genre ='Comedy' ORDER BY Rating Desc LIMIT 10;";

$result = $conn->query($sql);



echo "<table border='1'>
<tr>
<th>Name</th>
<th>Rating</th>
</tr>";

while ($row = $result->fetch_assoc()) {
echo "<tr>";
echo "<td>" . $row['Name'] . "</td>";
echo "<td>" . $row['Rating'] . "</td>";
echo "</tr>"; 
}
echo "</table>";