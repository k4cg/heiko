Changelog
=========


(unreleased)
------------
- Release: 4.2.0. [Florian Baumann]
- Add setuptools as dev dep. [Simon Kuhnle]
- Fix version bump requirement. [Simon Kuhnle]
- Clean up login prompt, display version. [Simon Kuhnle]
- Changelog: 4.1.0. [Florian Baumann]
- Release: 4.1.0. [Florian Baumann]
- Fix readme format. [Florian Baumann]
- Fix relaease. [Florian Baumann]
- Readme fix. [Florian Baumann]
- Changelog: 4.0.0. [Florian Baumann]
- Release: 4.0.0. [Florian Baumann]
- Fix bumpversion. [Florian Baumann]
- Remove cli. [Florian Baumann]
- Release upgrade. [Florian Baumann]
- Migrated configurable tty to pip package. [Florian Baumann]
- Style changes. [Florian Baumann]
- Removed requirements.txt. [Florian Baumann]
- Convert heiko to pip package. [Florian Baumann]
- Merge pull request #55 from blarz/nfc-commandline. [ChrisC]

  Make NFC TTY configurable via commandline
- Make NFC TTY configurable via commandline. [Simon Kuhnle]
- Add summary of coins spent. [Florian Baumann]
- Merge pull request #54 from blarz/unused-imports. [Florian Baumann]

  Remove unused imports
- Remove unused imports. [Simon Kuhnle]
- PEP8 Style. [Florian Baumann]
- Merge pull request #52 from blarz/fix_user_create_error. [Florian
  Baumann]

  Fix non-admin user creation...
- Fix non-admin user creation... [Simon Kuhnle]
- Fix ident problem. [Florian Baumann]
- Errorhandling, spelling and log output to. [Florian Baumann]
- Merge pull request #49 from k4cg/feature/transfer. [Florian Baumann]

  Add transfer credits to other user
- Fix transfer with integer. [Florian Baumann]
- Add transfer credits to other user. [Florian Baumann]
- Add prompt for NFC card during setup. [Simon Kuhnle]
- Merge pull request #48 from blarz/autologout. [Florian Baumann]

  Add autologout
- Add sigalarm handler. [Simon Kuhnle]
- Format numbers with filling zero precision in tables. [Florian
  Baumann]
- Format numbers with filling zero precision. [Florian Baumann]
- Add update_item functionality for new prices. [Florian Baumann]
- Fix newline in welcome message. [Simon Kuhnle]
- Remove useless print() [Florian Baumann]
- Merge pull request #47 from blarz/nfcOnlyOnRealTTYs. [Florian Baumann]
- NFC: Only enable on real TTY (tty1) [Simon Kuhnle]

  Until now, logging in via SSH would mess everything up.
- Merge pull request #45 from blarz/fix_variables. [ChrisC]

  Fix variables in credit setter error log
- Fix variables in credit setter error log. [Simon Kuhnle]
- Merge pull request #44 from blarz/simpler_input_condition. [ChrisC]

  Simplify user input conditions
- Simplify input conditions. [Simon Kuhnle]
- Merge pull request #43 from blarz/loginWithoutNFC. [ChrisC]

  Make login possible without NFC
- Make login possible without NFC. [Simon Kuhnle]
- Fixed bug in python3.5 vs. python3.7 with json decoder. [Christian
  Carlowitz]
- Extract calls to 'clear' into banner functions. [Simon Kuhnle]
- Add config option to disallow inserting coins by user. [Christian
  Carlowitz]
- Allow adding credits by admin. [Christian Carlowitz]
- Show total revenue in item stats. [Christian Carlowitz]
- NFC: implemented password reset for NFC card rewrite. [Christian
  Carlowitz]
- NFC: allow creating "nfc only" user (with random dummy password)
  [Christian Carlowitz]
- Merge branch 'master' of github.com:k4cg/heiko. [Christian Carlowitz]
- Fix readability in menu condition. [Simon Kuhnle]
- NFC: move card setup code to own function in nfc module. [Christian
  Carlowitz]
