import dataclasses
import json
import os
from datetime import datetime

from src.dir_constans import REPORTS_DIR
from src.website_config import WebsiteConfig


@dataclasses.dataclass
class Report:
    correct_password: str
    breaking_duration: str
    website_config: WebsiteConfig


class ReportGenerator:
    def generate_report(self, password, website_config, breaking_duration) -> None:
        reports_dir = REPORTS_DIR
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S%z")

        if password == "":
            file_name = "failed" + str(timestamp) + ".json"
        else:
            file_name = "success" + str(timestamp) + ".json"

        report = Report(correct_password=password, breaking_duration="{:.2f}".format(breaking_duration),
                        website_config=website_config)
        with open(os.path.join(reports_dir, file_name), "w") as fp:
            fp.write(json.dumps(dataclasses.asdict(report), indent=4))
