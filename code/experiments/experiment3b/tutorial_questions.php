<html>

<?php session_start();

if (isset($_POST['answerA'])){
	$_SESSION['CurrTutorialQuiz']=$_POST['CurrTutorialQuiz'];
	$savetrialindex = $_SESSION['CurrTutorialQuiz']-2;
	$_SESSION['answersTutorial'][$savetrialindex]=$_POST['answerA'] . $_POST['answerB'] . $_POST['answerC'];
}
else{
	$_SESSION['TutorialLengthQuiz']=7; # How many tutorial slides are there?
	$_SESSION['CurrTutorialQuiz']=1;
	$_SESSION['CorrectAnswers']=[["100"],["010"],["110","011","101"],["110","011"],["010","001"],["100","011"],["100","010","001"]];
}
?>
<?php function checkCorrectAnswers($abc) {
	$count_correct = 0;
	for ($x = 0; $x < $_SESSION['TutorialLengthQuiz']-1; $x++) {
		
		if (in_array($_SESSION['answersTutorial'][$x],$_SESSION['CorrectAnswers'][$x])){
			$count_correct = $count_correct + 1;
			}
			}
		if ($count_correct >= $_SESSION['TutorialLengthQuiz']-1){
			return 1;
		}
		else{
			return 0;
			}

	}
?>
<script>
function validateForm()
{
var q1=document.forms["ControlForm"]["answerA"].value;
var q2=document.forms["ControlForm"]["answerB"].value;
var q3=document.forms["ControlForm"]["answerC"].value;
if (q1==null || q1=="" || q2==null || q2=="" || q3==null || q3=="")
  {
  alert("Please judge all fishermen before moving on.");
  return false;
  }
var currTut = <?php echo $_SESSION['CurrTutorialQuiz']?>;
var totalTut = <?php echo $_SESSION['TutorialLengthQuiz']?>;
if (currTut >= totalTut){
var test = <?php echo checkCorrectAnswers(q1+q2+q3);?>;
}
else{
var test = 1;
}
if (test == 0){
	alert("You did not answer enough trial questions correctly. Please review the material.")
	window.location="http://krallen.scripts.mit.edu/Responsibility/index.php";
	return false;
	}
}
</script>
<body>
<center>
Quiz<br>

<?php
echo number_format(round($_SESSION['CurrTutorialQuiz']*100/$_SESSION['TutorialLengthQuiz']),0);
?>
%<br>

<img src="TutorialQuiz/<?php echo $_SESSION['CurrTutorialQuiz'];?>.png" height=450/>

<form name="ControlForm" method="post" action="<?php if($_SESSION['CurrTutorialQuiz']>=$_SESSION['TutorialLengthQuiz']){echo 'begin_threefishermen.php';}else{echo 'tutorial_questions.php';} ?>" onsubmit="return validateForm()">
<input type="hidden" name="CurrTutorialQuiz" value="<?php echo $_SESSION['CurrTutorialQuiz']+1;?>">
<table><tr><th colspan=3><center>Fisherman A</center></th><td>&nbsp;&nbsp;</td><th colspan=3><center>Fisherman B</center></th></tr>

<tr><th colspan=3><center><select size="2" name="answerA" multiple="">
<option value="1">Clear the trees.</option>
<option value="0">Go fishing.</option>
</select></center></th>
<td>&nbsp;&nbsp;</td>
<th colspan=3><center><select size="2" name="answerB" multiple="">
<option value="1">Clear the trees.</option>
<option value="0">Go fishing.</option>
</select></center></th></tr>
</table> 
<table><tr><th colspan=3><center>Fisherman C</center></th></tr>
<tr><th colspan=3><center>
<select size="2" name="answerC" multiple="">
<option value="1">Clear the trees.</option>
<option value="0">Go fishing.</option>
</select></center></th> </tr>
</table>
<center>
<button type="submit">Continue</button>
</center>
</form>
</center>
</body>
</html>
