$log=@(("172.16.16.128","212.58.226.142","HTTP","GET /rss/newsonlineworldedition/frontpage/rss.xml"), 
("5.106.2.58","172.16.16.128","HTTP","GET /image/video1.png"), ("78.49.105.7","172.16.16.129","FTP","REQUEST: USER testuser"), ("201.100.16.196","172.16.16.128","HTTP","GET /blogfeed.js"), ("80.5.206.201","172.16.16.128","HTTP","GET /image/btn_learn.gif"), ("196.1.203.4","172.16.16.128","HTTP","GET /image/header.png"))

foreach ($line in $log) {
	if ($line[2] -eq "HTTP" -and $line[3] -like "GET*") {
		Write-Host "Requete HTTP : $($line[3].Substring(4))"
	}
}
