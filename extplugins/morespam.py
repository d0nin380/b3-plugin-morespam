#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       morespam.py
#       
#       Copyright 2011-2013 d0nin380 <d0nin380<at>gmail<dot>com>
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
#
#
# CHANGELOG
#   23/03/2011 - 1.0.0 - d0nin380
#   * Initial Release
#   31/03/2013 - 1.0.1 - d0nin380
#   * Fixed plugin name
#   * multiple entries separated by semicolon instead of comma
#

__version__ = '1.0.1'
__author__ = 'd0nin380'

import b3, re, b3.events, random, b3.plugin

class MorespamPlugin(b3.plugin.Plugin):
    """ Plugin for b3 to spam messages like !ns !owned !lol etc... """
    
    def startup(self):
        self._adminPlugin = self.console.getPlugin('admin')
        self._p2p_cmddict = {}
        self._cmddict = {}
        self._helpdict = {}
        self._sections = ['commands', 'commands-p2p', 'responses', 'help-messages']
        self._failed_section = ""
        if not self._adminPlugin:
            self.error('Could not find admin plugin')
            return False
    
        #Make sure all the sections needed are in the xml file.
        for section in self._sections:
            if section in self.config.sections():
                pass
            else:
                self._failed_section=section
                self.warning("Plugin did not start because of missing section [%s] in the config file." % self._failed_section)
                return False
                
        try:
            for cmd in self.config.options('commands-p2p'):
                _response = self.config.get('responses', cmd)
                level = self.config.get('commands-p2p', cmd)
                sp = cmd.split('-')
                alias = None
                if len(sp) == 2:
                    cmd, alias = sp
                
                func = self.getCmd(cmd)
                if func:
                    try:
                        func.__func__.__doc__ = self.config.get("help-messages", cmd)
                    except Exception, msg:
                        self.debug("%s No help message set in MoreSpam.xml." % msg)
                        func.__func__.__doc__ = None
                    self._adminPlugin.registerCommand(self, cmd, level, func, alias)
                    self._p2p_cmddict[cmd] = _response.split(';')
        except Exception, msg:
            self.debug("Something is wrong with your morespam.xml section %s. Some commands may not work." % msg)
        
        try:
            for cmd in self.config.options('commands'):
                _response = self.config.get('responses', cmd)
                level = self.config.get('commands', cmd)
                sp = cmd.split('-')
                alias = None
                if len(sp) == 2:
                    cmd, alias = sp
                func = self.getCmd(cmd)
                if func:
                    try:
                        func.__func__.__doc__ = self.config.get("help-messages", cmd)
                    except Exception, msg:
                        self.debug("%s No help message set in MoreSpam.xml." % msg)
                        func.__func__.__doc__ = None
                    self._adminPlugin.registerCommand(self, cmd, level, func, alias)
                    self._cmddict[cmd] = _response
        except Exception, msg:
            self.debug("Something is wrong with your MoreSpam.xml section %s. Some commands may not work." % msg)
        
        self.debug('Started')
    
        
    def getCmd(self, cmd):
        cmd = 'cmd_handler'
        func = getattr(self, cmd, self.cmd_handler.__doc__)
        return func
    
        
    def cmd_handler(self, data, client=None, cmd=None):
        __doc__ = "help msg for: %s" % cmd
        m = self._adminPlugin.parseUserCmd(data)
        if cmd.command in self._p2p_cmddict.keys():
            if not m:
                client.message('^7Invalid parameters, you must supply a player name')
                return False            
            sclient = self._adminPlugin.findClientPrompt(m[0], client)
            if sclient:
                self.console.say(
                    '^2%s ^3says: %s %s' % (client.name,
                    random.choice(self._p2p_cmddict[cmd.command]),
                    sclient.name))

        else:
            client.message(self._cmddict[cmd.command])
            
if __name__ == '__main__':

    from b3.fake import fakeConsole, joe, reg, superadmin
 
    myplugin = MorespamPlugin(fakeConsole, '@b3/extplugins/conf/morespam.xml')
    print("\n\n * * * * * * * * * * * *  Tests starting below * * * * * * * * * * * * \n\n")
 
    # we call onStartup() as the real B3 would do
    myplugin.onStartup()
 
    # make superadmin connect to the fake game server on slot 0
    superadmin.connects(cid=0)
 
    # make joe and reg connect to the fake game server on slot 1
    joe.connects(cid=1)
    reg.connects(cid=2)
 
    # superadmin put joe in group user
    superadmin.says('!putgroup reg admin')
 
    # make joe try our commands
    reg.says('!ns joe')
    reg.says('!lol joe')
