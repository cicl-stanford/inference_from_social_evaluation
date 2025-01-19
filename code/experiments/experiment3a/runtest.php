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
	$savetrialindex=$_SESSION['currtrial']-1;
	$savetrialnumber=$_SESSION['trials'][$savetrialindex];
	$_SESSION['answers'][$savetrialnumber]=$_POST['answer'];
}
$currvar=$_SESSION['trials'][$_SESSION['currtrial']]; #Get trial number.
$_SESSION['currtrial']++; #move on
#echo '<p>' . print_r($_SESSION) . '</p>';
?>
<body>
<center>
Trial: <?echo $_SESSION['currtrial']; ?> out of <?echo $_SESSION['trialamount']; ?>.<br>
<img src="TestImages/<?php echo $_SESSION['Files'][$currvar];?>"/><br>

<form name="TestForm" method="post" action="<?php if ($_SESSION['currtrial']>=$_SESSION['trialamount']){ echo 'end.php';} else {echo 'runtest.php';}?>" onsubmit="return validateForm()">
<table>
	<tr>
		<td></td>
		<td><input type="text" value="0.5" name="answer" data-slider="true" data-slider-theme="volume"></td>
		<td></td>
	</tr>
	<tr><td><br></td><td><br></td><td><br></td></tr>
	<tr>
		<td><center>Definitely<br>fish</font></center></td>
		<td><center>not sure</center></td>
		<td><center>Definitely<br>clear road</font></center></td>
	</tr>
</table><br>
<button type="submit">Continue</button>
</form>
</center>
</body>
</html>