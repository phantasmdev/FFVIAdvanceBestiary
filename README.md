# Final Fantasy VI Advance Bestiary
This application stores all the bestiary data of every enemy in Final Fantasy VI Advance.
This program is mainly used to find enemy information. Right now at its core, it is currently
just mimicking the base game at its core, but may potentially be updated more to include
more sophisticated information.

# Developer Requirements
- PyQt5
- Python version 3.11+

# Usage

There are two files in this repo: enemydata.py and app_window.py.

## enemydata.py
enemydata.py can import the Bestiary class, where you will have access to every object and each attribute inside it.
There's several ways to access each enemy, such as for loops to iterate over every enemy.
Enemies can also be referenced by the index of their object, as well as each piece of information for their stats, weakness, etc.

For example, to get the Guard's HP, you can code in the following:

<code language="Python">import enemydata as Bestiary
print(Bestiary.Bestiary.bestiary_list[0].health)
</code>

## app_window.py
This is the script that handles the UI using PyQt5.

# Deployment

If you're looking to obtain the actual program, you can download it here:
https://www.mediafire.com/file/sjigyu8zatznapu/Final_Fantasy_VI_Advance_Bestiary.exe/file

<i>Note: This program may eventually be added to an umbrella program that will bundle this and any other Bestiary programs together.
Feel free to continue to use the base program for the time being, however because of the way Python handles importing modules,
downloading separate programs can consume a lot of disk space.</i>

This program was last updated and deployed on December 22, 2024.
