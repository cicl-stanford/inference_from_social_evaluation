<html>
<?php session_start();
$_SESSION['Condition']=rand(0,1);
if ($_SESSION['Condition'] > 0){
     $_SESSION['Files']=array('t1_a1b2c2.pdf.png','t1_a2b2c2.pdf.png','t1_a3b1c2.pdf.png','t1_a2b3c3.pdf.png','t1_a2b1c1.pdf.png','t1_a1b3c3.pdf.png','t1_a3b3c3.pdf.png','t1_a1b1c2.pdf.png','t1_a2b1c3.pdf.png','t2_a1b2c2.pdf.png','t2_a2b2c2.pdf.png','t2_a3b1c2.pdf.png','t2_a2b3c3.pdf.png','t2_a2b1c1.pdf.png','t2_a1b3c3.pdf.png','t2_a3b3c3.pdf.png','t2_a1b1c2.pdf.png','t2_a2b1c3.pdf.png','t3_a1b2c2.pdf.png','t3_a2b2c2.pdf.png','t3_a3b1c2.pdf.png','t3_a2b3c3.pdf.png','t3_a2b1c1.pdf.png','t3_a1b3c3.pdf.png','t3_a3b3c3.pdf.png','t3_a1b1c2.pdf.png','t3_a2b1c3.pdf.png');
}else{
	$_SESSION['Files']=array('t1_a2b1c2.pdf.png','t1_a3b2c2.pdf.png','t1_a1b1c3.pdf.png','t1_a1b2c3.pdf.png','t1_a3b2c3.pdf.png','t1_a1b1c1.pdf.png','t1_a3b1c3.pdf.png','t1_a2b2c3.pdf.png','t1_a3b1c1.pdf.png','t2_a2b1c2.pdf.png','t2_a3b2c2.pdf.png','t2_a1b1c3.pdf.png','t2_a1b2c3.pdf.png','t2_a3b2c3.pdf.png','t2_a1b1c1.pdf.png','t2_a3b1c3.pdf.png','t2_a2b2c3.pdf.png','t2_a3b1c1.pdf.png','t3_a2b1c2.pdf.png','t3_a3b2c2.pdf.png','t3_a1b1c3.pdf.png','t3_a1b2c3.pdf.png','t3_a3b2c3.pdf.png','t3_a1b1c1.pdf.png','t3_a3b1c3.pdf.png','t3_a2b2c3.pdf.png','t3_a3b1c1.pdf.png');
}
#echo '<p>' . print_r($_SESSION) . '</p>';
?>
<body>
<center>
Introduction<br>
5%<br>

<img src="TutorialSlides/1.jpg" />
<form method="get" action="page2.html">
<button type="submit">Continue</button>
</form>
</center>
</body>
</html>
