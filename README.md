HOLOWHAS HomeAssistant Integration

Seamlessly integrate your HOLOWHAS devices with HomeAssistant for unified control, automation, and monitoring.

Features

Full control of HOLOWHAS devices from HomeAssistant

Real-time status updates

Automation support (triggers, actions, conditions)

Unified management across multiple devices

Installation
HACS (Recommended)

Open HACS in HomeAssistant.

Go to Integrations → Explore & Add Repositories.

Search for HOLOWHAS and install.

Restart HomeAssistant.

Manual

Download the repository.

Copy the holowhas folder into <config_dir>/custom_components/.

Restart HomeAssistant.

Configuration

Go to Settings → Devices & Services → Add Integration.

Search for HOLOWHAS and follow the setup wizard.

Enter your device credentials or API token if required.

Usage

Control your devices directly from the HomeAssistant dashboard.

Create automations using device states and events.

Monitor device status and logs in real-time.

Example Automation
alias: Turn on HOLOWHAS at sunset
trigger:
  platform: sun
  event: sunset
action:
  service: holowhas.turn_on
  target:
    device_id: your_device_id

Support

GitHub Issues: [link]

Email: support@holowhas.com

License

MIT License
