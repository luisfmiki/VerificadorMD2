#!/bin/bash

# ainda necessita de uma otimização nas partes comentadas


hashes=$1
pastaDosArquivos=$2
IFSOLD=$IFS
SECONDS=0

# a velocidade desse script seria mais rápida se não dependesse do acesso à internet
# mas como o algoritmo usado em questão é o MD2, não restam outras opções 
postReq() {
   	local payload="action=ajax_hash&text=`cat $1`&algo=md2"
   	local r=`curl --data "$payload" https://www.tools4noobs.com/ --no-progress-meter`
        func_result=$r
	echo $func_result
}

#aqui vai me dar um arranjo em que cada item é nome de um arquivo ou valor de hash
#o ideal seria capturar apenas os valores de hash para o arranjo, talvez com regex?
IFS=$'\t\n'
for linha in `cat $PWD/$hashes`;do
	lista_de_hash+=("$linha")
done


# adiciona a barra se o argumento do diretório vier sem
if [ -f $hashes ] && [ -d $pastaDosArquivos ]; then
	if [ "${pastaDosArquivos: -1}" != "/" ]; then
	       CamAbsoluto=$PWD/$pastaDosArquivos/
        else
 	       CamAbsoluto=$PWD/$pastaDosArquivos
	fi

IFS=$IFSOLD
	
	for arq in $CamAbsoluto*.txt; do		
		#postReq $arq
		resultado=`postReq $arq | grep -oP ' \K\w+(?=</div)'`
		status=0
		# quebra a iteração do arranjo lista_de_hash caso o valor de hash do arquivo bater
		# com qualquer item do arranjo (necessesita de uma otimização do tipo dicionário
		# usado em python)
		for hsh in "${lista_de_hash[@]}"; do
			if [ $hsh = $resultado ]; then
				status=1
				break
			fi
		done
		#cat $PWD/$hashes | while read hsh
		#do
		#if [ $hsh = $resultado\n ]; then
		#		status=1
		#	fi
		# se o valor de hash não bater com nenhum do arquivo legitimo de hash
		# então afirma-se que o atual arquivo foi modificado
		if [ $status -eq 0 ]; then
			msg=`echo "Alterado --> $arq" | grep -o "$pastaDosArquivos.\+txt"`
			echo "Alterado --> $msg"
		fi
		IFS=$IFSOLD	
		resultado=""		
	done
	# aqui é uma consideração caso o volume de arquivos a serem verificados for muito grande
	if [ $SECONDS -gt 10 ]; then
		echo "OBS: o tempo de exec. do script depende, sobretudo, da velocidade de sua rede"
	fi	
fi
