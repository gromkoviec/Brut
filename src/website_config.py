from dataclasses import dataclass


@dataclass
class WebsiteConfig:
    url: str
    login_username: str
    passwords_file_name: str
    username_selector: str
    password_selector: str
    submit_button_selector: str
