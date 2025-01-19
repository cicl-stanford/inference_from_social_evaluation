<html>
<?php session_start();?>
<body>
<center>
Introduction<br>
90%<br>
<form action="page17.php" method="post">
    <input type="submit" value="Go back." 
         name="Submit" id="frm1_submit" />
</form><br>

<img src="TutorialSlides/18<?php if ($_SESSION['Condition']>0){echo 'b';}else{echo 'a';}?>.jpg" />
<form method="get" action="page19.php">
<button type="submit">Continue</button>
</form>
</center>
</body>
</html>
