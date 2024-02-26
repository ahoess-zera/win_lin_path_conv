# win_lin_path_conv
Converts UNC-path (Windows) to SMB-paths (Linux) and tries to open them using their specific default application. Works for folders and files.

# Install
* Place the script `win_lin_path_conv.py` in some folder where it can remain without getting moved.
* Move `win_lin_path_conv.desktop` e.g. on the desktop and adapt it:
   * Replace `<PATH_TO>` with the script's full path
   * Replace `<PARAMS>` with parameters you want to use (see `win_lin_path_conv.py -h` for more information on that)

## Fastest version
Besides just executing this script on the command line or changing to the Desktop to double click the created icon, probably the best and fastest way to use this script is by creating a starter in the task bar. Do to this, the parameters from the adapted `win_lin_path_conv.desktop` can be applied when creating a new task bar starter directly or just by drag&drop the adapted `win_lin_path_conv.desktop` file onto the desired position in the task bar.

# Run
To execute this script, perform these steps:
1) The **Windows-UNC-path** needs to get **copied to clipboard** that shall get converted and executed. To do this, you can copy it from somethere, but the fastest method is to just select it with the mouse, as this also copies it into the clipboard.
2) Execute the script (e.g. with a **single click on** its created **task bar icon**). This will try to convert and execute the path from the clipboard. Note: sometimes it will complain that the converted SMB-path of a file - even if it is valid and exists - is not a folder (reason unknown). -> Just retry.

