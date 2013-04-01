#       README-MoreSpam.txt
# 		Plugin for B3 (www.bigbrotherbot.com)
#       
#       Copyright 2011 d0nin380 <d0nin380<at>gmail<dot>com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

Description:
	A very basic plugin to add custom say-commands just by editing the config file.
	Check the MoreSpam.xml for details.
	You can rename or delete the existing cmds and add ones you want.
	
	Make sure your responses "name" settings are the same as the commands and commands-p2p "name" settings INCLUDING the aliases.
	
	help-messages "name" settings must be without the alias.
	
	***NOTE*** The plugin will NOT work if you change the names of the sections. ***NOTE**
	

Installation:
	1. Unzip the content of this package into your B3 folder. It will
	place the MoreSpam.py file in b3/extplugins and the config file morespam.xml in
	your b3/extplugins/conf folder.

	2. Open morespam.xml with your texteditor and edit it to your liking.

	3. Open your B3.xml file (in b3/conf) and add the next line in the
	<plugins> section of the file:

		<plugin config="@b3/extplugins/conf/morespam.xml" name="morespam" />

	4. Restart your b3
	
Support:
	Support will ONLY be provided in http://forum.bigbrotherbot.net/releases/morespam-plugin/ so do not email me or anybody else your support questions.
	
# CHANGELOG
#   2011/03/23 - 1.0.0 - d0nin380
#   * Initial Release
#   29/03/2013 - 1.0.1 - d0nin380
#   * Fixed plugin name
#   * Code now matches B3 coding conventions
#
    
