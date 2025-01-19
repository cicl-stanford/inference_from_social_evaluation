<html>
<?php session_start();

if (isset($_POST['CurrTutorial'])){
	$_SESSION['CurrTutorial']=$_POST['CurrTutorial'];
}
else{
	$_SESSION['TutorialLength']=20; # How many tutorial slides are there?
	$_SESSION['CurrTutorial']=1;
}

# echo '<p>' . print_r($_SESSION) . '</p>';
?>
<body>
<center>
Introduction<br>
<?php
echo number_format(round($_SESSION['CurrTutorial']*100/$_SESSION['TutorialLength']),0);
?>
%<br>

<img src="Tutorial/<?php echo $_SESSION['CurrTutorial'];?>.JPG" height=500/>
<?php
if ($_SESSION['CurrTutorial']!=1){
	echo "<form method=\"post\" action=\"index.php\"><input type=\"hidden\" name=\"CurrTutorial\" value=\"";
	echo max($_SESSION['CurrTutorial']-1,1);
	echo "\"><button type=\"submit\">Go back</button></form>";
}?>
<form method="post" action="<?php if($_SESSION['CurrTutorial']>=$_SESSION['TutorialLength']){echo 'questions.html';}else{echo 'index.php';} ?>">
<input type="hidden" name="CurrTutorial" value="<?php echo $_SESSION['CurrTutorial']+1;?>">
<button type="submit">Continue</button>
</form>
</center>
</body>
</html>