- NFC: enable auth sector access in python module. [Christian Carlowitz]
- NFC: implemented card token retrieval and auth. [Christian Carlowitz]
- Bugfix: prevent nfc module crash if no reader is present. [Christian
  Carlowitz]
- Order menu via keys using sorted() [Florian Baumann]
- Improve navigation usability. [Florian Baumann]
- Create drink actions in user menu dynamically. [Simon Kuhnle]
- Do not duplicate item validation checks. [Simon Kuhnle]
- Fix item stats name. [Simon Kuhnle]

  list_items is actually listing the item stats.
- Merge pull request #36 from blarz/removenfcunusedimport. [ChrisC]
- NFC: Remove unused import. [Simon Kuhnle]
- Add catch for add drink wrong answer. [Florian Baumann]
- Prevent loading nfc module if nfc is not enabled. [Christian
  Carlowitz]
- Merge pull request #31 from blarz/handleEOF. [Florian Baumann]

  Handle EOF (Ctrl-D) gracefully
- Handle EOF (Ctrl-D) gracefully. [Simon Kuhnle]
- Merge pull request #34 from blarz/fix_non_admin_user. [Florian
  Baumann]

  Fix admin menu access violation
- Fix admin menu access violation. [Simon Kuhnle]

  Non-admin users going to the admin menu crashed, because we didn't return both bools.
- NFC: Add README with deps and build instructions (#35) [Simon]

  * NFC: Add README with deps and build instructions
- Fix typo in item name check message. [Simon Kuhnle]
- Implemented nfc token generation and writing to card. [Christian
  Carlowitz]
- Nfc: fixed bug in python module. [Christian Carlowitz]
- Nfc: implemented multi block writes and reads. [Christian Carlowitz]
- Added very basic nfc module. [Christian Carlowitz]
- Merge pull request #28 from blarz/removeStarImport. [Florian Baumann]

  Remove star imports in heiko-cli
- Remove star imports in heiko-cli. [Simon Kuhnle]
- Merge pull request #30 from blarz/disable_say. [Florian Baumann]

  Don't play any sounds if voice is disabled
- Don't play any sounds if voice is disabled. [Simon Kuhnle]
- Merge pull request #29 from blarz/fix_typo. [Florian Baumann]

  Fix typo in delete log message
- Fix typo delete log message. [Simon Kuhnle]
- Merge pull request #27 from blarz/ignore_vscode. [Florian Baumann]

  Add more IDE config files to .gitignore
- Add more IDE config files to .gitignore. [Simon Kuhnle]
- Add voice options to config template (#26) [Simon]

  * Add voice options to config template

  * Add general sound path to config, too

  * Add default path for path_sounds
- Add flake8 configuration. [Simon Kuhnle]
- Merge pull request #23 from blarz/removeUnusedVariables. [Florian
  Baumann]

  Remove unused variables
- Remove unused variables. [Simon Kuhnle]

  Found with flake8
- Merge pull request #22 from blarz/removeUnusedImports. [Florian
  Baumann]

  Remove unused imports
- Remove unused imports. [Simon Kuhnle]

  Found with flake8
- Cosmetics for admin menue. [Florian Baumann]
- Cash sounds. [Florian Baumann]
- Fix. [Florian Baumann]
- Fix menu. [Florian Baumann]
- Spezialmenue. [Florian Baumann]
- Flora Mate. [Florian Baumann]
- Remote utf8 char. [Florian Baumann]
- Fix admin menue with cfgobj. [Florian Baumann]
- Remove generate message. [Florian Baumann]
- Remove debug messages. [Florian Baumann]
- Dep. [Florian Baumann]
- Config options for voice. [Florian Baumann]
- Add ibm watson to generate t2s greetings for users. [Florian Baumann]
- Converted everything to wav files. [Florian Baumann]
- Quit sound. [Florian Baumann]
- Todo remove. [Florian Baumann]
- Voice should not be critical foor the system. [Florian Baumann]
- Mapping fix. [Florian Baumann]
- Utf8 fix. [Florian Baumann]
- Utf8 fix. [Florian Baumann]
- Better cheers. [Florian Baumann]
- Fix. [Florian Baumann]
- Fixes voice. [Florian Baumann]
- Add voice to heiko! [Florian Baumann]
- Add readline, for cmd history - thx chris_c. [Florian Baumann]
- Menu info. [Florian Baumann]
- Update LICENSE. [Florian Baumann]
- Fix yaml requiremnts. [Florian Baumann]
- Merge pull request #17 from k4cg/feature/config-support. [Florian
  Baumann]

  Adding configuration file support to move config out of code.
