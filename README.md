## barcode-httpd

`barcode-httpd` converts any camera-phone running Android into a keyboard emulating barcode reader. It runs a simple
webserver that redirects to the free [ZXing](https://code.google.com/p/zxing/) Android app to scan the barcode. When
done, the app redirects back to the webserver, which validates the scanned barcode and injects it into the system as
keystrokes.

I strongly urge you to pass a sensible validation regexp on the command line. Any input that passes this validation is
injected and may do evil things to your system.

## Requirements

`barcode-httpd` requires `flask` to run. To inject keypresses into the system, either the `evdev` module or the
`xdotool` command-line tool are required.

### Usage

	$ ./barcode-httpd.py --help                                                                                                                                                                                                                                                         :(
	usage: barcode-httpd.py [-h] --validation VALIDATION [--uinput | --xdotool]
	
	optional arguments:
	  -h, --help            show this help message and exit
	  --validation VALIDATION
	                        regular expression to match validate barcode with
	  --uinput              use uinput to inject keyboard events
	  --xdotool             use xdotool to inject keyboard events

### License

`barcode-httpd` is free software released into the public domain.
