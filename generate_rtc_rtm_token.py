from src.RtcTokenBuilder2 import RtcTokenBuilder, Role_Publisher
import os


def main():
    app_id = "xxxxxxxxxx"
    app_certificate = "xxxxxxxxxxxxxxx"

    if not app_id or not app_certificate:
        raise RuntimeError("Missing AGORA_APP_ID or AGORA_APP_CERTIFICATE")

    channel_name = "test"
    account = "1002"

    token = RtcTokenBuilder.build_token_with_rtm(
        app_id,
        app_certificate,
        channel_name,
        account,
        Role_Publisher,
        3600,
        3600
    )

    print(token)


if __name__ == "__main__":
    main()
