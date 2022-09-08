# What this is

Barebones event listener for sending simulated win32api mouse input into Wine applications from host Linux system

# Summary

"Bootleg IPC" approach to sending virtual input into Wine for when you don't want to/can't set up sockets, shared memory, or named pipes.

Many applications running inside of Wine expect either raw input or input using Windows APIs that typical input automation tools like xdotool cannot satisfy.
For example, while it is possible to reliably move the onscreen cursor programmatically using xdotool (the cursor merely mirroring the position of the host system's cursor), simulated mouse clicks 
(LEFTDOWN, MIDDLEDOWN, RIGHTDOWN) generally fail to break this barrier (varies from application to application).

This creates a scenario like the following:

```
#!/bin/bash
run some commands
xdotool mousemove X Y
xdotool click 1 <-- this part will fail; can move cursor, but not click!
logic continues
```

wineclick provides a low-conf method of writing automation scripts in a shell vernacular and traversing this barrier.

By echoing out commands to a plaintext `wineclick` file while the listener is running in the same wineprefix as the target application,
you can incorporate this behavior into automation scripts and reliably click, hold, and release the left, middle, and right buttons.

The resultant script would look like:

```
#!/bin/bash
run some commands
xdotool mousemove X Y
echo "left" >> wineclick
logic continues
```

wineclick does not concern itself with cursor movement, leaving the user to implement it natively, and serves only to bridge the above gap when sending click events.

# Build

If you do not wish to build the executable, you can obtain it via the [release page](https://github.com/aclist/wineclick/releases/download/wineclick/wineclick.tar.gz).

1. Obtain Windows 64-bit Python installer
https://www.python.org/downloads/windows/ (direct link: https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe)

2. Create a wineprefix

```
export WINEPREFIX=$HOME/.pyinstaller
```
3. Set Wine version to Windows 8.1

- Run `winecfg`
- Select Applications tab
- Use Windows version dropdown

4. Follow default prompts to install Python into the Wine prefix.

5. Install `pyinstaller` and necessary dependencies using pip
- Navigate to `<WINEPREFIX>/drive_c/users/<your username>/AppData/Local/Programs/Python/Python310`

```
wine python.exe Scripts/pip.exe install pyinstaller pywin32 tailhead

```
6. Compile script into executable using pyinstaller
```
wine Scripts/pyinstaller.exe --onefile wineclick.py
```

- The executable will be output in the current working directory under `/dist`.

# Setup

Launch the desired Windows application/game using Wine/Proton.
While it is running, activate the same Wine prefix as the application and launch wineclick.exe with Wine. wineclick.exe can be located anywhere, but it must be adjacent to a plain text file called 
`wineclick`, which you should stage in your shell script before commencing input automation.

Echo commands into the "wineclick" file to trigger input events.

# Usage

Available triggers are:

- left
- right
- middle

```
$ echo left >> wineclick
CLICK: left
```

The three above triggers also take the `_up` and `_down` suffixes, as below:

```
$ echo left_down >> wineclick
HOLD: left
$ echo left_up >> wineclick
RELEASE: right
```

Lastly, you can invoke the `exit` trigger for programmatic closure of the listener.
Alternatively, keyboard interrupt (Ctrl-C) can be sent to the shell running the executable.

The listener supports file rotation: after initially creating the `wineclick` file, you can delete or move it, then recreate it, and the listener will continue following new lines. This can be useful 
if you expect to write a lot of triggers into the file and want to periodically expunge it.

Note that due to the way files are written, it is generally preferable to use the `>>` syntax to append to the file, rather than `>` to overwrite it. Overwriting is permissible if you remove the file 
in between commands; otherwise, the listener will be unable to tail it.

Therefore, while the below constructs will work:

```
echo left > wineclick
rm wineclick
echo right > wineclick
```
```
echo left >> wineclick
echo right >> wineclick
```

The following construct will not:

```
echo left > wineclick
echo right > wineclick
```

Barebones scripting examples of how you could integrate wineclick into a shell script are provided under [examples](examples).

# Further reading

This generic method can be extended to support other triggers and events.

https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event

