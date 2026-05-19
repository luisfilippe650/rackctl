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

### Option 3 — Run directly with pip (development)

```bash
git clone https://github.com/luisfilippe650/rackctl.git
cd rackctl
pip install -r requirements.txt
python -m src --help
```

---

## Configuration

On first run, `rackctl` automatically creates a configuration file at:

```
~/.config/rackctl/config.yaml
```

Default contents:

```yaml
api_url: http://localhost:8000/v1
timeout: 10
```

Edit it with any text editor to point to your RackTables API:

```bash
nano ~/.config/rackctl/config.yaml
```

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
| `rackctl locations create <name>` | Create a new location |
| `rackctl locations delete <location_id>` | Delete a location by ID |
| `rackctl locations list` | List all locations |
| `rackctl locations list-rows` | List all locations with their associated rows |

**Examples:**

```bash
rackctl locations create "Datacenter São Paulo"
rackctl locations delete 3
rackctl locations list
rackctl locations list-rows
```

---

### Rows

Manage rows within locations.

| Command | Description |
|---|---|
| `rackctl rows create <name>` | Create a new row |
| `rackctl rows delete <row_id>` | Delete a row by ID |
| `rackctl rows list` | List all rows |
| `rackctl rows list-racks` | List all rows with their associated racks |
| `rackctl rows add-location <row_id> <location_id>` | Assign a location to a row |
| `rackctl rows delete-location <row_id> <location_id>` | Remove the location from a row |
| `rackctl rows rename <row_id> <name>` | Rename a row |

**Examples:**

```bash
rackctl rows create "Row A"
rackctl rows delete 5
rackctl rows list
rackctl rows list-racks
rackctl rows add-location 5 2
rackctl rows delete-location 5 2
rackctl rows rename 5 "Row B"
```

---

### Racks

Manage racks within rows.

| Command | Description |
|---|---|
| `rackctl racks create <name> --height <u> --row <row_id>` | Create a new rack |
| `rackctl racks delete <rack_id>` | Delete a rack by ID |
| `rackctl racks list` | List all racks |
| `rackctl racks occupancy` | Show occupancy for all racks |
| `rackctl racks show-occupancy <rack_id>` | Show occupancy for a specific rack |
| `rackctl racks show <rack_id>` | Show details of a specific rack |
| `rackctl racks rename <rack_id> <name>` | Rename a rack |

**Examples:**

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

### Objects

Manage objects (servers, devices) and their placement in racks.

| Command | Description |
|---|---|
| `rackctl objects create <name> <objtype_id>` | Create a new object |
| `rackctl objects delete <object_id>` | Delete an object by ID |
| `rackctl objects list` | List all objects |
| `rackctl objects mount <rack_id> <object_id> <start_unit> <height>` | Mount an object in a rack |
| `rackctl objects unmount <object_id>` | Unmount an object from its rack |
| `rackctl objects move <object_id> <source_rack_id> <destination_rack_id> <start_unit> <height>` | Move an object to a different rack |
| `rackctl objects types` | List all available object types |
| `rackctl objects rename <object_id> <name>` | Rename an object |

**Examples:**

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

## License

MIT