- Adding configuration file support to move config out of code. [dagonC]
- Adding JetBrains IDE project folder to gitignore. [dagonC]
- Migration status message fix. [Florian Baumann]
- Migration status message fix. [Florian Baumann]
- Migration now supports negative credits. [Florian Baumann]
- Userstats implemented. Fixes #8. [Florian Baumann]
- Handling not available backend. [Florian Baumann]
- Adds consumptions to list_items. [Florian Baumann]
- Update README.md. [Florian Baumann]
- Login cred removal. [Florian Baumann]
- Implemented tabluar view for database outputs. Fixes #9. [Florian
  Baumann]
- Implemented Service Stats. Fixes #14. [Florian Baumann]
- Implemented change_password(). Fixes #3. [Florian Baumann]
- Migrated welcome banner. [Florian Baumann]
- Implemented signal handling. Fixes #13. [Florian Baumann]
- Menu mapping fix. [Florian Baumann]
- Update status line. [Florian Baumann]
- Fixes for swagger client. [Florian Baumann]
- Import fix. [Florian Baumann]
- Added reset_credits() [Florian Baumann]
- Moar int, less float. [Florian Baumann]
- Admin fix. [Florian Baumann]
- Typo. [Florian Baumann]
- Catch errors in find_user. [Florian Baumann]
- Fix find_user. [Florian Baumann]
- Added find_user_by_username() [Florian Baumann]
- Merge. [Florian Baumann]
- Added better handling for sqlite connection. [Florian Baumann]
- Added delete_user() to admin menu. [Florian Baumann]
- Switched to .isalnum() instead of string.ascii_letters() [Florian
  Baumann]
- Various login() and menu() behaviour fixes. [Florian Baumann]
- Fixed int() problems with backend. [Florian Baumann]
- Added migrate_user() function. Fixes #6. [Florian Baumann]
- Added success msg for create_item() [Florian Baumann]
- Added reset_user_password(). Fixes #4. [Florian Baumann]
- Added validation for length of username. [Florian Baumann]
- Added delete_item to admin menu. [Florian Baumann]
- Fix Banner Euro representation. [Florian Baumann]
- Added show_item and reflect price in success of consume_item. [Florian
  Baumann]
- Fix consume success error message. [Florian Baumann]
- Added admin_menu for administrative tasks. [Florian Baumann]
- Merge pull request #1 from k4cg/import-vorschlag. [Florian Baumann]

  Fix für imports
- Outsourced in utils.py. [Florian Baumann]
- Fix für imports. [Poschi]
- Imports. [Florian Baumann]
- Moved create_item to heiko.items. [Florian Baumann]
- Modified file structure to be a bit more modular. [Florian Baumann]
- Admin information in the banner. [Florian Baumann]
- Restructure code and document every single function. [Florian Baumann]
- Added some responses to consume function. [Florian Baumann]
- Documentation. [Florian Baumann]
- Added add_credits. [Florian Baumann]
- Added create_item method. [Florian Baumann]
- Added consume function. [Florian Baumann]
- Added create_user method. [Florian Baumann]
- Added banner method, better menu behavoir and list users/items.
  [Florian Baumann]
- Added. [Florian Baumann]
- Bit of cleanup. [Florian Baumann]
- Init. [Florian Baumann]


