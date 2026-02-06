# Rayzor

```text
      ____   ___ __  __ ____  ____  ____
     / __ \/    |\ \/ /__  / / __ \/ __ \
    / /_/ / /| | \  /   / / / / / / /_/ /
   / _, _/ ___ | / /   / /_/ /_/ / _, _/
  /_/ |_/_/  |_|/_/   /____\____/_/ |_|

```

> **CUTTING THROUGH NOISE. FINDING SIGNAL.**

Rayzor is a high-concurrency CLI tool to collect, clean, and test V2Ray/Sing-box configurations from the Telegram ecosystem.

## Setup

1. **Install**

```bash
pip install -r requirement.txt

```

2. **Configure Core**
   Download **Sing-box** and set the path in `setting.json`:

```json
"CORE_PATH": "./path/to/sing-box"

```

## Commands

Run Rayzor using `python rayzor.py [COMMAND]`.

### 1. Collect

Scrapes configs from your channel list for the last `X` hours.

```bash
python rayzor.py collect --channels sources.txt --hours-back 24 --output raw.txt

```

### 2. Clean Configs

Removes duplicates to keep your list unique.

```bash
python rayzor.py clean-configs --configs raw.txt --output unique.txt

```

### 3. Ping

Tests latency using the real Sing-box core. Saves the working ones.

```bash
python rayzor.py ping --configs unique.txt --output valid.txt --result stats.csv

```

### 4. Extract

Finds new channel links mentioned inside other channels.

```bash
python rayzor.py extract --channels sources.txt --days-back 7 --output new_sources.txt

```

### 5. Check

Verifies if a specific channel actually posts V2Ray configs.

```bash
python rayzor.py check --channels potential.txt --days-back 2 --output verified.txt

```

### 6. Clean Channels

Sorts and formats your channel list (removes duplicates, sort, converts to lowercase).

```bash
python rayzor.py clean-channels --channels list.txt --output sorted_list.txt

```
