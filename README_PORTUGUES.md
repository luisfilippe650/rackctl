# rackctl

Uma interface de linha de comando (CLI) para interagir com o [RackTables REST API ](https://github.com/luisfilippe650/racktables-rest-api). Gerencie sua infraestrutura de data center ? localiza��es, fileiras, racks e objetos ? diretamente pelo terminal.

---

## Requisitos

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

Instale as depend�ncias:

```bash
pip install -r requirements.txt
```

---

## Configura��o

A URL base da API � configurada em `src/config.py` por meio da vari�vel de ambiente `RACK_API_URL`.

Crie um arquivo `.env` dentro de `/src`:

```env
RACK_API_URL="http://localhost:8000/v1"
```

Ou edite `src/config.py` diretamente para alterar a URL base padr�o.

---

## Uso

```
rackctl <recurso> <comando> [argumentos]
```

---

## Comandos

### Localiza��es

Gerencie as localiza��es f�sicas do seu data center.

| Comando | Descri��o |
|---|---|
| `rackctl locations create <name>` | Cria uma nova localiza��o |
| `rackctl locations delete <location_id>` | Remove uma localiza��o pelo ID |
| `rackctl locations list` | Lista todas as localiza��es |
| `rackctl locations list-rows` | Lista todas as localiza��es com suas fileiras associadas |

**Exemplos:**

```bash
rackctl locations create "Datacenter S�o Paulo"
rackctl locations delete 3
rackctl locations list
rackctl locations list-rows
```

---

### Fileiras (Rows)

Gerencie as fileiras dentro das localiza��es.

| Comando | Descri��o |
|---|---|
| `rackctl rows create <name>` | Cria uma nova fileira |
| `rackctl rows delete <row_id>` | Remove uma fileira pelo ID |
| `rackctl rows list` | Lista todas as fileiras |
| `rackctl rows list-racks` | Lista todas as fileiras com seus racks associados |
| `rackctl rows add-location <row_id> <location_id>` | Associa uma localiza��o a uma fileira |
| `rackctl rows delete-location <row_id> <location_id>` | Remove a localiza��o de uma fileira |
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

| Comando | Descri��o |
|---|---|
| `rackctl racks create <name> --height <u> --row <row_id>` | Cria um novo rack |
| `rackctl racks delete <rack_id>` | Remove um rack pelo ID |
| `rackctl racks list` | Lista todos os racks |
| `rackctl racks occupancy` | Exibe a ocupa��o de todos os racks |
| `rackctl racks show-occupancy <rack_id>` | Exibe a ocupa��o de um rack espec�fico |
| `rackctl racks show <rack_id>` | Exibe os detalhes de um rack espec�fico |
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

| Comando | Descri��o |
|---|---|
| `rackctl objects create <name> <objtype_id>` | Cria um novo objeto |
| `rackctl objects delete <object_id>` | Remove um objeto pelo ID |
| `rackctl objects list` | Lista todos os objetos |
| `rackctl objects mount <rack_id> <object_id> <start_unit> <height>` | Monta um objeto em um rack |
| `rackctl objects unmount <object_id>` | Desmonta um objeto do rack |
| `rackctl objects move <object_id> <source_rack_id> <destination_rack_id> <start_unit> <height>` | Move um objeto para outro rack |
| `rackctl objects types` | Lista todos os tipos de objetos dispon�veis |
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
??? api/
?   ??? objects/
?   ?   ??? mount_unmount_client.py
?   ?   ??? move_client.py
?   ?   ??? objects_client.py
?   ??? rackspace/
?       ??? locations_client.py
?       ??? rack_client.py
?       ??? rows_client.py
??? cli/
?   ??? objects/
?   ??? rackspace/
?       ??? locations/
?       ??? rack/
?       ??? rows/
??? .gitignore
??? .env
??? __main__.py
??? config.py
??? rackctl
??? requirements.txt
```

---

## Licen�a

MIT
