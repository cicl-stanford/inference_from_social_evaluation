<html>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
 <link href="css/simple-slider.css" rel="stylesheet" type="text/css" />
 <link href="css/simple-slider-volume.css" rel="stylesheet" type="text/css"/>
 <script src="js/simple-slider.js"></script>
<?php 
error_reporting(-1);

session_start();

if (isset($_POST['Q1'])){
	$savetrialindex=$_SESSION['currtrial']-1;
	$_SESSION['choices'][$savetrialindex]=$_POST['Q1'];
	$_SESSION['confidence'][$savetrialindex]=$_POST['Confidence'];
}

$Id=$_SESSION['user'];

$con = mysql_connect("mysql.mit.edu","jjara","X");
if(!$con){
	die('Could not connect to database. Please email this text to jjara@mit.edu to receive payment: . ' . mysql_error() . '. Input code ZERRORZ in MTurk to receive payment.');
}
mysql_select_db("jjara+turk_experiments", $con);

#Build query
$trials=$_SESSION['trials'];
$choices=$_SESSION['choices'];
$confidences=$_SESSION['confidence'];
for ($i = 0; $i < $_SESSION['trialamount'];$i++){
	$query = "INSERT INTO HoH (Id, Video, Choice, Confidence) VALUES ('$Id', '$trials[$i]','$choices[$i]', '$confidences[$i]')";
	$result = mysql_query($query, $con);
	if(!$result){
		die ('Could not update database. Please email this text to jjara@mit.edu to receive payment: . ' . mysql_error() . '. Input code ZERRORZ in MTurk to receive payment.');
	}
}
#Update database
$TrialId=$_SESSION['ConditionId'];
$query = "UPDATE HoH_Conditions SET Subjects=Subjects-1 WHERE Id=$TrialId";
$result = mysql_query($query, $con);
if(!$result){
	die ('Could not update database. Please email this text to jjara@mit.edu to receive payment: . ' . mysql_error() . '. Input code ZERRORZ in MTurk to receive payment.');
}
mysql_close($con);
?>

<center>
<h2>Almost done!<br><br>


<form name="Questions" action="end.php" onclick="return checkVideo()" onsubmit="return validateForm()" method="post"><br>

1. How old are you?<br><br>
<input type="text" name="Age"><br><br>

2. What gender are you?<br><br>
<select size="2" name="Gender" multiple="">
<option value="M">Male</font></option>
<option value="F">Female</font></option>
</select><br><br>

3. How helpful of a person do you think you are?<br><br>
<table>
	<tr>
		<td></td>
		<td><input type="text" value="0.5" name="Helpful" data-slider="true" data-slider-theme="volume"></td>
		<td></td>
	</tr>
	<tr>
		<td><br></td>
		<td><br></td>
		<td><br></td>
	</tr>
	<tr>
		<td><center>Extremely<br>Unhelpful</center></td>
		<td><center>Average</center></td>
		<td><center>Extremely<br>helpful</center></td>
	</tr>
</table><br><br>

4. Do you have any comments?<br><br>
<textarea name="Comments" cols="25" rows="5">Enter your comments here...</textarea><br><br>

<input type="submit" value="Continue">
</form>

	</center>
</body>
</html>