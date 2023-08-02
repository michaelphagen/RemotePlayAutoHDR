# RemotePlayAutoHDR

Turn off HDR when using Steam Remote Play

## What is this?

An app that monitors Steam's logs (streaming_log.txt) and turns off HDR when using Remote Play. It will turn HDR back on when you close Remote Play.

## Why?

Remote play doesn't support HDR and will make your screen look washed out. This app will turn off HDR when you start Remote Play and turn it back on when you close Remote Play.

## How to use

1. Download the latest release from [here](https://github.com/michaelphagen/RemotePlayAutoHDR/releases)
2. Extract the zip file to a folder
3. Run RemotePlayAutoHDR.exe (or make a shortcut to it from your [startup folder](https://support.microsoft.com/en-us/windows/add-an-app-to-run-automatically-at-startup-in-windows-10-150da165-dcd9-7230-517b-cf3c295d89dd))
4. Enjoy!

## Options

The app runs in the notification area and you can do 2 things with it:

- Open the log file (by double clicking the icon or selecting "Open Log")
- Exit the app (by right clicking the icon and selecting "Exit")

## Dependencies

RemotePlayAutoHDR uses [Ji Huang's HDRSwitch](https://github.com/cocafe/HDRSwitch) for now, which is bundled into the package and repo. I plan to re-write this in C and remove the dependency on HDRSwitch.
