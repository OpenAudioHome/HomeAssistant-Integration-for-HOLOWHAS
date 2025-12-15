# HOLOWHAS HomeAssistant Integration

Seamlessly integrate your HOLOWHAS devices with HomeAssistant for unified control, automation, and monitoring.  

## Features
- Full control of HOLOWHAS devices from HomeAssistant  
- Real-time status updates  
- Automation support (triggers, actions, conditions)  
- Unified management across multiple devices  

## Installation

### HACS (Recommended)
1. Open HACS in HomeAssistant.  
2. Go to **Integrations → Explore & Add Repositories**.  
3. Search for `HOLOWHAS` and install.  
4. Restart HomeAssistant.  

### Manual
1. Download the repository.  
2. Copy the `holowhas` folder into `<config_dir>/custom_components/`.  
3. Restart HomeAssistant.  

## Configuration
1. Go to **Settings → Devices & Services → Add Integration**.  
2. Search for **HOLOWHAS** and follow the setup wizard.  
3. Enter your device credentials or API token if required.  

## Usage
- Control your devices directly from the HomeAssistant dashboard.  
- Create automations using device states and events.  
- Monitor device status and logs in real-time.  

## Example Automation
```yaml
alias: Turn on HOLOWHAS at sunset
trigger:
  platform: sun
  event: sunset
action:
  service: holowhas.turn_on
  target:
    device_id: your_device_id
```
## Support
- GitHub Issues: [link](https://github.com/OpenAudioHome/HomeAssistant-Integration-for-HOLOWHAS/issues)
- Email: support@openaudiohome.com

## License
MIT License
