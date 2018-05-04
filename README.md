# Brain- Computer Interface Codebase
------------------------------------

This is the codebase for BCI suite. Designed and written by OHSU and NEU. Contributions Welcome!


## Features
-----------

*RSVPKeyboard*

```
	*RSVP KeyboardTM* is an EEG (electroencephalography) based BCI (brain
		computer interface) typing system. It utilizes a visual presentation technique
		called rapid serial visual presentation (RSVP). In RSVP, the options are
		presented rapidly at a single location with a temporal separation. Similarly
		in RSVP KeyboardTM, the symbols (the letters and additional symbols) are
		shown at the center of screen. When the subject wants to select a symbol,
		they await the intended symbol during the presentation and elicit a p300 response to a target symbol.

	To run on windows, execute the .exe to start with GUI. Otherwise, run `python gui/RSVPKeyboard.py` in your terminal to begin.
```
*Shuffle Speller*
```
	TBD.
```

*Matrix*
```
	TBD.
```

## Dependencies
---------------
This project requires Psychopy, Python v 3.6.5, and other packages. See requirements.txt. When possible integration with other open source
libraries will be done.


## Installation
---------------

# BCI Setup

In order to run BCI suite on your computer, first install **Python 3.6.5** [from here.](https://www.python.org/downloads/) Then, you need to install required modules using pip (python's package manager). Pip should already be installed, but if not go [here.](https://pip.pypa.io/en/stable/installing/). You must install Docker and Docker-Machine to use the Language Model developed by CSLU. There are instructions in the language model directory for getting the image you need (think of it as a callable server). If not using, set fake_lm to true. Depending on your OS, you may also need some compiling libraries. For example, some of the data science libraries (numpy, scipy) need C compiling libraries for python especially for Windows [from here.](https://www.microsoft.com/en-us/download/details.aspx?id=44266).


1. Run `pip install -r requirements.txt`

You will also need to set a python path for your session. If running demo or other files and you get an error that a module doesn't exist, try setting your path again. You can set your path as follows:

2. run `export PYTHONPATH=.` for Mac or `set PYTHONPATH=.` for Windows

3. If using Mac, you will need to install XCode and enable command line tools. `xcode-select --install`

## Bash Script

To use, create a virtual env named `bci-env` in your Documents folder.
Clone the repo to that folder as well.
`pip install -r requirements.txt` while that environment is activated.
If those assumptions are met, simply click on the run_bci.sh and the gui will pop-up allowing you to execute the experiments.
Change the paths or script names here is needed.

## Usage

Start by running `python gui/BCInterface.py` in your command prompt or terminal.

You may also invoke the experiment directly using command line tools for bci_main.py

Ex.
	 `python bci_main.py` *this will default parameters, mode, user, and type.*

You can pass it attributes with flags, if desired.
    	Ex.
    		`python bci_main.py --user "bci_user" --mode "RSVP"`

## Modules and Vital Functions
------------------------------

This a list of the major modules and their functionality. Each module will contain its own README, demo and test scripts. Please check them out for more information!

- `acquistion`: acquires data, gives back desired time series, saves at end of session.
- `display`: handles display of stimuli on screen, passing back stimuli timing.
- `signal_model`: trains and classifies eeg responses based on eeg and triggers.
- `gui`: end-user interface into system. See BCInterface.py and RSVPKeyboard.py.
- `helpers`: input/output functions needed for system, as well as helpful intilization functions.
- `utils`: utility functions needed for operation and installation.
- `language_model`: gives prob of letters during typing.
- `parameters`: json file for parameters.
- `static`: images, misc manuals, and readable texts for gui.
- `bci_main`: executor of experiments.

## Demo and Tests
-----------------

All major functions and modules have demo and test files associated with them. This should help orient you to the functionality as well as serve as documentation. *If you add to the repo, you should be adding tests and fixing any test that fail when you change the code.*

For example, you may run the bci_main demo by:
> run `python demo/bci_main_demo.py`

This demo will load in parameters and execute a demo task defined in the file. There are demo files for all modules listed above except language_model, helpers, and utils.

This repository uses pytest for execution of tests. You may execute them by:

> run `py.test` or `pytest` depending on your OS

## Contribution Guidelines
--------------------------

1. All added code will need tests and a demo (if a large feature).
2. All tests must pass to merge, even if they are seemingly unrelated to your task.
3. Pull requests must be tested locally and by the requester on a different computer.
4. Use Spaces, not Tabs.
5. Use informative names for functions and classes.
6. Document the input and output of your functions / classes in the code. eg in-line commenting
7. Do not push IDE or other local configuration files.
8. All new modules or major functionality should be documented outside of the code with a README.md. See REAME.md in repo or go to this site for inspiration: https://github.com/matiassingers/awesome-readme. Always use a Markdown interpreter before pushing. There are many free online or your IDE may come with one.

For further instruction:

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Use this resource for examples: http://docs.python-guide.org/en/latest/writing/style/

## Testing
----------

Please have all requirements installed. When writing tests, put them in the correct module, in a tests folder, and prefix the file and test itself with `test` in order for pytest to discover it. See other module's tests for examples!

To run all tests, in the command line:

```python
py.test
```


To run a single modules tests (ex. acquisition), in the command line:

```python
py.test acquisition
```

To generate test coverage metrics, in the command line:

```python
coverage run -m py.test

#Generate a command line report
coverage report

# Generate html doc in the bci folder. Navigate to index.html and click.
coverage html

```

## Authorship
--------------

Tab Memmott (OHSU)

Aziz Kocanaogullari (NEU)

Matthew Lawhead (OSHU- OCTRI)

Berkan Kadioglu (NEU)

Dani Smektala (OHSU_

Andac Demir (NEU)

Shaobin Xu (OHSU)

Shiran Dudy (OHSU)
