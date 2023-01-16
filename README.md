# karhub_challenge
## Desafio proposto pela [Karhub](https://www.karhub.com.br/)    

Criar um ambiente virtual para isolar o projeto da versão nativa de Python
```bash
python -m venv venv
```

Ativar o ambiente acima criado.
Comando para Linux
```bash
source venv/bin/activate
```
Comando para Windows
```cmd
venv/Scripts/Activate
``` 

Instalar as libs utilizadas para a resolução do desafio.
```bash
pip install -r requirements.txt
```

Ao rodar o projeto, será lida a planilha `b_list_cp_application_complete.xlsx` e criado um arquivo `.csv` com todos os valores coletados desta planilha (`karhub_challenge.xlsx`).
Para rodar basta:    
```bash
python main.py
``` 