<?php 

session_start();

	if(!isset($_SESSION['userlogin'])){
		header("Location: login.php");
	}

	if(isset($_GET['logout'])){
		session_destroy();
		unset($_SESSION);
		header("Location: login.php");
	}

?>

  
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>Movie Rating</title>
	<link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/movindex.css" rel="stylesheet">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="js/focus.js"></script>
    <script src="js/functions.js"></script>
    
    
    
    



	<script>
    $(window).on("load resize", function () {
      if($(window).width() < 995){
        $('#catdesk').hide();
        $('#catmob').show();
        $('#mobsep').show();
      }else{
        $('#catmob').hide();
        $('#catdesk').show();
        $('#mobsep').hide();
      }
    }).resize();
    </script>
<style>
body {
  background-image: url('img/background1.jpg');
  background-repeat: no-repeat;
  background-size: cover
  
    }
</style>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {box-sizing: border-box;}

body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.topnav {
  overflow: hidden;
  background-color: #ff06e6;
}

.topnav a {
  float: left;
  display: block;
  color: black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #9c069c;
  color: white;
}

.topnav input[type=text] {
  float: right;
  padding: 6px;
  margin-top: 8px;
  margin-right: 16px;
  border: none;
  font-size: 17px;
}

@media screen and (max-width: 600px) {
  .topnav a, .topnav input[type=text] {
    float: none;
    display: block;
    text-align: left;
    width: 100%;
    margin: 0;
    padding: 14px;
  }
  
  .topnav input[type=text] {
    border: 1px solid #ccc;  
  }
}
</style>
    
</head>

<body>

<div class="topnav">
  <a class="active" href="#home">Home</a>
  <a href="#about">About</a>
  <a href="index.php?logout=true">Logout</a>
  <input type="text" placeholder="Search..">
  
</div>
    <!-- Page Content -->
    <div class="container">

        <div class="row">

          <div class="col-md-3" id="catdesk" style="display: none">
              <p style="font-size:160%;"> Search </p>
              <div class="list-group">
                <a href="Rated25.php" class="list-group-item" id="Action">TOP 25 Rated Movies</a>
                <a href="Revenue.php" class="list-group-item" id="Adventure">Top 25 Revenue</a>
                <a href="test.php" class="list-group-item" id="Animation">Add Review </a>
                <a href="comdy10.php" class="list-group-item" id="Comedy">Top 10 Comedy movies</a>
                <a href="Drama10.php" class="list-group-item" id="Drama">Top 10 Drama Movies</a>
                <a href="Romance.php" class="list-group-item" id="Thriller">Top 10 Romance</a>
                
              </div>
          </div>
		  
<form action="searchM.php" method="post">

<input type="text" value="Search Movie" name="movie" class="textfield_effect" maxlength="30" onfocus="this.value=''">
</td>
</tr>
<tr>
  <td align="center" style="font-family:Calibri">
<input type="submit"  value="Goo!!"/>
</form>


<form action="Actor.php" method="post">

<input type="text" value="Search Cast for a Movie" name="cast" class="textfield_effect" maxlength="30" onfocus="this.value=''">
</td>
</tr>
<tr>
  <td align="center" style="font-family:Calibri">
<input type="submit"  value="Goo!!"/>
</form>


    <form action="Genre.php" method="post">
    <select name="genre"  >
        <option value="" disabled selected>Choose Genre</option>
        <option value="Thriller">Thriller</option>
        <option value="Comedy">Comedy</option>
        <option value="Drama">Drama</option>
        <option value="Action">Action</option>
        <option value="Fantasy">Fantasy</option>
        <option value="Mystery">Mystery</option>
        <option value="Horror">Horror</option>
        <option value="Romance">Romance</option>
        <option value="Documentary">Documentary</option>
        <option value="History">History</option>
        <option value="Short">Short</option>
        <option value="Animation">Animation</option>
        <option value="Crime">Crime</option>
        <option value="Adventure">Adventure</option>
        <option value="Family">Family</option>
        <option value="Biography">Biography</option>
        <option value="Science Fiction">Science Fiction</option>
        <option value="Musical">Musical</option>
        <option value="War">War</option>
        <option value="Religious">Religious</option>
    </select>

    <input type="submit" name="submit" vlaue="Choose options">
</form>






          

        </div>
        <!-- /.row -->

    </div>
    <!-- /.container -->



    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>
	<script type="text/javascript">
      var movieCategory=document.getElementById('Category');
      movieCategory.onchange=function() {
        var op=this.options[this.selectedIndex];
        if (op.value!="empty"){
          window.open(op.value, "_self");
        }
      }
    </script>

</body>

</html>




