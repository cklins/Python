cd D:\download\LVR\analyze\O_·s¦Ë¥«
foreach($file in Get-ChildItem){
	Get-Content $file.name | Out-File -Encoding UTF8 "utf8_$file"
}