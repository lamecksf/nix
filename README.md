# nix

Mitology: https://pt.wikipedia.org/wiki/Nix<br>
ASCII (modelo usado : STARWARS): http://www.kammerl.de/ascii/AsciiSignature.php


<pre>
.__   __.  __  ___   ___
|  \ |  | |  | \  \ /  /
|   \|  | |  |  \  V  / 
|  . `  | |  |   >   <  
|  |\   | |  |  /  .  \ 
|__| \__| |__| /__/ \__\
</pre>
                        
<br>

<hr>

NIX aspira um programa em shell para descrição, localização e tracking de um IP de forma dinâmica. Incialmente foi desenvolvida em python à objeto.
A motivação surgiu aps usar o "anonsurf myip" retornando um IP e o código de um país. Minha biblioteca "geo" estava desatualizada promovendo um erro interno. Precisei buscar informações do IP abrindo o navegador, entrando no site de localização e inserindo os dados. Resolvi então facilitar escrevendo o projeto, inicialmente, com o lookup do IP. A base esta pronta. Contribua caso o deseje.

A inspiraço para o nome nix surgiu á circunstância sobre a necessidade de busca de informaçes do IPas 2:00 a.m. Nix, na mitologia, refere-se a personificaço da noite e deusa dos segredos e mistrios noturnos. Ficou bem apropriado.

# INSTRUÇÃO

#Para compilar local: 
<p>python nix.py -h</p>
<p>ou</p>
<p>chmod 777 nix.py</p>
<p>./nix.py -h</p>

#Para inserir na varivel de ambiente:
1. Jogue a pasta nix em /usr/bin/
2. Insira na variável $PATH : export PATH=$PATH:/usr/bin/nix/
3. Certifique-se que foi inserida: echo $PATH
4. Teste em qualquer diretrio digitando: nix.py -h

Permanentes:<br>
<p>sudo nano /etc/bash.bashrc</p>
<p>nano .bashrc</p>
<p>Ou dinamize isso conforme suas necessidades</p>

<hr>

#Comandos iniciais
<pre>
                   .__   __.  __  ___   ___
                   |  \ |  | |  | \  \ /  /
                   |   \|  | |  |  \  V  / 
                   |  . `  | |  |   >   <  
                   |  |\   | |  |  /  .  \ 
                   |__| \__| |__| /__/ \__\  nvX.X


    NIx Geo IP Tracking 1.0 (c) 2017 Lameck
    https://github.com/lamecksf/nix/

    usage: python nit.py [options]

         ##########################################
                  SET IDENTIFIE PROTOCOL
         ##########################################

         -i, --ip <iptarget or myip>    Target IP

                   --all      All params
                --status          Status
               --country         Country
          --country_code    Country Code
                --region          Region
                  --city            City
               --zipcode         Zipcode
                   --lat        Latitude
                   --lon       Longitude
              --timezone        Timezone
                   --isp             ISP
                   --org    Organization
                    --as              As
                 --query  Identificate Protocol
                   --zpc  Postal Address System (Br)


      nit.py --ip myip --all --zpc


       ##########################################
                       SET ZIPCODE
       ##########################################

                  --gzip  Get Zipcode Area
                       country code >>>  Set code of country
                            zipcode >>>  Set zipecode of area

     nit.py --gzip 


</pre>

0. Constante myip busca seu IP externo e é definido sobre o parametro --ip : nix.py -i myip

1. --all - Lista todos os parmetros: nix.py --ip myip --all ou nix.py -i 8.8.8.8 --all
2. --status Lista o status de busca sobre a api: nix.py -i myip --status
3. --country Lista o país da busca sobre o IP: nix.py -i myip --country
4. --country_code Lista o código do pais da busca sobre o IP (referenciado em outras tools): nix.py -i myip --country_code
5. --region Lista a região que encontra-se os registros do IP: nix.py -i myip --region
6. --city Lista a cidade de referncia do IP: nix.py -i myip --city
7. --zipcode Lista o código postal da referncia de busca: nix.py -i myip --zipcode
8. --lat Lista a latitude da referência (posteriormente será usada no google maps): nix.py -i myip --lat
9. --lon Lista longitude da referência (posteriormente será usada no google maps): nix.py -i myip --lon
10. --timezone Lista a time zone da referncia: nix.py -i myip --timezone
11. --isp Lista o Internet Service Provider da referncia: nix.py -i myip --isp
12. --org Lista a Organização que nomeia a referência: nix.py -i myip --org
13. --as Lista nome fantasia sobre a referncia 12: nix.py -i myip --as
14. --query Lista o IP de busca: nix.py -i myip --query

<hr>

#Novas
1. Próximas atualizaçes contar com google maps. Será disponibilizado as keys do projeto dessa forma no precisar criar uma key para usar as dependncias da api do google.
2. Integrar com as bibliotecas dos correios do meu país (Brasil)

A ideia a longo prazo é criar um toolkit.<br>
Só diversão.
