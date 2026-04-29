# rackctl

Uma interface de linha de comando (CLI) para interagir com o [RackTables REST API ](https://github.com/luisfilippe650/racktables-rest-api). Gerencie sua infraestrutura de data center ? localizações, fileiras, racks e objetos ? diretamente pelo terminal.

---

## Requisitos

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

Instale as dependências:

```bash
pip install -r requirements.txt.txt
```

---

## Configuraçõo

A URL base da API é configurada em `src/config.py` por meio da variável de ambiente `RACK_API_URL`.

Crie um arquivo `.env` dentro de `/src`:

```env
RACK_API_URL="http://localhost:8000/v1"
```

Ou edite `src/config.py` diretamente para alterar a URL base padrão.

---

## Uso

```
rackctl <recurso> <comando> [argumentos]
```

---


## Comandos
 
### Localizações
 
Gerencie as localizações físicas do seu data center.
 
| Comando | Descrição |
|---|---|
| `rackctl locations create <name>` | Cria uma nova localização |
| `rackctl locations delete <location_id>` | Remove uma localização pelo ID |
| `rackctl locations list` | Lista todas as localizações |
| `rackctl locations list-rows` | Lista todas as localizações com suas fileiras associadas |
 
**Exemplos:**
 
```bash
rackctl locations create "Datacenter São Paulo"
rackctl locations delete 3
rackctl locations list
rackctl locations list-rows
```
 
---
 
### Fileiras (Rows)
 
Gerencie as fileiras dentro das localizações.
 
| Comando | Descrição |
|---|---|
| `rackctl rows create <name>` | Cria uma nova fileira |
| `rackctl rows delete <row_id>` | Remove uma fileira pelo ID |
| `rackctl rows list` | Lista todas as fileiras |
| `rackctl rows list-racks` | Lista todas as fileiras com seus racks associados |
| `rackctl rows add-location <row_id> <location_id>` | Associa uma localização a uma fileira |
| `rackctl rows delete-location <row_id> <location_id>` | Remove a localização de uma fileira |
| `rackctl rows rename <row_id> <name>` | Renomeia uma fileira |
 
**Exemplos:**
 
```bash
rackctl rows create "Fileira A"
rackctl rows delete 5
rackctl rows list
rackctl rows list-racks
rackctl rows add-location 5 2
rackctl rows delete-location 5 2
rackctl rows rename 5 "Fileira B"
```
 
---
 
### Racks
 
Gerencie os racks dentro das fileiras.
 
| Comando | Descrição |
|---|---|
| `rackctl racks create <name> --height <u> --row <row_id>` | Cria um novo rack |
| `rackctl racks delete <rack_id>` | Remove um rack pelo ID |
| `rackctl racks list` | Lista todos os racks |
| `rackctl racks occupancy` | Exibe a ocupação de todos os racks |
| `rackctl racks show-occupancy <rack_id>` | Exibe a ocupação de um rack específico |
| `rackctl racks show <rack_id>` | Exibe os detalhes de um rack específico |
| `rackctl racks rename <rack_id> <name>` | Renomeia um rack |
 
**Exemplos:**
 
```bash
rackctl racks create "Rack-01" --height 42 --row 3
rackctl racks delete 7
rackctl racks list
rackctl racks occupancy
rackctl racks show-occupancy 7
rackctl racks show 7
rackctl racks rename 7 "Rack-02"
```
 
---
 
### Objetos
 
Gerencie objetos (servidores, dispositivos) e seu posicionamento nos racks.
 
| Comando | Descrição |
|---|---|
| `rackctl objects create <name> <objtype_id>` | Cria um novo objeto |
| `rackctl objects delete <object_id>` | Remove um objeto pelo ID |
| `rackctl objects list` | Lista todos os objetos |
| `rackctl objects mount <rack_id> <object_id> <start_unit> <height>` | Monta um objeto em um rack |
| `rackctl objects unmount <object_id>` | Desmonta um objeto do rack |
| `rackctl objects move <object_id> <source_rack_id> <destination_rack_id> <start_unit> <height>` | Move um objeto para outro rack |
| `rackctl objects types` | Lista todos os tipos de objetos disponíveis |
| `rackctl objects rename <object_id> <name>` | Renomeia um objeto |
 
**Exemplos:**
 
```bash
rackctl objects create "web-server-01" 4
rackctl objects delete 12
rackctl objects list
rackctl objects mount 7 12 10 2
rackctl objects unmount 12
rackctl objects move 12 7 9 1 2
rackctl objects types
rackctl objects rename 12 "web-server-02"
```
 
---
 
## Estrutura do Projeto
 
```
src/
├── api/
│   ├── objects/
│   │   ├── mount_unmount_client.py
│   │   ├── move_client.py
│   │   └── objects_client.py
│   └── rackspace/
│       ├── locations_client.py
│       ├── rack_client.py
│       └── rows_client.py
├── cli/
│   ├── objects/
│   ├── rackspace/
│       ├── locations/
│       ├── rack/
│       └── rows/
├── .gitignore
├── .env
├── __main__.py
├── config.py
├── rackctl
└── requirements.txt
```
 
---
 
## Licença
 
MIT
 
