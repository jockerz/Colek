#!/bin/bash

print_help() {
    echo -e "Usage \t$0 <option>"
    echo -e "Options \n\tnew : create new md and python file (Will be prompted)"
    echo -e "\thelp: print this"
    exit
}

make_it() {
    echo "Create new. Type the name(for .py and .md filename), followed by [ENTER]"
    read name
    if [ -f ${name}.md ]; then
        echo "$name.md is exist. Use another name"
        exit 1
    fi
    if [ -f ${name}.py ]; then
        echo "$name.md is exist. Use another name"
        exit 2
    fi
    echo "Creating $name.md and $name.py"
    echo "Description(in one line)"
    read Desc
    echo "## $Desc" >> ${name}.md
    echo -e "\n\n[EDIT ME]\n\n" >> ${name}.md
    echo -e "\n##[Back to main page](https://github.com/jockerz/Colek) \n" >> ${name}.md
    echo "[+] ${name}.md is created"
    echo -e "#!/usr/bin/python \n\nprint \"[EDIT ME]\"" >> ${name}.py
    echo "[+] ${name}.py is created"

}

if [ $# -ne 1 ]; then
    print_help
fi

case $1 in
    "new")
    make_it
    ;;
    *)
    print_help
    ;;
esac
