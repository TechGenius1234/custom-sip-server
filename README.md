# Custom Business SIP Server

This is a fully custom, lightweight SIP server developed for business use. It features user management, IVR, and SIP trunking capabilities, all managed through a JSON-based database.

## Features
- **SIP Registration**: Supports standard SIP registration for softphones and hardware phones.
- **IVR Engine**: Customizable IVR menus defined in `data/config.json`.
- **JSON Database**: No complex SQL setup; all data is stored in a readable JSON file.
- **Web Admin Dashboard**: Easy-to-use web interface for managing users and viewing status.
- **Standalone Executable**: Packaged as a single file for easy deployment.

## Getting Started
1. Run the executable: `./custom_sip_server`
2. Access the Web Admin at `http://localhost:8080` to manage extensions.
3. Register your SIP phones using the extensions and passwords defined in the admin panel.
4. Default IVR is accessible at extension `999`.

## Configuration
All configurations are stored in `data/config.json`. You can modify IVR menus, trunk settings, and user details directly or via the web admin.

## Technical Details
- **Language**: Python
- **SIP Stack**: Sippy B2BUA
- **Web Framework**: Flask
- **Database**: JSON (Flat-file)
- **Packaging**: PyInstaller
