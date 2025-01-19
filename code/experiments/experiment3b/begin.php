<html>
<?php

# Create local cookies to store data
session_start();

# Give subject a random Id
$_SESSION['user']=substr(str_shuffle(str_repeat('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',5)),0,7);
# Remember 
$_SESSION['CurrTest']=0; #Initialize what trial subject is completing

# HERE GET MYSQL FROM Blame_Conditions, where views is in the minimum and select
# a random one. Store that on trials
$con = mysql_connect("sql.mit.edu","krallen","password");
if(!$con){
	die('Error establishing connection. Please email this text to krallen@mit.edu . ' . mysql_error());
}
mysql_select_db("krallen+turk_experiments",$con);
$query = "select * from Blame_Conditions where Views=0 and OnView=0 ORDER BY RAND() LIMIT 0,1";
$result = mysql_query($query,$con) or die(mysql_error());
$row=mysql_fetch_assoc($result);

# If there aren't any paths that are guarnateed no one is doing
# then give them one of the ones that are currently on view.
if (empty($row['Id'])){
    $query = "select * from Blame_Conditions where Views=0 ORDER BY RAND() LIMIT 0,1";
    $result = mysql_query($query,$con) or die(mysql_error());
    $row=mysql_fetch_assoc($result);
}

$queryR = "select * from Rewards";
$resultR = mysql_query($queryR,$con) or die(mysql_error());
$rowR=mysql_fetch_assoc($resultR);

$rewards_best = $rowR['Best'];
$rewards_act = $rowR['Actual'];

$trials=$row['Trials'];

$LoanQuery = "Update Blame_Conditions SET OnView=1 WHERE Id = " . $row['Id'];
$res2 = mysql_query($LoanQuery,$con);

$trials=explode(' ',$trials);
$rewards_best = explode(' ',$rewards_best);
$rewards_act = explode(' ',$rewards_act);
mysql_close($con);

$_SESSION['TestLimit']=count($trials); # How many test trials are there?

# $trials=range(0,$_SESSION['TestLimit']-1); #Create and shuffle list of trials
shuffle($trials);
$_SESSION['trials']=$trials;
$_SESSION['SqlConditionId']=$row['Id']; # Mark when the participant finished.
$_SESSION['RewardsBest'] = $rewards_best;
$_SESSION['RewardsActual']= $rewards_act;
# echo '<p>' . print_r($_SESSION) . '</p>';
?>
<body>
<center>
<center>
<h1>
Let's get started! <br><br>
Sometimes, the fishermen could have gotten more fish if they had acted differently. <br>
We'll show you cases when this happened and you'll judge how much you think <br>
a specific fisherman is to blame. <br><br>
Please make sure your web browser is maximized for the test trials.<br>
</h1>
</center>
<form method="get" action="runtest.php">
<button type="submit">Begin</button>
</form>
</center>
</body>
</html>
