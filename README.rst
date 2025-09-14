==========
pyreadline
==========


pyreadline is a Python implementation of GNU readline for Windows, derived from Gary Bishop's ctypes-based UNC readline package.
The project is incomplete but has been tested on Windows 2000 and Windows XP.
Version 2.0 runs on Python 2.6, 2.7, and 3.2+ using the same code.

Features:

* Keyboard text selection and copy/paste.
* Shift+arrow keys for text selection.
* Control-C can be used for copy; activate with `allow_ctrl_c(True)` in the config file.
* Double tapping Control-C raises a `KeyboardInterrupt`; use `ctrl_c_tap_time_interval(x)` to set the tap window (default 0.3 s).
* `paste()` pastes the first line of content on the clipboard.
* `ipython_paste()` pastes tab-separated data as a list of lists or a NumPy array if all data is numeric.
* `paste_multiline_code()` pastes multi-line code, removing any empty lines.
 
 
 The latest development version is always available at the IPython git 
 repository_.

.. _repository: https://github.com/pyreadline/pyreadline.git
