#! /usr/bin/env python
import urllib.parse
import argparse
import re

from flask import Flask, redirect, url_for
app = Flask(__name__)

# The phone should be able to resolve this hostname
app.config['SERVER_NAME'] = 'computer.example.com:5000'


parser = argparse.ArgumentParser()
parser.add_argument('--validation', required=True, help='regular expression to match validate barcode with')
group = parser.add_mutually_exclusive_group()
group.add_argument('--uinput', action='store_const', const=True, help='use uinput to inject keyboard events')
group.add_argument('--xdotool', action='store_const', const=True, help='use xdotool to inject keyboard events')
args = parser.parse_args()

if args.uinput:
    from evdev import UInput, ecodes
    ui = UInput()
if args.xdotool:
    from subprocess import call


@app.route("/")
@app.route("/scan/<barcode>")
def scan(barcode=None):
    if barcode is not None:
        print('Received barcode "{}"'.format(barcode))


        if re.match(args.validation, barcode):
            for c in barcode:
                if args.xdotool:
                    call(["xdotool", "key", c])
                if args.uinput:
                    key = getattr(ecodes, 'KEY_' + c)
                    ui.write(ecodes.EV_KEY, key, 1)
                    ui.write(ecodes.EV_KEY, key, 0)
                    ui.syn()
        else:
            print('Barcode "{}" does not match validation regex "{}"'.format(barcode, args.validation))
    return redirect('zxing://scan/?ret=' + url_for('scan', barcode='{CODE}', _external=True))

if __name__ == "__main__":
    #app.debug = True
    app.run(host='0.0.0.0')
