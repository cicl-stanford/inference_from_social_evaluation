<html>
<?php session_start(); #Create local cookies to store data
#Give subject a random Id
$_SESSION['user']=substr(str_shuffle(str_repeat('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',5)),0,7);
$_SESSION['trialamount']=sizeof($_SESSION['Files']); #How many trials are there?
$_SESSION['currtrial']=0; #Initialize what trial subject is completing
$trials=range(0,$_SESSION['trialamount']-1); #Create and shuffle list of trials
shuffle($trials);
$_SESSION['trials']=$trials;
$_SESSION['answers']=array_fill(0,$_SESSION['trialamount'],-1); #Fill in response vector with -1. Note that second argument is array size, not range limit.
#echo '<p>' . print_r($_SESSION) . '</p>';
?>
<body>
<center>

<img src="TestImages/Intro.jpg" />
<form method="get" action="runtest.php">
<button type="submit">Continue</button>
</form>
</center>
</body>
</html>