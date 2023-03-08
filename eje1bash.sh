echo "Programa que pide un numero y tienes que adivinar cual es el correcto"

while [ true ]
do

    echo "Escriba un numero: "
    read numero

    if [[ "$numero" == 12 ]]; then
    break

    fi
    echo "Ese no es e numero"
    clear
    echo "Numero equivocado sigue intentando"

done

echo "Encontraste el numero 12, pasaste la prueba"