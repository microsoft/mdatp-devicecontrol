# Device Control for Windows

## Getting Started

Step-by-step instructions for [getting started](Getting%20Started/readme.md) with device control.

## devices

Step-by-step examples on how to configure device control to restrict access to [devices](device/readme.md) like USBs, CD/DVD drivers, and Windows Portable Devices

## printers

Step-by-step examples on how configure device control to restrict access to [printers](printer/readme.md)

## Group Policy (GPO) administrative templates

If you don't see some settings in the device control, group policy, you need to install the templates to the central store for Group Policy.

- Administrative template: [WindowsDefender.admx](WindowsDefender.admx)
- Settings localization en-us for WindowsDefender.admx: [WindowsDefender.adml](WindowsDefender.adml)

> [!NOTE]  
> Make sure to install the .adml in the en-us subfolder of the central store.

Learn More
- [How to create and manage the Central Store for Group Policy Administrative Templates in Windows](https://learn.microsoft.com/en-us/troubleshoot/windows-client/group-policy/create-and-manage-central-store)
