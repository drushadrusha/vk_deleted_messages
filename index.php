<?php

	$event = $_GET['e'];
	$text = $_GET['t'];
	$textJson = json_decode($text);
	$attachments = json_encode($textJson[6]);
	$message = $textJson[4];
	$message_id = $textJson[0];

	$mysqli = new mysqli("localhost", "user", "password", "vkmessages");

	if($event == "2"){
		$message = $textJson[0];
		$message_id = 0;
	}

	if ($mysqli->query("INSERT INTO `events` (`id`, `event`, `text`, `message_id`, `message`, `sender`, `attachments`) VALUES (NULL, '$event', '$text', '$message_id', '$message', '$textJson[2]', '$attachments' );") === TRUE) {
		echo "ok";
	}

?>