<?php
session_start(); 

$Id = $_SESSION['SqlConditionId'] . "_" . $_SESSION['user'];

#Save new data point
$savetrialindex=$_SESSION['CurrTest']-1;
$savetrialnumber=$_SESSION['trials'][$savetrialindex];
$_SESSION['PathId'][$savetrialindex]=$savetrialnumber;
$_SESSION['answers'][$savetrialindex]=$_POST['answer'];

$con = mysql_connect("sql.mit.edu","krallen","password");
	if (!$con){
	  die('DATABASE CONNECTION ERROR: Please input code "ZZZZZZ" into form and email jjara@mit.edu for reimbursement<br>' . mysql_error());
}

mysql_select_db("krallen+turk_experiments", $con);

# Mark that the condition was completed
$FinishedQuery = "Update Blame_Conditions SET Views=Views+1 WHERE Id = " . $_SESSION['SqlConditionId'];
$res2 = mysql_query($FinishedQuery,$con);

#Build query
$Trials=$_SESSION['trials'];
$answer=$_SESSION['answers'];

for ($i = 0; $i < $_SESSION['TestLimit'];$i++){
	$query = "INSERT INTO Blame (Id, Trial, Judgment) VALUES ('$Id', '$Trials[$i]', '$answer[$i]')";
	$result = mysql_query($query, $con);
	if(!$result){
		die ('Could not update database. Please email this text to krallen@mit.edu to receive payment: . ' . mysql_error() . '. Input code ZERRORZ in MTurk to receive payment.');
	}
}
  mysql_close($con);
?>
<body><br><br><br><br>
	<h2>
	<center> Thank you for participating! If you have any comments please email jjara@mit.edu . Insert the following code in MTurk to receive payment:
</h2>
<center>
<h1><br><br> <?php echo $_SESSION['SqlConditionId'] . "PX" . $_SESSION['user'];?></h1></center>
</center>
</body>
</html>


