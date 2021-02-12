<?php 
$sure=strtotime("now");


if ($sure>=strtotime("06") or $sure<strtotime("10")) {
	echo "Günaydın";
}

elseif ($sure>=strtotime("10") or $sure<strtotime("17")) {
	echo "İyi Günler";
}

elseif ($sure>=strtotime("17") or $sure<strtotime("20")) {
	echo "İyi Akşamlar";
}

elseif ($sure>=strtotime("20") or $sure<strtotime("00")) {
	echo "İyi Geceler";
}

else {
	echo "Esenlikler Dilerim";
}

?>