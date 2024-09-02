### Version PT/BR

#### Desenvolvido por: Pedro Augusto, José Perdigão, Cristiano Monteiro e Dr. Vincícius Abreu

# TDB - THEOBROMA DATABASE

# Para instalação inicial no sistema linux (Distro debian/ubuntu), siga os seguintes comandos:

 Acesse a pasta 'cacao_linux'
> cd TDB-Theobroma-Database/

 Execute o script 'install.sh'
> bash install_docker.sh

Recupere o ip do container com:
sudo docker inspect TheobromaDB | grep '"IPAddress": "172*'

Acesse o site:
ip_do_container:4002
