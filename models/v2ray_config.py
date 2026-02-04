from typing import Any

CONFIG_PATTERN = r"(?:vmess|vless|trojan|ss|tuic|hysteria2?)://[a-zA-Z0-9\-_@.:?=&%#]+"


class V2rayConfig:
    link: str
    parsed_data: dict[str, Any]

    def __init__(self, link: str, parsed_data: dict[str, Any]) -> None:
        self.link = link
        self.parsed_data = parsed_data
