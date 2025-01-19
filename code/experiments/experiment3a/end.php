<?php
session_start(); 

$Id=$_SESSION['user'];

#Save new data point
$savetrialindex=$_SESSION['currtrial']-1;
$savetrialnumber=$_SESSION['trials'][$savetrialindex];
$_SESSION['answers'][$savetrialnumber]=$_POST['answer'];

$con = mysql_connect("sql.mit.edu","jjara","X");
	if (!$con){
	  die('DATABASE CONNECTION ERROR: Please input code "ZZZZZZ" into form and email jjara@mit.edu for reimbursement');
}

mysql_select_db("jjara+turk_experiments", $con);

#Build query
$trials=$_SESSION['Files'];
$answer=$_SESSION['answers'];
for ($i = 0; $i < $_SESSION['trialamount'];$i++){
	$query = "INSERT INTO Responsibility (Id, Trial, Judgment) VALUES ('$Id', '$trials[$i]', '$answer[$i]')";
	$result = mysql_query($query, $con);
	if(!$result){
		die ('Could not update database. Please email this text to jjara@mit.edu to receive payment: . ' . mysql_error() . '. Input code ZERRORZ in MTurk to receive payment.');
	}
}
  mysql_close($con);
?>
<html>
<body><br><br><br><br>
	<h2>
	<center> Thank you for participating! If you have any comments please email jjara@mit.edu . Insert the following code in MTurk to receive payment:
</h2>
<center>
<h1><br><br> <?php print($_SESSION[user]) ?></h1></center>
</body>
</html>
