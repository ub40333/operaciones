#!bin/bash
clear
#banner
echo -e "\e[1;34m"
figlet MATRICES
echo -e "\e[1;33m"
echo creado por por:@ub4033
#ejemplo
echo -e "\e[1;31m"
echo "ejemplo de la matriz"
matriz1=[[a,b,c,d],[e,f,g,h],[i,j,k,l],[m,n,o,p]];
echo $matriz1
echo -e "\e[1;33m"
#script
echo welcome

echo -e "\e[1;34m"
python /data/data/com.termux/files/home/operaciones/script/matrices.py
echo -e "\e[1;33m"
echo 'preciona enter para salir'
read ENTER
exit
