# rackctl

A command-line interface (CLI) for interacting with the [RackTables REST API](https://github.com/luisfilippe650/racktables-rest-api). Manage your data center infrastructure — locations, rows, racks, and objects — directly from your terminal.

---

## Requirements

- Python 3.8+
- `python3-requests`
- `python-dotenv`
- `pyyaml`

---

## Installation

### Option 1 — Install via `.deb` package (recommended)

Download the latest `.deb` package and install:

```bash
sudo dpkg -i rackctl_1.0.0-1_all.deb
sudo apt-get install -f   # install missing dependencies if needed
```

Verify the installation:

```bash
rackctl --help
```

### Option 2 — Build the `.deb` from source

> **Prerequisites:** Ubuntu 20.04 / 22.04 / 24.04 (or any Debian-based distro)

**1. Clone the repository:**

```bash
git clone https://github.com/luisfilippe650/rackctl.git
cd rackctl
```

**2. Install build dependencies:**

```bash
sudo apt update
sudo apt install -y devscripts debhelper dh-python python3-all \
    python3-setuptools python3-requests python3-dotenv python3-yaml
```

**3. Build the package:**

```bash
dpkg-buildpackage -us -uc -b
```

**4. Install the generated `.deb`:**

```bash
sudo dpkg -i ../rackctl_1.0.0-1_all.deb
```

### Option 3 — Run directly (development)

```bash
git clone https://github.com/luisfilippe650/rackctl.git
cd rackctl
pip install -r requirements.txt
./rackctl --help
```

---

## Configuration

The Debian package installs the global configuration file at:

```
/etc/rackctl/rackctl.yaml
```

Default contents:

```yaml
api_url: http://localhost:8000/v1/racktables
timeout: 10
```

Edit it with any text editor to point to your RackTables API:

```bash
sudo nano /etc/rackctl/rackctl.yaml
```

When running from source without that file, configure the API through
`RACKCTL_API_URL` and optionally set `RACKCTL_TIMEOUT`. If neither is set,
the defaults shown above are used.

---

## Usage

```
rackctl <resource> <command> [arguments]
```

---

## Commands

### Locations

Manage physical locations in your data center.

| Command | Description |
|---|---|
| `rackctl locations create --name <name>` | Create a new location |
| `rackctl locations delete (--id <id> \| --name <name>)` | Delete a location by ID or name |
| `rackctl locations by-name --name <name>` | Get a location by name |
| `rackctl locations list` | List all locations |
| `rackctl locations list-rows` | List all locations with their associated rows |

**Examples:**

```bash
rackctl locations create --name "Datacenter São Paulo"
rackctl locations delete --id 3
rackctl locations by-name --name "Datacenter São Paulo"
rackctl locations list
rackctl locations list-rows
```

---

### Rows

Manage rows within locations.

| Command | Description |
|---|---|
| `rackctl rows create --name <name>` | Create a new row |
| `rackctl rows delete (--id <id> \| --name <name>)` | Delete a row by ID or name |
| `rackctl rows by-name --name <name>` | Get a row by name |
| `rackctl rows list` | List all rows |
| `rackctl rows list-racks` | List all rows with their associated racks |
| `rackctl rows add-location --row <id> --location <id>` | Assign a location to a row |
| `rackctl rows delete-location --row <id> --location <id>` | Remove the location from a row |
| `rackctl rows rename --id <id> --name <name>` | Rename a row |

**Examples:**

```bash
rackctl rows create --name "Row A"
rackctl rows delete --id 5
rackctl rows list
rackctl rows list-racks
rackctl rows add-location --row 5 --location 2
rackctl rows delete-location --row 5 --location 2
rackctl rows rename --id 5 --name "Row B"
```

---

### Racks

Manage racks within rows.

| Command | Description |
|---|---|
| `rackctl racks create --name <name> --height <u> --row <row_id>` | Create a new rack |
| `rackctl racks delete (--id <id> \| --name <name>)` | Delete a rack by ID or name |
| `rackctl racks by-name --name <name>` | Get a rack by name |
| `rackctl racks list` | List all racks |
| `rackctl racks occupancy` | Show occupancy for all racks |
| `rackctl racks show-occupancy (--id <id> \| --name <name>)` | Show occupancy for a specific rack |
| `rackctl racks show (--id <id> \| --name <name>)` | Show details of a specific rack |
| `rackctl racks rename --id <id> --name <name>` | Rename a rack |

**Examples:**

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

### Objects

Manage objects (servers, devices) and their placement in racks.

| Command | Description |
|---|---|
| `rackctl objects create --name <name> --type-id <objtype_id>` | Create a new object |
| `rackctl objects delete (--id <id> \| --name <name>)` | Delete an object by ID or name |
| `rackctl objects list [--page N] [--per-page N]` | List manageable objects |
| `rackctl objects list-all [--search <text>]` | List objects of all types |
| `rackctl objects by-name --name <name>` | Get an object by name |
| `rackctl objects by-service-tag --service-tag <tag>` | Get an object by service tag |
| `rackctl objects summary (--id <id> \| --name <name>)` | Show an object's attributes |
| `rackctl objects update --id <id> --set FIELD=VALUE` | Update fixed fields or dynamic attributes |
| `rackctl objects mount --id <rack_id> --object-id <id> --start-unit <u> --height <u>` | Mount an object in a rack |
| `rackctl objects unmount (--id <id> \| --name <name>)` | Unmount an object from its rack |
| `rackctl objects move --id <id> --rack <destination_id> --start-unit <u>` | Move an object to a different rack |
| `rackctl objects types` | List all available object types |
| `rackctl objects dictionary --chapter-id <id>` | List dictionary options |
| `rackctl objects rename --id <id> --name <name>` | Rename an object |

**Examples:**

```bash
rackctl objects create --name "web-server-01" --type-id 4
rackctl objects delete --id 12
rackctl objects list
rackctl objects list-all --search "web-server"
rackctl objects summary --id 12 --include-options
rackctl objects update --id 12 --set "label=production" --set "has_problems=false"
rackctl objects update --id 12 --clear "Serial Number"
rackctl objects mount --id 7 --object-id 12 --start-unit 10 --height 2
rackctl objects unmount --id 12
rackctl objects move --id 12 --source-rack 7 --rack 9 --start-unit 1 --height 2
rackctl objects types
rackctl objects rename --id 12 --name "web-server-02"
```

---

## License

MIT
