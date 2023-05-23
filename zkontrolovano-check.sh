rpm -q $1
if [[ $? -eq 0 ]]; then
    echo "Balicek je nainstalovan"
    echo "Balicek odinstaluji"
    sudo dnf remove $1 -y
    rpm -q $1
    if [[ $? -eq 1 ]]; then
        echo "Balicek uspesne odinstalovan"
    fi
elif [[ $? -eq 1 ]]; then
    echo "Balicek neni nainstalovan"
    echo "Instaluji"
    sudo dnf install $1 -y
    rpm -q $1
    if [[ $? -eq 0 ]]; then
        echo "Balicek uspesne nainstalovan"
    fi
fi
