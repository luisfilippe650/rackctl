# rackctl

Interface de linha de comando (CLI) para interagir com a [RackTables REST API](https://github.com/luisfilippe650/racktables-rest-api). Gerencie a infraestrutura do seu datacenter — localizações, fileiras, racks e objetos — diretamente pelo terminal.

---

## Requisitos

- Python 3.8+
- `python3-requests`
- `python-dotenv`
- `pyyaml`

---

## Instalação

### Opção 1 — Instalar via pacote `.deb` (recomendado)

Baixe o pacote `.deb` mais recente e instale:

```bash
sudo dpkg -i rackctl_1.0.0-1_all.deb
sudo apt-get install -f   # instala dependências faltantes se necessário
```

Verifique a instalação:

```bash
rackctl --help
```

### Opção 2 — Compilar o `.deb` a partir do código-fonte

> **Pré-requisitos:** Ubuntu 20.04 / 22.04 / 24.04 (ou qualquer distro baseada em Debian)

**1. Clone o repositório:**

```bash
git clone https://github.com/luisfilippe650/rackctl.git
cd rackctl
```

**2. Instale as dependências de build:**

```bash
sudo apt update
sudo apt install -y devscripts debhelper dh-python python3-all \
    python3-setuptools python3-requests python3-dotenv python3-yaml
```

**3. Compile o pacote:**

```bash
dpkg-buildpackage -us -uc -b
```

> O arquivo `.deb` será gerado **um nível acima** da pasta do projeto.

**4. Instale o `.deb` gerado:**

```bash
sudo dpkg -i ../rackctl_1.0.0-1_all.deb
```

### Opção 3 — Executar diretamente (desenvolvimento)

```bash
git clone https://github.com/luisfilippe650/rackctl.git
cd rackctl
pip install -r requirements.txt
./rackctl --help
```

---

## Configuração

O `rackctl` utiliza um arquivo de configuração global localizado em:

```
/etc/rackctl/rackctl.yaml
```

Conteúdo padrão:

```yaml
api_url: http://localhost:8000/v1/racktables
timeout: 10
```

Edite com qualquer editor de texto (usando sudo) para apontar para sua API do RackTables:

```bash
sudo nano /etc/rackctl/rackctl.yaml
```

---

## Uso

```
rackctl <recurso> <comando> [argumentos]
```

---

## Comandos

### Localizações

Gerencie as localizações físicas do seu datacenter.

| Comando | Descrição |
|---|---|
| `rackctl locations create --name <nome>` | Cria uma nova localização |
| `rackctl locations delete (--id <id> \| --name <nome>)` | Remove uma localização pelo ID ou nome |
| `rackctl locations by-name --name <nome>` | Busca uma localização pelo nome |
| `rackctl locations list` | Lista todas as localizações |
| `rackctl locations list-rows` | Lista todas as localizações com suas fileiras associadas |

**Exemplos:**

```bash
rackctl locations create --name "Datacenter São Paulo"
rackctl locations delete --id 3
rackctl locations by-name --name "Datacenter São Paulo"
rackctl locations list
rackctl locations list-rows
```

---

### Fileiras (Rows)

Gerencie fileiras dentro das localizações.

| Comando | Descrição |
|---|---|
| `rackctl rows create --name <nome>` | Cria uma nova fileira |
| `rackctl rows delete (--id <id> \| --name <nome>)` | Remove uma fileira pelo ID ou nome |
| `rackctl rows by-name --name <nome>` | Busca uma fileira pelo nome |
| `rackctl rows list` | Lista todas as fileiras |
| `rackctl rows list-racks` | Lista todas as fileiras com seus racks associados |
| `rackctl rows add-location --row <id> --location <id>` | Associa uma localização a uma fileira |
| `rackctl rows delete-location --row <id> --location <id>` | Remove a localização de uma fileira |
| `rackctl rows rename --id <id> --name <nome>` | Renomeia uma fileira |

**Exemplos:**

```bash
rackctl rows create --name "Fileira A"
rackctl rows delete --id 5
rackctl rows list
rackctl rows list-racks
rackctl rows add-location --row 5 --location 2
rackctl rows delete-location --row 5 --location 2
rackctl rows rename --id 5 --name "Fileira B"
```

---

### Racks

Gerencie racks dentro das fileiras.

| Comando | Descrição |
|---|---|
| `rackctl racks create --name <nome> --height <u> --row <row_id>` | Cria um novo rack |
| `rackctl racks delete (--id <id> \| --name <nome>)` | Remove um rack pelo ID ou nome |
| `rackctl racks by-name --name <nome>` | Busca um rack pelo nome |
| `rackctl racks list` | Lista todos os racks |
| `rackctl racks occupancy` | Exibe a ocupação de todos os racks |
| `rackctl racks show-occupancy (--id <id> \| --name <nome>)` | Exibe a ocupação de um rack específico |
| `rackctl racks show (--id <id> \| --name <nome>)` | Exibe os detalhes de um rack específico |
| `rackctl racks rename --id <id> --name <nome>` | Renomeia um rack |

**Exemplos:**

```bash
rackctl racks create --name "Rack-01" --height 42 --row 3
rackctl racks delete --id 7
rackctl racks list
rackctl racks occupancy
rackctl racks show-occupancy --id 7 --include-objects
rackctl racks show --id 7
rackctl racks rename --id 7 --name "Rack-02"
```

---

### Objetos

Gerencie objetos (servidores, dispositivos) e seu posicionamento nos racks.

| Comando | Descrição |
|---|---|
| `rackctl objects create --name <nome> --type-id <objtype_id>` | Cria um novo objeto |
| `rackctl objects delete (--id <id> \| --name <nome>)` | Remove um objeto pelo ID ou nome |
| `rackctl objects list [--page N] [--per-page N]` | Lista objetos gerenciáveis |
| `rackctl objects list-all [--search <texto>]` | Lista objetos de todos os tipos |
| `rackctl objects by-name --name <nome>` | Busca um objeto pelo nome |
| `rackctl objects by-service-tag --service-tag <tag>` | Busca um objeto pela service tag |
| `rackctl objects summary (--id <id> \| --name <nome>)` | Exibe os atributos de um objeto |
| `rackctl objects update --id <id> --set CAMPO=VALOR` | Atualiza campos fixos ou atributos dinâmicos |
| `rackctl objects mount --id <rack_id> --object-id <id> --start-unit <u> --height <u>` | Monta um objeto em um rack |
| `rackctl objects unmount (--id <id> \| --name <nome>)` | Desmonta um objeto do seu rack |
| `rackctl objects move --id <id> --rack <destination_id> --start-unit <u>` | Move um objeto para outro rack |
| `rackctl objects types` | Lista todos os tipos de objetos disponíveis |
| `rackctl objects dictionary --chapter-id <id>` | Lista opções de um dicionário |
| `rackctl objects rename --id <id> --name <nome>` | Renomeia um objeto |

**Exemplos:**

```bash
rackctl objects create --name "web-server-01" --type-id 4
rackctl objects delete --id 12
rackctl objects list
rackctl objects list-all --search "web-server"
rackctl objects summary --id 12 --include-options
rackctl objects update --id 12 --set "label=producao" --set "has_problems=false"
rackctl objects update --id 12 --clear "Serial Number"
rackctl objects mount --id 7 --object-id 12 --start-unit 10 --height 2
rackctl objects unmount --id 12
rackctl objects move --id 12 --source-rack 7 --rack 9 --start-unit 1 --height 2
rackctl objects types
rackctl objects rename --id 12 --name "web-server-02"
```
---

## Licença

MIT
