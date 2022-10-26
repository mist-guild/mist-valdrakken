import os
import json
import requests


def send_applicant_webhook(new_applicant):
    webhook_assets = get_webhook_assets(new_applicant.wow_class)

    applicant_webhook_json = {
        "embeds": [
            {
                "author": {
                    "name": f"{new_applicant.character_name} - {new_applicant.id}",
                    "icon_url": webhook_assets["image"],
                },
                "title": f"New Application for {new_applicant.team_choice}",
                "thumbnail": {
                    "url": webhook_assets["image"],
                },
                "description": f"A new {new_applicant.wow_class} has applied! Click on the title to review the application.",
                "color": webhook_assets["color"],
            }
        ]
    }
    webhook_url = os.getenv("WEBHOOK_URL")
    requests.post(webhook_url, json=applicant_webhook_json)


def get_webhook_assets(wow_class):
    folder = os.path.dirname(os.path.abspath(__file__))
    with open(folder + "/webhook_assets.json", "r") as f:
        webhook_assets = json.load(f)[wow_class]
    return webhook_assets
