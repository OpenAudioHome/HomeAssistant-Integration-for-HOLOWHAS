# OpenAudio Home Assistant Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)
[![GitHub Release](https://img.shields.io/github/release/OpenAudioHome/HomeAssistant-Integration-for-HOLOWHAS.svg)](https://github.com/OpenAudioHome/HomeAssistant-Integration-for-HOLOWHAS/releases)
[![License](https://img.shields.io/github/license/OpenAudioHome/HomeAssistant-Integration-for-HOLOWHAS.svg)](LICENSE)

OpenAudio integration for Home Assistant.

This integration allows Home Assistant to control and monitor OpenAudio amplifiers and multi-room audio systems over the local network.

## Features

- Zone media player support
- Volume control
- Mute/unmute
- Input/source selection
- Real-time zone status updates
- Multi-zone support
- Local network communication
- Config Flow support
- HACS compatible

---

# Installation

## HACS Installation

1. Open HACS

2. Go to:
Integrations

3. Click:
⋮ → Custom repositories

4. Add repository:
https://github.com/OpenAudioHome/HomeAssistant-Integration-for-HOLOWHAS

5. Category:
Integration

6. Search for:
OpenAudio

7. Install and restart Home Assistant.

---

# Manual Installation

Copy:
custom_components/openaudio

into:
config/custom_components/

Result:
config/
└── custom_components/
       └── openaudio/

Restart Home Assistant.

---

# Configuration

1. Open Home Assistant

2. Navigate to:
Settings → Devices & Services

3. Click:
Add Integration

4. Search for:
OpenAudio

5. Enter:
- OpenAudio device IP address
- Polling interval

---

# Supported Platforms

| Platform     | Supported |
|--------------|-----------|
| media_player | Yes       |
| sensor       | Yes       |

---
# Screenshots

## Media Player

<img src=\"screenshots/zone.png\" width=\"500\">
<img src=\"screenshots/source.png\" width=\"500\">
<img src=\"screenshots/zone_player.png\" width=\"500\">
<img src=\"screenshots/source_player.png\" width=\"500\">

## Device Configuration

<img src=\"screenshots/configuration.png\" width=\"500\">
<img src=\"screenshots/device_create.png\" width=\"500\">

---

# Requirements

- Home Assistant 2025.1.0 or newer
- OpenAudio device connected to local network

---

# Troubleshooting

## Device Not Found

- Verify device IP address
- Verify Home Assistant and OpenAudio are on the same network
- Verify firewall settings

## Integration Unavailable

- Restart Home Assistant
- Verify device firmware
- Check Home Assistant logs

---

# Debug Logging

Add the following to `configuration.yaml`:

```yaml
logger:
logs:
 custom_components.openaudio: debug
```
---

## Support
- GitHub Issues: [link](https://github.com/OpenAudioHome/HomeAssistant-Integration-for-HOLOWHAS/issues)
- Email: support@openaudio.io

## Note
For HOLOWHAS, you need use firmware 1.1.24

For HOLOWHAS Ultra, you need use firmware 1.3.39

For HOLOWHAS Plus, you need use firmware 1.14.37 (with PWM function)

For HOLOWHAS Max, you need use firmware 1.15.40 (with PWM function).

If you don't have latest firmware version, just contact support@openaudio.io.
