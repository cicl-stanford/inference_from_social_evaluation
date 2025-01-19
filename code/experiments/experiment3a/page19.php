<html>
<?php session_start();?>
<body>
<center>
Introduction<br>
95%<br>
<form action="page18.php" method="post">
    <input type="submit" value="Go back." 
         name="Submit" id="frm1_submit" />
</form><br>

<img src="TutorialSlides/19<?php if ($_SESSION['Condition']>0){echo 'b';}else{echo 'a';}?>.jpg" />
<form method="get" action="page20.php">
<button type="submit">Continue</button>
</form>
</center>
</body>
</html>
