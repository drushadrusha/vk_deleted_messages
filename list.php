<!DOCTYPE html>
<html>
<head>
	<title>list</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

</head>
<body>
	<br>
	<div class="container">

		<?php 

			$mysqli = new mysqli("localhost", "user", "password", "vkmessages");

			$result = $mysqli->query("SELECT * FROM events WHERE event = 2");


			while ($row = mysqli_fetch_row($result)) {

				?>

		<div class="card">
		  <div class="card-body">
		    <h5 class="card-title"><a href="http://vk.com/id<?php echo $row[3]; ?>"><?php echo $row[3]; ?></a></h5>
		    <p class="card-text">
		    	<?php
		    	echo "deleted message id: ".$row[4];
		    	echo "<br>";
		    	$query = "SELECT * FROM events WHERE message_id = $row[4]";
		    	$message = $mysqli->query($query);

		    	$message = mysqli_fetch_row($message);
		    	$deletedMessage = $message[4];
		    	echo "<b>".$deletedMessage."</b><br>";
		    	$deletedMessageDate = $message[7];
		    	echo "Дата: ".$deletedMessageDate."<br>";
		    	$deletedMessageAttachments = $message[6];
		    	echo "Вложения: ".$deletedMessageAttachments;
		    	?></p>
		  </div>
		</div>
		<br>

		<?php

	    		}


		?>

	</div>

</body>
</html>
