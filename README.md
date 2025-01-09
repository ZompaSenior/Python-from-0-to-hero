# Python from 0 to hero

Il fantastico corso che spiega Python dalle basi ai principi più avanzati!

# Preprazione ambiente di sviluppo

Per l'ambiente di sviluppo ho utilizzato MiniConda.

## Installazione MiniConda

Rimando alla pagina ufficiale, per la versione più aggiornta da scaricare:

https://docs.conda.io/en/latest/miniconda.html

Per quanto riguarda l'installazione, trovate qui la guida per i vari OS:

https://docs.anaconda.com/miniconda/install/#quick-command-line-install

## Preparazione della Virtual Env

La Virtual Env è una cartella che permetterà di gestire l'installazione isolata
di Python per il corso Python from 0 to hero.

    $ conda create --name Python-from-0-to-hero python=3.12
    $ conda activate Python-from-0-to-hero
    $ pip install jupyterlab jupyterlab-rise

## Verifica

Per controllare che tutto funzioni, basta attivare la virtualenv se non lo avete
già fatto (`conda activate Python-from-0-to-hero`) ed in seguito eseguire il
seguente comando:

    $ jupyter-lab

A questo punto si dovrebbe aprire una pagina nel vostro browser di default con
Jupyter Lab.


