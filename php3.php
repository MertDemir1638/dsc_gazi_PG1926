<!DOCTYPE html>
<html>
<head>
	<title>Asal Sayı Bulma</title>
</head>
<body>

	
<form action="" method="post">
	Sayı: <input type="text" name="syy">   
	<input type="submit" name="Kontrol ET">
</form>
</body>
</html>



<?php
$sayi=$_POST['syy'];
$asal=0; $i=2;
do
{ 
	if ($sayi % $i == 0)
	{
		
		$asal = 1;
	}
	$i++;
}
while($i<$sayi);
if ($asal != 1)
{
	echo "Girilen Sayı Asaldır..!";
}
else
{
	echo "Girilen Sayı Asal Değildir..!";
}
 
?>

