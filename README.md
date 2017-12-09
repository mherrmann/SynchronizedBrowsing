# SynchronizedBrowsing
[fman](https://fman.io) plugin implementing WinSCP's
[synchronized browsing](https://winscp.net/eng/docs/task_navigate#synchronize_browsing)
feature. When the plugin is active and you go up a directory, then fman also 
goes up a directory in the opposite pane. When you open a folder, then the 
folder with the same name is opened in the other pane. If that folder does not 
exist, you are asked whether you want to create it.

## Usage
Synchronized browsing is enabled as soon as you install the plugin. To turn it 
off, use fman's [Command Palette](https://fman.io/docs/shortcuts) to execute the
command `Toggle synchronized browsing`.

## Installation
Use fman's
[built-in command for installing plugins](https://fman.io/docs/installing-plugins).