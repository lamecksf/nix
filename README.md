# nix

Mitology: https://pt.wikipedia.org/wiki/Nix<br>
ASCII: http://www.kammerl.de/ascii/AsciiSignature.php


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

NIX aspira um programa em shell para descrição, localização e tracking de um IP de forma dinâmica.

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

<hr>

#Comandos iniciais
<pre>
                   .__   __.  __  ___   ___
                   |  \ |  | |  | \  \ /  /
                   |   \|  | |  |  \  V  / 
                   |  . `  | |  |   >   <  
                   |  |\   | |  |  /  .  \ 
                   |__| \__| |__| /__/ \__\  v1.0


    NIx Geo IP Tracking 1.0 (c) 2017 Lameck
    github.isso.isso

    usage: python nit.py [options]

                -i, --ip       Target IP

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


       nit.py --ip myip --all

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
