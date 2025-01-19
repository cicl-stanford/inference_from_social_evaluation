<html>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
  <script src="js/simple-slider.js"></script>
  <link href="css/simple-slider.css" rel="stylesheet" type="text/css" />
  <link href="css/simple-slider-volume.css" rel="stylesheet" type="text/css" />
 <script>
function validateForm()
{
var q1=document.forms["TestForm"]["answer"].value;
if (q1==0.5)
  {
  alert("Please interact with the slider before moving on.");
  return false;
  }
}
</script>
<?php
session_start(); #Load variables.
if (isset($_POST['answer'])){
	$savetrialindex=$_SESSION['CurrTest']-1;
	$savetrialnumber=$_SESSION['trials'][$savetrialindex];
	$_SESSION['answers'][$savetrialindex]=$_POST['answer'];
}
$currvar=$_SESSION['trials'][$_SESSION['CurrTest']]; #Get trial number.
$_SESSION['CurrTest']++; #move on
#echo '<p>' . print_r($_SESSION) . '</p>';
#echo '<p>' . print_r($currvar) . '</p>';
?>
<body>
<center>

Trial: <?echo $_SESSION['CurrTest']; ?> out of <?echo $_SESSION['TestLimit']; ?>.<br>
<table>
<tr>
<td><center>
<img src="TestImages/<?php echo $currvar . '/1.jpg';?>" height=450px/></center></td>
<td><br><br><br><br><br><br><font size="6"><b><u>   Fish sacs</u></b><br><b>Best possible:</b> <?php echo $_SESSION['RewardsBest'][$currvar-1];?> <br> <b>Actually sold:</b> <?php echo $_SESSION['RewardsActual'][$currvar-1];?> </font></td>
</tr>
<tr>
<td>
<center>
<form name="TestForm" method="post" action="<?php if ($_SESSION['CurrTest']>=$_SESSION['TestLimit']){ echo 'end.php';} else {echo 'runtest.php';}?>" onsubmit="return validateForm()">
	<table>
	<tr>
		<td></td>
		<td><input type="text" value="0.5" name="answer" data-slider="true" data-slider-theme="volume"></td>
		<td></td>
	</tr>
	<tr><td><br></td><td><br></td><td><br></td></tr>
	<tr>
		<td><center>Not at<br>all</center></td>
		<td><center>Somewhat</center></td>
		<td><center>Very much</font></center></td>
	</tr>
</table><br><center>
<button type="submit">Continue</button>
</center>
</form>
</tr>
</center>
</td>
</table>
</center>
</body>
</html>