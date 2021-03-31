#!/bin/bash

hashes=$1
pastaDosArquivos=$2
IFSOLD=$IFS
SECONDS=0

postReq() {
   	local payload="action=ajax_hash&text=`cat $1`&algo=md2"
   	local r=`curl --data "$payload" https://www.tools4noobs.com/ --no-progress-meter`
        func_result=$r
}


if [ -f $hashes ] && [ -d $pastaDosArquivos ]; then
	if [ "${pastaDosArquivos: -1}" != "/" ]; then
	       CamAbsoluto=$PWD/$pastaDosArquivos/
        else
 	       CamAbsoluto=$PWD/$pastaDosArquivos
	fi
	
	for arq in $CamAbsoluto*.txt; do		
		postReq $arq
		resultado=`echo $func_result | grep -oP ' \K\w+(?=</div)'`
		IFS=$'\n'
		status=0
		for hsh in `cat $PWD/$hashes`; do
			if [ $hsh = $resultado ]; then
				status=1
			fi
		done
		if [ $status -eq 0 ]; then
			msg=`echo "Alterado --> $arq" | grep -o "$pastaDosArquivos.\+txt"`
			echo "Alterado --> $msg"
		fi
		if [ $SECONDS -gt 10 ]; then
			echo "OBS: o tempo de exec. do script depende, sobretudo, da velocidade de sua rede"
		fi		
	 	IFS=$IFSOLD
		resultado=""		
	done
fi

