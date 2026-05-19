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

### Opção 3 — Executar diretamente com pip (desenvolvimento)

```bash
git clone https://github.com/luisfilippe650/rackctl.git
cd rackctl
pip install -r requirements.txt
python -m src --help
```

---

## Configuração

Na primeira execução, o `rackctl` cria automaticamente um arquivo de configuração em:

```
~/.config/rackctl/config.yaml
```

Conteúdo padrão:

```yaml
api_url: http://localhost:8000/v1
timeout: 10
```

Edite com qualquer editor de texto para apontar para sua API do RackTables:

```bash
nano ~/.config/rackctl/config.yaml
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
| `rackctl locations create <nome>` | Cria uma nova localização |
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

Gerencie fileiras dentro das localizações.

| Comando | Descrição |
|---|---|
| `rackctl rows create <nome>` | Cria uma nova fileira |
| `rackctl rows delete <row_id>` | Remove uma fileira pelo ID |
| `rackctl rows list` | Lista todas as fileiras |
| `rackctl rows list-racks` | Lista todas as fileiras com seus racks associados |
| `rackctl rows add-location <row_id> <location_id>` | Associa uma localização a uma fileira |
| `rackctl rows delete-location <row_id> <location_id>` | Remove a localização de uma fileira |
| `rackctl rows rename <row_id> <nome>` | Renomeia uma fileira |

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

Gerencie racks dentro das fileiras.

| Comando | Descrição |
|---|---|
| `rackctl racks create <nome> --height <u> --row <row_id>` | Cria um novo rack |
| `rackctl racks delete <rack_id>` | Remove um rack pelo ID |
| `rackctl racks list` | Lista todos os racks |
| `rackctl racks occupancy` | Exibe a ocupação de todos os racks |
| `rackctl racks show-occupancy <rack_id>` | Exibe a ocupação de um rack específico |
| `rackctl racks show <rack_id>` | Exibe os detalhes de um rack específico |
| `rackctl racks rename <rack_id> <nome>` | Renomeia um rack |

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
| `rackctl objects create <nome> <objtype_id>` | Cria um novo objeto |
| `rackctl objects delete <object_id>` | Remove um objeto pelo ID |
| `rackctl objects list` | Lista todos os objetos |
| `rackctl objects mount <rack_id> <object_id> <start_unit> <height>` | Monta um objeto em um rack |
| `rackctl objects unmount <object_id>` | Desmonta um objeto do seu rack |
| `rackctl objects move <object_id> <source_rack_id> <destination_rack_id> <start_unit> <height>` | Move um objeto para outro rack |
| `rackctl objects types` | Lista todos os tipos de objetos disponíveis |
| `rackctl objects rename <object_id> <nome>` | Renomeia um objeto |

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

## Licença

MIT
