# CHANGELOGS

## Table of Contents
+ [2024-05-03](#2024-05-03)

## Log Entries
### 2024-05-03
#### 1206H
+ Initial Commit

- New
    - Added new document 'README.md'
    - Added new document 'CHANGELOGS.md'
    - Added new directory 'manuals': Entry point for holding all manuals for various categories - imagine an All-in-One 'man' page compendium for programming languages, setup guides, compilation guides, libraries/modules, frameworks etc etc
        - Added new directory 'software-development' for Programming-based manuals
            - Added new directory 'programming-languages/' for Programming Languages
                - Added new directory 'python/' for Python manuals
                    - Added new directory 'libraries' for manuals on python libraries
                        - Added new directory 'built-in' for specifically python built-in standard libraries
                            + Added new document 'sqlite3.md' for Python SQLite3 library

#### 1228H
- New
    - Added new manuals/documentations to 'manuals/software-development/programming-languages/python/libraries/built-in/' for python built-in standard libraries
        + BeautifulSoup4.md
        - PyInstaller/
            + Added new document 'README.md'
            + Added new document 'Specfile.md'
            + Added new document 'manual.md'
            + Added new document 'setup.md'
        + argparse.md
        + asyncio.md
        + binascii.md
        - flask/
            + README.md
            - docs/
                + quickstart-guide.md
            + manual.md
            + setup.md
        + hashlib.md
        + html.md
        + json.md
        + multiprocessing/
            + manual.md
            - Snippets/
                + list-iteration-vs-for-loop.md
        - mysql-connector-python/
            + README.md
            + manual.md
            + setup.md
        - netfilterqueue/
            + README.md
            + manual.md
            - examples/
                + nfq.py.md
        - os/
            + README.md
            + manual.md
            + setup.md
        + paramiko.md
        + pip.md
        - platform/
            + README.md
            + manual.md
            + setup.md
        - pycryptodome/
            + README.md
            + manual.md
            - examples/
                + main.py
                - aes/
                    + decrypt.py
                    + encrypt.py
                - hybrid/
                    + decrypt.py
                    + encrypt.py
                - rsa/
                    + decrypt.py
                    + encrypt.py
                    + keygen.py
        + random.md
        + re.md
        + requests.md
        - rich/
            + README.md
            + docs.md
            + manual.md
        + ruamel.yaml.md
        + scapy.md
        - setuptools/
            + README.md
            + manual.md
            + setup.md
        - socket/
            + README.md
            + manual.md
            - examples/
                + reverse-shell.md
        - subprocess/
            + README.md
            + manual.md
            - examples/
                + stream-redirects-equivalent-in-python.md
                + symmetric-key-encryption-with-gpg.md
        + sys.md
        + tensorflow.md
        + threading.md
        + toml.md
        + tomllib.md

- Updates
    - Updated document 'README.md' in 'manuals/software-development/programming-languages/python/libraries/'
        + Added new manuals/documentations and packages on built-in libraries

#### 1443H
- Updates
    - Updated document 'sqlite3.md' in 'manuals/software-development/programming-languages/python/libraries/built-in/'
        + Added function documentation for 'sqlite3.Connection().rollback()' to rollback any non-committed transactions back to the baseline
        + Added usages and operational workflow usages for '.rollback()'

